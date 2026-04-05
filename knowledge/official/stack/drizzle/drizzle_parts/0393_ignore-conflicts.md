### Ignore conflicts

<Callout type='warning'>
`--ignore-conflicts` available starting from `drizzle-orm@1.0.0-beta.16`
</Callout>

In case you need `migrate` command to skip commutativity checks and bypass it, you can use `--ignore-conflicts`. If there is a situation you want to use it, then
there is a big chance that `drizzle-kit` didn't check migrations right and it's a bug. Please report us your case, so we can fix it

```shell
drizzle-kit migrate --ignore-conflicts
```

