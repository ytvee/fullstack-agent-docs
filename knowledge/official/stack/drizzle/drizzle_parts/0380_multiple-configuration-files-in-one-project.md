### Multiple configuration files in one project
You can have multiple config files in the project, it's very useful when you have multiple database stages or multiple databases or different databases on the same project:
<Npx>
  drizzle-kit export --config=drizzle-dev.config.ts
  drizzle-kit export --config=drizzle-prod.config.ts
</Npx>
```plaintext {5-6}
📦 <project root>
 ├ 📂 drizzle
 ├ 📂 src
 ├ 📜 .env
 ├ 📜 drizzle-dev.config.ts
 ├ 📜 drizzle-prod.config.ts
 ├ 📜 package.json
 └ 📜 tsconfig.json
```

