### Optimizations on our Control Flow Graph

In many cases, control flow analysis will traverse nodes that don't provide any new information.
We observed that in the absence of any early termination or effects in the antecedents (or "dominators") of certain nodes meant that those nodes could always be skipped over.
As such, TypeScript now constructs its control flow graphs to take advantage of this by linking to an earlier node that *does* provide interesting information for control flow analysis.
This yields a flatter control flow graph, which can be more efficient to traverse.
This optimization has yielded modest gains, but with up to 2% reductions in build time on certain codebases.

You can [read more here](https://github.com/microsoft/TypeScript/pull/58013).
