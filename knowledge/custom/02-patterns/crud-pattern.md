---
category: patterns
topic: crud-pattern
status: draft
---

## Проблема / Контекст

CRUD operations are the backbone of every application, yet they are the most commonly implemented incorrectly in Next.js App Router. The common failure modes are:

1. **List page**: Using `useEffect` + `fetch` when a Server Component can query Drizzle directly
2. **Forms**: Building uncontrolled forms without schema validation, missing server-side re-validation
3. **Mutations**: Calling Route Handlers from Client Components when Server Actions are simpler and type-safe
4. **Error handling**: Letting unhandled errors crash the page instead of showing inline validation errors
5. **Optimistic UI**: Either missing entirely (showing a loading spinner) or implemented incorrectly with manual state management

This document shows the complete, correct end-to-end CRUD pattern for a `Project` resource.

## Решение

### 1. Zod Schema (shared client + server)

```typescript
// src/features/projects/schemas.ts
import { z } from 'zod'

export const projectSchema = z.object({
  name: z
    .string()
    .min(1, 'Project name is required')
    .max(100, 'Name must be 100 characters or less')
    .trim(),
  description: z
    .string()
    .max(500, 'Description must be 500 characters or less')
    .optional()
    .or(z.literal('')),
  visibility: z.enum(['public', 'private'], {
    errorMap: () => ({ message: 'Visibility must be public or private' }),
  }),
})

export const updateProjectSchema = projectSchema.extend({
  id: z.string().min(1),
})

export type ProjectFormValues = z.infer<typeof projectSchema>
export type UpdateProjectValues = z.infer<typeof updateProjectSchema>
```

### 2. Drizzle Schema

```typescript
// src/server/db/schema.ts (projects table)
import { pgTable, text, timestamp, pgEnum } from 'drizzle-orm/pg-core'
import { createId } from '@paralleldrive/cuid2'
import { users } from './schema'

export const visibilityEnum = pgEnum('visibility', ['public', 'private'])

export const projects = pgTable('projects', {
  id: text('id').primaryKey().$defaultFn(() => createId()),
  name: text('name').notNull(),
  description: text('description'),
  visibility: visibilityEnum('visibility').notNull().default('private'),
  userId: text('user_id').notNull().references(() => users.id, { onDelete: 'cascade' }),
  createdAt: timestamp('created_at').defaultNow().notNull(),
  updatedAt: timestamp('updated_at').defaultNow().notNull(),
})

export type Project = typeof projects.$inferSelect
export type NewProject = typeof projects.$inferInsert
```

### 3. Query Functions (Server Only)

```typescript
// src/entities/project/queries.ts
import 'server-only'
import { db } from '@/server/db'
import { projects } from '@/server/db/schema'
import { eq, desc, and } from 'drizzle-orm'
import type { Project } from '@/server/db/schema'

export async function getProjectsByUserId(userId: string): Promise<Project[]> {
  return db.query.projects.findMany({
    where: eq(projects.userId, userId),
    orderBy: [desc(projects.createdAt)],
  })
}

export async function getProjectById(
  projectId: string,
  userId: string
): Promise<Project | undefined> {
  return db.query.projects.findFirst({
    where: and(eq(projects.id, projectId), eq(projects.userId, userId)),
  })
}
```

### 4. Server Actions

```typescript
// src/features/projects/actions.ts
'use server'

import { auth } from '@/server/auth'
import { db } from '@/server/db'
import { projects } from '@/server/db/schema'
import { eq, and } from 'drizzle-orm'
import { revalidatePath } from 'next/cache'
import { redirect } from 'next/navigation'
import { z } from 'zod'
import { projectSchema, updateProjectSchema } from './schemas'
import type { ActionResult } from '@/types/api'
import type { Project } from '@/server/db/schema'

export async function createProject(
  input: z.infer<typeof projectSchema>
): Promise<ActionResult<Project>> {
  const session = await auth()
  if (!session?.user?.id) return { success: false, error: 'Unauthorized' }

  const parsed = projectSchema.safeParse(input)
  if (!parsed.success) {
    return {
      success: false,
      error: 'Validation failed',
      fieldErrors: parsed.error.flatten().fieldErrors as Record<string, string[]>,
    }
  }

  const [project] = await db
    .insert(projects)
    .values({
      ...parsed.data,
      description: parsed.data.description || null,
      userId: session.user.id,
    })
    .returning()

  revalidatePath('/projects')
  return { success: true, data: project }
}

export async function updateProject(
  input: z.infer<typeof updateProjectSchema>
): Promise<ActionResult<Project>> {
  const session = await auth()
  if (!session?.user?.id) return { success: false, error: 'Unauthorized' }

  const parsed = updateProjectSchema.safeParse(input)
  if (!parsed.success) {
    return {
      success: false,
      error: 'Validation failed',
      fieldErrors: parsed.error.flatten().fieldErrors as Record<string, string[]>,
    }
  }

  const { id, ...data } = parsed.data

  // Verify ownership before updating
  const existing = await db.query.projects.findFirst({
    where: and(eq(projects.id, id), eq(projects.userId, session.user.id)),
    columns: { id: true },
  })
  if (!existing) return { success: false, error: 'Project not found' }

  const [updated] = await db
    .update(projects)
    .set({ ...data, description: data.description || null, updatedAt: new Date() })
    .where(eq(projects.id, id))
    .returning()

  revalidatePath('/projects')
  revalidatePath(`/projects/${id}`)
  return { success: true, data: updated }
}

export async function deleteProject(projectId: string): Promise<ActionResult> {
  const session = await auth()
  if (!session?.user?.id) return { success: false, error: 'Unauthorized' }

  const existing = await db.query.projects.findFirst({
    where: and(eq(projects.id, projectId), eq(projects.userId, session.user.id)),
    columns: { id: true },
  })
  if (!existing) return { success: false, error: 'Project not found' }

  await db.delete(projects).where(eq(projects.id, projectId))

  revalidatePath('/projects')
  return { success: true, data: undefined }
}
```

### 5. List Page (Server Component)

```typescript
// src/app/(dashboard)/projects/page.tsx
import { auth } from '@/server/auth'
import { getProjectsByUserId } from '@/entities/project/queries'
import { ProjectList } from '@/features/projects/ui/project-list'
import { Button } from '@/components/ui/button'
import Link from 'next/link'
import { redirect } from 'next/navigation'
import { PlusIcon } from 'lucide-react'

export const metadata = {
  title: 'Projects',
}

export default async function ProjectsPage() {
  const session = await auth()
  if (!session?.user?.id) redirect('/login')

  const userProjects = await getProjectsByUserId(session.user.id)

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <h1 className="text-2xl font-bold tracking-tight">Projects</h1>
        <Button asChild>
          <Link href="/projects/new">
            <PlusIcon className="mr-2 h-4 w-4" />
            New Project
          </Link>
        </Button>
      </div>

      {userProjects.length === 0 ? (
        <div className="flex flex-col items-center gap-2 py-16 text-center">
          <p className="text-lg font-medium">No projects yet</p>
          <p className="text-muted-foreground">Create your first project to get started.</p>
          <Button asChild className="mt-4">
            <Link href="/projects/new">Create Project</Link>
          </Button>
        </div>
      ) : (
        <ProjectList projects={userProjects} />
      )}
    </div>
  )
}
```

### 6. Project List Client Component (with Delete)

```typescript
// src/features/projects/ui/project-list.tsx
'use client'

import { useOptimistic, useTransition } from 'react'
import { deleteProject } from '../actions'
import { ProjectCard } from '@/entities/project/ui/project-card'
import { toast } from 'sonner'
import type { Project } from '@/server/db/schema'

interface ProjectListProps {
  projects: Project[]
}

export function ProjectList({ projects }: ProjectListProps) {
  const [isPending, startTransition] = useTransition()
  const [optimisticProjects, removeOptimistic] = useOptimistic(
    projects,
    (state, deletedId: string) => state.filter((p) => p.id !== deletedId)
  )

  function handleDelete(projectId: string) {
    startTransition(async () => {
      removeOptimistic(projectId)
      const result = await deleteProject(projectId)
      if (!result.success) {
        toast.error(result.error)
        // Next.js will re-render with server data after revalidatePath,
        // which restores the item if the delete failed server-side
      } else {
        toast.success('Project deleted')
      }
    })
  }

  return (
    <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-3">
      {optimisticProjects.map((project) => (
        <ProjectCard
          key={project.id}
          project={project}
          onDelete={() => handleDelete(project.id)}
        />
      ))}
    </div>
  )
}
```

### 7. Project Form (Create and Edit)

```typescript
// src/features/projects/ui/project-form.tsx
'use client'

import { useForm } from 'react-hook-form'
import { zodResolver } from '@hookform/resolvers/zod'
import { useTransition } from 'react'
import { useRouter } from 'next/navigation'
import { toast } from 'sonner'
import {
  Form,
  FormControl,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from '@/components/ui/form'
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from '@/components/ui/select'
import { Input } from '@/components/ui/input'
import { Textarea } from '@/components/ui/textarea'
import { Button } from '@/components/ui/button'
import { projectSchema, type ProjectFormValues } from '../schemas'
import { createProject, updateProject } from '../actions'
import type { Project } from '@/server/db/schema'

interface ProjectFormProps {
  project?: Project  // undefined = create mode, defined = edit mode
}

export function ProjectForm({ project }: ProjectFormProps) {
  const router = useRouter()
  const [isPending, startTransition] = useTransition()
  const isEditing = !!project

  const form = useForm<ProjectFormValues>({
    resolver: zodResolver(projectSchema),
    defaultValues: {
      name: project?.name ?? '',
      description: project?.description ?? '',
      visibility: project?.visibility ?? 'private',
    },
  })

  function onSubmit(values: ProjectFormValues) {
    startTransition(async () => {
      const result = isEditing
        ? await updateProject({ ...values, id: project.id })
        : await createProject(values)

      if (!result.success) {
        // Set server-side field errors on the form
        if (result.fieldErrors) {
          for (const [field, errors] of Object.entries(result.fieldErrors)) {
            form.setError(field as keyof ProjectFormValues, {
              type: 'server',
              message: errors[0],
            })
          }
        } else {
          toast.error(result.error)
        }
        return
      }

      toast.success(isEditing ? 'Project updated' : 'Project created')
      router.push('/projects')
    })
  }

  return (
    <Form {...form}>
      <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-6">
        <FormField
          control={form.control}
          name="name"
          render={({ field }) => (
            <FormItem>
              <FormLabel>Project Name</FormLabel>
              <FormControl>
                <Input placeholder="My Awesome Project" {...field} />
              </FormControl>
              <FormMessage />
            </FormItem>
          )}
        />

        <FormField
          control={form.control}
          name="description"
          render={({ field }) => (
            <FormItem>
              <FormLabel>Description <span className="text-muted-foreground">(optional)</span></FormLabel>
              <FormControl>
                <Textarea
                  placeholder="What is this project about?"
                  className="resize-none"
                  rows={3}
                  {...field}
                />
              </FormControl>
              <FormMessage />
            </FormItem>
          )}
        />

        <FormField
          control={form.control}
          name="visibility"
          render={({ field }) => (
            <FormItem>
              <FormLabel>Visibility</FormLabel>
              <Select onValueChange={field.onChange} defaultValue={field.value}>
                <FormControl>
                  <SelectTrigger>
                    <SelectValue placeholder="Select visibility" />
                  </SelectTrigger>
                </FormControl>
                <SelectContent>
                  <SelectItem value="private">Private — only you</SelectItem>
                  <SelectItem value="public">Public — anyone with the link</SelectItem>
                </SelectContent>
              </Select>
              <FormMessage />
            </FormItem>
          )}
        />

        <div className="flex gap-3">
          <Button type="submit" disabled={isPending}>
            {isPending
              ? isEditing ? 'Saving…' : 'Creating…'
              : isEditing ? 'Save Changes' : 'Create Project'}
          </Button>
          <Button
            type="button"
            variant="outline"
            onClick={() => router.back()}
            disabled={isPending}
          >
            Cancel
          </Button>
        </div>
      </form>
    </Form>
  )
}
```

### 8. Create and Edit Pages

```typescript
// src/app/(dashboard)/projects/new/page.tsx
import { ProjectForm } from '@/features/projects/ui/project-form'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'

export const metadata = { title: 'New Project' }

export default function NewProjectPage() {
  return (
    <div className="mx-auto max-w-xl">
      <Card>
        <CardHeader>
          <CardTitle>Create Project</CardTitle>
        </CardHeader>
        <CardContent>
          <ProjectForm />
        </CardContent>
      </Card>
    </div>
  )
}
```

```typescript
// src/app/(dashboard)/projects/[projectId]/edit/page.tsx
import { auth } from '@/server/auth'
import { getProjectById } from '@/entities/project/queries'
import { ProjectForm } from '@/features/projects/ui/project-form'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { notFound, redirect } from 'next/navigation'

export default async function EditProjectPage({
  params,
}: {
  params: Promise<{ projectId: string }>
}) {
  const session = await auth()
  if (!session?.user?.id) redirect('/login')

  const { projectId } = await params
  const project = await getProjectById(projectId, session.user.id)
  if (!project) notFound()

  return (
    <div className="mx-auto max-w-xl">
      <Card>
        <CardHeader>
          <CardTitle>Edit Project</CardTitle>
        </CardHeader>
        <CardContent>
          <ProjectForm project={project} />
        </CardContent>
      </Card>
    </div>
  )
}
```

### Summary — The Pattern

```
┌─────────────────────────────────────────────────────┐
│ CRUD Flow                                            │
│                                                      │
│  schemas.ts ──────────────────────┐                  │
│      │ (Zod types)                │                  │
│      ├──► ProjectForm (client)    │                  │
│      │    react-hook-form         │                  │
│      │    zodResolver             │                  │
│      │                            │                  │
│      └──► actions.ts (server)     │                  │
│           auth() check            │                  │
│           zod.safeParse()         │                  │
│           db.insert/update/delete │                  │
│           revalidatePath()        │                  │
│           return ActionResult<T>  │                  │
│                                   │                  │
│  page.tsx (RSC)                   │                  │
│    await getProjects()  ──────────┘                  │
│    <ProjectList projects={...} />                    │
│                                                      │
│  ProjectList (client)                                │
│    useOptimistic for delete                          │
│    calls deleteProject() action                      │
└─────────────────────────────────────────────────────┘
```

## Антипаттерн

```typescript
// BAD 1: Form submitting to a Route Handler instead of Server Action
const onSubmit = async (data: ProjectFormValues) => {
  await fetch('/api/projects', {
    method: 'POST',
    body: JSON.stringify(data),
  })
}
// Loses type safety, requires manual error parsing, adds round-trip overhead

// BAD 2: No server-side validation — trusting zodResolver on client alone
export async function createProject(input: ProjectFormValues) {
  'use server'
  // Skipping zod.safeParse — the client could be tampered with
  await db.insert(projects).values({ ...input, userId: '...' })
}

// BAD 3: Fetching data in Client Component with useEffect
'use client'
function ProjectsPage() {
  const [projects, setProjects] = useState([])
  useEffect(() => {
    fetch('/api/projects').then(r => r.json()).then(d => setProjects(d.data))
  }, [])
  // Server Component + Drizzle query is 0 client JS, no loading state needed
}

// BAD 4: Not checking ownership before update/delete — IDOR vulnerability
export async function deleteProject(id: string) {
  'use server'
  const session = await auth()
  // Missing: verify session.user.id === project.userId
  await db.delete(projects).where(eq(projects.id, id))  // Any user can delete!
}
```

## Связанные документы

- `02-patterns/optimistic-ui.md` — Detailed optimistic update patterns
- `02-patterns/auth-flow.md` — Getting session in Server Actions
- `01-architecture/api-design.md` — When Server Actions vs Route Handlers
- `01-architecture/data-flow.md` — Where data fetching belongs
