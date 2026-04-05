### Stricter Spread Checks in JSX

When writing a `...spread` in JSX, TypeScript now enforces stricter checks that the given type is actually an object.
As a result, values with the types `unknown` and `never` (and more rarely, just bare `null` and `undefined`) can no longer be spread into JSX elements.

So for the following example:

```tsx
import * as React from "react";

interface Props {
    stuff?: string;
}

function MyComponent(props: unknown) {
    return <div {...props} />;
}
```

you'll now receive an error like the following:

```
Spread types may only be created from object types.
```

This makes this behavior more consistent with spreads in object literals.

For more details, [see the change on GitHub](https://github.com/microsoft/TypeScript/pull/48570).
