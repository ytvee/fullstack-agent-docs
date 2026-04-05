#### Link your local project to a hosted Supabase project

You can create new Supabase project in the [dashboard](https://supabase.com/dashboard) or by following this [link](https://database.new/).

Copy the `Reference ID` from project settings and use it to link your local development project to a hosted Supabase project by running the following command:

```bash copy
supabase link --project-ref=<REFERENCE_ID>
```

Push your schema changes to the hosted Supabase project by running the following command:

```bash copy
supabase db push
```

