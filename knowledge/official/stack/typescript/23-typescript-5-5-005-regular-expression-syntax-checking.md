## Regular Expression Syntax Checking

Until now, TypeScript has typically skipped over most regular expressions in code.
This is because regular expressions technically have an extensible grammar and TypeScript never made any effort to compile regular expressions to earlier versions of JavaScript.
Still, this meant that lots of common problems would go undiscovered in regular expressions, and they would either turn into errors at runtime, or silently fail.

But TypeScript now does basic syntax checking on regular expressions!

```ts
let myRegex = /@robot(\s+(please|immediately)))? do some task/;
//                                            ~
// error!
// Unexpected ')'. Did you mean to escape it with backslash?
```

This is a simple example, but this checking can catch a lot of common mistakes.
In fact, TypeScript's checking goes slightly beyond syntactic checks.
For instance, TypeScript can now catch issues around backreferences that don't exist.

```ts
let myRegex = /@typedef \{import\((.+)\)\.([a-zA-Z_]+)\} \3/u;
//                                                        ~
// error!
// This backreference refers to a group that does not exist.
// There are only 2 capturing groups in this regular expression.
```

The same applies to named capturing groups.

```ts
let myRegex = /@typedef \{import\((?<importPath>.+)\)\.(?<importedEntity>[a-zA-Z_]+)\} \k<namedImport>/;
//                                                                                        ~~~~~~~~~~~
// error!
// There is no capturing group named 'namedImport' in this regular expression.
```

TypeScript's checking is now also aware of when certain RegExp features are used when newer than your target version of ECMAScript.
For example, if we use named capturing groups like the above in an ES5 target, we'll get an error.

```ts
let myRegex = /@typedef \{import\((?<importPath>.+)\)\.(?<importedEntity>[a-zA-Z_]+)\} \k<importedEntity>/;
//                                  ~~~~~~~~~~~~         ~~~~~~~~~~~~~~~~
// error!
// Named capturing groups are only available when targeting 'ES2018' or later.
```

The same is true for certain regular expression flags as well.

Note that TypeScript's regular expression support is limited to regular expression *literals*.
If you try calling `new RegExp` with a string literal, TypeScript will not check the provided string.

We would like to thank [GitHub user graphemecluster](https://github.com/graphemecluster/) who iterated a ton with us [to get this feature into TypeScript](https://github.com/microsoft/TypeScript/pull/55600).
