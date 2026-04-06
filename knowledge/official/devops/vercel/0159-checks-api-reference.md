---
id: "vercel-0159"
title: "Checks API Reference"
description: "The Vercel Checks API let you create tests and assertions that run after each deployment has been built, and are powered by Vercel Integrations."
category: "vercel-checks"
subcategory: "checks"
type: "api-reference"
source: "https://vercel.com/docs/checks/checks-api"
tags: ["checks-api-reference", "checks-api", "api-reference", "cli-command"]
related: ["0160-anatomy-of-the-checks-api.md", "0161-working-with-checks.md", "0188-vercel-install.md"]
last_updated: "2026-04-03T23:47:16.989Z"
---

# Checks API Reference

API endpoints allow integrations to interact with the Vercel platform. Integrations can run checks every time you create a deployment.

> **💡 Note:** The `post` and `patch` endpoints
> must be called with an OAuth2, or it will produce a
> `400` error.


