---
id: "vercel-0217"
title: "Code Owners changelog"
description: "Find out what"
category: "vercel-code-owners"
subcategory: "code-owners"
type: "changelog"
source: "https://vercel.com/docs/code-owners/changelog"
tags: ["code-owners-changelog", "owners", "changelog", "upgrade-instructions", "releases", "1-0-7"]
related: ["0220-getting-started-with-code-owners.md", "0218-vercel-code-owners.md", "0221-code-owners.md"]
last_updated: "2026-04-03T23:47:17.744Z"
---

# Code Owners changelog

> **🔒 Permissions Required**: Code Owners

## Upgrade instructions

<CodeBlock>
  <Code tab="pnpm">
    ```bash
    pnpm i @vercel-private/code-owners
    ```
  </Code>
  <Code tab="yarn">
    ```bash
    yarn i @vercel-private/code-owners
    ```
  </Code>
  <Code tab="npm">
    ```bash
    npm i @vercel-private/code-owners
    ```
  </Code>
  <Code tab="bun">
    ```bash
    bun i @vercel-private/code-owners
    ```
  </Code>
</CodeBlock>

## Releases

### `1.0.7`

This patch adds support for underscores in usernames and team slugs to match Github.

### `1.0.6`

This patch updates the minimum length of Github username to match Github's validation.

### `1.0.5`

This patch updates some dependencies for performance and security.

### `1.0.4`

This patch updates some dependencies for performance and security.

### `1.0.3`

This patch updates some dependencies for performance and security, and fixes an
issue where CLI output was colorless in GitHub Actions.

### `1.0.2`

This patch updates some dependencies for performance and security.

### `1.0.1`

This patch delivers improvements to our telemetry. While these improvements
are not directly user-facing, they enhance our ability to monitor and optimize
performance.

### `1.0.0`

Initial release of Code Owners.


