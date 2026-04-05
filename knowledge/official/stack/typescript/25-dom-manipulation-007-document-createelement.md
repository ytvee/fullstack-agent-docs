### `Document.createElement`

The definition for this method is (I have omitted the _deprecated_ definition):

```ts
createElement<K extends keyof HTMLElementTagNameMap>(tagName: K, options?: ElementCreationOptions): HTMLElementTagNameMap[K];
createElement(tagName: string, options?: ElementCreationOptions): HTMLElement;
```

This is an overloaded function definition. The second overload is simplest and works a lot like the `getElementById` method does. Pass it any `string` and it will return a standard HTMLElement. This definition is what enables developers to create unique HTML element tags.

For example `document.createElement('xyz')` returns a `<xyz></xyz>` element, clearly not an element that is specified by the HTML specification.

> For those interested, you can interact with custom tag elements using the `document.getElementsByTagName`

For the first definition of `createElement`, it is using some advanced generic patterns. It is best understood broken down into chunks, starting with the generic expression: `<K extends keyof HTMLElementTagNameMap>`. This expression defines a generic parameter `K` that is _constrained_ to the keys of the interface `HTMLElementTagNameMap`. The map interface contains every specified HTML tag name and its corresponding type interface. For example here are the first 5 mapped values:

```ts
interface HTMLElementTagNameMap {
    "a": HTMLAnchorElement;
    "abbr": HTMLElement;
    "address": HTMLElement;
    "applet": HTMLAppletElement;
    "area": HTMLAreaElement;
        ...
}
```

Some elements do not exhibit unique properties and so they just return `HTMLElement`, but other types do have unique properties and methods so they return their specific interface (which will extend from or implement `HTMLElement`).

Now, for the remainder of the `createElement` definition: `(tagName: K, options?: ElementCreationOptions): HTMLElementTagNameMap[K]`. The first argument `tagName` is defined as the generic parameter `K`. The TypeScript interpreter is smart enough to _infer_ the generic parameter from this argument. This means that the developer does not have to specify the generic parameter when using the method; whatever value is passed to the `tagName` argument will be inferred as `K` and thus can be used throughout the remainder of the definition. This is exactly what happens; the return value `HTMLElementTagNameMap[K]` takes the `tagName` argument and uses it to return the corresponding type. This definition is how the `p` variable from the code snippet gets a type of `HTMLParagraphElement`. And if the code was `document.createElement('a')`, then it would be an element of type `HTMLAnchorElement`.
