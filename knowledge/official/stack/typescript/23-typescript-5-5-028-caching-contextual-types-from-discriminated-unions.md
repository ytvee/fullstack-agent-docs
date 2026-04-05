### Caching Contextual Types from Discriminated Unions

When TypeScript asks for the contextual type of an expression like an object literal, it will often encounter a union type.
In those cases, TypeScript tries to filter out members of the union based on known properties with well known values (i.e. discriminant properties).
This work can be fairly expensive, especially if you end up with an object consisting of many many properties.
In TypeScript 5.5, [much of the computation is cached once so that TypeScript doesn't need to recompute it for every property in the object literal](https://github.com/microsoft/TypeScript/pull/58372).
Performing this optimization shaved 250ms off of compiling the TypeScript compiler itself.
