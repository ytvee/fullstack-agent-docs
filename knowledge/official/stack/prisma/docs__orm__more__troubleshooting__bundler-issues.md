# Bundler issues (/docs/orm/more/troubleshooting/bundler-issues)



Problem with vercel/pkg [#problem-with-vercelpkg]

If you use [vercel/pkg](https://github.com/vercel/pkg) to package your Node.js project, you might encounter an `ENOENT` error like:

```
spawn /snapshot/enoent-problem/node_modules/.prisma/client/query-engine-debian-openssl-1.1.x ENOENT
```

Solution [#solution]

Add your Prisma query engine binary path to the `pkg/assets` section of your `package.json` file:

```json
{
  "pkg": {
    "assets": ["node_modules/.prisma/client/*.node"]
  }
}
```

See [this Github issue](https://github.com/prisma/prisma/issues/8449) for further discussion.
