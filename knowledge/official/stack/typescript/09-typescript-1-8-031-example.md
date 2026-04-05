##### Example

```ts
import { jsxFactory } from "jsxFactory";

var div = <div>Hello JSX!</div>;
```

Compiled with:

```shell
tsc --jsx react --reactNamespace jsxFactory --m commonJS
```

Results in:

```js
"use strict";
var jsxFactory_1 = require("jsxFactory");
var div = jsxFactory_1.jsxFactory.createElement("div", null, "Hello JSX!");
```
