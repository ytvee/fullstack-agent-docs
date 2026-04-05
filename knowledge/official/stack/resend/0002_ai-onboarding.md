# AI Onboarding

Source: https://resend.com/docs/ai-onboarding

Everything you need to onboard your AI agent to Resend.

If you're developing with AI, Resend offers several resources to improve your experience.

* [Resend MCP Server](#resend-mcp-server)
* [Resend CLI](#resend-cli)
* [Resend Docs for Agents](#resend-docs-for-agents)
* [Email Skills for Agents](#email-skills-for-agents)
* [Quick Start Guides](#quick-start-guides)
* [OpenClaw Guide](#openclaw-guide)
* [Chat SDK](#chat-sdk)
* [AI Builder Integrations](#ai-builder-integrations)

## Prerequisite: Create an API Key

Currently, we require a human to create a Resend account. Once you have an account, you'll need to [create an API key](https://resend.com/api-keys). With an API key, your agent can perform many other tasks.

<Info>
  To send or receive with Resend, you'll need to [verify a domain](https://resend.com/domains). While an agent can [create a domain](/api-reference/domains/create-domain), the API returns DNS records you will need to add in your DNS provider before [verifying your DNS records](/api-reference/domains/verify-domain). You may find it easier to verify your domain in the dashboard.
</Info>

## Resend MCP Server

MCP is an open protocol that standardizes how applications provide context to LLMs. Among other benefits, it provides LLMs tools to act on your behalf. Our [MCP server](https://github.com/resend/resend-mcp) is open-source and covers our full API surface area.

The Resend MCP server is available on NPM and can be added to any supported MCP client. For example:

```json
{
  "mcpServers": {
    "resend": {
      "command": "npx",
      "args": ["-y", "resend-mcp"],
      "env": {
        "RESEND_API_KEY": "re_xxxxxxxxx"
      }
    }
  }
}
```

<Card title="MCP Server" icon="microchip-ai" href="/mcp-server">
View installation instructions for Cursor, Codex, Claude Desktop, Windsurf,
and more.
</Card>

## Resend CLI

The Resend CLI lets you send emails, manage your account, and develop locally — from the terminal. It's built for humans, AI agents, and CI/CD pipelines.

```bash
