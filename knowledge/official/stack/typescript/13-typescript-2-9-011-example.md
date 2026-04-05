##### Example

Given a declaration of a class `Pet` in a module file:

```ts
// module.d.ts

export declare class Pet {
  name: string;
}
```

Can be used in a non-module file `global-script.ts`:

```ts
// global-script.ts

function adopt(p: import("./module").Pet) {
  console.log(`Adopting ${p.name}...`);
}
```

This also works in JSDoc comments to refer to types from other modules in `.js`:

```js
// a.js

/**
 * @param p { import("./module").Pet }
 */
function walk(p) {
  console.log(`Walking ${p.name}...`);
}
```
