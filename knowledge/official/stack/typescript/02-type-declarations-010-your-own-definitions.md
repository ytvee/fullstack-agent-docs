### Your Own Definitions

In the uncommon event that a library didn't bundle its own types and didn't have a definition on DefinitelyTyped, you can write a declaration file yourself.
See the appendix [Writing Declaration Files](/docs/handbook/declaration-files/introduction.html) for a guide.

If you want to silence warnings about a particular module without writing a declaration file, you can also quick declare the module as type `any` by putting an empty declaration for it in a `.d.ts` file in your project.
For example, if you wanted to use a module named `some-untyped-module` without having definitions for it, you would write:

```ts twoslash
declare module "some-untyped-module";
```
