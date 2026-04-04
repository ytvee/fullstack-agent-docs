---
category: patterns
topic: payments
status: draft
---

## Проблема / Контекст

Интеграция Stripe для SaaS-приложений требует: создания покупателя, checkout сессий, биллинг-портала, обработки webhook-ов и хранения статуса подписки в БД. Критически важно: вся бизнес-логика должна реагировать на webhook-и, а не на redirect после оплаты — пользователь может закрыть браузер до редиректа.

Ключевые сценарии:
- Новый пользователь оформляет подписку
- Обновление тарифа (upgrade/downgrade)
- Отмена и возобновление подписки
- Обработка failed payments
- Биллинг-портал для управления картой и счетами

## Решение

**Архитектура:** Server Actions создают Stripe объекты и редиректят. Webhook handler (`/api/webhooks/stripe`) обрабатывает события и обновляет БД. `useSubscription` хук читает состояние из БД через Zustand store. Никогда не доверяй клиентским данным о статусе — только БД, синхронизированная через webhook-и.

**Установка:**
```bash
npm install stripe @stripe/stripe-js
```

**Переменные окружения:**
```env
STRIPE_SECRET_KEY=sk_live_...         # никогда не NEXT_PUBLIC_
STRIPE_WEBHOOK_SECRET=whsec_...
NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY=pk_live_...
NEXT_PUBLIC_APP_URL=https://yourapp.com
```

## Пример кода

### 1. Drizzle схема для подписок

```typescript
// src/db/schema/subscriptions.ts
import { pgTable, text, timestamp, uuid, pgEnum, boolean } from "drizzle-orm/pg-core";
import { users } from "./users";

export const subscriptionStatusEnum = pgEnum("subscription_status", [
  "active",
  "canceled",
  "incomplete",
  "incomplete_expired",
  "past_due",
  "trialing",
  "unpaid",
  "paused",
]);

export const subscriptions = pgTable("subscriptions", {
  id: uuid("id").primaryKey().defaultRandom(),
  userId: uuid("user_id")
    .notNull()
    .unique() // один пользователь = одна подписка
    .references(() => users.id, { onDelete: "cascade" }),
  stripeCustomerId: text("stripe_customer_id").unique(),
  stripeSubscriptionId: text("stripe_subscription_id").unique(),
  stripePriceId: text("stripe_price_id"),
  stripeCurrentPeriodEnd: timestamp("stripe_current_period_end"),
  status: subscriptionStatusEnum("status").notNull().default("incomplete"),
  cancelAtPeriodEnd: boolean("cancel_at_period_end").notNull().default(false),
  createdAt: timestamp("created_at").defaultNow().notNull(),
  updatedAt: timestamp("updated_at").defaultNow().notNull(),
});

export type Subscription = typeof subscriptions.$inferSelect;
```

### 2. Stripe singleton

```typescript
// src/lib/stripe.ts
import Stripe from "stripe";

// Используем единственный инстанс во всём серверном коде
export const stripe = new Stripe(process.env.STRIPE_SECRET_KEY!, {
  apiVersion: "2024-11-20.acacia",
  typescript: true,
});

// Хелпер: получить или создать Stripe customer для пользователя
export async function getOrCreateStripeCustomer(
  userId: string,
  email: string,
  name?: string | null
): Promise<string> {
  // Сначала проверяем БД
  const { db } = await import("@/db");
  const { subscriptions } = await import("@/db/schema/subscriptions");
  const { eq } = await import("drizzle-orm");

  const existing = await db.query.subscriptions.findFirst({
    where: eq(subscriptions.userId, userId),
    columns: { stripeCustomerId: true },
  });

  if (existing?.stripeCustomerId) {
    return existing.stripeCustomerId;
  }

  // Создаём нового customer в Stripe
  const customer = await stripe.customers.create({
    email,
    name: name ?? undefined,
    metadata: { userId }, // важно для reconciliation
  });

  // Сохраняем или обновляем в БД
  await db
    .insert(subscriptions)
    .values({
      userId,
      stripeCustomerId: customer.id,
      status: "incomplete",
    })
    .onConflictDoUpdate({
      target: subscriptions.userId,
      set: { stripeCustomerId: customer.id },
    });

  return customer.id;
}
```

### 3. Server Actions для Stripe операций

```typescript
// src/actions/billing.ts
"use server";

import { redirect } from "next/navigation";
import { auth } from "@/lib/auth";
import { stripe, getOrCreateStripeCustomer } from "@/lib/stripe";
import { db } from "@/db";
import { subscriptions } from "@/db/schema/subscriptions";
import { eq } from "drizzle-orm";

// Создать checkout сессию для новой подписки
export async function createCheckoutSession(priceId: string): Promise<never> {
  const session = await auth();
  if (!session?.user?.id || !session.user.email) {
    redirect("/login");
  }

  const customerId = await getOrCreateStripeCustomer(
    session.user.id,
    session.user.email,
    session.user.name
  );

  const checkoutSession = await stripe.checkout.sessions.create({
    customer: customerId,
    mode: "subscription",
    payment_method_types: ["card"],
    line_items: [{ price: priceId, quantity: 1 }],
    success_url: `${process.env.NEXT_PUBLIC_APP_URL}/billing?success=true`,
    cancel_url: `${process.env.NEXT_PUBLIC_APP_URL}/pricing`,
    subscription_data: {
      metadata: { userId: session.user.id },
      trial_period_days: 14, // 14-дневный trial
    },
    // Разрешаем промокоды
    allow_promotion_codes: true,
    // Автоматически применяем налоги если настроены в Stripe
    automatic_tax: { enabled: true },
    customer_update: {
      address: "auto", // обновляем адрес customer для налогов
    },
  });

  if (!checkoutSession.url) throw new Error("Failed to create checkout session");
  redirect(checkoutSession.url);
}

// Открыть Stripe billing portal
export async function createBillingPortalSession(): Promise<never> {
  const session = await auth();
  if (!session?.user?.id) {
    redirect("/login");
  }

  const subscription = await db.query.subscriptions.findFirst({
    where: eq(subscriptions.userId, session.user.id),
    columns: { stripeCustomerId: true },
  });

  if (!subscription?.stripeCustomerId) {
    redirect("/pricing");
  }

  const portalSession = await stripe.billingPortal.sessions.create({
    customer: subscription.stripeCustomerId,
    return_url: `${process.env.NEXT_PUBLIC_APP_URL}/billing`,
  });

  redirect(portalSession.url);
}

// Получить статус подписки (для Server Components)
export async function getSubscriptionStatus() {
  const session = await auth();
  if (!session?.user?.id) return null;

  return db.query.subscriptions.findFirst({
    where: eq(subscriptions.userId, session.user.id),
  });
}
```

### 4. Webhook handler — критически важная часть

```typescript
// src/app/api/webhooks/stripe/route.ts
import { headers } from "next/headers";
import { NextResponse } from "next/server";
import type Stripe from "stripe";
import { stripe } from "@/lib/stripe";
import { db } from "@/db";
import { subscriptions } from "@/db/schema/subscriptions";
import { eq } from "drizzle-orm";

// Обязательно: отключаем body parsing для верификации подписи
export const runtime = "nodejs"; // edge не поддерживает getRawBody

async function handleSubscriptionUpsert(
  stripeSubscription: Stripe.Subscription
): Promise<void> {
  const userId = stripeSubscription.metadata?.userId;
  if (!userId) {
    console.error("Subscription without userId metadata:", stripeSubscription.id);
    return;
  }

  const priceId = stripeSubscription.items.data[0]?.price.id ?? null;
  const currentPeriodEnd = stripeSubscription.current_period_end
    ? new Date(stripeSubscription.current_period_end * 1000)
    : null;

  await db
    .insert(subscriptions)
    .values({
      userId,
      stripeSubscriptionId: stripeSubscription.id,
      stripeCustomerId:
        typeof stripeSubscription.customer === "string"
          ? stripeSubscription.customer
          : stripeSubscription.customer.id,
      stripePriceId: priceId,
      stripeCurrentPeriodEnd: currentPeriodEnd,
      status: stripeSubscription.status,
      cancelAtPeriodEnd: stripeSubscription.cancel_at_period_end,
    })
    .onConflictDoUpdate({
      target: subscriptions.userId,
      set: {
        stripeSubscriptionId: stripeSubscription.id,
        stripePriceId: priceId,
        stripeCurrentPeriodEnd: currentPeriodEnd,
        status: stripeSubscription.status,
        cancelAtPeriodEnd: stripeSubscription.cancel_at_period_end,
        updatedAt: new Date(),
      },
    });
}

export async function POST(req: Request) {
  const body = await req.text();
  const headersList = await headers();
  const signature = headersList.get("stripe-signature");

  if (!signature) {
    return NextResponse.json({ error: "Missing signature" }, { status: 400 });
  }

  let event: Stripe.Event;

  try {
    event = stripe.webhooks.constructEvent(
      body,
      signature,
      process.env.STRIPE_WEBHOOK_SECRET!
    );
  } catch (error) {
    console.error("Webhook signature verification failed:", error);
    return NextResponse.json({ error: "Invalid signature" }, { status: 400 });
  }

  try {
    switch (event.type) {
      // Пользователь успешно оформил подписку через checkout
      case "checkout.session.completed": {
        const session = event.data.object as Stripe.Checkout.Session;
        if (session.mode !== "subscription") break;

        // Загружаем полный subscription объект
        const subscription = await stripe.subscriptions.retrieve(
          session.subscription as string
        );
        await handleSubscriptionUpsert(subscription);
        break;
      }

      // Обновление подписки: upgrade, downgrade, возобновление
      case "customer.subscription.updated": {
        const subscription = event.data.object as Stripe.Subscription;
        await handleSubscriptionUpsert(subscription);
        break;
      }

      // Удаление/отмена подписки
      case "customer.subscription.deleted": {
        const subscription = event.data.object as Stripe.Subscription;
        await db
          .update(subscriptions)
          .set({
            status: "canceled",
            stripeSubscriptionId: null,
            stripePriceId: null,
            updatedAt: new Date(),
          })
          .where(eq(subscriptions.stripeSubscriptionId, subscription.id));
        break;
      }

      // Неудачный платёж
      case "invoice.payment_failed": {
        const invoice = event.data.object as Stripe.Invoice;
        if (invoice.subscription) {
          await db
            .update(subscriptions)
            .set({ status: "past_due", updatedAt: new Date() })
            .where(
              eq(subscriptions.stripeSubscriptionId, invoice.subscription as string)
            );
          // TODO: отправить email через Resend
        }
        break;
      }

      default:
        // Логируем необработанные события для мониторинга
        console.log(`Unhandled Stripe event: ${event.type}`);
    }

    return NextResponse.json({ received: true });
  } catch (error) {
    console.error(`Error processing webhook ${event.type}:`, error);
    // Возвращаем 500 — Stripe будет ретраить
    return NextResponse.json({ error: "Webhook handler failed" }, { status: 500 });
  }
}
```

### 5. Zustand store для подписки

```typescript
// src/stores/subscription-store.ts
import { create } from "zustand";
import type { Subscription } from "@/db/schema/subscriptions";

interface SubscriptionStore {
  subscription: Subscription | null;
  isLoading: boolean;
  setSubscription: (sub: Subscription | null) => void;
  setLoading: (loading: boolean) => void;
}

export const useSubscriptionStore = create<SubscriptionStore>((set) => ({
  subscription: null,
  isLoading: true,
  setSubscription: (subscription) => set({ subscription, isLoading: false }),
  setLoading: (isLoading) => set({ isLoading }),
}));
```

### 6. Хук useSubscription

```typescript
// src/hooks/use-subscription.ts
"use client";

import { useEffect } from "react";
import { useSubscriptionStore } from "@/stores/subscription-store";
import type { Subscription } from "@/db/schema/subscriptions";

// Инициализируется данными с сервера через Server Component
export function useSubscription() {
  const { subscription, isLoading } = useSubscriptionStore();

  const isActive =
    subscription?.status === "active" || subscription?.status === "trialing";

  const isPastDue = subscription?.status === "past_due";

  const isCanceled = subscription?.status === "canceled";

  const willCancelAtPeriodEnd = subscription?.cancelAtPeriodEnd === true;

  // Проверка доступа к фиче по тарифу
  const hasPlan = (priceId: string) => subscription?.stripePriceId === priceId;

  return {
    subscription,
    isLoading,
    isActive,
    isPastDue,
    isCanceled,
    willCancelAtPeriodEnd,
    hasPlan,
  };
}

// Клиентский провайдер для инициализации store
// src/components/providers/subscription-provider.tsx
"use client";

import { useEffect } from "react";
import { useSubscriptionStore } from "@/stores/subscription-store";
import type { Subscription } from "@/db/schema/subscriptions";

export function SubscriptionProvider({
  subscription,
  children,
}: {
  subscription: Subscription | null;
  children: React.ReactNode;
}) {
  const setSubscription = useSubscriptionStore((s) => s.setSubscription);

  useEffect(() => {
    setSubscription(subscription);
  }, [subscription, setSubscription]);

  return <>{children}</>;
}
```

### 7. Server Component для инициализации + UI

```typescript
// src/app/(app)/billing/page.tsx
import { getSubscriptionStatus } from "@/actions/billing";
import { SubscriptionProvider } from "@/components/providers/subscription-provider";
import { BillingPageClient } from "./billing-client";
import { PLANS } from "@/lib/plans";

export default async function BillingPage() {
  const subscription = await getSubscriptionStatus();

  return (
    <SubscriptionProvider subscription={subscription}>
      <BillingPageClient plans={PLANS} />
    </SubscriptionProvider>
  );
}

// src/app/(app)/billing/billing-client.tsx
"use client";

import { useSubscription } from "@/hooks/use-subscription";
import { createCheckoutSession, createBillingPortalSession } from "@/actions/billing";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";

export function BillingPageClient({ plans }: { plans: Plan[] }) {
  const { subscription, isActive, isPastDue, willCancelAtPeriodEnd } =
    useSubscription();

  return (
    <div className="space-y-6">
      {/* Текущий статус */}
      {subscription && (
        <div className="rounded-lg border p-4">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm text-muted-foreground">Текущий план</p>
              <p className="font-medium">
                {plans.find((p) => p.priceId === subscription.stripePriceId)?.name ?? "Unknown"}
              </p>
            </div>
            <Badge variant={isActive ? "default" : "destructive"}>
              {subscription.status}
            </Badge>
          </div>
          {willCancelAtPeriodEnd && (
            <p className="mt-2 text-sm text-amber-600">
              Подписка отменена и закончится{" "}
              {subscription.stripeCurrentPeriodEnd?.toLocaleDateString("ru-RU")}
            </p>
          )}
          {isPastDue && (
            <p className="mt-2 text-sm text-red-600">
              Проблема с оплатой. Пожалуйста, обновите платёжные данные.
            </p>
          )}
        </div>
      )}

      {/* Управление подпиской */}
      {isActive ? (
        <form action={createBillingPortalSession}>
          <Button type="submit" variant="outline">
            Управление подпиской
          </Button>
        </form>
      ) : (
        <div className="grid gap-4 sm:grid-cols-2">
          {plans.map((plan) => (
            <div key={plan.priceId} className="rounded-lg border p-4">
              <h3 className="font-medium">{plan.name}</h3>
              <p className="text-2xl font-bold">{plan.price}</p>
              <form action={createCheckoutSession.bind(null, plan.priceId)}>
                <Button type="submit" className="mt-4 w-full">
                  Подписаться
                </Button>
              </form>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
```

### 8. Локальное тестирование со Stripe CLI

```bash
# Установка Stripe CLI
brew install stripe/stripe-cli/stripe

# Авторизация
stripe login

# Перенаправление webhook-ов на локальный сервер
stripe listen --forward-to localhost:3000/api/webhooks/stripe

# CLI выведет webhook secret — скопируй в .env.local:
# STRIPE_WEBHOOK_SECRET=whsec_...

# Тестовые события
stripe trigger checkout.session.completed
stripe trigger customer.subscription.updated
stripe trigger customer.subscription.deleted
stripe trigger invoice.payment_failed

# Проверка конкретного события
stripe events resend evt_...
```

### 9. Middleware защита платных роутов

```typescript
// src/middleware.ts (добавить к существующему)
import { getSubscriptionStatus } from "@/actions/billing";

// В middleware проверяем доступ к premium роутам
const PREMIUM_ROUTES = ["/app/advanced", "/app/export", "/app/api"];

// Лучший подход — через Edge-совместимый JWT claim
// Добавляй isSubscribed в JWT при авторизации через Auth.js callback
```

## Антипаттерн

```typescript
// ПЛОХО: Доверяем redirect параметру вместо webhook
// src/app/billing/success/page.tsx
export default async function SuccessPage({
  searchParams,
}: {
  searchParams: { session_id: string };
}) {
  // НИКОГДА так не делай — пользователь может подделать URL
  // или закрыть браузер до редиректа
  await db.update(users).set({ isPremium: true }); // ← ОПАСНО
  return <div>Спасибо за подписку!</div>;
}

// ПЛОХО: Не верифицируем подпись webhook
export async function POST(req: Request) {
  const body = await req.json(); // ← Нет верификации!
  // Злоумышленник может отправить любое событие
  await db.update(users).set({ isPremium: true });
}

// ПЛОХО: Храним Stripe secret в переменной с NEXT_PUBLIC_
// .env
NEXT_PUBLIC_STRIPE_SECRET_KEY=sk_live_... // ← УТЕЧКА КЛЮЧА В БРАУЗЕР
```

**Правила:**
1. Вся бизнес-логика обновления статуса — только в webhook handler
2. Всегда верифицируй подпись через `stripe.webhooks.constructEvent`
3. Webhook handler должен быть идемпотентным (один и тот же event может прийти дважды)
4. Используй `metadata.userId` в Stripe объектах для связки с БД
5. STRIPE_SECRET_KEY — только серверная переменная, без NEXT_PUBLIC_

## Связанные документы

- `knowledge/custom/02-patterns/rbac.md` — ограничение доступа по тарифу
- `knowledge/custom/03-antipatterns/secrets-exposure.md` — защита Stripe ключей
- `knowledge/custom/06-security/` — общая безопасность платёжных данных
