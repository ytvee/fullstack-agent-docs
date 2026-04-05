## `--target es2022`

TypeScript's `--target` option now supports `es2022`.
This means features like class fields now have a stable output target where they can be preserved.
It also means that new built-in functionality like the [`at()` method on `Array`s](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/at), [`Object.hasOwn`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/hasOwn), or [the `cause` option on `new Error`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/Error#rethrowing_an_error_with_a_cause) can be used either with this new `--target` setting, or with `--lib es2022`.

This functionality was [implemented](https://github.com/microsoft/TypeScript/pull/46291) by [Kagami Sascha Rosylight (saschanaz)](https://github.com/saschanaz) over several PRs, and we're grateful for that contribution!
