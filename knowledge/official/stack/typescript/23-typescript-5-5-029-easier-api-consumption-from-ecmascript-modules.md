## Easier API Consumption from ECMAScript Modules

Previously, if you were writing an ECMAScript module in Node.js, named imports were not available from the `typescript` package.

```ts
import { createSourceFile } from "typescript"; // ❌ error

import * as ts from "typescript";
ts.createSourceFile // ❌ undefined???

ts.default.createSourceFile // ✅ works - but ugh!
```

This is because [cjs-module-lexer](https://github.com/nodejs/cjs-module-lexer) did not recognize the pattern of TypeScript's generated CommonJS code.
This has been fixed, and users can now use named imports from the TypeScript npm package with ECMAScript modules in Node.js.

```ts
import { createSourceFile } from "typescript"; // ✅ works now!

import * as ts from "typescript";
ts.createSourceFile // ✅ works now!
```

For more information, [see the change here](https://github.com/microsoft/TypeScript/pull/57133).
