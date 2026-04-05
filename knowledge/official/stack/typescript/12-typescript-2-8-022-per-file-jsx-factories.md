## Per-file JSX factories

TypeScript 2.8 adds support for a per-file configurable JSX factory name using `@jsx dom` pragma.
JSX factory can be configured for a compilation using [`jsxFactory`](/tsconfig#jsxFactory) (default is `React.createElement`). With TypeScript 2.8 you can override this on a per-file-basis by adding a comment to the beginning of the file.
