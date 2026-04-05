# Views

<IsSupportedChipGroup chips={{ 'PostgreSQL': true, 'SQLite': true, 'MySQL': true, 'SingleStore': false, 'MSSQL': true, 'CockroachDB': true }} />
There're several ways you can declare views with Drizzle ORM.  

You can declare views that have to be created or you can declare views that already exist in the database. 

You can declare views statements with an inline `query builder` syntax, with `standalone query builder` and with raw `sql` operators. 

When views are created with either inlined or standalone query builders, view columns schema will be automatically inferred, 
yet when you use `sql` you have to explicitly declare view columns schema.

