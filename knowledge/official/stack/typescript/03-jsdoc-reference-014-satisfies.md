### `@satisfies`

`@satisfies` provides access to the postfix [operator `satisfies`](/docs/handbook/release-notes/typescript-4-9.html) in TypeScript. Satisfies is used to declare that a value implements a type but does not affect the type of the value. 

```js twoslash
// @errors: 1360
// @ts-check
/**
 * @typedef {"hello world" | "Hello, world"} WelcomeMessage
 */

/** @satisfies {WelcomeMessage} */
const message = "hello world"
//     ^?

/** @satisfies {WelcomeMessage} */
const failingMessage = "Hello world!"

/** @type {WelcomeMessage} */
const messageUsingType = "hello world"
//     ^?
```
