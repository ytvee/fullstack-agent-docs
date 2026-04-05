### Custom migrations
You can generate empty migration files to write your own custom SQL migrations 
for DDL alternations currently not supported by Drizzle Kit or data seeding. Extended docs on custom migrations - [see here](/docs/kit-custom-migrations)

```shell
drizzle-kit generate --custom --name=seed-users
```
<Section>
```plaintext {5}
📦 <project root>
 ├ 📂 drizzle
 │ ├ 📂 20242409125510_init
 │ └ 📂 20242409125510_seed-users
 ├ 📂 src
 └ …
```
```sql
-- ./drizzle/20242409125510_seed/migration.sql

INSERT INTO "users" ("name") VALUES('Dan');
INSERT INTO "users" ("name") VALUES('Andrew');
INSERT INTO "users" ("name") VALUES('Dandrew');
```
</Section>

