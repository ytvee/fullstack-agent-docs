## Indexed Access Inference Improvements

TypeScript now can correctly infer to indexed access types which immediately index into a mapped object type.

```ts
interface TypeMap {
  number: number;
  string: string;
  boolean: boolean;
}

type UnionRecord<P extends keyof TypeMap> = {
  [K in P]: {
    kind: K;
    v: TypeMap[K];
    f: (p: TypeMap[K]) => void;
  };
}[P];

function processRecord<K extends keyof TypeMap>(record: UnionRecord<K>) {
  record.f(record.v);
}

// This call used to have issues - now works!
processRecord({
  kind: "string",
  v: "hello!",

  // 'val' used to implicitly have the type 'string | number | boolean',
  // but now is correctly inferred to just 'string'.
  f: (val) => {
    console.log(val.toUpperCase());
  },
});
```

This pattern was already supported and allowed TypeScript to understand that the call to `record.f(record.v)` is valid, but previously the call to `processRecord` would give poor inference results for `val`

TypeScript 4.6 improves this so that no type assertions are necessary within the call to `processRecord`.

For more information, you can [read up on the pull request](https://github.com/microsoft/TypeScript/pull/47109).
