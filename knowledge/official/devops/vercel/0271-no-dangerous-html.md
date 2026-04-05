--------------------------------------------------------------------------------
title: "NO_DANGEROUS_HTML"
description: "Prevent the unsafe creation of DOM via HTML methods in your application."
last_updated: "2026-04-03T23:47:18.287Z"
source: "https://vercel.com/docs/conformance/rules/NO_DANGEROUS_HTML"
--------------------------------------------------------------------------------

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


