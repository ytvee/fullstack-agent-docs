### `dialect`
<rem025/>

Dialect of the database you're using 
|               |                                                 |
| :------------ | :-----------------------------------            |
| type        | <Dialects/>                                     |
| default        | --                                     |
| commands    | `generate` `migrate` `push` `pull` `check` `up` |

<rem025/>
```ts {4}
import { defineConfig } from "drizzle-kit";

export default defineConfig({
  dialect: "mysql", 
});
```


