# dev (/docs/cli/dev)



The `prisma dev` command starts a [local Prisma Postgres](/postgres/database/local-development) database that you can run Prisma ORM commands against. It's useful for development and testing and allows easy migration to [Prisma Postgres](/postgres) in production.

Usage [#usage]

```bash
prisma dev [options]
```

Options [#options]

| Option             | Description                                               | Default   |
| ------------------ | --------------------------------------------------------- | --------- |
| `-n`, `--name`     | Name of the server (helps isolate state between projects) | `default` |
| `-p`, `--port`     | Main port number the Prisma Dev server will listen on     | `51213`   |
| `-P`, `--db-port`  | Port number the database server will listen on            | `51214`   |
| `--shadow-db-port` | Port number the shadow database server will listen on     | `51215`   |
| `-d`, `--detach`   | Run the server in the background                          | `false`   |
| `--debug`          | Enable debug logging                                      | `false`   |

Subcommands [#subcommands]

| Command                              | Description                       |
| ------------------------------------ | --------------------------------- |
| [`prisma dev ls`](/cli/dev/ls)       | List available servers            |
| [`prisma dev rm`](/cli/dev/rm)       | Remove servers                    |
| [`prisma dev start`](/cli/dev/start) | Start one or more stopped servers |
| [`prisma dev stop`](/cli/dev/stop)   | Stop servers                      |

Examples [#examples]

Start a local Prisma Postgres server [#start-a-local-prisma-postgres-server]

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
    npx prisma dev
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm dlx prisma dev
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn dlx prisma dev
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bunx --bun prisma dev
    ```
  </CodeBlockTab>
</CodeBlockTabs>

Output:

```text
✔  Great Success!

   Your  prisma dev  server default is ready and listening on ports 63567-63569.

╭──────────────────────────────────╮
│[q]uit  [h]ttp url  [t]cp urls    │
╰──────────────────────────────────╯
```

Start with a specific name [#start-with-a-specific-name]

Create a named instance for project isolation:

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
    npx prisma dev --name="mydbname"
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm dlx prisma dev --name="mydbname"
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn dlx prisma dev --name="mydbname"
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bunx --bun prisma dev --name="mydbname"
    ```
  </CodeBlockTab>
</CodeBlockTabs>

Run in detached mode [#run-in-detached-mode]

Run the server in the background:

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
    npx prisma dev --detach
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm dlx prisma dev --detach
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn dlx prisma dev --detach
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bunx --bun prisma dev --detach
    ```
  </CodeBlockTab>
</CodeBlockTabs>

This frees up your terminal. Use `prisma dev ls` to see running servers and `prisma dev stop` to stop them.

Specify custom ports [#specify-custom-ports]

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
    npx prisma dev --port 5000 --db-port 5001 --shadow-db-port 5002
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm dlx prisma dev --port 5000 --db-port 5001 --shadow-db-port 5002
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn dlx prisma dev --port 5000 --db-port 5001 --shadow-db-port 5002
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bunx --bun prisma dev --port 5000 --db-port 5001 --shadow-db-port 5002
    ```
  </CodeBlockTab>
</CodeBlockTabs>


