#### Strict `null` & `undefined` Checks

By default, TypeScript assumes that `null` and `undefined` are in the domain of every type.
That means anything declared with the type `number` could be `null` or `undefined`.
Since `null` and `undefined` are such a frequent source of bugs in JavaScript and TypeScript, TypeScript has the [`strictNullChecks`](/tsconfig#strictNullChecks) option to spare you the stress of worrying about these issues.

When [`strictNullChecks`](/tsconfig#strictNullChecks) is enabled, `null` and `undefined` get their own types called `null` and `undefined` respectively.
Whenever anything is _possibly_ `null`, you can use a union type with the original type.
So for instance, if something could be a `number` or `null`, you'd write the type out as `number | null`.

If you ever have a value that TypeScript thinks is possibly `null`/`undefined`, but you know better, you can use the postfix `!` operator to tell it otherwise.

```ts
declare var foo: string[] | null;

foo.length; // error - 'foo' is possibly 'null'

foo!.length; // okay - 'foo!' just has type 'string[]'
```

As a heads up, when using [`strictNullChecks`](/tsconfig#strictNullChecks), your dependencies may need to be updated to use [`strictNullChecks`](/tsconfig#strictNullChecks) as well.
