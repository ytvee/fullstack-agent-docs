#### Sequentially Added Properties

Some people find it more aesthetically pleasing to create an object and add properties immediately after like so:

```js
var options = {};
options.color = "red";
options.volume = 11;
```

TypeScript will say that you can't assign to `color` and `volume` because it first figured out the type of `options` as `{}` which doesn't have any properties.
If you instead moved the declarations into the object literal themselves, you'd get no errors:

```ts
let options = {
  color: "red",
  volume: 11,
};
```

You could also define the type of `options` and add a type assertion on the object literal.

```ts
interface Options {
  color: string;
  volume: number;
}

let options = {} as Options;
options.color = "red";
options.volume = 11;
```

Alternatively, you can just say `options` has the type `any` which is the easiest thing to do, but which will benefit you the least.
