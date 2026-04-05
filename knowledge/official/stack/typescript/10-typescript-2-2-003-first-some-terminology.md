##### First some terminology

A **mixin constructor type** refers to a type that has a single construct signature with a single rest argument of type `any[]` and an object-like return type. For example, given an object-like type `X`, `new (...args: any[]) => X` is a mixin constructor type with an instance type `X`.

A **mixin class** is a class declaration or expression that `extends` an expression of a type parameter type. The following rules apply to mixin class declarations:

- The type parameter type of the `extends` expression must be constrained to a mixin constructor type.
- The constructor of a mixin class (if any) must have a single rest parameter of type `any[]` and must use the spread operator to pass those parameters as arguments in a `super(...args)` call.

Given an expression `Base` of a parametric type `T` with a constraint `X`, a mixin class `class C extends Base {...}` is processed as if `Base` had type `X` and the resulting type is the intersection `typeof C & T`.
In other words, a mixin class is represented as an intersection between the mixin class constructor type and the parametric base class constructor type.

When obtaining the construct signatures of an intersection type that contains mixin constructor types, the mixin construct signatures are discarded and their instance types are mixed into the return types of the other construct signatures in the intersection type.
For example, the intersection type `{ new(...args: any[]) => A } & { new(s: string) => B }` has a single construct signature `new(s: string) => A & B`.
