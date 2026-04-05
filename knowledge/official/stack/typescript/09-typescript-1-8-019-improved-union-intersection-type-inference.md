## Improved union/intersection type inference

TypeScript 1.8 improves type inference involving source and target sides that are both union or intersection types.
For example, when inferring from `string | string[]` to `string | T`, we reduce the types to `string[]` and `T`, thus inferring `string[]` for `T`.
