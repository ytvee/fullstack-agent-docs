#### Importing from Modules

You might start out getting a bunch of errors like `Cannot find name 'require'.`, and `Cannot find name 'define'.`.
In these cases, it's likely that you're using modules.
While you can just convince TypeScript that these exist by writing out

```ts
// For Node/CommonJS
declare function require(path: string): any;
```

or

```ts
// For RequireJS/AMD
declare function define(...args: any[]): any;
```

it's better to get rid of those calls and use TypeScript syntax for imports.

First, you'll need to enable some module system by setting TypeScript's [`module`](/tsconfig#module) option.
Valid options are `commonjs`, `amd`, `system`, and `umd`.

If you had the following Node/CommonJS code:

```js
var foo = require("foo");

foo.doStuff();
```

or the following RequireJS/AMD code:

```js
define(["foo"], function (foo) {
  foo.doStuff();
});
```

then you would write the following TypeScript code:

```ts
import foo = require("foo");

foo.doStuff();
```
