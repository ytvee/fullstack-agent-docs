---
category: patterns
topic: file-upload
status: draft
---

## Проблема / Контекст

Загрузка файлов в Next.js 15 требует: безопасного хранилища, валидации на сервере, защиты роутов по аутентификации, сохранения метаданных в БД и хорошего UX с preview. Нативный `<input type="file">` + ручной upload на S3 — это много boilerplate и потенциальные дыры в безопасности. UploadThing решает инфраструктуру, оставляя контроль над логикой.

Типичные требования:
- Загрузка аватаров, документов, изображений
- Валидация типа и размера файла до загрузки
- Только авторизованные пользователи могут загружать
- После загрузки — сохранить URL в БД
- Preview до и после загрузки

## Решение

**Архитектура:** UploadThing предоставляет File Router (серверный конфиг) + хук `useUploadThing` (клиент). Файл роутер определяет endpoint-ы с валидацией и callback-ами. Callback `onUploadComplete` вызывается на сервере после успешной загрузки — здесь сохраняем в БД.

**Установка:**
```bash
npm install uploadthing @uploadthing/react
```

**Переменные окружения:**
```env
UPLOADTHING_SECRET=sk_live_...
UPLOADTHING_APP_ID=your-app-id
```

## Пример кода

### 1. Drizzle схема для хранения файлов

```typescript
// src/db/schema/files.ts
import { pgTable, text, timestamp, uuid, integer, pgEnum } from "drizzle-orm/pg-core";
import { users } from "./users";

export const fileTypeEnum = pgEnum("file_type", ["avatar", "document", "image"]);

export const files = pgTable("files", {
  id: uuid("id").primaryKey().defaultRandom(),
  userId: uuid("user_id")
    .notNull()
    .references(() => users.id, { onDelete: "cascade" }),
  url: text("url").notNull(),
  key: text("key").notNull().unique(), // UploadThing file key
  name: text("name").notNull(),
  size: integer("size").notNull(), // bytes
  type: fileTypeEnum("type").notNull(),
  createdAt: timestamp("created_at").defaultNow().notNull(),
});

export type File = typeof files.$inferSelect;
export type NewFile = typeof files.$inferInsert;
```

### 2. UploadThing File Router

```typescript
// src/lib/uploadthing/core.ts
import { createUploadthing, type FileRouter } from "uploadthing/next";
import { auth } from "@/lib/auth";
import { db } from "@/db";
import { files } from "@/db/schema/files";
import { UTApi } from "uploadthing/server";

const f = createUploadthing();

export const ourFileRouter = {
  // Endpoint для аватаров — только изображения, макс 4MB
  avatarUploader: f({ image: { maxFileSize: "4MB", maxFileCount: 1 } })
    .middleware(async () => {
      const session = await auth();
      if (!session?.user?.id) throw new Error("Unauthorized");
      return { userId: session.user.id };
    })
    .onUploadComplete(async ({ metadata, file }) => {
      // Удаляем старый аватар если есть
      const existing = await db.query.files.findFirst({
        where: (f, { and, eq }) =>
          and(eq(f.userId, metadata.userId), eq(f.type, "avatar")),
      });

      if (existing) {
        const utapi = new UTApi();
        await utapi.deleteFiles(existing.key);
        await db.delete(files).where(eq(files.id, existing.id));
      }

      // Сохраняем новый файл в БД
      await db.insert(files).values({
        userId: metadata.userId,
        url: file.url,
        key: file.key,
        name: file.name,
        size: file.size,
        type: "avatar",
      });

      // Обновляем аватар пользователя
      await db
        .update(users)
        .set({ image: file.url })
        .where(eq(users.id, metadata.userId));

      // Возвращаем данные клиенту (доступны в onClientUploadComplete)
      return { uploadedBy: metadata.userId, url: file.url };
    }),

  // Endpoint для документов — PDF/DOCX, макс 16MB, до 5 файлов
  documentUploader: f({
    pdf: { maxFileSize: "16MB", maxFileCount: 5 },
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document": {
      maxFileSize: "16MB",
      maxFileCount: 5,
    },
  })
    .middleware(async ({ req }) => {
      const session = await auth();
      if (!session?.user?.id) throw new Error("Unauthorized");

      // Проверяем роль для загрузки документов
      if (session.user.role !== "admin" && session.user.role !== "member") {
        throw new Error("Insufficient permissions");
      }

      return { userId: session.user.id };
    })
    .onUploadComplete(async ({ metadata, file }) => {
      await db.insert(files).values({
        userId: metadata.userId,
        url: file.url,
        key: file.key,
        name: file.name,
        size: file.size,
        type: "document",
      });

      return { url: file.url, name: file.name };
    }),

  // Endpoint для изображений в контенте — до 8MB, до 10 штук
  imageUploader: f({ image: { maxFileSize: "8MB", maxFileCount: 10 } })
    .middleware(async () => {
      const session = await auth();
      if (!session?.user?.id) throw new Error("Unauthorized");
      return { userId: session.user.id };
    })
    .onUploadComplete(async ({ metadata, file }) => {
      await db.insert(files).values({
        userId: metadata.userId,
        url: file.url,
        key: file.key,
        name: file.name,
        size: file.size,
        type: "image",
      });

      return { url: file.url };
    }),
} satisfies FileRouter;

export type OurFileRouter = typeof ourFileRouter;
```

### 3. Route Handler

```typescript
// src/app/api/uploadthing/route.ts
import { createRouteHandler } from "uploadthing/next";
import { ourFileRouter } from "@/lib/uploadthing/core";

export const { GET, POST } = createRouteHandler({
  router: ourFileRouter,
  // config опционально — для кастомного логирования
  config: {
    logLevel: process.env.NODE_ENV === "development" ? "debug" : "error",
  },
});
```

### 4. Компонент загрузки аватара с preview

```typescript
// src/components/upload/avatar-upload.tsx
"use client";

import { useState, useCallback } from "react";
import { useUploadThing } from "@/lib/uploadthing/client";
import { useDropzone } from "react-dropzone";
import Image from "next/image";
import { Button } from "@/components/ui/button";
import { toast } from "sonner";
import { Loader2, Upload, X } from "lucide-react";
import { cn } from "@/lib/utils";

interface AvatarUploadProps {
  currentAvatarUrl?: string | null;
  onUploadComplete: (url: string) => void;
  className?: string;
}

export function AvatarUpload({
  currentAvatarUrl,
  onUploadComplete,
  className,
}: AvatarUploadProps) {
  const [preview, setPreview] = useState<string | null>(currentAvatarUrl ?? null);
  const [selectedFile, setSelectedFile] = useState<File | null>(null);
  const [isUploading, setIsUploading] = useState(false);

  const { startUpload, permittedFileInfo } = useUploadThing("avatarUploader", {
    onClientUploadComplete: (res) => {
      const uploaded = res[0];
      if (uploaded?.serverData?.url) {
        setPreview(uploaded.serverData.url);
        onUploadComplete(uploaded.serverData.url);
        toast.success("Аватар обновлён");
      }
      setIsUploading(false);
      setSelectedFile(null);
    },
    onUploadError: (error) => {
      toast.error(`Ошибка загрузки: ${error.message}`);
      setIsUploading(false);
      // Восстанавливаем preview до ошибки
      setPreview(currentAvatarUrl ?? null);
      setSelectedFile(null);
    },
    onUploadBegin: () => {
      setIsUploading(true);
    },
  });

  const onDrop = useCallback((acceptedFiles: File[]) => {
    const file = acceptedFiles[0];
    if (!file) return;

    // Создаём локальный preview до загрузки
    const objectUrl = URL.createObjectURL(file);
    setPreview(objectUrl);
    setSelectedFile(file);

    // Cleanup object URL при unmount
    return () => URL.revokeObjectURL(objectUrl);
  }, []);

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    accept: { "image/*": [".jpg", ".jpeg", ".png", ".webp", ".gif"] },
    maxFiles: 1,
    maxSize: 4 * 1024 * 1024, // 4MB
    disabled: isUploading,
    onDropRejected: (rejections) => {
      const error = rejections[0]?.errors[0];
      if (error?.code === "file-too-large") {
        toast.error("Файл слишком большой. Максимум 4MB.");
      } else if (error?.code === "file-invalid-type") {
        toast.error("Неподдерживаемый формат. Используйте JPG, PNG или WebP.");
      }
    },
  });

  const handleUpload = async () => {
    if (!selectedFile) return;
    await startUpload([selectedFile]);
  };

  const handleCancel = () => {
    setPreview(currentAvatarUrl ?? null);
    setSelectedFile(null);
  };

  return (
    <div className={cn("flex flex-col items-center gap-4", className)}>
      {/* Preview */}
      <div
        {...getRootProps()}
        className={cn(
          "relative h-24 w-24 cursor-pointer overflow-hidden rounded-full border-2 border-dashed transition-colors",
          isDragActive
            ? "border-primary bg-primary/10"
            : "border-muted-foreground/25 hover:border-primary",
          isUploading && "cursor-not-allowed opacity-60"
        )}
      >
        <input {...getInputProps()} />
        {preview ? (
          <Image
            src={preview}
            alt="Avatar preview"
            fill
            className="object-cover"
            sizes="96px"
          />
        ) : (
          <div className="flex h-full w-full items-center justify-center">
            <Upload className="h-8 w-8 text-muted-foreground" />
          </div>
        )}
        {isUploading && (
          <div className="absolute inset-0 flex items-center justify-center bg-black/50">
            <Loader2 className="h-6 w-6 animate-spin text-white" />
          </div>
        )}
      </div>

      {/* Кнопки действий — появляются только если выбран новый файл */}
      {selectedFile && !isUploading && (
        <div className="flex gap-2">
          <Button size="sm" onClick={handleUpload}>
            <Upload className="mr-2 h-4 w-4" />
            Загрузить
          </Button>
          <Button size="sm" variant="outline" onClick={handleCancel}>
            <X className="mr-2 h-4 w-4" />
            Отмена
          </Button>
        </div>
      )}

      {/* Подсказка */}
      {!selectedFile && !isUploading && (
        <p className="text-xs text-muted-foreground">
          JPG, PNG или WebP. Макс. 4MB.
        </p>
      )}
    </div>
  );
}
```

### 5. UploadThing клиентский хелпер

```typescript
// src/lib/uploadthing/client.ts
import { generateUploadButton, generateUploadDropzone, generateReactHelpers } from "@uploadthing/react";
import type { OurFileRouter } from "./core";

export const UploadButton = generateUploadButton<OurFileRouter>();
export const UploadDropzone = generateUploadDropzone<OurFileRouter>();

// useUploadThing с полной типизацией
export const { useUploadThing, uploadFiles } = generateReactHelpers<OurFileRouter>();
```

### 6. Server Action для удаления файла

```typescript
// src/actions/files.ts
"use server";

import { auth } from "@/lib/auth";
import { db } from "@/db";
import { files } from "@/db/schema/files";
import { eq, and } from "drizzle-orm";
import { UTApi } from "uploadthing/server";
import { revalidatePath } from "next/cache";

export async function deleteFile(fileId: string): Promise<{ success: boolean; error?: string }> {
  const session = await auth();
  if (!session?.user?.id) {
    return { success: false, error: "Unauthorized" };
  }

  // Находим файл — обязательно проверяем владельца
  const file = await db.query.files.findFirst({
    where: (f, { and, eq }) =>
      and(eq(f.id, fileId), eq(f.userId, session.user.id)),
  });

  if (!file) {
    return { success: false, error: "File not found" };
  }

  try {
    // Удаляем из UploadThing storage
    const utapi = new UTApi();
    await utapi.deleteFiles(file.key);

    // Удаляем запись из БД
    await db.delete(files).where(eq(files.id, fileId));

    revalidatePath("/profile");
    return { success: true };
  } catch (error) {
    console.error("Failed to delete file:", error);
    return { success: false, error: "Failed to delete file" };
  }
}
```

### 7. Компонент загрузки документов (множественная загрузка)

```typescript
// src/components/upload/document-upload.tsx
"use client";

import { useState } from "react";
import { useUploadThing } from "@/lib/uploadthing/client";
import { Button } from "@/components/ui/button";
import { Progress } from "@/components/ui/progress";
import { toast } from "sonner";
import { FileText, Loader2, Upload, X } from "lucide-react";
import { formatBytes } from "@/lib/utils";

interface UploadedDocument {
  url: string;
  name: string;
}

interface DocumentUploadProps {
  onUploadComplete: (docs: UploadedDocument[]) => void;
}

export function DocumentUpload({ onUploadComplete }: DocumentUploadProps) {
  const [files, setFiles] = useState<File[]>([]);
  const [uploadProgress, setUploadProgress] = useState(0);

  const { startUpload, isUploading } = useUploadThing("documentUploader", {
    onUploadProgress: setUploadProgress,
    onClientUploadComplete: (res) => {
      const docs = res.map((r) => ({
        url: r.url,
        name: r.name,
      }));
      onUploadComplete(docs);
      setFiles([]);
      setUploadProgress(0);
      toast.success(`Загружено ${docs.length} документ(ов)`);
    },
    onUploadError: (error) => {
      toast.error(error.message);
      setUploadProgress(0);
    },
  });

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const selected = Array.from(e.target.files ?? []);
    // Клиентская валидация перед UI
    const valid = selected.filter((f) => {
      if (f.size > 16 * 1024 * 1024) {
        toast.error(`${f.name}: файл больше 16MB`);
        return false;
      }
      return true;
    });
    setFiles(valid.slice(0, 5)); // макс 5 файлов
  };

  const removeFile = (index: number) => {
    setFiles((prev) => prev.filter((_, i) => i !== index));
  };

  return (
    <div className="space-y-4">
      <div className="flex items-center gap-3">
        <label
          htmlFor="doc-upload"
          className="flex cursor-pointer items-center gap-2 rounded-md border px-4 py-2 text-sm font-medium hover:bg-muted"
        >
          <Upload className="h-4 w-4" />
          Выбрать файлы
        </label>
        <input
          id="doc-upload"
          type="file"
          multiple
          accept=".pdf,.docx"
          className="hidden"
          onChange={handleFileChange}
          disabled={isUploading}
        />
        <span className="text-xs text-muted-foreground">PDF, DOCX • Макс. 16MB • До 5 файлов</span>
      </div>

      {/* Список выбранных файлов */}
      {files.length > 0 && (
        <ul className="space-y-2">
          {files.map((file, index) => (
            <li
              key={`${file.name}-${index}`}
              className="flex items-center gap-3 rounded-md border p-3"
            >
              <FileText className="h-5 w-5 shrink-0 text-muted-foreground" />
              <div className="min-w-0 flex-1">
                <p className="truncate text-sm font-medium">{file.name}</p>
                <p className="text-xs text-muted-foreground">{formatBytes(file.size)}</p>
              </div>
              {!isUploading && (
                <button
                  onClick={() => removeFile(index)}
                  className="shrink-0 rounded p-1 hover:bg-muted"
                >
                  <X className="h-4 w-4" />
                </button>
              )}
            </li>
          ))}
        </ul>
      )}

      {/* Прогресс загрузки */}
      {isUploading && (
        <div className="space-y-1">
          <Progress value={uploadProgress} className="h-2" />
          <p className="text-xs text-muted-foreground">{uploadProgress}%</p>
        </div>
      )}

      {/* Кнопка отправки */}
      {files.length > 0 && (
        <Button
          onClick={() => startUpload(files)}
          disabled={isUploading}
          className="w-full"
        >
          {isUploading ? (
            <>
              <Loader2 className="mr-2 h-4 w-4 animate-spin" />
              Загрузка...
            </>
          ) : (
            <>
              <Upload className="mr-2 h-4 w-4" />
              Загрузить {files.length} файл(ов)
            </>
          )}
        </Button>
      )}
    </div>
  );
}
```

## Антипаттерн

```typescript
// ПЛОХО: Нет проверки авторизации в middleware
export const badFileRouter = {
  anyUploader: f({ image: { maxFileSize: "4MB" } })
    // Нет .middleware() — любой может загружать!
    .onUploadComplete(async ({ file }) => {
      // Нет сохранения в БД — файл существует в хранилище, но нигде не записан
      console.log(file.url);
    }),
};

// ПЛОХО: Валидация только на клиенте
function BadUpload() {
  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (file && file.size > 4 * 1024 * 1024) {
      alert("Too big"); // Клиентская проверка обходится легко
      return;
    }
    // Загружаем без серверной валидации
    uploadToS3Directly(file); // Прямая загрузка на S3 с клиента — опасно
  };
}

// ПЛОХО: Не проверяем владельца при удалении
async function badDeleteFile(fileId: string) {
  "use server";
  // Любой авторизованный пользователь может удалить любой файл!
  await db.delete(files).where(eq(files.id, fileId));
  await utapi.deleteFiles(fileId);
}
```

**Правила:**
1. Всегда проверяй авторизацию в `.middleware()` — это единственное место, которое нельзя обойти
2. `onUploadComplete` вызывается на сервере — здесь делай все DB операции
3. При удалении файла — всегда проверяй `userId` владельца
4. Не доверяй клиентской валидации размера/типа — UploadThing валидирует на сервере по конфигу роутера
5. Удаляй файлы из UploadThing storage при удалении из БД (через `UTApi.deleteFiles`)

## Связанные документы

- `knowledge/custom/02-patterns/rbac.md` — защита роутов по ролям
- `knowledge/custom/03-antipatterns/secrets-exposure.md` — безопасность API ключей UploadThing
- `knowledge/custom/06-security/` — общая безопасность загрузок
