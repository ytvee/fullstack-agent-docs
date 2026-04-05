#### Update your Prisma schema

Add Drizzle generator to your Prisma schema. `output` is the path where generated Drizzle schema TS files will be placed.
```prisma copy filename="schema.prisma" {5-8}
generator client {
  provider = "prisma-client-js"
}

generator drizzle {
  provider = "drizzle-prisma-generator"
  output   = "./drizzle" // Where to put generated Drizle tables
}

// Rest of your Prisma schema

datasource db {
  provider = "postgresql"
  url      = env("DB_URL")
}

model User {
  id    Int     @id @default(autoincrement())
  email String  @unique
  name  String?
}

...
```

