# Getting Started (/docs/studio/getting-started)



Installation [#installation]

Prisma Studio comes bundled with the Prisma CLI. To get started, make sure you have Node.js installed, then install the Prisma CLI:

<CodeBlockTabs defaultValue="npm" groupId="package-manager" persist>
  <CodeBlockTabsList>
    <CodeBlockTabsTrigger value="npm">
      npm
    </CodeBlockTabsTrigger>

    <CodeBlockTabsTrigger value="pnpm">
      pnpm
    </CodeBlockTabsTrigger>

    <CodeBlockTabsTrigger value="yarn">
      yarn
    </CodeBlockTabsTrigger>

    <CodeBlockTabsTrigger value="bun">
      bun
    </CodeBlockTabsTrigger>
  </CodeBlockTabsList>

  <CodeBlockTab value="npm">
    ```bash
    npm install -g prisma
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm add -g prisma
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn global add prisma
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bun add --global prisma
    ```
  </CodeBlockTab>
</CodeBlockTabs>

Launching Studio [#launching-studio]

With a Prisma Project [#with-a-prisma-project]

If you have an existing Prisma project, navigate to your project directory and run:

<CodeBlockTabs defaultValue="npm" groupId="package-manager" persist>
  <CodeBlockTabsList>
    <CodeBlockTabsTrigger value="npm">
      npm
    </CodeBlockTabsTrigger>

    <CodeBlockTabsTrigger value="pnpm">
      pnpm
    </CodeBlockTabsTrigger>

    <CodeBlockTabsTrigger value="yarn">
      yarn
    </CodeBlockTabsTrigger>

    <CodeBlockTabsTrigger value="bun">
      bun
    </CodeBlockTabsTrigger>
  </CodeBlockTabsList>

  <CodeBlockTab value="npm">
    ```bash
    npx prisma studio
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm dlx prisma studio
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn dlx prisma studio
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bunx --bun prisma studio
    ```
  </CodeBlockTab>
</CodeBlockTabs>

This will start the Studio server and open it in your default browser at `http://localhost:5555`.

Without a Prisma Project [#without-a-prisma-project]

You can also use Studio with any database by providing a connection string:

<CodeBlockTabs defaultValue="npm" groupId="package-manager" persist>
  <CodeBlockTabsList>
    <CodeBlockTabsTrigger value="npm">
      npm
    </CodeBlockTabsTrigger>

    <CodeBlockTabsTrigger value="pnpm">
      pnpm
    </CodeBlockTabsTrigger>

    <CodeBlockTabsTrigger value="yarn">
      yarn
    </CodeBlockTabsTrigger>

    <CodeBlockTabsTrigger value="bun">
      bun
    </CodeBlockTabsTrigger>
  </CodeBlockTabsList>

  <CodeBlockTab value="npm">
    ```bash
    npx prisma studio --url="postgresql://user:password@localhost:5432/yourdb"
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm dlx prisma studio --url="postgresql://user:password@localhost:5432/yourdb"
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn dlx prisma studio --url="postgresql://user:password@localhost:5432/yourdb"
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bunx --bun prisma studio --url="postgresql://user:password@localhost:5432/yourdb"
    ```
  </CodeBlockTab>
</CodeBlockTabs>

Connecting to Your Database [#connecting-to-your-database]

1. **Using environment variables**:
   Create a `.env` file in your project root with your database URL:

   ```
   DATABASE_URL="postgresql://user:password@localhost:5432/yourdb"
   ```

   Then run: `npx prisma studio`

2. **Using command line**:
   ```bash
   npx prisma studio --url="your-database-connection-string"
   ```

Basic Usage [#basic-usage]

Browsing Data [#browsing-data]

* The left sidebar lists all your database tables
* Click on a table to view its data
* Use the search bar to quickly find tables or columns

Editing Data [#editing-data]

* **Edit cells**: Double-click any cell to edit its value
* **Add records**: Click the "+" button to add a new record
* **Delete records**: Select records using checkboxes and click the trash icon

Filtering and Sorting [#filtering-and-sorting]

* Click the filter icon to add filters
* Click on column headers to sort the table
* Use the search box to filter records by any field

Common Tasks [#common-tasks]

Viewing Table Relationships [#viewing-table-relationships]

* Related tables are shown as expandable rows
* Click the "+" icon to view related records

Exporting Data [#exporting-data]

* Use the export button to download data as CSV or JSON
* Select specific columns to include in the export

Next Steps [#next-steps]

* Learn how to [embed Studio in your application](/studio/integrations/embedding)
* Discover [VS Code integration](/studio/integrations/vscode-integration) features


