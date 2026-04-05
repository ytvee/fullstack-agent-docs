## Checked Indexed Accesses (`--noUncheckedIndexedAccess`)

TypeScript has a feature called _index signatures_.
These signatures are a way to signal to the type system that users can access arbitrarily-named properties.

```ts twoslash
interface Options {
  path: string;
  permissions: number;

  // Extra properties are caught by this index signature.
  [propName: string]: string | number;
}

function checkOptions(opts: Options) {
  opts.path; // string
  opts.permissions; // number

  // These are all allowed too!
  // They have the type 'string | number'.
  opts.yadda.toString();
  opts["foo bar baz"].toString();
  opts[Math.random()].toString();
}
```

In the above example, `Options` has an index signature that says any accessed property that's not already listed should have the type `string | number`.
This is often convenient for optimistic code that assumes you know what you're doing, but the truth is that most values in JavaScript do not support every potential property name.
Most types will not, for example, have a value for a property key created by `Math.random()` like in the previous example.
For many users, this behavior was undesirable, and felt like it wasn't leveraging the full strict-checking of [`strictNullChecks`](/tsconfig#strictNullChecks).

That's why TypeScript 4.1 ships with a new flag called [`noUncheckedIndexedAccess`](/tsconfig#noUncheckedIndexedAccess).
Under this new mode, every property access (like `foo.bar`) or indexed access (like `foo["bar"]`) is considered potentially undefined.
That means that in our last example, `opts.yadda` will have the type `string | number | undefined` as opposed to just `string | number`.
If you need to access that property, you'll either have to check for its existence first or use a non-null assertion operator (the postfix `!` character).

```ts twoslash
// @errors: 2532 18048
// @noUncheckedIndexedAccess
interface Options {
  path: string;
  permissions: number;

  // Extra properties are caught by this index signature.
  [propName: string]: string | number;
}
// ---cut---
function checkOptions(opts: Options) {
  opts.path; // string
  opts.permissions; // number

  // These are not allowed with noUncheckedIndexedAccess
  opts.yadda.toString();
  opts["foo bar baz"].toString();
  opts[Math.random()].toString();

  // Checking if it's really there first.
  if (opts.yadda) {
    console.log(opts.yadda.toString());
  }

  // Basically saying "trust me I know what I'm doing"
  // with the '!' non-null assertion operator.
  opts.yadda!.toString();
}
```

One consequence of using [`noUncheckedIndexedAccess`](/tsconfig#noUncheckedIndexedAccess) is that indexing into an array is also more strictly checked, even in a bounds-checked loop.

```ts twoslash
// @errors: 2532 18048
// @noUncheckedIndexedAccess
function screamLines(strs: string[]) {
  // This will have issues
  for (let i = 0; i < strs.length; i++) {
    console.log(strs[i].toUpperCase());
  }
}
```

If you don't need the indexes, you can iterate over individual elements by using a `for`-`of` loop or a `forEach` call.

```ts twoslash
// @noUncheckedIndexedAccess
function screamLines(strs: string[]) {
  // This works fine
  for (const str of strs) {
    console.log(str.toUpperCase());
  }

  // This works fine
  strs.forEach((str) => {
    console.log(str.toUpperCase());
  });
}
```

This flag can be handy for catching out-of-bounds errors, but it might be noisy for a lot of code, so it is not automatically enabled by the [`strict`](/tsconfig#strict) flag; however, if this feature is interesting to you, you should feel free to try it and determine whether it makes sense for your team's codebase!

You can learn more [at the implementing pull request](https://github.com/microsoft/TypeScript/pull/39560).
