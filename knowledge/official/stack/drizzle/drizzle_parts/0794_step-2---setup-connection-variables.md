#### Step 2 - Setup connection variables

Create a `.env` file in the root of your project and add your database connection variable:

```plaintext copy
DATABASE_URL=postgresql://{username}:{password}@{host}:{port}/postgres?sslmode=verify-full
```

<Callout title='tips'>
You can obtain your connection credentials from the PlanetScale dashboard by navigating to your database, clicking **"Connect"**, and creating a **"Default role"**. See the [PlanetScale connection guide](https://planetscale.com/docs/postgres/tutorials/planetscale-postgres-drizzle#create-credentials-and-connect) for detailed steps.
</Callout>

