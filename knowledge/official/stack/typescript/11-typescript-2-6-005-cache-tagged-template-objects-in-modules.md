## Cache tagged template objects in modules

TypeScript 2.6 fixes the tagged string template emit to align better with the ECMAScript spec.
As per the [ECMAScript spec](https://tc39.github.io/ecma262/#sec-gettemplateobject), every time a template tag is evaluated, the _same_ template strings object (the same `TemplateStringsArray`) should be passed as the first argument.
Before TypeScript 2.6, the generated output was a completely new template object each time.
Though the string contents are the same, this emit affects libraries that use the identity of the string for cache invalidation purposes, e.g. [lit-html](https://github.com/PolymerLabs/lit-html/issues/58).
