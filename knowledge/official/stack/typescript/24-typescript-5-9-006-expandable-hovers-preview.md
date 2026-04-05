## Expandable Hovers (Preview)

*Quick Info* (also called "editor tooltips" and "hovers") can be very useful for peeking at variables to see their types, or at type aliases to see what they actually refer to.
Still, it's common for people to want to *go deeper* and get details from whatever's displayed within the quick info tooltip.
For example, if we hover our mouse over the parameter `options` in the following example:

```ts
export function drawButton(options: Options): void
```

We're left with `(parameter) options: Options`.

![Tooltip for a parameter declared as `options` which just shows `options: Options`.](https://devblogs.microsoft.com/typescript/wp-content/uploads/sites/11/2025/06/bare-hover-5.8-01.png)

Do we really need to jump to the definition of the type `Options` just to see what members this value has?

Previously, that was actually the case.
To help here, TypeScript 5.9 is now previewing a feature called *expandable hovers*, or "quick info verbosity".
If you use an editor like VS Code, you'll now see a `+` and `-` button on the left of these hover tooltips.
Clicking on the `+` button will expand out types more deeply, while clicking on the `-` button will collapse to the last view.

<video autoplay loop style="width: 100%;" src="https://devblogs.microsoft.com/typescript/wp-content/uploads/sites/11/2025/06/expandable-quick-info-1.mp4" aria-label="Expanding quick info to see more about the type of `Options`."></video>

This feature is currently in preview, and we are seeking feedback for both TypeScript and our partners on Visual Studio Code.
For more details, see [the PR for this feature here](https://github.com/microsoft/TypeScript/pull/59940).
