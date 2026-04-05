#### Step 2 - Initialize the driver and make a query

You would need to have a `wrangler.toml` file for Durable Objects database and will look something like this:
```toml {16-18,21-24}
#:schema node_modules/wrangler/config-schema.json
name = "sqlite-durable-objects"
main = "src/index.ts"
compatibility_date = "2024-11-12"
compatibility_flags = [ "nodejs_compat" ]

