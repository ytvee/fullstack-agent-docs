---
id: "vercel-0303"
title: "WORKSPACE_MISSING_CONFORMANCE_SCRIPT"
description: "All packages must define a conformance script that invokes the Conformance package."
category: "vercel-conformance"
subcategory: "conformance"
type: "concept"
source: "https://vercel.com/docs/conformance/rules/WORKSPACE_MISSING_CONFORMANCE_SCRIPT"
tags: ["workspace", "missing", "script", "rules", "example", "how-to-fix"]
related: ["0304-workspace-missing-package-json.md", "0301-typescript-configuration.md", "0302-typescript-only.md"]
last_updated: "2026-04-03T23:47:18.459Z"
---

# WORKSPACE_MISSING_CONFORMANCE_SCRIPT

> **🔒 Permissions Required**: Conformance

Conformance requires a script to exist in every workspace in the
repository. This makes sure that Conformance rules are running on all code.
This test throws an error if a workspace does not define a `conformance` script
in the `package.json` file.

## Example

A workspace contains a `package.json` file that looks like:

```json filename="package.json"
{
  "name": "test-workspace",
  "scripts": {
    "build": "tsc -b"
  }
}
```

It does not contain a `conformance` script, so this check will fail.

## How to fix

Install the `@vercel-private/conformance` package in this workspace and define
a `conformance` script in the `package.json` file.

```json filename="package.json"
{
  "name": "test-workspace",
  "scripts": {
    "build": "tsc -b",
    "conformance": "vercel conformance"
  },
  "devDependencies": {
    "@vercel-private/conformance": "^1.0.0"
  }
}
```


