#### Test your code locally

Run the following command to start the Netlify dev server:

```bash copy
netlify dev
```

When you first run the command it will suggest to configure VS Code to use Edge Functions. Click `Yes` to configure it. `settings.json` file will be created in the `.vscode` directory.
If you still see red underlines, you can restart the Deno Language Server.

Open your browser and navigate to the route `/user`. You should see the user data returned from the Neon database:

```plaintext
[]
```

It could be an empty array if you haven't added any data to the `users_table` table.

