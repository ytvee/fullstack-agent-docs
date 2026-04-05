## String literal types

It's not uncommon for an API to expect a specific set of strings for certain values.
For instance, consider a UI library that can move elements across the screen while controlling the ["easing" of the animation.](https://wikipedia.org/wiki/Inbetweening)

```ts
declare class UIElement {
  animate(options: AnimationOptions): void;
}

interface AnimationOptions {
  deltaX: number;
  deltaY: number;
  easing: string; // Can be "ease-in", "ease-out", "ease-in-out"
}
```

However, this is error prone - there is nothing stopping a user from accidentally misspelling one of the valid easing values:

```ts
// No errors
new UIElement().animate({ deltaX: 100, deltaY: 100, easing: "ease-inout" });
```

With TypeScript 1.8, we've introduced string literal types.
These types are written the same way string literals are, but in type positions.

Users can now ensure that the type system will catch such errors.
Here's our new `AnimationOptions` using string literal types:

```ts
interface AnimationOptions {
  deltaX: number;
  deltaY: number;
  easing: "ease-in" | "ease-out" | "ease-in-out";
}

// Error: Type '"ease-inout"' is not assignable to type '"ease-in" | "ease-out" | "ease-in-out"'
new UIElement().animate({ deltaX: 100, deltaY: 100, easing: "ease-inout" });
```
