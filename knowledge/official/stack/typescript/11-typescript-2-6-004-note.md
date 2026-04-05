##### Note

Under [`strictFunctionTypes`](/tsconfig#strictFunctionTypes) the first assignment is still permitted if `compare` was declared as a method.
Effectively, `T` is bivariant in `Comparer<T>` because it is used only in method parameter positions.

```ts
interface Comparer<T> {
  compare(a: T, b: T): number;
}

declare let animalComparer: Comparer<Animal>;
declare let dogComparer: Comparer<Dog>;

animalComparer = dogComparer; // Ok because of bivariance
dogComparer = animalComparer; // Ok
```

TypeScript 2.6 also improves type inference involving contravariant positions:

```ts
function combine<T>(...funcs: ((x: T) => void)[]): (x: T) => void {
  return x => {
    for (const f of funcs) f(x);
  };
}

function animalFunc(x: Animal) {}
function dogFunc(x: Dog) {}

let combined = combine(animalFunc, dogFunc); // (x: Dog) => void
```

Above, all inferences for `T` originate in contravariant positions, and we therefore infer the _best common subtype_ for `T`.
This contrasts with inferences from covariant positions, where we infer the _best common supertype_.
