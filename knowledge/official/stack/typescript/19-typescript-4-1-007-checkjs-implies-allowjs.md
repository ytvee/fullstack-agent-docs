## `checkJs` Implies `allowJs`

Previously if you were starting a checked JavaScript project, you had to set both [`allowJs`](/tsconfig#allowJs) and [`checkJs`](/tsconfig#checkJs).
This was a slightly annoying bit of friction in the experience, so [`checkJs`](/tsconfig#checkJs) now implies [`allowJs`](/tsconfig#allowJs) by default.

[See more details at the pull request](https://github.com/microsoft/TypeScript/pull/40275).
