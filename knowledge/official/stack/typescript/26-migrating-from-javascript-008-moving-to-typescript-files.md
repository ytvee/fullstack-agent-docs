## Moving to TypeScript Files

At this point, you're probably ready to start using TypeScript files.
The first step is to rename one of your `.js` files to `.ts`.
If your file uses JSX, you'll need to rename it to `.tsx`.

Finished with that step?
Great!
You've successfully migrated a file from JavaScript to TypeScript!

Of course, that might not feel right.
If you open that file in an editor with TypeScript support (or if you run `tsc --pretty`), you might see red squiggles on certain lines.
You should think of these the same way you'd think of red squiggles in an editor like Microsoft Word.
TypeScript will still translate your code, just like Word will still let you print your documents.

If that sounds too lax for you, you can tighten that behavior up.
If, for instance, you _don't_ want TypeScript to compile to JavaScript in the face of errors, you can use the [`noEmitOnError`](/tsconfig#noEmitOnError) option.
In that sense, TypeScript has a dial on its strictness, and you can turn that knob up as high as you want.

If you plan on using the stricter settings that are available, it's best to turn them on now (see [Getting Stricter Checks](#getting-stricter-checks) below).
For instance, if you never want TypeScript to silently infer `any` for a type without you explicitly saying so, you can use [`noImplicitAny`](/tsconfig#noImplicitAny) before you start modifying your files.
While it might feel somewhat overwhelming, the long-term gains become apparent much more quickly.
