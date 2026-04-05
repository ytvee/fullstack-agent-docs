### Operands for `delete` must be optional.

When using the `delete` operator in [`strictNullChecks`](/tsconfig#strictNullChecks), the operand must now be `any`, `unknown`, `never`, or be optional (in that it contains `undefined` in the type).
Otherwise, use of the `delete` operator is an error.

```ts twoslash
// @errors: 2790
interface Thing {
  prop: string;
}

function f(x: Thing) {
  delete x.prop;
}
```

See more details on [the implementing pull request](https://github.com/microsoft/TypeScript/pull/37921).
