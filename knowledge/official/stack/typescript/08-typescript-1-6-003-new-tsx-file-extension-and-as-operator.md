#### New `.tsx` file extension and `as` operator

TypeScript 1.6 introduces a new `.tsx` file extension.
This extension does two things: it enables JSX inside of TypeScript files, and it makes the new `as` operator the default way to cast (removing any ambiguity between JSX expressions and the TypeScript prefix cast operator).
For example:

```ts
var x = <any>foo;
// is equivalent to:
var x = foo as any;
```
