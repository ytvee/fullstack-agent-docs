## Isolated Declarations

*This section was co-authored by [Rob Palmer](https://github.com/robpalme) who supported the design of isolated declarations.*

Declaration files (a.k.a. `.d.ts` files) describe the shape of existing libraries and modules to TypeScript.
This lightweight description includes the library's type signatures and excludes implementation details such as the function bodies.
They are published so that TypeScript can efficiently check your usage of a library without needing to analyse the library itself.
Whilst it is possible to handwrite declaration files, if you are authoring typed code, it's much safer and simpler to let TypeScript generate them automatically from source files using `--declaration`.

The TypeScript compiler and its APIs have always had the job of generating declaration files;
however, there are some use-cases where you might want to use other tools, or where the traditional build process doesn't scale.
