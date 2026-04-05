## Basic usage

In order to use JSX you must do two things.

1. Name your files with a `.tsx` extension
2. Enable the [`jsx`](/tsconfig#jsx) option

TypeScript ships with several JSX modes: `preserve`, `react` (classic runtime), `react-jsx` (automatic runtime), `react-jsxdev` (automatic development runtime), and `react-native`.
The `preserve` mode will keep the JSX as part of the output to be further consumed by another transform step (e.g. [Babel](https://babeljs.io/)).
Additionally the output will have a `.jsx` file extension.
The `react` mode will emit `React.createElement`, does not need to go through a JSX transformation before use, and the output will have a `.js` file extension.
The `react-native` mode is the equivalent of `preserve` in that it keeps all JSX, but the output will instead have a `.js` file extension.

| Mode           | Input     | Output                                            | Output File Extension |
| -------------- | --------- | ------------------------------------------------- | --------------------- |
| `preserve`     | `<div />` | `<div />`                                         | `.jsx`                |
| `react`        | `<div />` | `React.createElement("div")`                      | `.js`                 |
| `react-native` | `<div />` | `<div />`                                         | `.js`                 |
| `react-jsx`    | `<div />` | `_jsx("div", {}, void 0);`                        | `.js`                 |
| `react-jsxdev` | `<div />` | `_jsxDEV("div", {}, void 0, false, {...}, this);` | `.js`                 |

You can specify this mode using either the [`jsx`](/tsconfig#jsx) command line flag or the corresponding option [`jsx` in your tsconfig.json](/tsconfig#jsx) file.

> \*Note: You can specify the JSX factory function to use when targeting react JSX emit with [`jsxFactory`](/tsconfig#jsxFactory) option (defaults to `React.createElement`)
