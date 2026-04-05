##### Example

```ts
type Maybe<T> = T | void;

function isDefined<T>(x: Maybe<T>): x is T {
  return x !== undefined && x !== null;
}

function isUndefined<T>(x: Maybe<T>): x is void {
  return x === undefined || x === null;
}

function getOrElse<T>(x: Maybe<T>, defaultValue: T): T {
  return isDefined(x) ? x : defaultValue;
}

function test1(x: Maybe<string>) {
  let x1 = getOrElse(x, "Undefined"); // string
  let x2 = isDefined(x) ? x : "Undefined"; // string
  let x3 = isUndefined(x) ? "Undefined" : x; // string
}

function test2(x: Maybe<number>) {
  let x1 = getOrElse(x, -1); // number
  let x2 = isDefined(x) ? x : -1; // number
  let x3 = isUndefined(x) ? -1 : x; // number
}
```
