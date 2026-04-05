--------------------------------------------------------------------------------
title: "INTERNAL_UNARCHIVE_FAILED"
description: "Unarchiving of the deployment or resource failed. This is an internal error."
last_updated: "2026-04-03T23:47:20.492Z"
source: "https://vercel.com/docs/errors/INTERNAL_UNARCHIVE_FAILED"
--------------------------------------------------------------------------------

# INTERNAL_UNARCHIVE_FAILED

The `INTERNAL_UNARCHIVE_FAILED` error typically occurs when the platform encounters a problem trying to extract your deployment's archive. This issue often can be related to one of the following:

- The structure of your project or the contents within it
- The size of your deployment bundle for Vercel functions exceeds the limit. For Vercel functions, the [maximum uncompressed size is 250 MB](/docs/functions/runtimes#bundle-size-limits)

**Error Code:** `500`

**Name:** Internal Server Error

## Troubleshoot

To troubleshoot this error, follow these steps:

- **Check your project files**: Check for any files or directories that have been unnecessarily included in the deployment. Removing unnecessary files or directories can help reduce the size of your deployment
- **Check bundle size**: Looking into your `includeFiles` and `excludeFiles` configuration to specify items affecting the function size. See [bundle size limits](/docs/functions/runtimes#bundle-size-limits)


