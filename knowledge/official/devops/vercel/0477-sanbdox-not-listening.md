---
id: "vercel-0477"
title: "SANBDOX_NOT_LISTENING"
description: "The Sandbox is not listening on the requested port. This is an application error."
category: "vercel-errors"
subcategory: "errors"
type: "guide"
source: "https://vercel.com/docs/errors/SANDBOX_NOT_LISTENING"
tags: ["sanbdox-not-listening", "sanbdox", "not", "listening", "sandbox-not-listening", "troubleshoot"]
related: ["0476-sanbdox-not-found.md", "0458-not-found.md", "0478-sanbdox-stopped.md"]
last_updated: "2026-04-03T23:47:20.651Z"
---

# SANBDOX_NOT_LISTENING

The `SANDBOX_NOT_LISTENING` error occurs when you are trying to access a Sandbox that is not listening on the requested port. This could happen if the port is malconfigured, or the process running on that port has exited.

**Error Code:** `502`

**Name:** Bad Gateway

## Troubleshoot

To troubleshoot this error, follow these steps:

1. **Verify the configured port:** Make sure that the `ports` field used in `Sandbox.create` matches the port your application is listening on. Follow the [documentation](/docs/vercel-sandbox) to learn more
2. **Check the Sandbox history:** Navigate to the [Sandboxes dashboard](/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Fobservability%2Fsandboxes\&title=Go+to+Sandboxes), select the one you are accessing, and check the history section to see which commands were run and if any errors occurred


