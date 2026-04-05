### For example

This sample code:

```tsx
export const HelloWorld = () => <h1>Hello world</h1>;
```

React: `"react-jsx"`<sup>[[1]](https://reactjs.org/blog/2020/09/22/introducing-the-new-jsx-transform.html)</sup>

```tsx twoslash
declare module JSX {
  interface Element {}
  interface IntrinsicElements {
    [s: string]: any;
  }
}
// @showEmit
// @noErrors
// @jsx: react-jsx
export const HelloWorld = () => <h1>Hello world</h1>;
```

React dev transform: `"react-jsxdev"`<sup>[[1]](https://reactjs.org/blog/2020/09/22/introducing-the-new-jsx-transform.html)</sup>

```tsx twoslash
declare module JSX {
  interface Element {}
  interface IntrinsicElements {
    [s: string]: any;
  }
}
// @showEmit
// @noErrors
// @jsx: react-jsxdev
export const HelloWorld = () => <h1>Hello world</h1>;
```

Preserve: `"preserve"`

```tsx twoslash
declare module JSX {
  interface Element {}
  interface IntrinsicElements {
    [s: string]: any;
  }
}
// @showEmit
// @noErrors
// @jsx: preserve
export const HelloWorld = () => <h1>Hello world</h1>;
```

React Native: `"react-native"`

```tsx twoslash
declare module JSX {
  interface Element {}
  interface IntrinsicElements {
    [s: string]: any;
  }
}
// @showEmit
// @noErrors
// @jsx: react-native
export const HelloWorld = () => <h1>Hello world</h1>;
```


Legacy React runtime: `"react"`

```tsx twoslash
declare module JSX {
  interface Element {}
  interface IntrinsicElements {
    [s: string]: any;
  }
}
// @showEmit
// @noErrors
export const HelloWorld = () => <h1>Hello world</h1>;
```

This option can be used on a per-file basis too using an `@jsxRuntime` comment.

Always use the classic runtime (`"react"`) for this file:

```tsx
/* @jsxRuntime classic */
export const HelloWorld = () => <h1>Hello world</h1>;
```

Always use the automatic runtime (`"react-jsx"`) for this file:

```tsx
/* @jsxRuntime automatic */
export const HelloWorld = () => <h1>Hello world</h1>;
```
