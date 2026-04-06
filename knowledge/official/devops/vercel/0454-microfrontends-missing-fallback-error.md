---
id: "vercel-0454"
title: "MICROFRONTENDS_MISSING_FALLBACK_ERROR"
description: "The microfrontend request did not have a fallback for the environment."
category: "vercel-errors"
subcategory: "errors"
type: "guide"
source: "https://vercel.com/docs/errors/MICROFRONTENDS_MISSING_FALLBACK_ERROR"
tags: ["microfrontends", "missing", "fallback", "error", "troubleshoot", "setup"]
related: ["0441-internal-microfrontends-build-error.md", "0443-internal-microfrontends-unexpected-error.md", "0453-microfrontends-middleware-error.md"]
last_updated: "2026-04-03T23:47:20.522Z"
---

# MICROFRONTENDS_MISSING_FALLBACK_ERROR

The `MICROFRONTENDS_MISSING_FALLBACK_ERROR` error occurs when a microfrontends request did not match any other deployments in the same environment, and no deployment could be found for the specified fallback.

## Troubleshoot

To troubleshoot this error, follow these steps:

In the [Production](/docs/deployments/environments#production-environment) environment, this error should not occur since every request is routed to the Production environment of mcirofrontends projects. Make sure that every project in the microfrontends group has a production deployment.

In non-Production environments, the fallback is configured in the [Fallback Environment](/docs/microfrontends/managing-microfrontends#fallback-environment) setting. Based on the configured option, check that every project has a deployment for that environment.

If the issue persists after checking that every project has a deployment in the configured Fallback Environment setting, please contact Vercel support to reach out to the team.


