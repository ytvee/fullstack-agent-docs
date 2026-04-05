## Minimal and Updated `tsc --init`

For a while, the TypeScript compiler has supported an `--init` flag that can create a `tsconfig.json` within the current directory.
In the last few years, running `tsc --init` created a very "full" `tsconfig.json`, filled with commented-out settings and their descriptions.
We designed this with the intent of making options discoverable and easy to toggle.

However, given external feedback (and our own experience), we found it's common to immediately delete most of the contents of these new `tsconfig.json` files.
When users want to discover new options, we find they rely on auto-complete from their editor, or navigate to [the tsconfig reference on our website](https://www.typescriptlang.org/tsconfig/) (which the generated `tsconfig.json` links to!).
What each setting does is also documented on that same page, and can be seen via editor hovers/tooltips/quick info.
While surfacing some commented-out settings might be helpful, the generated `tsconfig.json` was often considered overkill.

We also felt that it was time that `tsc --init` initialized with a few more prescriptive settings than we already enable.
We looked at some common pain points and papercuts users have when they create a new TypeScript project.
For example, most users write in modules (not global scripts), and `--moduleDetection` can force TypeScript to treat every implementation file as a module.
Developers also often want to use the latest ECMAScript features directly in their runtime, so `--target` can typically be set to `esnext`.
JSX users often find that going back to set `--jsx` is needless friction, and its options are slightly confusing.
And often, projects end up loading more declaration files from `node_modules/@types` than TypeScript actually needs; but specifying an empty `types` array can help limit this.

In TypeScript 5.9, a plain `tsc --init` with no other flags will generate the following `tsconfig.json`:

```json5
{
  // Visit https://aka.ms/tsconfig to read more about this file
  "compilerOptions": {
    // File Layout
    // "rootDir": "./src",
    // "outDir": "./dist",

    // Environment Settings
    // See also https://aka.ms/tsconfig_modules
    "module": "nodenext",
    "target": "esnext",
    "types": [],
    // For nodejs:
    // "lib": ["esnext"],
    // "types": ["node"],
    // and npm install -D @types/node

    // Other Outputs
    "sourceMap": true,
    "declaration": true,
    "declarationMap": true,

    // Stricter Typechecking Options
    "noUncheckedIndexedAccess": true,
    "exactOptionalPropertyTypes": true,

    // Style Options
    // "noImplicitReturns": true,
    // "noImplicitOverride": true,
    // "noUnusedLocals": true,
    // "noUnusedParameters": true,
    // "noFallthroughCasesInSwitch": true,
    // "noPropertyAccessFromIndexSignature": true,

    // Recommended Options
    "strict": true,
    "jsx": "react-jsx",
    "verbatimModuleSyntax": true,
    "isolatedModules": true,
    "noUncheckedSideEffectImports": true,
    "moduleDetection": "force",
    "skipLibCheck": true,
  }
}
```

For more details, see the [implementing pull request](https://github.com/microsoft/TypeScript/pull/61813) and [discussion issue](https://github.com/microsoft/TypeScript/issues/58420).
