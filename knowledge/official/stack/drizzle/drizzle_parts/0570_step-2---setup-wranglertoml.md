#### Step 2 - Setup wrangler.toml

You would need to have a `wrangler.toml` file for D1 database and will look something like this:
```toml
#:schema node_modules/wrangler/config-schema.json
name = "sqlite-durable-objects"
main = "src/index.ts"
compatibility_date = "2024-11-12"
compatibility_flags = [ "nodejs_compat" ]

