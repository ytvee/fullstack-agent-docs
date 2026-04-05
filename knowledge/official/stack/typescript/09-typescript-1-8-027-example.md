##### Example

```ts
var a: MyObject[];
for (var x in a) {
  // Type of x is implicitly string
  var obj = a[x]; // Type of obj is MyObject
}
```
