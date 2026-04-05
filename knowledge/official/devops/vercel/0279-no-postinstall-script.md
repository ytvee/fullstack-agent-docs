--------------------------------------------------------------------------------
title: "NO_POSTINSTALL_SCRIPT"
description: "Prevent the use of "
last_updated: "2026-04-03T23:47:18.341Z"
source: "https://vercel.com/docs/conformance/rules/NO_POSTINSTALL_SCRIPT"
--------------------------------------------------------------------------------

# NO_POSTINSTALL_SCRIPT

> **🔒 Permissions Required**: Conformance

Modifying, adding, or updating any dependencies in your application triggers the execution of the `"postinstall"` script. Consequently, incorporating a `"postinstall"` script in your application's package.json leads to increased installation times for all users.

## How to fix

If you hit this issue, you can resolve it by removing the `"postinstall"` script in the `package.json` file.

```JSX filename="package.json" {3}
{
  "scripts": {
    "postinstall": "sleep 360"
  },
}
```


