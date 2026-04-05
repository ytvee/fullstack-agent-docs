### Use-case: Parallel Declaration Emit and Parallel Checking

Imagine if you had a monorepo containing many projects and a multi-core CPU that just wished it could help you check your code faster.
Wouldn't it be great if we could check all those projects at the same time by running each project on a different core?

Unfortunately we don't have the freedom to do all the work in parallel.
The reason is that we have to build those projects in dependency order, because each project is checking against the declaration files of their dependencies.
So we must build the dependency first to generate the declaration files.
TypeScript's project references feature works the same way, building the set of projects in "topological" dependency order.

As an example, if we have two projects called `backend` and `frontend`, and they both depend on a project called `core`, TypeScript can't start type-checking either `frontend` or `backend` until `core` has been built and its declaration files have been generated.

![frontend and backend point to core, other stuff might point to each of those](https://devblogs.microsoft.com/typescript/wp-content/uploads/sites/11/2024/04/5-5-beta-isolated-declarations-deps.png)

In the above graph, you can see that we have a bottleneck.
Whilst we can build `frontend` and `backend` in parallel, we need to first wait for `core` to finish building before either can start.

How could we improve upon this?
Well, if a fast tool could generate all those declaration files for `core` *in parallel*, TypeScript then could immediately follow that by type-checking `core`, `frontend`, and `backend` also *in parallel*.
