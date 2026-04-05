## Optional Variance Annotations for Type Parameters

Let's take the following types.

```ts
interface Animal {
    animalStuff: any;
}

interface Dog extends Animal {
    dogStuff: any;
}

// ...

type Getter<T> = () => T;

type Setter<T> = (value: T) => void;
```

Imagine we had two different instances of `Getter`s.
Figuring out whether any two different `Getter`s are substitutable for one another depends entirely on `T`.
In the case of whether an assignment of `Getter<Dog>`&nbsp;&rarr;&nbsp;`Getter<Animal>` is valid, we have to check whether `Dog`&nbsp;&rarr;&nbsp;`Animal` is valid.
Because each type for `T` just gets related in the same "direction", we say that the `Getter` type is *covariant* on `T`.
On the other hand, checking whether `Setter<Dog>`&nbsp;&rarr;&nbsp;`Setter<Animal>` is valid involves checking whether `Animal`&nbsp;&rarr;&nbsp;`Dog` is valid.
That "flip" in direction is kind of like how in math, checking whether &minus;*x*&nbsp;&lt;&nbsp;*&minus;y* is the same as checking whether *y*&nbsp;&lt;&nbsp;*x*.
When we have to flip directions like this to compare `T`, we say that `Setter` is *contravariant* on `T`.

With TypeScript 4.7, we're now able to *explicitly* specify variance on type parameters.

So now, if we want to make it explicit that `Getter` is covariant on `T`, we can now give it an `out` modifier.

```ts
type Getter<out T> = () => T;
```

And similarly, if we also want to make it explicit that `Setter` is contravariant on `T`, we can give it an `in` modifier.

```ts
type Setter<in T> = (value: T) => void;
```

`out` and `in` are used here because a type parameter's variance depends on whether it's used in an *output* or an *input*.
Instead of thinking about variance, you can just think about if `T` is used in output and input positions.

There are also cases for using both `in` and `out`.

```ts
interface State<in out T> {
    get: () => T;
    set: (value: T) => void;
}
```

When a `T` is used in both an output and input position, it becomes *invariant*.
Two different `State<T>`s can't be interchanged unless their `T`s are the same.
In other words, `State<Dog>` and `State<Animal>` aren't substitutable for the other.

Now technically speaking, in a purely structural type system, type parameters and their variance don't really matter - you can just plug in types in place of each type parameter and check whether each matching member is structurally compatible.
So if TypeScript uses a structural type system, why are we interested in the variance of type parameters?
And why might we ever want to annotate them?

One reason is that it can be useful for a reader to explicitly see how a type parameter is used at a glance.
For much more complex types, it can be difficult to tell whether a type is meant to be read, written, or both.
TypeScript will also help us out if we forget to mention how that type parameter is used.
As an example, if we forgot to specify both `in` and `out` on `State`, we'd get an error.

```ts
interface State<out T> {
    //          ~~~~~
    // error!
    // Type 'State<sub-T>' is not assignable to type 'State<super-T>' as implied by variance annotation.
    //   Types of property 'set' are incompatible.
    //     Type '(value: sub-T) => void' is not assignable to type '(value: super-T) => void'.
    //       Types of parameters 'value' and 'value' are incompatible.
    //         Type 'super-T' is not assignable to type 'sub-T'.
    get: () => T;
    set: (value: T) => void;
}
```

Another reason is precision and speed!
TypeScript already tries to infer the variance of type parameters as an optimization.
By doing this, it can type-check larger structural types in a reasonable amount of time.
Calculating variance ahead of time allows the type-checker to skip deeper comparisons and just compare type arguments which can be *much* faster than comparing the full structure of a type over and over again.
But often there are cases where this calculation is still fairly expensive, and the calculation may find circularities that can't be accurately resolved, meaning there's no clear answer for the variance of a type.

```ts
type Foo<T> = {
    x: T;
    f: Bar<T>;
}

type Bar<U> = (x: Baz<U[]>) => void;

type Baz<V> = {
    value: Foo<V[]>;
}

declare let foo1: Foo<unknown>;
declare let foo2: Foo<string>;

foo1 = foo2;  // Should be an error but isn't ❌
foo2 = foo1;  // Error - correct ✅
```

Providing an explicit annotation can speed up type-checking at these circularities and provide better accuracy.
For instance, marking `T` as invariant in the above example can help stop the problematic assignment.

```diff
- type Foo<T> = {
+ type Foo<in out T> = {
      x: T;
      f: Bar<T>;
  }
```

We don't necessarily recommend annotating every type parameter with its variance;
For example, it's possible (but not recommended) to make variance a little stricter than is necessary, so TypeScript won't stop you from marking something as invariant if it's really just covariant, contravariant, or even independent.
So if you do choose to add explicit variance markers, we would encourage thoughtful and precise use of them.

But if you're working with deeply recursive types, especially if you're a library author, you may be interested in using these annotations to the benefit of your users.
Those annotations can provide wins in both accuracy and type-checking speed, which can even affect their code editing experience.
Determining when variance calculation is a bottleneck on type-checking time can be done experimentally, and determined using tooling like our [analyze-trace](https://github.com/microsoft/typescript-analyze-trace) utility.


For more details on this feature, you can [read up on the pull request](https://github.com/microsoft/TypeScript/pull/48240).
