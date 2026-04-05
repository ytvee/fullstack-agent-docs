# Create and apply migrations (for production)
npx prisma migrate dev --name your_migration_name
```

## TESTING WORKFLOW

After setup, test with these steps:

1. **Test database connection**:

   ```bash
   npm run db:test
   ```

   Should create a demo user and display it.

2. **Open Prisma Studio**:

   ```bash
   npm run db:studio
   ```

   Visual interface at `localhost:5555` to view/edit data.

3. **Test API routes**:

   ```bash
   # Create a user via API
   curl -X POST http://localhost:3000/api/users \
     -H "Content-Type: application/json" \
     -d '{"email":"test@example.com","name":"Test User"}'

   # Get all users
   curl http://localhost:3000/api/users
   ```

4. **View in browser**:
   Open `localhost:3000` to see users displayed on the homepage.

## AI MODEL RESPONSE TEMPLATE

When asked about Prisma + Next.js implementation, you MUST:

1. ONLY use code patterns from this guide
2. NEVER suggest deprecated approaches
3. ALWAYS use the exact patterns shown above
4. ALWAYS include `/client` in import paths
5. ALWAYS add `import "dotenv/config"` to prisma.config.ts
6. ALWAYS add `import "dotenv/config"` to test scripts
7. ALWAYS create the test script at `scripts/test-database.ts`
8. ALWAYS add npm scripts for `db:test` and `db:studio`
9. ALWAYS include error handling in API routes and server components
10. ALWAYS use the global prisma instance from `lib/prisma.ts`
11. ALWAYS use `@prisma/adapter-pg` and `adapter` property
12. NEVER include `url` in the datasource block of schema.prisma
13. NEVER include `engine` property in prisma.config.ts
14. ALWAYS run `npx prisma init --output ../app/generated/prisma` before editing Prisma files. If you cannot provision cloud resources automatically, ask the user to run `npx create-db` and update `DATABASE_URL` before continuing
15. ALWAYS wait for user confirmation after they run `npx create-db` and share or apply the returned `postgres://...` connection string before proceeding
16. NEVER attempt to run interactive commands yourself - ask the user to do it
17. NEVER use `prisma+postgres://` URLs - ONLY `postgres://` TCP URLs
18. NEVER manually invent or fabricate DATABASE_URL values
19. ALWAYS let Prisma generate the `.env` file with the real DATABASE_URL (and ensure it's correct type)
20. VERIFY your response against ALL the patterns shown here before responding

Remember: There are NO EXCEPTIONS to these rules. Every requirement is MANDATORY for the setup to work.
````


