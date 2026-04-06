---
id: "vercel-0135"
title: "Local Development Behavior"
description: "How BotID behaves in local development environments and testing options"
category: "vercel-security"
subcategory: "botid"
type: "guide"
source: "https://vercel.com/docs/botid/local-development-behavior"
tags: ["local", "development", "behavior", "local-development-behavior", "using-developmentoptions", "setup"]
related: ["0133-form-submissions.md", "0132-advanced-botid-configuration.md", "0134-get-started-with-botid.md"]
last_updated: "2026-04-03T23:47:16.304Z"
---

# Local Development Behavior

During local development, BotID behaves differently than in production to facilitate testing and development workflows. In development mode, `checkBotId()` always returns `{ isBot: false }`, allowing all requests to pass through. This ensures your development workflow isn't interrupted by bot protection while building and testing features.

### Using developmentOptions

If you need to test BotID's different return values in local development, you can use the `developmentBypass` option:

```ts filename="app/api/sensitive/route.ts"
import { checkBotId } from 'botid/server';
import { NextRequest, NextResponse } from 'next/server';

export async function POST(request: NextRequest) {
  const verification = await checkBotId({
    developmentOptions: {
      bypass: 'BAD-BOT', // default: 'HUMAN'
    },
  });

  if (verification.isBot) {
    return NextResponse.json({ error: 'Access denied' }, { status: 403 });
  }

  // Your protected logic here
}
```

> **💡 Note:** The `developmentOptions` option only works in development mode and is ignored
> in production. In production, BotID always performs real bot detection.

This allows you to:

- Test your bot handling logic without deploying to production
- Verify error messages and fallback behaviors
- Ensure your application correctly handles both human and bot traffic


