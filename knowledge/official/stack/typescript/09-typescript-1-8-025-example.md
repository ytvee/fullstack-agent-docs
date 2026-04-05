##### Example

```ts
let list = [];
for (let i = 0; i < 5; i++) {
  list.push(() => i);
}

list.forEach((f) => console.log(f()));
```

is compiled to:

```js
var list = [];
var _loop_1 = function (i) {
  list.push(function () {
    return i;
  });
};
for (var i = 0; i < 5; i++) {
  _loop_1(i);
}
list.forEach(function (f) {
  return console.log(f());
});
```

And results in

```cmd
0
1
2
3
4
```
