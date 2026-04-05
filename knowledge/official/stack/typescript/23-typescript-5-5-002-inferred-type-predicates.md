## Inferred Type Predicates

*This section was written by [Dan Vanderkam](https://github.com/danvk), who [implemented this feature in TypeScript 5.5](https://github.com/microsoft/TypeScript/pull/57465). Thanks Dan!*

TypeScript's control flow analysis does a great job of tracking how the type of a variable changes as it moves through your code:

```tsx
interface Bird {
    commonName: string;
    scientificName: string;
    sing(): void;
}

// Maps country names -> national bird.
// Not all nations have official birds (looking at you, Canada!)
declare const nationalBirds: Map<string, Bird>;

function makeNationalBirdCall(country: string) {
  const bird = nationalBirds.get(country);  // bird has a declared type of Bird | undefined
  if (bird) {
    bird.sing();  // bird has type Bird inside the if statement
  } else {
    // bird has type undefined here.
  }
}
```

By making you handle the `undefined` case, TypeScript pushes you to write more robust code.

In the past, this sort of type refinement was more difficult to apply to arrays. This would have been an error in all previous versions of TypeScript:

```tsx
function makeBirdCalls(countries: string[]) {
  // birds: (Bird | undefined)[]
  const birds = countries
    .map(country => nationalBirds.get(country))
    .filter(bird => bird !== undefined);

  for (const bird of birds) {
    bird.sing();  // error: 'bird' is possibly 'undefined'.
  }
}
```

This code is perfectly fine: we've filtered all the `undefined` values out of the list.
But TypeScript hasn't been able to follow along.

With TypeScript 5.5, the type checker is fine with this code:

```tsx
function makeBirdCalls(countries: string[]) {
  // birds: Bird[]
  const birds = countries
    .map(country => nationalBirds.get(country))
    .filter(bird => bird !== undefined);

  for (const bird of birds) {
    bird.sing();  // ok!
  }
}
```

Note the more precise type for `birds`.

This works because TypeScript now infers a [type predicate](https://www.typescriptlang.org/docs/handbook/2/narrowing.html#using-type-predicates) for the `filter` function.
You can see what's going on more clearly by pulling it out into a standalone function:

```tsx
// function isBirdReal(bird: Bird | undefined): bird is Bird
function isBirdReal(bird: Bird | undefined) {
  return bird !== undefined;
}
```

`bird is Bird` is the type predicate.
It means that, if the function returns `true`, then it's a `Bird` (if the function returns `false` then it's `undefined`).
The type declarations for `Array.prototype.filter` know about type predicates, so the net result is that you get a more precise type and the code passes the type checker.

TypeScript will infer that a function returns a type predicate if these conditions hold:

1. The function does not have an explicit return type or type predicate annotation.
2. The function has a single `return` statement and no implicit returns.
3. The function does not mutate its parameter.
4. The function returns a `boolean` expression that's tied to a refinement on the parameter.

Generally this works how you'd expect.
Here's a few more examples of inferred type predicates:

```tsx
// const isNumber: (x: unknown) => x is number
const isNumber = (x: unknown) => typeof x === 'number';

// const isNonNullish: <T>(x: T) => x is NonNullable<T>
const isNonNullish = <T,>(x: T) => x != null;
```

Previously, TypeScript would have just inferred that these functions return `boolean`.
It now infers signatures with type predicates like `x is number` or `x is NonNullable<T>`.

Type predicates have "if and only if" semantics.
If a function returns `x is T`, then it means that:

1. If the function returns `true` then `x` has the type `T`.
2. If the function returns `false` then `x` does *not* have type `T`.

If you're expecting a type predicate to be inferred but it's not, then you may be running afoul of the second rule. This often comes up with "truthiness" checks:

```tsx
function getClassroomAverage(students: string[], allScores: Map<string, number>) {
  const studentScores = students
    .map(student => allScores.get(student))
    .filter(score => !!score);

  return studentScores.reduce((a, b) => a + b) / studentScores.length;
  //     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  // error: Object is possibly 'undefined'.
}
```

TypeScript did not infer a type predicate for `score => !!score`, and rightly so: if this returns `true` then `score` is a `number`.
But if it returns `false`, then `score` could be either `undefined` or a `number` (specifically, `0`).
This is a real bug: if any student got a zero on the test, then filtering out their score will skew the average upwards.
Fewer will be above average and more will be sad!

As with the first example, it's better to explicitly filter out `undefined` values:

```tsx
function getClassroomAverage(students: string[], allScores: Map<string, number>) {
  const studentScores = students
    .map(student => allScores.get(student))
    .filter(score => score !== undefined);

  return studentScores.reduce((a, b) => a + b) / studentScores.length;  // ok!
}
```

A truthiness check *will* infer a type predicate for object types, where there's no ambiguity.
Remember that functions must return a `boolean` to be a candidate for an inferred type predicate: `x => !!x` might infer a type predicate, but `x => x` definitely won't.

Explicit type predicates continue to work exactly as before.
TypeScript will not check whether it would infer the same type predicate.
Explicit type predicates ("is") are no safer than a type assertion ("as").

It's possible that this feature will break existing code if TypeScript now infers a more precise type than you want. For example:

```tsx
// Previously, nums: (number | null)[]
// Now, nums: number[]
const nums = [1, 2, 3, null, 5].filter(x => x !== null);

nums.push(null);  // ok in TS 5.4, error in TS 5.5
```

The fix is to tell TypeScript the type that you want using an explicit type annotation:

```tsx
const nums: (number | null)[] = [1, 2, 3, null, 5].filter(x => x !== null);
nums.push(null);  // ok in all versions
```

For more information, check out the [implementing pull request](https://github.com/microsoft/TypeScript/pull/57465) and [Dan's blog post about implementing this feature](https://effectivetypescript.com/2024/04/16/inferring-a-type-predicate/).
