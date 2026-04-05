##### Example

Assuming that `__dirname` is always available on `import.meta`, the declaration would be done through reopening `ImportMeta` interface:

```ts
// node.d.ts
interface ImportMeta {
  __dirname: string;
}
```

And usage would be:

```ts
import.meta.__dirname; // Has type 'string'
```

`import.meta` is only allowed when targeting `ESNext` modules and ECMAScript targets.
