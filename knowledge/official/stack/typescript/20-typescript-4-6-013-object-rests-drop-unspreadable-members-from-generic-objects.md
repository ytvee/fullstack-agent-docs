### Object Rests Drop Unspreadable Members from Generic Objects

Object rest expressions now drop members that appear to be unspreadable on generic objects.
In the following example...

```ts
class Thing {
  someProperty = 42;

  someMethod() {
    // ...
  }
}

function foo<T extends Thing>(x: T) {
  let { someProperty, ...rest } = x;

  // Used to work, is now an error!
  // Property 'someMethod' does not exist on type 'Omit<T, "someProperty" | "someMethod">'.
  rest.someMethod();
}
```

the variable `rest` used to have the type `Omit<T, "someProperty">` because TypeScript would strictly analyze which other properties were destructured.
This doesn't model how `...rest` would work in a destructuring from a non-generic type because `someMethod` would typically be dropped as well.
In TypeScript 4.6, the type of `rest` is `Omit<T, "someProperty" | "someMethod">`.

This can also come up in cases when destructuring from `this`.
When destructuring `this` using a `...rest` element, unspreadable and non-public members are now dropped, which is consistent with destructuring instances of a class in other places.

```ts
class Thing {
  someProperty = 42;

  someMethod() {
    // ...
  }

  someOtherMethod() {
    let { someProperty, ...rest } = this;

    // Used to work, is now an error!
    // Property 'someMethod' does not exist on type 'Omit<T, "someProperty" | "someMethod">'.
    rest.someMethod();
  }
}
```

For more details, [see the corresponding change here](https://github.com/microsoft/TypeScript/pull/47078).
