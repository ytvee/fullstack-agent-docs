### Monomorphized Control Flow Nodes

In TypeScript 5.5, nodes of the control flow graph have been monomorphized so that they always hold a consistent shape.
By doing so, check times will often be reduced by about 1%.

[See this change here](https://github.com/microsoft/TypeScript/pull/57977).
