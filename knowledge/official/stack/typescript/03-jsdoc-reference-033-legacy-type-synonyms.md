### Legacy type synonyms

A number of common types are given aliases for compatibility with old JavaScript code.
Some of the aliases are the same as existing types, although most of those are rarely used.
For example, `String` is treated as an alias for `string`.
Even though `String` is a type in TypeScript, old JSDoc often uses it to mean `string`.
Besides, in TypeScript, the capitalized versions of primitive types are wrapper types -- almost always a mistake to use.
So the compiler treats these types as synonyms based on usage in old JSDoc:

- `String -> string`
- `Number -> number`
- `Boolean -> boolean`
- `Void -> void`
- `Undefined -> undefined`
- `Null -> null`
- `function -> Function`
- `array -> Array<any>`
- `promise -> Promise<any>`
- `Object -> any`
- `object -> any`

The last four aliases are turned off when `noImplicitAny: true`:

- `object` and `Object` are built-in types, although `Object` is rarely used.
- `array` and `promise` are not built-in, but might be declared somewhere in your program.
