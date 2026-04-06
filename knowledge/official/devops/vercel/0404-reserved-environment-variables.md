---
id: "vercel-0404"
title: "Reserved environment variables"
description: "Reserved environment variables are reserved by Vercel Vercel Function runtimes."
category: "vercel-environment-variables"
subcategory: "environment-variables"
type: "concept"
source: "https://vercel.com/docs/environment-variables/reserved-environment-variables"
tags: ["aws-lambda", "runtime", "restrictions", "node-js", "function-runtime"]
related: ["0403-environment-variables.md", "0408-system-environment-variables.md", "0400-framework-environment-variables.md"]
last_updated: "2026-04-03T23:47:20.222Z"
---

# Reserved environment variables

The following [environment variable](/docs/environment-variables) names are [reserved](https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html#configuration-envvars-runtime) and therefore unavailable for use:

- `AWS_SECRET_KEY`
- `AWS_EXECUTION_ENV`
- `AWS_LAMBDA_LOG_GROUP_NAME`
- `AWS_LAMBDA_LOG_STREAM_NAME`
- `AWS_LAMBDA_FUNCTION_NAME`
- `AWS_LAMBDA_FUNCTION_MEMORY_SIZE`
- `AWS_LAMBDA_FUNCTION_VERSION`
- `NOW_REGION`
- `TZ`
- `LAMBDA_TASK_ROOT`
- `LAMBDA_RUNTIME_DIR`

## Allowed environment variables

The following [environment variable](/docs/environment-variables) names are [allowed](/kb/guide/how-can-i-use-aws-sdk-environment-variables-on-vercel) by Vercel Vercel Function runtimes:

- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_SESSION_TOKEN`
- `AWS_REGION`
- `AWS_DEFAULT_REGION`

> **💡 Note:** These variables may appear in your Vercel Functions even if you don't set them in your project explicitly. These values do not grant any AWS permissions and are not usable as AWS credentials. Configure your own AWS credentials using environment variables or set up [OIDC](/docs/oidc/aws).


