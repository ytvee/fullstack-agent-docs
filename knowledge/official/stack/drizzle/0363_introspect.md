### `introspect`
<rem025/>

Configuration for `drizzle-kit pull` command.

`casing` is responsible for in-code column keys casing

|               |                      |
| :------------ | :-----------------   |
| type          | `{ casing: "preserve" \| "camel" }` |
| default       | `{ casing: "camel" }`                    |
| commands      | `pull`   |

<rem025/>

<CodeTabs items={["camel", "preserve"]}>
<Section>
```ts
import * as p from "drizzle-orm/pg-core"

export const users = p.pgTable("users", {
  id: p.serial(),
  firstName: p.text("first-name"),
  lastName: p.text("LastName"),
  email: p.text(),
  phoneNumber: p.text("phone_number"),
});
```
```sql
SELECT a.attname AS column_name, format_type(a.atttypid, a.atttypmod) as data_type FROM pg_catalog.pg_attribute a;
```
``` 
 column_name   | data_type        
---------------+------------------------
 id            | serial
 first-name    | text
 LastName      | text
 email         | text
 phone_number  | text
```
</Section>
<Section>
```ts
import * as p from "drizzle-orm/pg-core"

export const users = p.pgTable("users", {
  id: p.serial(),
  "first-name": p.text("first-name"),
  LastName: p.text("LastName"),
  email: p.text(),
  phone_number: p.text("phone_number"),
});
```
```sql
SELECT a.attname AS column_name, format_type(a.atttypid, a.atttypmod) as data_type FROM pg_catalog.pg_attribute a;
```
``` 
 column_name   | data_type        
---------------+------------------------
 id            | serial
 first-name    | text
 LastName      | text
 email         | text
 phone_number  | text
```
</Section>
</CodeTabs>


