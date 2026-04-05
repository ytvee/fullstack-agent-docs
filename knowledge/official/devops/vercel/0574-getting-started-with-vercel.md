--------------------------------------------------------------------------------
title: "Getting started with Vercel"
description: "Install the Vercel CLI, add the Vercel Plugin or agent skills, and deploy your first project."
last_updated: "2026-04-03T23:47:22.295Z"
source: "https://vercel.com/docs/getting-started-with-vercel"
--------------------------------------------------------------------------------

# Getting started with Vercel

Deploy your app on Vercel in three steps: install the CLI, add agent support if you use an AI coding agent, and deploy.

## Prerequisites

- A [Vercel account](/signup)
- [Node.js 18+](https://nodejs.org/)

## Install the Vercel CLI

Every Vercel workflow starts with the CLI. Install it whether or not you use an AI coding agent. Agents that can run terminal commands use the CLI to deploy, pull environment variables, and manage projects.

- ### Install Vercel CLI
  <CodeBlock>
    <Code tab="pnpm">
      ```bash
      pnpm i vercel
      ```
    </Code>
    <Code tab="yarn">
      ```bash
      yarn i vercel
      ```
    </Code>
    <Code tab="npm">
      ```bash
      npm i vercel
      ```
    </Code>
    <Code tab="bun">
      ```bash
      bun i vercel
      ```
    </Code>
  </CodeBlock>

- ### Log in to Vercel
  ```bash
  vercel login
  ```
  Follow the prompts to authenticate with your Vercel account.

- ### Deploy your project
  Navigate to your project directory and run:
  ```bash
  vercel
  ```
  The CLI detects your framework, builds your project, and deploys it. To deploy to production:
  ```bash
  vercel --prod
  ```

See the [CLI documentation](/docs/cli) for the full command reference.

## Install the Vercel Plugin

If you use [Claude Code](https://docs.anthropic.com/en/docs/claude-code) or [Cursor](https://www.cursor.com), install the [Vercel Plugin](https://github.com/vercel/vercel-plugin). It gives your agent deployment skills, framework best practices, and slash commands like `/vercel-plugin:deploy prod` and `/vercel-plugin:env`.

```bash
npx plugins add vercel/vercel-plugin
```

The plugin activates automatically. No configuration needed.

See the [Vercel Plugin documentation](/docs/agent-resources/vercel-plugin) for the full list of skills, specialist agents, and slash commands.

## Install Vercel Skills for other agents

If you use Cline, Windsurf, GitHub Copilot, or any of the 18+ agents supported by [Skills.sh](https://skills.sh), install Vercel Skills instead. Skills give your agent the same deployment and framework expertise in a format compatible with your tool.

```bash
npx skills add vercel-labs/agent-skills
```

To install a specific skill:

```bash
npx skills add vercel-labs/agent-skills --skill vercel-react-best-practices
```

See [Agent Skills](/docs/agent-resources/skills) for the full list.

## Deploy from the dashboard

You can also deploy without the CLI. Go to the [New Project](/new) page, connect your [GitHub](/docs/git/vercel-for-github), [GitLab](/docs/git/vercel-for-gitlab), or [Bitbucket](/docs/git/vercel-for-bitbucket) account, select a repo, and click **Deploy**. Every push to your connected branch triggers a new deployment automatically.

## Next steps

- [Fundamental concepts](/docs/fundamentals) – How requests, builds, and compute work on Vercel
- [Set up environment variables](/docs/environment-variables)
- [Add a custom domain](/docs/domains/set-up-custom-domain)
- [Explore supported frameworks](/docs/frameworks)
- [Vercel Functions](/docs/functions) – Run server-side code on demand
- [Connect the Vercel MCP server](/docs/agent-resources/vercel-mcp) – Give AI agents direct access to your Vercel account
- [Agent resources](/docs/agent-resources) – Documentation access, skills, and CLI workflows for AI agents


