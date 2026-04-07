---
id: "vercel-0171"
title: "vercel certs"
description: "Learn how to manage certificates for your domains using the vercel certs CLI command."
category: "vercel-cli"
subcategory: "cli"
type: "api-reference"
source: "https://vercel.com/docs/cli/certs"
tags: ["ssl", "certs", "usage", "extended-usage", "unique-options", "challenge-only"]
related: ["0177-vercel-dns.md", "0178-vercel-domains.md", "0170-vercel-cache.md"]
last_updated: "2026-04-03T23:47:17.199Z"
---

# vercel certs

The `vercel certs` command is used to manage certificates for domains, providing functionality to list, issue, and remove them. Vercel manages certificates for domains automatically.

## Usage

```bash filename="terminal"
vercel certs ls
```

*Using the \`vercel certs\` command to list all
certificates under the current scope.*

## Extended Usage

```bash filename="terminal"
vercel certs issue [domain1, domain2, domain3]
```

*Using the \`vercel certs\` command to issue certificates
for multiple domains.*

```bash filename="terminal"
vercel certs rm [certificate-id]
```

*Using the \`vercel certs\` command to remove a
certificate by ID.*

## Unique Options

These are options that only apply to the `vercel certs` command.

### Challenge Only

The `--challenge-only` option can be used to only show the challenges needed to issue a certificate.

```bash filename="terminal"
vercel certs issue foo.com --challenge-only
```

*Using the \`vercel certs\` command with the
\`--challenge-only\` option.*

### Limit

The `--limit` option can be used to specify the maximum number of certs returned when using `ls`. The default value is `20` and the maximum is `100`.

```bash filename="terminal"
vercel certs ls --limit 100
```

*Using the \`vercel certs ls\` command with the
\`--limit\` option.*

## Global Options

The following [global options](/docs/cli/global-options) can be passed when using the  command:

- [`--cwd`](/docs/cli/global-options#current-working-directory)
- [`--debug`](/docs/cli/global-options#debug)
- [`--global-config`](/docs/cli/global-options#global-config)
- [`--help`](/docs/cli/global-options#help)
- [`--local-config`](/docs/cli/global-options#local-config)
- [`--no-color`](/docs/cli/global-options#no-color)
- [`--scope`](/docs/cli/global-options#scope)
- [`--token`](/docs/cli/global-options#token)

For more information on global options and their usage, refer to the [options section](/docs/cli/global-options).


