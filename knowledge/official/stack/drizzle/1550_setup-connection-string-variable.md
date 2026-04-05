#### Setup connection string variable

Navigate to the Xata dashboard and copy the PostgreSQL connection string. You can find this on the branch overview page.

Add `DATABASE_URL` variable to your `.env` or `.env.local` file:

```plaintext copy
DATABASE_URL=<YOUR_XATA_DATABASE_URL>
```

The connection string format will be:
```plaintext
postgresql://postgres:<password>@<branch-id>.<region>.xata.tech/<database>?sslmode=require
```

Example:
```plaintext
postgresql://postgres:password@t56hgfp7hd2sjfeiqcn66qpo8s.us-east-1.xata.tech/app?sslmode=require
```

<Callout type="info">
Xata provides branch-based development, allowing you to create isolated database branches for development, staging, and production environments.
</Callout>

