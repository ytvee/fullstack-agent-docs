---
id: "vercel-0304"
title: "WORKSPACE_MISSING_PACKAGE_JSON"
description: "All directories that match a workspace glob must include a package.json file."
category: "vercel-conformance"
subcategory: "conformance"
type: "concept"
source: "https://vercel.com/docs/conformance/rules/WORKSPACE_MISSING_PACKAGE_JSON"
tags: ["conformance-rules", "workspace", "package-json", "pnpm", "monorepo"]
related: ["0303-workspace-missing-conformance-script.md", "0305-conformance-rules.md", "0237-getting-started-with-conformance.md"]
last_updated: "2026-04-03T23:47:18.463Z"
---

# WORKSPACE_MISSING_PACKAGE_JSON

> **🔒 Permissions Required**: Conformance

All directories that match a glob used to configure package manager workspaces
must be defined as a package and contain a `package.json` file. This check
prevents confusion where a new directory may be placed within a directory that
is configured to be a workspace but the new directory is not actually a
workspace.

## Example

The repository configures pnpm workspaces in this file:

```yaml filename="pnpm-workspace.yaml"
packages:
  - 'apps/*'
  - 'packages/*'
```

If a directory is defined in `packages/not-a-package`, then this test will fail
saying that the `not-a-package` directory must contain a `package.json` file.

## How to fix

Directories that match a workspace glob but do not have a `package.json` file
should either be converted to a package, be moved to a different directory, or
be excluded in the workspaces configuration.


