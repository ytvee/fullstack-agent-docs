--------------------------------------------------------------------------------
title: "MICROFRONTENDS_MIDDLEWARE_ERROR"
description: "The microfrontend middleware returned an invalid application."
last_updated: "2026-04-03T23:47:20.510Z"
source: "https://vercel.com/docs/errors/MICROFRONTENDS_MIDDLEWARE_ERROR"
--------------------------------------------------------------------------------

# MICROFRONTENDS_MIDDLEWARE_ERROR

The `MICROFRONTENDS_MIDDLEWARE_ERROR` error occurs when the middleware returned a header `x-vercel-mfe-zone` with an invalid value. The value must be a name of an application from `microfrontends.json`.

## Troubleshoot

To troubleshoot this error, follow these steps:

1. If you are setting the header, ensure that the value is a valid application name.
2. If you are not setting the header, this is an error caused by the [@vercel/microfrontends](https://www.npmjs.com/package/@vercel/microfrontends) package. Please [open an issue](https://github.com/vercel/microfrontends/issues) and include the error message.


