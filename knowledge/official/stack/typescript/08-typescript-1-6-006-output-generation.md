#### Output generation

TypeScript ships with two JSX modes: `preserve` and `react`.

- The `preserve` mode will keep JSX expressions as part of the output to be further consumed by another transform step. _Additionally the output will have a `.jsx` file extension._
- The `react` mode will emit `React.createElement`, does not need to go through a JSX transformation before use, and the output will have a `.js` file extension.

See the [[JSX]] wiki page for more information on using JSX in TypeScript.
