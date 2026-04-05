## ECMAScript Private Fields

TypeScript 3.8 brings support for ECMAScript's private fields, part of the [stage-3 class fields proposal](https://github.com/tc39/proposal-class-fields/).

```ts
class Person {
  #name: string;

  constructor(name: string) {
    this.#name = name;
  }

  greet() {
    console.log(`Hello, my name is ${this.#name}!`);
  }
}

let jeremy = new Person("Jeremy Bearimy");

jeremy.#name;
//     ~~~~~
// Property '#name' is not accessible outside class 'Person'
// because it has a private identifier.
```

Unlike regular properties (even ones declared with the `private` modifier), private fields have a few rules to keep in mind.
Some of them are:

- Private fields start with a `#` character. Sometimes we call these _private names_.
- Every private field name is uniquely scoped to its containing class.
- TypeScript accessibility modifiers like `public` or `private` can't be used on private fields.
- Private fields can't be accessed or even detected outside of the containing class - even by JS users! Sometimes we call this _hard privacy_.

Apart from "hard" privacy, another benefit of private fields is that uniqueness we just mentioned.
For example, regular property declarations are prone to being overwritten in subclasses.

```ts
class C {
  foo = 10;

  cHelper() {
    return this.foo;
  }
}

class D extends C {
  foo = 20;

  dHelper() {
    return this.foo;
  }
}

let instance = new D();
// 'this.foo' refers to the same property on each instance.
console.log(instance.cHelper()); // prints '20'
console.log(instance.dHelper()); // prints '20'
```

With private fields, you'll never have to worry about this, since each field name is unique to the containing class.

```ts
class C {
  #foo = 10;

  cHelper() {
    return this.#foo;
  }
}

class D extends C {
  #foo = 20;

  dHelper() {
    return this.#foo;
  }
}

let instance = new D();
// 'this.#foo' refers to a different field within each class.
console.log(instance.cHelper()); // prints '10'
console.log(instance.dHelper()); // prints '20'
```

Another thing worth noting is that accessing a private field on any other type will result in a `TypeError`!

```ts
class Square {
  #sideLength: number;

  constructor(sideLength: number) {
    this.#sideLength = sideLength;
  }

  equals(other: any) {
    return this.#sideLength === other.#sideLength;
  }
}

const a = new Square(100);
const b = { sideLength: 100 };

// Boom!
// TypeError: attempted to get private field on non-instance
// This fails because 'b' is not an instance of 'Square'.
console.log(a.equals(b));
```

Finally, for any plain `.js` file users, private fields _always_ have to be declared before they're assigned to.

```js
class C {
  // No declaration for '#foo'
  // :(

  constructor(foo: number) {
    // SyntaxError!
    // '#foo' needs to be declared before writing to it.
    this.#foo = foo;
  }
}
```

JavaScript has always allowed users to access undeclared properties, whereas TypeScript has always required declarations for class properties.
With private fields, declarations are always needed regardless of whether we're working in `.js` or `.ts` files.

```js
class C {
  /** @type {number} */
  #foo;

  constructor(foo: number) {
    // This works.
    this.#foo = foo;
  }
}
```

For more information about the implementation, you can [check out the original pull request](https://github.com/Microsoft/TypeScript/pull/30829)
