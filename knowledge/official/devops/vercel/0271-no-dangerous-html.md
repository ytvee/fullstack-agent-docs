---
id: "vercel-0271"
title: "NO_DANGEROUS_HTML"
description: "Prevent the unsafe creation of DOM via HTML methods in your application."
category: "vercel-conformance"
subcategory: "conformance"
type: "concept"
source: "https://vercel.com/docs/conformance/rules/NO_DANGEROUS_HTML"
tags: ["no", "dangerous", "html", "rules", "no-dangerous-html", "how-to-fix"]
related: ["0272-no-document-write.md", "0269-no-assign-window-location.md", "0273-no-eval.md"]
last_updated: "2026-04-03T23:47:18.287Z"
---

# NO_DANGEROUS_HTML

> **🔒 Permissions Required**: Conformance

Unsafe creation of DOM can be done a variety of ways:

- `element.innerHTML`
- `element.outerHTML`
- `DOMParser.parseFromString()`
- `element.insertAdjacentHTML()`
- `srcdoc` on iframe elements
- `dangerouslySetInnerHTML` prop in React apps

Usage of these methods is deemed an unsafe coding practice as the HTML might result in security vulnerabilities.

## How to fix

It is recommended to instead use alternative approaches for HTML construction - such as `document.createElement()` or a HTML sanitizer.


