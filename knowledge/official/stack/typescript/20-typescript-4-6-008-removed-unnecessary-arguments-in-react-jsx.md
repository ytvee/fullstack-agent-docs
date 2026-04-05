## Removed Unnecessary Arguments in `react-jsx`

Previously, when compiling code like the following in `--jsx react-jsx`

```tsx
export const el = <div>foo</div>;
```

TypeScript would produce the following JavaScript code:

```jsx
import { jsx as _jsx } from "react/jsx-runtime";
export const el = _jsx("div", { children: "foo" }, void 0);
```

That last `void 0` argument is unnecessary in this emit mode, and removing it can improve bundle sizes.

```diff
- export const el = _jsx("div", { children: "foo" }, void 0);
+ export const el = _jsx("div", { children: "foo" });
```

Thanks to [a pull request](https://github.com/microsoft/TypeScript/pull/47467) from [Alexander Tarasyuk](https://github.com/a-tarasyuk), TypeScript 4.6 now drops the `void 0` argument.
