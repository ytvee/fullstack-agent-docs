##### Example

```ts
if (false) {
  // @ts-ignore: Unreachable code error
  console.log("hello");
}
```

A `// @ts-ignore` comment suppresses all errors that originate on the following line.
It is recommended practice to have the remainder of the comment following `@ts-ignore` explain which error is being suppressed.

Please note that this comment only suppresses the error reporting, and we recommend you use this comments _very sparingly_.
