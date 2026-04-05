#### Get database connection string

On the left side-bar menu, select the "Settings" option, click on the Postgres logo, and click "generate credentials". Copy the connection string and add it to the `.env` file in your project:

```plaintext copy
NILEDB_URL=postgres://youruser:yourpassword@us-west-2.db.thenile.dev:5432:5432/your_db_name
```

