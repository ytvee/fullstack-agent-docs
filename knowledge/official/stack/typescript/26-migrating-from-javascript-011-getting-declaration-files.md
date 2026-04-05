#### Getting Declaration Files

If you started converting over to TypeScript imports, you'll probably run into errors like `Cannot find module 'foo'.`.
The issue here is that you likely don't have _declaration files_ to describe your library.
Luckily this is pretty easy.
If TypeScript complains about a package like `lodash`, you can just write

```shell
npm install -S @types/lodash
```

If you're using a module option other than `commonjs`, you'll need to set your [`moduleResolution`](/tsconfig#moduleResolution) option to `node`.

After that, you'll be able to import lodash with no issues, and get accurate completions.
