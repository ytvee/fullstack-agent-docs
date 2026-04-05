## The JSX function return type

By default, function components must return `JSX.Element | null`. However, this doesn’t always represent runtime behaviour. As of TypeScript 5.1, you can specify `JSX.ElementType` to override what is a valid JSX component type. Note that this doesn’t define what props are valid. The type of props is always defined by the first argument of the component that’s passed. The default looks something like this:

```ts
namespace JSX {
    export type ElementType =
        // All the valid lowercase tags
        | keyof IntrinsicElements
        // Function components
        | (props: any) => Element
        // Class components
        | new (props: any) => ElementClass;
    export interface IntrinsicAttributes extends /*...*/ {}
    export type Element = /*...*/;
    export type ElementClass = /*...*/;
}
```
