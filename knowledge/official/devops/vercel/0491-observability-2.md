---
id: "vercel-0491"
title: "Observability"
description: "Track feature flag evaluations and analyze their impact with Web Analytics."
category: "vercel-flags"
subcategory: "flags"
type: "concept"
source: "https://vercel.com/docs/flags/observability"
tags: ["web-analytics", "observability", "feature-flags", "why-track-flag-evaluations", "observability-options", "how-it-works"]
related: ["0492-integrate-flags-with-vercel-web-analytics.md", "0496-running-an-a-b-test.md", "0506-vercel-flags-2.md"]
last_updated: "2026-04-03T23:47:20.866Z"
---

# Observability

Feature flags play a crucial role in the software development lifecycle, enabling safe feature rollouts, experimentation, and A/B testing. When you integrate your feature flags with the Vercel platform, you can improve your application by using Vercel's observability features.

## Why track flag evaluations?

Tracking which flags are evaluated and when gives you insights into:

- How features perform in production
- Which user segments see which features
- The correlation between flags and application metrics
- Issues related to specific flag configurations

## Observability options

## How it works

The observability integration works by reporting flag values as your application evaluates them:

1. When your code evaluates a flag, call `reportValue(flagKey, flagValue)`
2. Vercel captures these evaluations and associates them with the request or event
3. View the data in the Web Analytics dashboard

If you're using the Flags SDK, flag reporting happens automatically—no manual instrumentation required.

## Next steps

- [Integrate flags with Web Analytics](/docs/flags/observability/web-analytics)
- [Learn about the Flags SDK](/docs/flags/flags-sdk-reference)


