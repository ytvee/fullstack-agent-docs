---
id: "vercel-0241"
title: "ESLINT_CONFIGURATION"
description: "Requires that a workspace package has ESLint installed and configured correctly"
category: "vercel-conformance"
subcategory: "conformance"
type: "concept"
source: "https://vercel.com/docs/conformance/rules/ESLINT_CONFIGURATION"
tags: ["eslint", "configuration", "rules", "eslint-configuration", "example", "how-to-fix"]
related: ["0301-typescript-configuration.md", "0244-eslint-rules-required.md", "0243-eslint-react-rules-required.md"]
last_updated: "2026-04-03T23:47:18.083Z"
---

# ESLINT_CONFIGURATION

> **🔒 Permissions Required**: Conformance

[ESLint](https://eslint.org/) is a tool to statically analyze code to find and
report problems. ESLint is required to be enabled for every workspace package
in a monorepo so that all code in the monorepo is checked for these problems.
Additionally, repositories can enforce that particular ESLint plugins are
installed and that specific rules are treated as errors.

This rule requires that:

- An ESLint config exists in the current workspace.
- A script to run ESLint exists in `package.json` in the current workspace.
- `reportUnusedDisableDirectives` is set to `true`, which detects and can
  autofix unused ESLint disable comments.
- `root` is set to `true`, which ensures that workspaces don't inherit
  unintended rules and configuration from ESLint configuration files in parent
  directories.

## Example

```sh
A Conformance error occurred in test "ESLINT_CONFIGURATION".

ESLint configuration must specify `reportUnusedDisableDirectives` to be `true`

To find out more information and how to fix this error, visit
/docs/conformance/rules/ESLINT_CONFIGURATION.

If this violation should be ignored, add the following entry to
/apps/dashboard/.allowlists/ESLINT_CONFIGURATION.allowlist.json and get approval from the appropriate person.

{
  "testName": "ESLINT_CONFIGURATION",
  "reason": "TODO: Add reason why this violation is allowed to be ignored.",
  "location": {
    "workspace": "dashboard"
  }
}
```

See the [ESLint docs](https://eslint.org/docs/latest/use/configure/) for more information on how to configure ESLint, including plugins and rules.

## How To Fix

The recommended approach for configuring ESLint in a monorepo is to have a
shared ESLint config in an internal package. See the [Turbo docs on ESLint](https://turborepo.com/docs/handbook/linting/eslint) to get started.

Once your monorepo has a shared ESLint config, you can add a `.eslintrc.cjs`
file to the root folder of your workspace with the contents:

```js copy filename=".eslintrc.cjs"
module.exports = {
  root: true,
  extends: ['eslint-config-custom/base'],
};
```

You should also add `"eslint-config-custom": "workspace:*"` to your
`devDependencies`.


