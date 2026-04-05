### Specifying database driver
<Callout type="warning">
**Expo SQLite** and **OP SQLite** are on-device(per-user) databases, there's no way to `push` migrations there.<br/>
For embedded databases Drizzle provides **embedded migrations** - check out our [get started](/docs/get-started/expo-new) guide.
</Callout>
Drizzle Kit does not come with a pre-bundled database driver, 
it will automatically pick available database driver from your current project based on the `dialect` - [see discussion](https://github.com/drizzle-team/drizzle-orm/discussions/2203).

Mostly all drivers of the same dialect share the same set of connection params, 
as for exceptions like `aws-data-api`, `pglight` and `d1-http` - you will have to explicitly specify `driver` param.

<DriversExamples/>

