## Improved control over mapped type modifiers

Mapped types support adding a `readonly` or `?` modifier to a mapped property, but they did not provide support for the ability to _remove_ modifiers.
This matters in [_homomorphic mapped types_](https://github.com/Microsoft/TypeScript/pull/12563) which by default preserve the modifiers of the underlying type.

TypeScript 2.8 adds the ability for a mapped type to either add or remove a particular modifier.
Specifically, a `readonly` or `?` property modifier in a mapped type can now be prefixed with either `+` or `-` to indicate that the modifier should be added or removed.
