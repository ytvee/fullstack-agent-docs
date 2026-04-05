## Dotted property for types with string index signatures

Types with a string index signature can be indexed using the `[]` notation, but were not allowed to use the `.`.
Starting with TypeScript 2.2 using either should be allowed.

```ts
interface StringMap<T> {
  [x: string]: T;
}

const map: StringMap<number>;

map["prop1"] = 1;
map.prop2 = 2;
```

This only applies to types with an _explicit_ string index signature.
It is still an error to access unknown properties on a type using `.` notation.
