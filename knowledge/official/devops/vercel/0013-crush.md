---
id: "vercel-0013"
title: "Crush"
description: "Use Crush with the AI Gateway."
category: "vercel-integrations"
subcategory: "integrations"
type: "integration"
source: "https://vercel.com/docs/agent-resources/coding-agents/crush"
tags: ["coding-agent", "terminal", "ai-gateway", "mcp-servers", "lsp"]
related: ["0016-coding-agents.md", "0015-opencode.md", "0092-ai-gateway.md"]
last_updated: "2026-04-03T23:47:13.747Z"
---

# Crush

[Crush](https://github.com/charmbracelet/crush) is a terminal-based AI coding assistant by Charmbracelet. It supports multiple LLM providers, LSP integration, MCP servers, and session-based context management. You can configure it to use AI Gateway for unified model access and spend monitoring.

## Configuring Crush

- ### Create an API Key
  Go to the [**AI Gateway**](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fai-gateway\&title=Go+to+AI+Gateway) section in the Vercel dashboard sidebar and click **API Keys** to create a new API Key.

- ### Install Crush
  Choose your preferred installation method:
  #### Homebrew
  ```bash filename="Terminal"
  brew install charmbracelet/tap/crush
  ```
  #### npm
  ```bash filename="Terminal"
  npm install -g @charmland/crush
  ```
  #### Go
  ```bash filename="Terminal"
  go install github.com/charmbracelet/crush@latest
  ```
  See the [Crush installation guide](https://github.com/charmbracelet/crush#installation) for additional installation options including Windows, Debian/Ubuntu, and Fedora/RHEL.

- ### Configure AI Gateway
  Start Crush:
  ```bash filename="Terminal"
  crush
  ```
  When prompted:
  1. **Select Provider**: Choose **Vercel AI Gateway**
  2. **Select Model**: Pick from AI Gateway's model library
  3. **Enter API Key**: Paste your AI Gateway API Key when prompted
  Crush saves your API Key to `~/.local/share/crush/crush.json`, so you only need to enter it once.

  Your requests will now be routed through AI Gateway. You can verify this by checking your [AI Gateway Overview](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fai-gateway\&title=Go+to+AI+Gateway) in the Vercel dashboard.

- ### (Optional) Monitor usage and spend
  View your usage, spend, and request activity in the [**AI Gateway**](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fai-gateway\&title=Go+to+AI+Gateway) section in the Vercel dashboard sidebar. See the [observability documentation](/docs/ai-gateway/capabilities/observability) for more details.


