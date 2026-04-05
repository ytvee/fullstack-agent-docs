## Locally scoped JSX namespaces

JSX type checking is driven by definitions in a JSX namespace, for instance `JSX.Element` for the type of a JSX element, and `JSX.IntrinsicElements` for built-in elements.
Before TypeScript 2.8 the `JSX` namespace was expected to be in the global namespace, and thus only allowing one to be defined in a project.
Starting with TypeScript 2.8 the `JSX` namespace will be looked under the `jsxNamespace` (e.g. `React`) allowing for multiple jsx factories in one compilation.
For backward compatibility the global `JSX` namespace is used as a fallback if none was defined on the factory function.
Combined with the per-file `@jsx` pragma, each file can have a different JSX factory.
