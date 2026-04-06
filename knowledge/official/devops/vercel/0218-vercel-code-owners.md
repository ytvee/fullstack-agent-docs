---
id: "vercel-0218"
title: "vercel-code-owners"
description: "Learn how to use Code Owners with the CLI."
category: "vercel-code-owners"
subcategory: "code-owners"
type: "guide"
source: "https://vercel.com/docs/code-owners/cli"
tags: ["owners", "cli", "using-the-cli", "sub-commands", "init", "validate"]
related: ["0220-getting-started-with-code-owners.md", "0217-code-owners-changelog.md", "0221-code-owners.md"]
last_updated: "2026-04-03T23:47:17.748Z"
---

# vercel-code-owners

> **🔒 Permissions Required**: Conformance

The `vercel-code-owners` command provides functionality to initialize and validate
Code Owners in your repository.

## Using the CLI

The Code Owners CLI is separate to the [Vercel CLI](/docs/cli). However you
**must** ensure that the Vercel CLI is
[installed](/docs/cli#installing-vercel-cli) and that you are [logged
in](/docs/cli/login) to use the Code Owners CLI.

## Sub-commands

The following sub-commands are available for this CLI.

### `init`

The `init` command sets up code owners files in the repository. See
[Getting Started](/docs/code-owners/getting-started#initalizing-code-owners) for more information on
using this command.

### `validate`

The `validate` command checks the syntax for all Code Owners files in the
repository for errors.

<CodeBlock>
  <Code tab="pnpm">
    ```bash
    pnpm i 
    ```
  </Code>
  <Code tab="yarn">
    ```bash
    yarn i 
    ```
  </Code>
  <Code tab="npm">
    ```bash
    npm i 
    ```
  </Code>
  <Code tab="bun">
    ```bash
    bun i 
    ```
  </Code>
</CodeBlock>


