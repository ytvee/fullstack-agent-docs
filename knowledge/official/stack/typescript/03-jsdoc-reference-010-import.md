### `@import`

The `@import` tag can let us reference exports from other files.

```js twoslash
// @filename: types.d.ts
export type Pet = {
  name: string,
};
// @filename: main.js
// ---cut---
/**
 * @import {Pet} from "./types"
 */

/**
 * @type {Pet}
 */
var myPet;
myPet.name;
```

These tags don't actually import files at runtime, and the symbols they bring into scope can only be used within JSDoc comments for type-checking.

```js twoslash
// @filename: dog.js
export class Dog {
  woof() {
    console.log("Woof!");
  }
}

// @filename: main.js
/** @import { Dog } from "./dog.js" */

const d = new Dog(); // error!
```
