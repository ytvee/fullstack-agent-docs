---
id: "vercel-0497"
title: "Setting up Flags Explorer"
description: "Add the Flags Explorer to the Vercel Toolbar so you can override flag values on preview deployments without affecting other users."
category: "vercel-flags"
subcategory: "flags"
type: "guide"
source: "https://vercel.com/docs/flags/vercel-flags/cli/set-up-flags-explorer"
tags: ["setting-up-flags-explorer", "preview-deployments", "flags-explorer", "setting", "up", "explorer"]
related: ["0496-running-an-a-b-test.md", "0494-cleaning-up-after-a-full-rollout.md", "0485-getting-started-with-flags-explorer.md"]
last_updated: "2026-04-03T23:47:20.911Z"
---

# Setting up Flags Explorer

The [Flags Explorer](/docs/flags/flags-explorer) adds a panel to the [Vercel Toolbar](/docs/vercel-toolbar) that lets you override flag values on preview deployments. Make sure you've [set up the toolbar](/docs/vercel-toolbar) first. This is a one-time setup per project.

## 1. Create a Flags Discovery Endpoint

The Flags Explorer reads flag metadata from a well-known API route:

```ts filename="app/.well-known/vercel/flags/route.ts"
import { createFlagsDiscoveryEndpoint, getProviderData } from 'flags/next';
import * as flags from '../../../../flags';

export const GET = createFlagsDiscoveryEndpoint(async () => {
  return getProviderData(flags);
});
```

This endpoint uses the `FLAGS_SECRET` environment variable to authenticate requests. Make sure you've pulled it with `vercel env pull`.

## 2. Deploy to preview

```bash filename="terminal"
vercel deploy
```

## 3. Use the toolbar

Visit the preview URL. The Flags Explorer panel appears in the Vercel Toolbar. Toggle any flag to override its value for your session without affecting other users.

See [Flags Explorer](/docs/flags/flags-explorer/getting-started) for the full setup guide, including how to share overrides with teammates via URL.


