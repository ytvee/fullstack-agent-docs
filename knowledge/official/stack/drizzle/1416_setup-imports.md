#### Setup imports

Create a `import_map.json` file in the root of your project and add the following content:

```json copy filename="import_map.json"
{
  "imports": {
    "drizzle-orm/": "https://esm.sh/drizzle-orm/",
    "postgres": "https://esm.sh/postgres"
  }
}
```

Read more about `import_map.json` in Netlify Edge Functions [here](https://docs.netlify.com/edge-functions/api/#import-maps).

