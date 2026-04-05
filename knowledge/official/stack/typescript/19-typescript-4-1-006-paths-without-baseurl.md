## `paths` without `baseUrl`

Using path-mapping is fairly common - often it's to have nicer imports, often it's to simulate monorepo linking behavior.

Unfortunately, specifying [`paths`](/tsconfig#paths) to enable path-mapping required also specifying an option called [`baseUrl`](/tsconfig#baseUrl), which allows bare specifier paths to be reached relative to the [`baseUrl`](/tsconfig#baseUrl) too.
This also often caused poor paths to be used by auto-imports.

In TypeScript 4.1, the [`paths`](/tsconfig#paths) option can be used without [`baseUrl`](/tsconfig#baseUrl).
This helps avoid some of these issues.
