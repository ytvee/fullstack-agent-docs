---
id: "vercel-0280"
title: "NO_SERIAL_ASYNC_CALLS"
description: "Prevent blocking serial async await calls in your applications."
category: "vercel-conformance"
subcategory: "conformance"
type: "concept"
source: "https://vercel.com/docs/conformance/rules/NO_SERIAL_ASYNC_CALLS"
tags: ["no", "serial", "async", "calls", "rules", "no-serial-async-calls"]
related: ["0278-no-mixed-async-modules.md", "0255-nextjs-no-fetch-in-server-props.md", "0250-nextjs-no-async-layout.md"]
last_updated: "2026-04-03T23:47:18.345Z"
---

# NO_SERIAL_ASYNC_CALLS

> **🔒 Permissions Required**: Conformance

Sequential execution of async/await calls can significantly impact performance because
each await call prevents further execution until resolving its Promise. This rule aims to
refactor sequential async/await calls into parallel executions to enhance performance.

You should note that this rule might not flag some async/await usage patterns. For example:

- Patterns involving conditional statements
- Call expressions
- Patterns that await in a manner that suggests non-serial dependencies between calls

For instance, scenarios where async calls depend conditionally on each other or are part of
complex expressions are not flagged. This includes cases where one async call's outcome is
necessary for subsequent calls, requiring serial execution due to logical or dependency reasons.

The following example **will not** be flagged by this rule:

```ts
async function updateDatabase() {
  const result1 = await async1();
  const result2 = await async2();
  doSomething(result1, result2);
}
```

These patterns fall outside the scope of this rule because safely suggesting parallelization requires more context,
and the rule uses conservative heuristics to avoid false positives.

## How to fix

Instead, of executing async logic sequentially, opt to refactor the logic so it can be run parallel.

This can be fixed using `Promise.all`:

```js
export async function getStaticProps() {
  const firstThing = await getFirstThing();
  const secondThing = await getSecondThing();

  return {
    props: {
      firstThing,
      secondThing,
    },
  };
}
```

We can extract both `await` expressions into a single `Promise.all`, as follows:

```js
export async function getStaticProps() {
  const [firstThing, secondThing] = await Promise.all([
    getFirstThing(),
    getSecondThing(),
  ]);

  return {
    props: {
      firstThing,
      secondThing,
    },
  };
}
```


