--------------------------------------------------------------------------------
title: "REACT_STABLE_CONTEXT_PROVIDER_VALUE"
description: "Prevent non-stable values from being used in React Context providers that could cause unnecessary re-renders."
last_updated: "2026-04-03T23:47:18.416Z"
source: "https://vercel.com/docs/conformance/rules/REACT_STABLE_CONTEXT_PROVIDER_VALUE"
--------------------------------------------------------------------------------

# REACT_STABLE_CONTEXT_PROVIDER_VALUE

> **🔒 Permissions Required**: Conformance

When non-stable values (i.e. object identities) are used as the `value` prop for `Context.Provider`,
React will trigger cascading updates to all components that use this context value on each
render, causing needless re-renders (affecting application performance) or causing
unintended consequences that may negatively affect the user-experience.

## Examples

Examples of incorrect code for this rule:

```jsx
return <SomeContext.Provider value={{ foo: 'bar' }}>...</SomeContext.Provider>;
```

Examples of correct code for this rule:

```jsx
const foo = useMemo(() => ({ foo: 'bar' }), []);

return <SomeContext.Provider value={foo}>...</SomeContext.Provider>;
```

## How to fix

One way to fix this issue may be to wrap the value in a `useMemo()`. If the value is a function
then `useCallback()` can be used as well. See the above examples for a reference on how you might
fix this by wrapping with `useMemo`.


