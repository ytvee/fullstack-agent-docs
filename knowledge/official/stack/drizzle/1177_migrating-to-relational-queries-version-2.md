# Migrating to Relational Queries version 2

<Callout type='error'>
This page explains concepts available on drizzle versions `1.0.0-beta.1` and higher.
</Callout>

<Npm>
drizzle-orm@beta
drizzle-kit@beta -D
</Npm>

<br/>

<Prerequisites>
- **Drizzle Relations v1** - [read here](/docs/relations)
- **Relational Queries v1** - [read here](/docs/rqb)
- **drizzle-kit pull** - [read here](/docs/drizzle-kit-pull)
- **Relations Fundamentals** - [read here](/docs/relations-schema-declaration)
</Prerequisites>

<Callout>
Below is the table of contents. Click an item to jump to that section:

- [What is working differently from v1](#what-was-changed-and-is-working-differently-from-v1)  
- [New features in v2](2#what-is-new)  
- [How to migrate relations definition from v1 to v2](#how-to-migrate-relations-schema-definition-from-v1-to-v2)  
- [How to migrate queries from v1 to v2](#how-to-migrate-queries-from-v1-to-v2)  
- [Partial upgrade, or how to stay on v1 even after an upgrade?](#partial-upgrade-or-how-to-stay-on-rqb-v1-even-after-an-upgrade)  
- [Internal changes(imports, internal types, etc.)](#internal-changes)
</Callout>

