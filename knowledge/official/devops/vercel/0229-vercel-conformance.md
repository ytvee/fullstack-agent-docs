--------------------------------------------------------------------------------
title: "vercel-conformance"
description: "Learn how Conformance improves collaboration, productivity, and software quality at scale."
last_updated: "2026-04-03T23:47:17.900Z"
source: "https://vercel.com/docs/conformance/cli"
--------------------------------------------------------------------------------

# vercel-conformance

> **🔒 Permissions Required**: Conformance

The `vercel-conformance` command is used to run
[Conformance](/docs/conformance) on your code.

## Using the CLI

The Conformance CLI is separate to the [Vercel CLI](/docs/cli). However you
**must** ensure that the Vercel CLI is
[installed](/docs/cli#installing-vercel-cli) and that you are [logged
in](/docs/cli/login) to use the Conformance CLI.

## Sub-commands

The following sub-commands are available for this CLI.

### `audit`

The `audit` command runs Conformance on code without needing to install any NPM
dependencies or build any of the code. This is useful for viewing Conformance
results on a repository that you don't own and may not have permissions to
modify or build.

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

> **⚠️ Warning:** `yarn dlx` only works with Yarn version 2 or newer, for Yarn v1 use the npx
> command.

If you would like to store the results of the conformance audit in a file, you
can redirect `stderr` to a file:

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

### `init`

The `init` command installs Conformance in the repository. See
[Getting Started](/docs/conformance/getting-started#initialize-conformance) for more information on
using this command.


