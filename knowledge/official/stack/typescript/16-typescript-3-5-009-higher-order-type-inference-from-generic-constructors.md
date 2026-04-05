## Higher order type inference from generic constructors

In TypeScript 3.4, we improved inference for when generic functions that return functions like so:

```ts
function compose<T, U, V>(f: (x: T) => U, g: (y: U) => V): (x: T) => V {
  return x => g(f(x));
}
```

took other generic functions as arguments, like so:

```ts
function arrayify<T>(x: T): T[] {
  return [x];
}

type Box<U> = { value: U };
function boxify<U>(y: U): Box<U> {
  return { value: y };
}

let newFn = compose(arrayify, boxify);
```

Instead of a relatively useless type like `(x: {}) => Box<{}[]>`, which older versions of the language would infer, TypeScript 3.4's inference allows `newFn` to be generic.
Its new type is `<T>(x: T) => Box<T[]>`.

TypeScript 3.5 generalizes this behavior to work on constructor functions as well.

```ts
class Box<T> {
  kind: "box";
  value: T;
  constructor(value: T) {
    this.value = value;
  }
}

class Bag<U> {
  kind: "bag";
  value: U;
  constructor(value: U) {
    this.value = value;
  }
}

function composeCtor<T, U, V>(
  F: new (x: T) => U,
  G: new (y: U) => V
): (x: T) => V {
  return x => new G(new F(x));
}

let f = composeCtor(Box, Bag); // has type '<T>(x: T) => Bag<Box<T>>'
let a = f(1024); // has type 'Bag<Box<number>>'
```

In addition to compositional patterns like the above, this new inference on generic constructors means that functions that operate on class components in certain UI libraries like React can more correctly operate on generic class components.

```ts
type ComponentClass<P> = new (props: P) => Component<P>;
declare class Component<P> {
  props: P;
  constructor(props: P);
}

declare function myHoc<P>(C: ComponentClass<P>): ComponentClass<P>;

type NestedProps<T> = { foo: number; stuff: T };

declare class GenericComponent<T> extends Component<NestedProps<T>> {}

// type is 'new <T>(props: NestedProps<T>) => Component<NestedProps<T>>'
const GenericComponent2 = myHoc(GenericComponent);
```

To learn more, [check out the original pull request on GitHub](https://github.com/microsoft/TypeScript/pull/31116).
