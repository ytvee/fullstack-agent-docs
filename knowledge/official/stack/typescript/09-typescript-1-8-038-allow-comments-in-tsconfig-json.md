## Allow comments in tsconfig.json

It's always nice to be able to document your configuration!
`tsconfig.json` now accepts single and multi-line comments.

```json tsconfig
{
  "compilerOptions": {
    "target": "ES2015", // running on node v5, yaay!
    "sourceMap": true // makes debugging easier
  },
  /*
   * Excluded files
   */
  "exclude": ["file.d.ts"]
}
```
