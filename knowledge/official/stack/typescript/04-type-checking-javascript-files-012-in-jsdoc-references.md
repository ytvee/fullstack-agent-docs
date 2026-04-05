### In JSDoc references

An unspecified type argument in JSDoc defaults to any:

```js twoslash
/** @type{Array} */
var x = [];

x.push(1); // OK
x.push("string"); // OK, x is of type Array<any>

/** @type{Array.<number>} */
var y = [];

y.push(1); // OK
y.push("string"); // Error, string is not assignable to number
```
