## React 17 JSX Factories

TypeScript 4.1 supports React 17's upcoming `jsx` and `jsxs` factory functions through two new options for the [`jsx`](/tsconfig#jsx) compiler option:

- `react-jsx`
- `react-jsxdev`

These options are intended for production and development compiles respectively.
Often, the options from one can extend from the other.
For example, a `tsconfig.json` for production builds might look like the following:

```json tsconfig
// ./src/tsconfig.json
{
  "compilerOptions": {
    "module": "esnext",
    "target": "es2015",
    "jsx": "react-jsx",
    "strict": true
  },
  "include": ["./**/*"]
}
```

and one for development builds might look like the following:

```json tsconfig
// ./src/tsconfig.dev.json
{
  "extends": "./tsconfig.json",
  "compilerOptions": {
    "jsx": "react-jsxdev"
  }
}
```

For more information, [check out the corresponding PR](https://github.com/microsoft/TypeScript/pull/39199).
