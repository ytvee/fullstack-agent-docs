#### Create a new Edge Function

Run the `supabase functions new [FUNCTION_NAME]` command to create a new Edge Function:

```bash copy
supabase functions new drizzle-tutorial
```

It will create a new folder with the function name in the `supabase/functions` directory:

```text
└── supabase
    └── functions
    │   └── drizzle-tutorial
    │   │   ├── .npmrc ## Function-specific npm configuration (if needed)
    │   │   ├── deno.json ## Function-specific Deno configuration
    │   │   └── index.ts ## Your function code
```

When you create a new Edge Function, it will use TypeScript by default. However, it is possible write Edge Function in JavaScript. Learn more about it in the [documentation](https://supabase.com/docs/guides/functions/quickstart#not-using-typescript).

