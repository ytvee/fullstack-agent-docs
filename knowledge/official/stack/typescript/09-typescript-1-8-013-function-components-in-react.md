## Function Components in React

TypeScript now supports [Function components](https://reactjs.org/docs/components-and-props.html#functional-and-class-components).
These are lightweight components that easily compose other components:

```ts
// Use parameter destructuring and defaults for easy definition of 'props' type
const Greeter = ({ name = "world" }) => <div>Hello, {name}!</div>;

// Properties get validated
let example = <Greeter name="TypeScript 1.8" />;
```

For this feature and simplified props, be sure to use the [latest version of react.d.ts](https://github.com/DefinitelyTyped/DefinitelyTyped/blob/master/types/react/index.d.ts).
