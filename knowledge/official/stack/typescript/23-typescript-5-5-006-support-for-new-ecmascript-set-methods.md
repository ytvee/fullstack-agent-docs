## Support for New ECMAScript `Set` Methods

TypeScript 5.5 declares [new proposed methods for the ECMAScript `Set` type](https://github.com/tc39/proposal-set-methods).

Some of these methods, like `union`, `intersection`, `difference`, and `symmetricDifference`, take another `Set` and return a new `Set` as the result.
The other methods, `isSubsetOf`, `isSupersetOf`, and `isDisjointFrom`, take another `Set` and return a `boolean`.
None of these methods mutate the original `Set`s.

Here's a quick example of how you might use these methods and how they behave:

```ts
let fruits = new Set(["apples", "bananas", "pears", "oranges"]);
let applesAndBananas = new Set(["apples", "bananas"]);
let applesAndOranges = new Set(["apples", "oranges"]);
let oranges = new Set(["oranges"]);
let emptySet = new Set();

////
// union
////

// Set(4) {'apples', 'bananas', 'pears', 'oranges'}
console.log(fruits.union(oranges));

// Set(3) {'apples', 'bananas', 'oranges'}
console.log(applesAndBananas.union(oranges));

////
// intersection
////

// Set(2) {'apples', 'bananas'}
console.log(fruits.intersection(applesAndBananas));

// Set(0) {}
console.log(applesAndBananas.intersection(oranges));

// Set(1) {'apples'}
console.log(applesAndBananas.intersection(applesAndOranges));

////
// difference
////

// Set(3) {'apples', 'bananas', 'pears'}
console.log(fruits.difference(oranges));

// Set(2) {'pears', 'oranges'}
console.log(fruits.difference(applesAndBananas));

// Set(1) {'bananas'}
console.log(applesAndBananas.difference(applesAndOranges));

////
// symmetricDifference
////

// Set(2) {'bananas', 'oranges'}
console.log(applesAndBananas.symmetricDifference(applesAndOranges)); // no apples

////
// isDisjointFrom
////

// true
console.log(applesAndBananas.isDisjointFrom(oranges));

// false
console.log(applesAndBananas.isDisjointFrom(applesAndOranges));

// true
console.log(fruits.isDisjointFrom(emptySet));

// true
console.log(emptySet.isDisjointFrom(emptySet));

////
// isSubsetOf
////

// true
console.log(applesAndBananas.isSubsetOf(fruits));

// false
console.log(fruits.isSubsetOf(applesAndBananas));

// false
console.log(applesAndBananas.isSubsetOf(oranges));

// true
console.log(fruits.isSubsetOf(fruits));

// true
console.log(emptySet.isSubsetOf(fruits));

////
// isSupersetOf
////

// true
console.log(fruits.isSupersetOf(applesAndBananas));

// false
console.log(applesAndBananas.isSupersetOf(fruits));

// false
console.log(applesAndBananas.isSupersetOf(oranges));

// true
console.log(fruits.isSupersetOf(fruits));

// false
console.log(emptySet.isSupersetOf(fruits));
```

We'd like to thank [Kevin Gibbons](https://github.com/bakkot) who not only co-championed the feature in ECMAScript, but [also provided the declarations for `Set`, `ReadonlySet`, and `ReadonlySetLike` in TypeScript](https://github.com/microsoft/TypeScript/pull/57230)!
