#### Create a Netlify configuration file

Create a `netlify.toml` file in the root of your project and add the following content:

```toml copy filename="netlify.toml"
[functions]
  deno_import_map = "./import_map.json"

[[edge_functions]]
  path = "/user"
  function = "user"
```

This configuration tells Netlify to use the `import_map.json` file for Deno imports and to route requests to the `/user` path to the `user.ts` function. 
Read more about `netlify.toml` [here](https://docs.netlify.com/configure-builds/file-based-configuration/).

