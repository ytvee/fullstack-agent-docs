## `import` types

Modules can import types declared in other modules. But non-module global scripts cannot access types declared in modules. Enter `import` types.

Using `import("mod")` in a type annotation allows for reaching in a module and accessing its exported declaration without importing it.
