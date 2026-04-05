--------------------------------------------------------------------------------
title: "SANBDOX_STOPPED"
description: "The Sandbox was stopped and is no longer reachable. This is a platform error."
last_updated: "2026-04-03T23:47:20.655Z"
source: "https://vercel.com/docs/errors/SANDBOX_STOPPED"
--------------------------------------------------------------------------------

# SANBDOX_STOPPED

The `SANDBOX_STOPPED` error occurs when you are trying to access a Sandbox that has been stopped. This could happen if the Sandbox was manually stopped by the owner, or if the Sandbox reached its configured timeout.

**Error Code:** `410`

**Name:** Gone

## Troubleshoot

To troubleshoot this error, follow these steps:

1. **Verify the Sandbox status:** Navigate to the [Sandboxes dashboard](/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Fobservability%2Fsandboxes\&title=Go+to+Sandboxes), select the one you are accessing, and check the history section to know why it was stopped
2. **Increase the timeout:** By default, Sandboxes have a timeout of 10 minutes. You can increase the timeout by passing the `timeout` property to the `Sandbox.create()` method (http://localhost:3024/docs/vercel-sandbox/sdk-reference#sandbox.create).


