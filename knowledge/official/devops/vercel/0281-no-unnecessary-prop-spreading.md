--------------------------------------------------------------------------------
title: "NO_UNNECESSARY_PROP_SPREADING"
description: "Disallows the usage of object spreading in a JSX component."
last_updated: "2026-04-03T23:47:18.351Z"
source: "https://vercel.com/docs/conformance/rules/NO_UNNECESSARY_PROP_SPREADING"
--------------------------------------------------------------------------------

# NO_UNNECESSARY_PROP_SPREADING

> **🔒 Permissions Required**: Conformance

This rule detects the usage of the spread operator when spreading an object as a prop within a JSX component.

When spreading an object in the component, the data types of the object's properties are not validated, potentially causing unexpected runtime errors or unintended behavior.

## Examples

In the following example, the `Header` component contains an object with the spread operator being applied to it.

We don't know if the props that the `Header` component reads will accept all the values contained in the `foo` object.

```tsx filename="app/dashboard/page.tsx" {2}
function HomePage() {
  return <Header {...{ foo }}>Hello World</Header>;
}

export default HomePage;
```

## How to fix

You can remove the spread operator from the JSX component, and list all props explicitly.

```tsx filename="app/dashboard/page.tsx" {2}
function HomePage() {
  return (
    <Header bar={foo.bar} baz={foo.baz}>
      Hello World
    </Header>
  );
}

export default HomePage;
```

In the example above, [TypeScript](https://www.typescriptlang.org/) will be able to type-check all props.


