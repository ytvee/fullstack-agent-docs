### Negative Case Checks for Union Literals

When checking if a source type is part of a union type, TypeScript will first do a fast look-up using an internal type identifier for that source.
If that look-up fails, then TypeScript checks for compatibility against every type within the union.

When relating a literal type to a union of purely literal types, TypeScript can now avoid that full walk against every other type in the union.
This assumption is safe because TypeScript always interns/caches literal types - though there are some edge cases to handle relating to "fresh" literal types.

[This optimization](https://github.com/microsoft/TypeScript/pull/53192) was able to reduce the type-checking time of [the code in this issue](https://github.com/microsoft/TypeScript/issues/53191) from about 45 seconds to about 0.4 seconds.
