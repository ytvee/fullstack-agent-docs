## Group-Aware Organize Imports

TypeScript has an *Organize Imports* editor feature for both JavaScript and TypeScript.
Unfortunately, it could be a bit of a blunt instrument, and would often naively sort your import statements.

For instance, if you ran Organize Imports on the following file...

```ts
// local code
import * as bbb from "./bbb";
import * as ccc from "./ccc";
import * as aaa from "./aaa";

// built-ins
import * as path from "path";
import * as child_process from "child_process"
import * as fs from "fs";

// some code...
```

You would get something like the following

```ts
// local code
import * as child_process from "child_process";
import * as fs from "fs";
// built-ins
import * as path from "path";
import * as aaa from "./aaa";
import * as bbb from "./bbb";
import * as ccc from "./ccc";


// some code...
```

This is... not ideal.
Sure, our imports are sorted by their paths, and our comments and newlines are preserved, but not in a way we expected.
Much of the time, if we have our imports grouped in a specific way, then we want to keep them that way.

TypeScript 4.7 performs Organize Imports in a group-aware manner.
Running it on the above code looks a little bit more like what you'd expect:

```ts
// local code
import * as aaa from "./aaa";
import * as bbb from "./bbb";
import * as ccc from "./ccc";

// built-ins
import * as child_process from "child_process";
import * as fs from "fs";
import * as path from "path";

// some code...
```

We'd like to extend our thanks to [Minh Quy](https://github.com/MQuy) who provided [this feature](https://github.com/microsoft/TypeScript/pull/48330).
