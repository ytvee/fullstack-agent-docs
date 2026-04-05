#### Step 8 - Applying changes to the database

With Expo, you would need to generate migrations using the `drizzle-kit generate` command and then apply them at runtime using the `drizzle-orm` `migrate()` function

Generate migrations:
```bash copy
npx drizzle-kit generate
```

