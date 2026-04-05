# Get Started with Drizzle and Gel

<Prerequisites>
  - **tsx** - package for running TypeScript files - [read here](https://tsx.is/)
  - **gel-js** - package for querying your Gel database - [read here](https://github.com/geldata/gel-js)
</Prerequisites>

Drizzle has native support for Gel connections with the `gel` client.

This is the basic file structure of the project. In the `src` directory, we have table definition in `index.ts`. In `drizzle` folder there are generated Gel to Drizzle schema

```plaintext
📦 <project root>
 ├ 📂 drizzle
 ├ 📂 src
 │ └ 📜 index.ts
 ├ 📜 drizzle.config.ts
 ├ 📜 package.json
 └ 📜 tsconfig.json
```

