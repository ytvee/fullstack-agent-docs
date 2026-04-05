## ECMAScript Module Support in Node.js

For the last few years, Node.js has been working to support ECMAScript modules (ESM).
This has been a very difficult feature, since the Node.js ecosystem is built on a different module system called CommonJS (CJS).
Interoperating between the two brings large challenges, with many new features to juggle;
however, support for ESM in Node.js was largely implemented in Node.js 12 and later.
Around TypeScript 4.5 we rolled out nightly-only support for ESM in Node.js to get some feedback from users and let library authors ready themselves for broader support.

TypeScript 4.7 adds this functionality with two new `module` settings: `node16` and `nodenext`.

```jsonc
{
    "compilerOptions": {
        "module": "node16",
    }
}
```

These new modes bring a few high-level features which we'll explore here.
