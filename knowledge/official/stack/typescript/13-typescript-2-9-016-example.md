##### Example

```ts
// settings.json

{
    "repo": "TypeScript",
    "dry": false,
    "debug": false
}
```

```ts
// a.ts

import settings from "./settings.json";

settings.debug === true; // OK
settings.dry === 2; // Error: Operator '===' cannot be applied boolean and number
```

```json tsconfig
// tsconfig.json

{
  "compilerOptions": {
    "module": "commonjs",
    "resolveJsonModule": true,
    "esModuleInterop": true
  }
}
```
