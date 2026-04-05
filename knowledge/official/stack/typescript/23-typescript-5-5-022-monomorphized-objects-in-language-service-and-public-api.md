### Monomorphized Objects in Language Service and Public API

In TypeScript 5.0, we ensured that our [`Node`](https://github.com/microsoft/TypeScript/pull/51682) and [`Symbol`](https://github.com/microsoft/TypeScript/pull/51880) objects had a consistent set of properties with a consistent initialization order.
Doing so helps reduce polymorphism in different operations, which allows runtimes to fetch properties more quickly.

By making this change, we witnessed impressive speed wins in the compiler;
however, most of these changes were performed on internal allocators for our data structures.
The language service, along with TypeScript's public API, uses a different set of allocators for certain objects.
This allowed the TypeScript compiler to be a bit leaner, as data used only for the language service would never be used in the compiler.

In TypeScript 5.5, the same monomorphization work has been done for the language service and public API.
What this means is that your editor experience, and any build tools that use the TypeScript API, will get a decent amount faster.
In fact, in our benchmarks, we've seen a **5-8% speedup in build times** when using the public TypeScript API's allocators, and **language service operations getting 10-20% faster**.
While this does imply an increase in memory, we believe that tradeoff is worth it and hope to find ways to reduce that memory overhead.
Things should feel a lot snappier now.

For more information, [see the change here](https://github.com/microsoft/TypeScript/pull/58045).
