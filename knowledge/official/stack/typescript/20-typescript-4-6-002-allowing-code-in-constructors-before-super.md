## Allowing Code in Constructors Before `super()`

In JavaScript classes it's mandatory to call `super()` before referring to `this`.
TypeScript enforces this as well, though it was a bit too strict in _how_ it ensured this.
In TypeScript, it was previously an error to contain _any_ code at the beginning of a constructor if its containing class had any property initializers.

```ts
class Base {
  // ...
}

class Derived extends Base {
  someProperty = true;

  constructor() {
    // error!
    // have to call 'super()' first because it needs to initialize 'someProperty'.
    doSomeStuff();
    super();
  }
}
```

This made it cheap to check that `super()` gets called before `this` is referenced, but it ended up rejecting a lot of valid code.
TypeScript 4.6 is now much more lenient in that check and permits other code to run before `super()`., all while still ensuring that `super()` occurs at the top-level before any references to `this`.

We'd like to extend our thanks to [Joshua Goldberg](https://github.com/JoshuaKGoldberg) for [patiently working with us to land this change](https://github.com/microsoft/TypeScript/pull/29374)!
