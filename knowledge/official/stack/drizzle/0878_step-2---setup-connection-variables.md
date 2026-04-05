#### Step 2 - Setup connection variables

<SetupEnv env_variable='DB_FILE_NAME' />

<Callout type='info' title='important'>
For example, if you want to create an SQLite database file in the root of your project for testing purposes, you need to use `file:` before the actual filename, as this is the format required by `LibSQL`, like this:
```plaintext copy
DB_FILE_NAME=file:local.db
```
You can check the **[LibSQL docs](https://docs.turso.tech/sdk/ts/reference#local-development)** for more info.
</Callout>

