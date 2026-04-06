---
id: "vercel-0492"
title: "Integrate flags with Vercel Web Analytics"
description: "Learn how to tag your page views and custom events with feature flags"
category: "vercel-flags"
subcategory: "flags"
type: "guide"
source: "https://vercel.com/docs/flags/observability/web-analytics"
tags: ["web-analytics", "observability", "feature-flags", "integrate", "web", "analytics"]
related: ["0491-observability-2.md", "0496-running-an-a-b-test.md", "0493-flags.md"]
last_updated: "2026-04-03T23:47:20.873Z"
---

# Integrate flags with Vercel Web Analytics

> **🔒 Permissions Required**: Web Analytics integration

![Image](`/docs-assets/static/docs/workflow-collaboration/feature-flags/flags-in-web-analytics-light.png`)

## Client-side tracking

Vercel Web Analytics can look up the values of evaluated feature flags in the DOM. It can then enrich page views and client-side events with these feature flags.

- ### Emit feature flags and connect them to Vercel Web Analytics
  To share your feature flags with Web Analytics you have to emit your feature flag values to the DOM as described in [Supporting Feature Flags](/docs/flags/flags-explorer/reference#values).

  This will automatically annotate all page views and client-side events with your feature flags.

- ### Tracking feature flags in client-side events
  Client-side events in Web Analytics will now automatically respect your flags and attach those to custom events.

  To manually overwrite the tracked flags for a specific `track` event, call:
  ```ts filename="component.ts"
  import { track } from '@vercel/analytics';

  track('My Event', {}, { flags: ['summer-sale'] });
  ```
  If the flag values on the client are encrypted, the entire encrypted string becomes part of the event payload. This can lead to the event getting reported without any flags when the encrypted string exceeds size limits.

## Server-side tracking

To track feature flags in server-side events:

1. First, report the feature flag value using `reportValue` to make the flag show up in [Runtime Logs](/docs/runtime-logs):

   ```ts {1, 8} filename="app/api/test/route.ts"
   import { reportValue } from 'flags';

   export async function GET() {
     reportValue('summer-sale', false);
     return Response.json({ ok: true });
   }
   ```

2. Once reported, any calls to `track` can look up the feature flag while handling a specific request:

   ```ts {1, 10} filename="app/api/test/route.ts"
   import { track } from '@vercel/analytics/server';
   import { reportValue } from 'flags';

   export async function GET() {
     reportValue('summer-sale', false);
     track('My Event', {}, { flags: ['summer-sale'] });

     return Response.json({ ok: true });
   }
   ```

> **💡 Note:** If you are using an implementation of the [Flags SDK](/docs/flags/flags-sdk-reference) you don't need to call
> `reportValue`. The respective implementation will automatically call
> `reportValue` for you.


