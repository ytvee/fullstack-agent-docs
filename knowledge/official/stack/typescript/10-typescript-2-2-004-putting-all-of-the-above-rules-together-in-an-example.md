##### Putting all of the above rules together in an example

```ts
class Point {
  constructor(public x: number, public y: number) {}
}

class Person {
  constructor(public name: string) {}
}

type Constructor<T> = new (...args: any[]) => T;

function Tagged<T extends Constructor<{}>>(Base: T) {
  return class extends Base {
    _tag: string;
    constructor(...args: any[]) {
      super(...args);
      this._tag = "";
    }
  };
}

const TaggedPoint = Tagged(Point);

let point = new TaggedPoint(10, 20);
point._tag = "hello";

class Customer extends Tagged(Person) {
  accountBalance: number;
}

let customer = new Customer("Joe");
customer._tag = "test";
customer.accountBalance = 0;
```

Mixin classes can constrain the types of classes they can mix into by specifying a construct signature return type in the constraint for the type parameter.
For example, the following `WithLocation` function implements a subclass factory that adds a `getLocation` method to any class that satisfies the `Point` interface (i.e. that has `x` and `y` properties of type `number`).

```ts
interface Point {
  x: number;
  y: number;
}

const WithLocation = <T extends Constructor<Point>>(Base: T) =>
  class extends Base {
    getLocation(): [number, number] {
      return [this.x, this.y];
    }
  };
```
