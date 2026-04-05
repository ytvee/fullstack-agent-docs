#### Initialize the tenant-aware middleware

Next, we'll add middleware to the example. This middleware grabs the tenant ID from the path parameters and stores it in the `AsyncLocalStorage`. 
The `tenantDB` wrapper that we created in `src/db/index.ts` uses this tenant ID to set `nile.tenant_id` when executing queries, 
which then guarantees that the queries will execute against this tenant's virtual database.

```typescript copy filename="src/app.ts"
// set the tenant ID in the context based on the URL parameter
app.use('/api/tenants/:tenantId/*', (req, res, next) => {
  const tenantId = req.params.tenantId;
  console.log("setting context to tenant: " + tenantId);
  tenantContext.run(tenantId, next);
});
```

<Callout>
The example gets the tenant ID from path parameter, but it is also common to set the tenant ID in a header such as `x-tenant-id` or in a cookie.
</Callout>

