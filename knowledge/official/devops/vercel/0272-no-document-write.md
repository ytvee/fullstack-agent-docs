---
id: "vercel-0272"
title: "NO_DOCUMENT_WRITE"
description: "Prevent unsafe usage of document.write() in your application."
category: "vercel-conformance"
subcategory: "conformance"
type: "concept"
source: "https://vercel.com/docs/conformance/rules/NO_DOCUMENT_WRITE"
tags: ["no", "document", "write", "rules", "no-document-write", "how-to-fix"]
related: ["0271-no-dangerous-html.md", "0269-no-assign-window-location.md", "0273-no-eval.md"]
last_updated: "2026-04-03T23:47:18.290Z"
---

# NO_DOCUMENT_WRITE

> **🔒 Permissions Required**: Conformance

Calls to `document.write()` or `document.writeln()` manipulate DOM directly without any sanitization and should be avoided.

Furthermore, these APIs can also cause performance issues and trigger will clear the page contents if used after page load.

## How to fix

Avoid usage of `document.write()` entirely in your application, and instead either use UI framework like React to handle writing to the document,
or use safer DOM APIs, such as `document.createElement()` instead.


