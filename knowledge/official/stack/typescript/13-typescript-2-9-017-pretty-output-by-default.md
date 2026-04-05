## `--pretty` output by default

Starting TypeScript 2.9 errors are displayed under [`pretty`](/tsconfig#pretty) by default if the output device is applicable for colorful text.
TypeScript will check if the output stream has [`isTty`](https://nodejs.org/api/tty.html) property set.

Use `--pretty false` on the command line or set `"pretty": false` in your `tsconfig.json` to disable [`pretty`](/tsconfig#pretty) output.
