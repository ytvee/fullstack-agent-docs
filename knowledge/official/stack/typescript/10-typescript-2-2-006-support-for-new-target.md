## Support for `new.target`

The `new.target` meta-property is new syntax introduced in ES2015.
When an instance of a constructor is created via `new`, the value of `new.target` is set to be a reference to the constructor function initially used to allocate the instance.
If a function is called rather than constructed via `new`, `new.target` is set to `undefined`.

`new.target` comes in handy when `Object.setPrototypeOf` or `__proto__` needs to be set in a class constructor. One such use case is inheriting from `Error` in NodeJS v4 and higher.
