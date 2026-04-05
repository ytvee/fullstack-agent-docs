## Resolution Customization with `moduleSuffixes`

TypeScript 4.7 now supports a `moduleSuffixes` option to customize how module specifiers are looked up.

```jsonc
{
    "compilerOptions": {
        "moduleSuffixes": [".ios", ".native", ""]
    }
}
```

Given the above configuration, an import like the following...

```ts
import * as foo from "./foo";
```

will try to look at the relative files `./foo.ios.ts`, `./foo.native.ts`, and finally `./foo.ts`.

<aside>

Note that the empty string `""` in `moduleSuffixes` is necessary for TypeScript to also look-up `./foo.ts`.
In a sense, the default value for `moduleSuffixes` is `[""]`.

</aside>

This feature can be useful for React Native projects where each target platform can use a separate `tsconfig.json` with differing `moduleSuffixes`.

[The `moduleSuffixes` option](https://github.com/microsoft/TypeScript/pull/48189) was contributed thanks to [Adam Foxman](https://github.com/afoxman)!
