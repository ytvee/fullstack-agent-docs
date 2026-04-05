### Value-based elements

Value-based elements are simply looked up by identifiers that are in scope.

```tsx
import MyComponent from "./myComponent";

<MyComponent />; // ok
<SomeOtherComponent />; // error
```

There are two ways to define a value-based element:

1. Function Component (FC)
2. Class Component

Because these two types of value-based elements are indistinguishable from each other in a JSX expression, first TS tries to resolve the expression as a Function Component using overload resolution. If the process succeeds, then TS finishes resolving the expression to its declaration. If the value fails to resolve as a Function Component, TS will then try to resolve it as a class component. If that fails, TS will report an error.
