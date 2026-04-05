## Class Property Inference from Constructors

TypeScript 4.0 can now use control flow analysis to determine the types of properties in classes when [`noImplicitAny`](/tsconfig#noImplicitAny) is enabled.

<!--prettier-ignore -->
```ts twoslash
class Square {
  // Previously both of these were any
  area;
// ^?
  sideLength;
// ^?
  constructor(sideLength: number) {
    this.sideLength = sideLength;
    this.area = sideLength ** 2;
  }
}
```

In cases where not all paths of a constructor assign to an instance member, the property is considered to potentially be `undefined`.

<!--prettier-ignore -->
```ts twoslash
// @errors: 2532 18048
class Square {
  sideLength;
// ^?

  constructor(sideLength: number) {
    if (Math.random()) {
      this.sideLength = sideLength;
    }
  }

  get area() {
    return this.sideLength ** 2;
  }
}
```

In cases where you know better (e.g. you have an `initialize` method of some sort), you'll still need an explicit type annotation along with a definite assignment assertion (`!`) if you're in [`strictPropertyInitialization`](/tsconfig#strictPropertyInitialization).

```ts twoslash
class Square {
  // definite assignment assertion
  //        v
  sideLength!: number;
  //         ^^^^^^^^
  // type annotation

  constructor(sideLength: number) {
    this.initialize(sideLength);
  }

  initialize(sideLength: number) {
    this.sideLength = sideLength;
  }

  get area() {
    return this.sideLength ** 2;
  }
}
```

For more details, [see the implementing pull request](https://github.com/microsoft/TypeScript/pull/37920).
