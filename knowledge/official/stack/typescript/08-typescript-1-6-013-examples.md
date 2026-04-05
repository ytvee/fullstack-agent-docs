##### Examples

```ts
abstract class Base {
  abstract getThing(): string;
  getOtherThing() {
    return "hello";
  }
}

let x = new Base(); // Error, 'Base' is abstract

// Error, must either be 'abstract' or implement concrete 'getThing'
class Derived1 extends Base {}

class Derived2 extends Base {
  getThing() {
    return "hello";
  }
  foo() {
    super.getThing(); // Error: cannot invoke abstract members through 'super'
  }
}

var x = new Derived2(); // OK
var y: Base = new Derived2(); // Also OK
y.getThing(); // OK
y.getOtherThing(); // OK
```
