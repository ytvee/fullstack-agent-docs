## Better checking for `null`/`undefined` in operands of expressions

TypeScript 2.2 improves checking of nullable operands in expressions. Specifically, these are now flagged as errors:

- If either operand of a `+` operator is nullable, and neither operand is of type `any` or `string`.
- If either operand of a `-`, `*`, `**`, `/`, `%`, `<<`, `>>`, `>>>`, `&`, `|`, or `^` operator is nullable.
- If either operand of a `<`, `>`, `<=`, `>=`, or `in` operator is nullable.
- If the right operand of an `instanceof` operator is nullable.
- If the operand of a `+`, `-`, `~`, `++`, or `--` unary operator is nullable.

An operand is considered nullable if the type of the operand is `null` or `undefined` or a union type that includes `null` or `undefined`.
Note that the union type case only occurs in [`strictNullChecks`](/tsconfig#strictNullChecks) mode because `null` and `undefined` disappear from unions in classic type checking mode.
