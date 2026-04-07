---
id: "vercel-0039"
title: "Vercel Plugin for AI Coding Agents"
description: "Install the Vercel plugin to give AI coding agents expert-level knowledge of the Vercel ecosystem, including skills, specialist agents, and automatic context injection."
category: "vercel-integrations"
subcategory: "agent-resources"
type: "integration"
source: "https://vercel.com/docs/agent-resources/vercel-plugin"
tags: ["plugin", "ai", "coding", "agents", "installation", "what-the-plugin-provides"]
related: ["0016-coding-agents.md", "0019-build-with-ai-agents-on-vercel.md", "0009-blackbox-ai.md"]
last_updated: "2026-04-03T23:47:14.205Z"
---

# Vercel Plugin for AI Coding Agents

The Vercel plugin turns any supported AI coding agent into a Vercel expert. It pre-loads agents with a relational knowledge graph of the entire Vercel ecosystem and automatically injects the right guidance at the right time based on what you're working on.

## Installation

Install the plugin with a single command:

```bash
npx plugins add vercel/vercel-plugin
```

The plugin activates automatically after installation. There are no additional setup steps or commands to learn.

## What the plugin provides

The plugin includes four main components that work together to enhance your AI coding agent:

| Component               | Description                                                                                                                                    |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| **Ecosystem graph**     | A relational knowledge graph covering every Vercel product, library, CLI, API, and service, with decision matrices and cross-product workflows |
| **38 skills**           | Deep-dive guidance for specific Vercel products, injected automatically when relevant                                                          |
| **3 specialist agents** | Purpose-built agents for deployment, performance optimization, and AI architecture                                                             |
| **5 slash commands**    | Quick actions for deploying, managing environment variables, bootstrapping projects, and more                                                  |

## Supported tools

| Tool                                                          | Status      |
| ------------------------------------------------------------- | ----------- |
| [Claude Code](https://docs.anthropic.com/en/docs/claude-code) | Supported   |
| [Cursor](https://www.cursor.com)                              | Supported   |
| [OpenAI Codex](https://openai.com/index/codex/)               | Coming soon |

## Prerequisites

- One of the supported AI coding tools listed above
- Node.js 18+

## How it works

After installing, the plugin detects what you're working on from your tool calls, file paths, and project configuration, then injects the right expertise at the right time. You use your AI agent as you normally would and the plugin handles the rest.

### Automatic context injection

The plugin uses lifecycle hooks that run during your session:

- **Session start context injection**: Injects the ecosystem graph into every session so the agent has baseline knowledge of the full Vercel platform
- **Session start repo profiler**: Scans config files and dependencies to prepare skill matching for a faster first tool call
- **Pre-tool-use skill injection**: When the agent reads, edits, or writes files, the plugin matches file paths and commands against skill patterns and injects relevant guidance
- **Pre-write/edit validation**: Before the agent writes or edits a file, the plugin catches deprecated patterns like sunset packages, old API names, and renamed files

### Skill injection

Skills are the core of the plugin's expertise. Each skill covers a specific Vercel product or feature in depth. The plugin injects up to three skills per tool call, prioritized by relevance, and deduplicates across the session so the same skill is never injected twice.

For example:

- Editing a `next.config.ts` file triggers the **nextjs** skill
- Running `vercel deploy` triggers the **deployments-cicd** skill
- Working with `useChat` or `streamText` triggers the **ai-sdk** skill

## Available skills

The plugin includes 38 skills covering the full Vercel ecosystem:

| Skill                   | Covers                                                                                                  |
| ----------------------- | ------------------------------------------------------------------------------------------------------- |
| `agent-browser`         | Browser automation CLI: dev server verification, page interaction, screenshots, form filling            |
| `agent-browser-verify`  | Automated dev-server verification: visual gut-check on page load, console errors, key UI elements       |
| `ai-elements`           | Pre-built React components for AI interfaces: chat UIs, tool call rendering, streaming responses        |
| `ai-gateway`            | Unified model API, provider routing, failover, cost tracking, 100+ models                               |
| `ai-sdk`                | AI SDK v6: text/object generation, streaming, tool calling, agents, MCP, providers, embeddings          |
| `auth`                  | Authentication integrations: Clerk, Descope, Auth0 setup for Next.js with Marketplace provisioning      |
| `bootstrap`             | Project bootstrapping orchestrator: linking, env provisioning, db setup, first-run commands             |
| `chat-sdk`              | Multi-platform chat bots: Slack, Telegram, Teams, Discord, Google Chat, GitHub, Linear                  |
| `cron-jobs`             | Vercel Cron Jobs configuration, scheduling, and best practices                                          |
| `deployments-cicd`      | Deployment and CI/CD — deploy, promote, rollback, `--prebuilt`, CI workflow files                       |
| `env-vars`              | Environment variable management: `.env` files, `vercel env` commands, OIDC tokens                       |
| `investigation-mode`    | Orchestrated debugging: runtime logs, workflow status, browser verify, deploy/env triage                |
| `json-render`           | AI chat response rendering — UIMessage parts, tool call displays, streaming states                      |
| `marketplace`           | Integration discovery, installation, auto-provisioned env vars, unified billing                         |
| `next-cache-components` | Next.js 16 Cache Components: PPR, `use cache`, cacheLife, cacheTag, updateTag                           |
| `next-forge`            | Production SaaS monorepo starter: Turborepo, Clerk, Prisma/Neon, Stripe, shadcn/ui                      |
| `next-upgrade`          | Next.js version upgrades: codemods, migration guides, dependency updates                                |
| `nextjs`                | App Router, Server Components, Server Actions, Cache Components, routing, rendering strategies          |
| `observability`         | Web Analytics, Speed Insights, runtime logs, Log Drains, OpenTelemetry, monitoring                      |
| `react-best-practices`  | React/Next.js performance optimization: 64 rules across 8 categories                                    |
| `routing-middleware`    | Request interception before cache, rewrites, redirects, personalization with Edge/Node.js/Bun runtimes  |
| `runtime-cache`         | Ephemeral per-region key-value cache, tag-based invalidation, shared across Functions/Middleware/Builds |
| `shadcn`                | shadcn/ui: CLI, component installation, custom registries, theming, Tailwind CSS integration            |
| `sign-in-with-vercel`   | OAuth 2.0/OIDC identity provider, user authentication via Vercel accounts                               |
| `turbopack`             | Next.js bundler, HMR, configuration, Turbopack vs Webpack                                               |
| `turborepo`             | Monorepo orchestration, caching, remote caching, `--affected`, pruned subsets                           |
| `v0-dev`                | AI code generation, agentic intelligence, GitHub integration                                            |
| `vercel-agent`          | AI-powered code review, incident investigation, SDK installation, PR analysis                           |
| `vercel-api`            | Vercel MCP Server and REST API: projects, deployments, env vars, domains, logs                          |
| `vercel-cli`            | All CLI commands: deploy, env, dev, domains, cache management, MCP integration, marketplace             |
| `vercel-flags`          | Feature flags, Flags Explorer, gradual rollouts, A/B testing, provider adapters                         |
| `vercel-functions`      | Serverless, Edge, Fluid Compute, streaming, Cron Jobs, configuration                                    |
| `vercel-queues`         | Durable event streaming, topics, consumer groups, retries, delayed delivery                             |
| `vercel-sandbox`        | Ephemeral Firecracker microVMs for running untrusted/AI-generated code safely                           |
| `vercel-services`       | Multiple services in one project: monorepo backends + frontends on the same domain                      |
| `vercel-storage`        | Blob, Edge Config, Neon Postgres, Upstash Redis, migration from sunset packages                         |
| `verification`          | Full-story verification: infers user story, verifies end-to-end browser → API → data → response         |
| `workflow`              | Workflow SDK: durable execution, DurableAgent, steps, Worlds, pause/resume                              |

## Specialist agents

The plugin includes three specialist agents that you can invoke for focused tasks:

| Agent                   | Expertise                                                                       |
| ----------------------- | ------------------------------------------------------------------------------- |
| `deployment-expert`     | CI/CD pipelines, deploy strategies, troubleshooting, environment variables      |
| `performance-optimizer` | Core Web Vitals, rendering strategies, caching, asset optimization              |
| `ai-architect`          | AI application design, model selection, streaming architecture, MCP integration |

## Slash commands

Invoke commands directly within your AI coding agent:

| Command                      | Purpose                                                           |
| ---------------------------- | ----------------------------------------------------------------- |
| `/vercel-plugin:bootstrap`   | Bootstrap a project with linking, env provisioning, and db setup  |
| `/vercel-plugin:deploy`      | Deploy to Vercel (preview or production)                          |
| `/vercel-plugin:env`         | Manage environment variables (list, pull, add, remove, diff)      |
| `/vercel-plugin:status`      | View project status, recent deployments, and environment overview |
| `/vercel-plugin:marketplace` | Discover and install Vercel Marketplace integrations              |

To deploy to production, pass `prod` as an argument: `/vercel-plugin:deploy prod`

## Debugging

If the plugin isn't injecting skills when expected, enable debug logging by setting the `VERCEL_PLUGIN_LOG_LEVEL` environment variable:

```bash
export VERCEL_PLUGIN_LOG_LEVEL=debug
```

Available log levels:

| Level     | Description                                 |
| --------- | ------------------------------------------- |
| `off`     | No logging (default)                        |
| `summary` | High-level injection summaries              |
| `debug`   | Detailed matching and dedup information     |
| `trace`   | Full pipeline traces with timing breakdowns |

You can also use the built-in doctor command to diagnose issues:

```bash
npx vercel-plugin doctor
```

This validates manifest parity, checks hook timeouts, and verifies dedup health.

## Reporting issues

If a skill gives incorrect advice or injection doesn't fire when expected, file an issue on [GitHub](https://github.com/vercel/vercel-plugin/issues). Include:

- What you were building
- What the plugin injected (or didn't). Enable debug logs with `VERCEL_PLUGIN_LOG_LEVEL=debug`
- What was wrong about it


