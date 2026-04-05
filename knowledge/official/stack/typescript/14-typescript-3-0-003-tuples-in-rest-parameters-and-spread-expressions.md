## Tuples in rest parameters and spread expressions

TypeScript 3.0 adds support to multiple new capabilities to interact with function parameter lists as tuple types.
TypeScript 3.0 adds support for:

- [Expansion of rest parameters with tuple types into discrete parameters.](#rest-parameters-with-tuple-types)
- [Expansion of spread expressions with tuple types into discrete arguments.](#spread-expressions-with-tuple-types)
- [Generic rest parameters and corresponding inference of tuple types.](#generic-rest-parameters)
- [Optional elements in tuple types.](#optional-elements-in-tuple-types)
- [Rest elements in tuple types.](#rest-elements-in-tuple-types)

With these features it becomes possible to strongly type a number of higher-order functions that transform functions and their parameter lists.
