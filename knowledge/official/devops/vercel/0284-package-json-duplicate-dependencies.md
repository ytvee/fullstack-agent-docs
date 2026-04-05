--------------------------------------------------------------------------------
title: "PACKAGE_JSON_DUPLICATE_DEPENDENCIES"
description: "Found duplicate dependencies between the list of dependencies and devDependencies or peerDependencies in a package.json file.."
last_updated: "2026-04-03T23:47:18.362Z"
source: "https://vercel.com/docs/conformance/rules/PACKAGE_JSON_DUPLICATE_DEPENDENCIES"
--------------------------------------------------------------------------------

# PACKAGE_JSON_DUPLICATE_DEPENDENCIES

> **🔒 Permissions Required**: Conformance

Packages that are listed in the `dependencies` section of `package.json` should
not be listed in `devDependencies` or `peerDependencies`. A package in the
`dependencies` section says that the package are required for the functionality
of your workspace, in which case there is no reason to also list it in
`devDependencies` or `peerDependencies`.

## Example

This `package.json` file would cause the check to fail:

```json filename="package.json"
{
  "name": "workspace",
  "dependencies": {
    "@next/mdx": "13.1.5"
  },
  "devDependencies": {
    "@next/mdx": "13.1.5"
  }
}
```

## How to fix

If the package is needed to use the package from your workspace, you can remove
the package from the `devDependencies` and `peerDependencies` sections. If the
package is only needed for development of your workspace or if the package is
only needed to express version compatibility requirements and it is not needed
for the functionality of your workspace when people use your package, then it
can be left in `devDependencies` or `peerDependencies` and be removed from
`dependencies`.


