### `readFile` Method is No Longer Optional on `LanguageServiceHost`

If you're creating `LanguageService` instances, then provided `LanguageServiceHost`s will need to provide a `readFile` method.
This change was necessary to support the new `moduleDetection` compiler option.

You can [read more on the change here](https://github.com/microsoft/TypeScript/pull/47495).
