## Strict function types

TypeScript 2.6 introduces a new strict checking flag, [`strictFunctionTypes`](/tsconfig#strictFunctionTypes).
The [`strictFunctionTypes`](/tsconfig#strictFunctionTypes) switch is part of the [`strict`](/tsconfig#strict) family of switches, meaning that it defaults to on in [`strict`](/tsconfig#strict) mode.
You can opt-out by setting `--strictFunctionTypes false` on your command line or in your tsconfig.json.

Under [`strictFunctionTypes`](/tsconfig#strictFunctionTypes) function type parameter positions are checked _contravariantly_ instead of _bivariantly_.
For some background on what variance means for function types check out [What are covariance and contravariance?](https://web.archive.org/web/20220823104433/https://www.stephanboyer.com/post/132/what-are-covariance-and-contravariance).

The stricter checking applies to all function types, _except_ those originating in method or constructor declarations.
Methods are excluded specifically to ensure generic classes and interfaces (such as `Array<T>`) continue to mostly relate covariantly.

Consider the following example in which `Animal` is the supertype of `Dog` and `Cat`:

```ts
declare let f1: (x: Animal) => void;
declare let f2: (x: Dog) => void;
declare let f3: (x: Cat) => void;
f1 = f2; // Error with --strictFunctionTypes
f2 = f1; // Ok
f2 = f3; // Error
```

The first assignment is permitted in default type checking mode, but flagged as an error in strict function types mode.
Intuitively, the default mode permits the assignment because it is _possibly_ sound, whereas strict function types mode makes it an error because it isn't _provably_ sound.
In either mode the third assignment is an error because it is _never_ sound.

Another way to describe the example is that the type `(x: T) => void` is _bivariant_ (i.e. covariant _or_ contravariant) for `T` in default type checking mode, but _contravariant_ for `T` in strict function types mode.
