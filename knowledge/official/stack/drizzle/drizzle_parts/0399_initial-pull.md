### Initial pull

<Callout type='error'>
This feature is available on  `1.0.0-beta.2` and higher.
</Callout>

<Npm>
drizzle-orm@beta
drizzle-kit@beta -D
</Npm>

<br/>

You can use the `--init` flag to mark the pulled schema as an applied migration in your database, 
so that all subsequent migrations are diffed against the initial one

```shell
npx drizzle-kit push --init
```

