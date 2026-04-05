##### Examples

```ts
var x: { foo: number };
x = { foo: 1, baz: 2 }; // Error, excess property `baz`

var y: { foo: number; bar?: number };
y = { foo: 1, baz: 2 }; // Error, excess or misspelled property `baz`
```

A type can include an index signature to explicitly indicate that excess properties are permitted:

```ts
var x: { foo: number; [x: string]: any };
x = { foo: 1, baz: 2 }; // Ok, `baz` matched by index signature
```
