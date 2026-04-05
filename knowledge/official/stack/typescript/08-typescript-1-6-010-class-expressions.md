## Class expressions

TypeScript 1.6 adds support for ES6 class expressions. In a class expression, the class name is optional and, if specified, is only in scope in the class expression itself. This is similar to the optional name of a function expression. It is not possible to refer to the class instance type of a class expression outside the class expression, but the type can of course be matched structurally. For example:

```ts
let Point = class {
  constructor(public x: number, public y: number) {}
  public length() {
    return Math.sqrt(this.x * this.x + this.y * this.y);
  }
};
var p = new Point(3, 4); // p has anonymous class type
console.log(p.length());
```
