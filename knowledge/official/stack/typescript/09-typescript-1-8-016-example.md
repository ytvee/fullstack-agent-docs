##### Example

Here `map.ts` can declare that it will internally patch the `Observable` type from `observable.ts` and add the `map` method to it.

```ts
// observable.ts
export class Observable<T> {
  // ...
}
```

```ts
// map.ts
import { Observable } from "./observable";

// Create an augmentation for "./observable"
declare module "./observable" {

    // Augment the 'Observable' class definition with interface merging
    interface Observable<T> {
        map<U>(proj: (el: T) => U): Observable<U>;
    }

}

Observable.prototype.map = /*...*/;
```

```ts
// consumer.ts
import { Observable } from "./observable";
import "./map";

let o: Observable<number>;
o.map((x) => x.toFixed());
```

Similarly, the global scope can be augmented from modules using a `declare global` declarations:
