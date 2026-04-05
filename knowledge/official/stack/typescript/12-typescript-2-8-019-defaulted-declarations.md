## Defaulted declarations

"Defaulted declarations" allow initializers that reference the declared name in the left side of a logical or:

```js
my = window.my || {};
my.app = my.app || {};
```
