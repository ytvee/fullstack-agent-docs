## Decoupled Type-Checking Between JSX Elements and JSX Tag Types

One pain point TypeScript had with JSX was its requirements on the type of every JSX element's tag.

For context, a JSX element is either of the following:

```tsx
// A self-closing JSX tag
<Foo />
// A regular element with an opening/closing tag
<Bar></Bar>
```

When type-checking `<Foo />` or `<Bar></Bar>`, TypeScript always looks up a namespace called `JSX` and fetches a type out of it called `Element` - or more directly, it looks up `JSX.Element`.

But to check whether `Foo` or `Bar` themselves were valid to use as tag names, TypeScript would roughly just grab the types returned or constructed by `Foo` or `Bar` and check for compatibility with `JSX.Element` (or another type called `JSX.ElementClass` if the type is constructable).

The limitations here meant that components could not be used if they returned or "rendered" a more broad type than just `JSX.Element`.
For example, a JSX library might be fine with a component returning `string`s or `Promise`s.

As a more concrete example, [React is considering adding limited support for components that return `Promise`s](https://github.com/acdlite/rfcs/blob/first-class-promises/text/0000-first-class-support-for-promises.md), but existing versions of TypeScript cannot express that without someone drastically loosening the type of `JSX.Element`.

```tsx
import * as React from "react";
async function Foo() {
    return <div></div>;
}
let element = <Foo />;
//             ~~~
// 'Foo' cannot be used as a JSX component.
//   Its return type 'Promise<Element>' is not a valid JSX element.
```

To provide libraries with a way to express this, TypeScript 5.1 now looks up a type called `JSX.ElementType`.
`ElementType` specifies precisely what is valid to use as a tag in a JSX element.
So it might be typed today as something like

```tsx
namespace JSX {
    export type ElementType =
        // All the valid lowercase tags
        keyof IntrinsicAttributes
        // Function components
        (props: any) => Element
        // Class components
        new (props: any) => ElementClass;
    export interface IntrinsicAttributes extends /*...*/ {}
    export type Element = /*...*/;
    export type ElementClass = /*...*/;
}
```

We'd like to extend our thanks to [Sebastian Silbermann](https://github.com/eps1lon) who contributed [this change](https://github.com/microsoft/TypeScript/pull/51328)!
