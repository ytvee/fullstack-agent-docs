### Cache Instantiations on Mappers

When TypeScript replaces type parameters with specific type arguments, it can end up instantiating many of the same intermediate types over and over again.
In complex libraries like Zod and tRPC, this could lead to both performance issues and errors reported around excessive type instantiation depth.
Thanks to [a change](https://github.com/microsoft/TypeScript/pull/61505) from [Mateusz Burzyński](https://github.com/Andarist), TypeScript 5.9 is able to cache many intermediate instantiations when work has already begun on a specific type instantiation.
This in turn avoids lots of unnecessary work and allocations.
