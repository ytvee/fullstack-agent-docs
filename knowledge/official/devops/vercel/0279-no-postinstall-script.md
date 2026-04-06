---
id: "vercel-0279"
title: "NO_POSTINSTALL_SCRIPT"
description: "Prevent the use of "
category: "vercel-conformance"
subcategory: "conformance"
type: "concept"
source: "https://vercel.com/docs/conformance/rules/NO_POSTINSTALL_SCRIPT"
tags: ["no", "postinstall", "script", "rules", "no-postinstall-script", "how-to-fix"]
related: ["0271-no-dangerous-html.md", "0272-no-document-write.md", "0276-no-inline-svg.md"]
last_updated: "2026-04-03T23:47:18.341Z"
---

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


