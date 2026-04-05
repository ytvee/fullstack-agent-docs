## Namespaced JSX Attributes

TypeScript now supports namespaced attribute names when using JSX.

```tsx
import * as React from "react";
// Both of these are equivalent:
const x = <Foo a:b="hello" />;
const y = <Foo a : b="hello" />;
interface FooProps {
    "a:b": string;
}
function Foo(props: FooProps) {
    return <div>{props["a:b"]}</div>;
}
```

Namespaced tag names are looked up in a similar way on `JSX.IntrinsicAttributes` when the first segment of the name is a lowercase name.

```tsx
// In some library's code or in an augmentation of that library:
namespace JSX {
    interface IntrinsicElements {
        ["a:b"]: { prop: string };
    }
}
// In our code:
let x = <a:b prop="hello!" />;
```

[This contribution](https://github.com/microsoft/TypeScript/pull/53799) was provided thanks to [Oleksandr Tarasiuk](https://github.com/a-tarasyuk).
