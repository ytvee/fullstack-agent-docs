--------------------------------------------------------------------------------
title: "PACKAGE_MANAGEMENT_NO_UNRESOLVED_IMPORTS"
description: "Import statements that can not be resolved to a local file or a package from package.json dependencies are not allowed."
last_updated: "2026-04-03T23:47:18.387Z"
source: "https://vercel.com/docs/conformance/rules/PACKAGE_MANAGEMENT_NO_UNRESOLVED_IMPORTS"
--------------------------------------------------------------------------------

# PACKAGE_MANAGEMENT_NO_UNRESOLVED_IMPORTS

> **🔒 Permissions Required**: Conformance

All imports must be able to be resolved to a file local to the workspace or a
package declared as a dependency within the `package.json` file. This ensures
that the workspace has not missed any dependencies and is not relying on
global dependencies.

## Example

```ts filename="component.ts"
import { useState } from 'react';
import { useRouter } from 'next/router';
```

The `package.json` is missing a dependency on the `next` package.

```json filename="package.json"
{
  "name": "shared-component-pkg",
  "dependencies": {
    "react": "19.0.0-beta-4508873393-20240430"
  }
}
```

## How to fix

If the workspace is missing a package dependency, add the appropriate one to
the `package.json` file of the workspace. In the example above, a dependency
on the `next` package should be added.


