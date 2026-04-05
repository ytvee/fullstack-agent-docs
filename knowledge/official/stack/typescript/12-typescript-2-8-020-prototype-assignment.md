## Prototype assignment

You can assign an object literal directly to the prototype property. Individual prototype assignments still work too:

```ts
var C = function(p) {
  this.p = p;
};
C.prototype = {
  m() {
    console.log(this.p);
  }
};
C.prototype.q = function(r) {
  return this.p === r;
};
```
