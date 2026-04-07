---
id: "vercel-0026"
title: "Vercel LMNT Integration"
description: "Learn how to add LMNT connectable account integration with Vercel."
category: "vercel-integrations"
subcategory: "agent-resources"
type: "integration"
source: "https://vercel.com/docs/agent-resources/integrations-for-models/lmnt"
tags: ["lmnt", "integrations-for-models", "use-cases", "getting-started", "prerequisites", "more-resources"]
related: ["0029-vercel-perplexity-integration.md", "0030-vercel-pinecone-integration.md", "0031-vercel-replicate-integration.md"]
last_updated: "2026-04-03T23:47:13.980Z"
---

# Vercel LMNT Integration

&#x20;provides data processing and
predictive analytics models, known for their precision and efficiency.
Integrating LMNT with Vercel enables your applications to offer accurate
insights and forecasts, particularly useful in finance and healthcare sectors.

## Use cases

You can use the Vercel and LMNT integration to power a variety of AI applications, including:

- **High quality text-to-speech**: Use LMNT to generate realistic speech that powers chatbots, AI-agents, games, and other digital media
- **Studio quality custom voices**: Use LMNT to clone voices that will faithfully reproduce the emotional richness and realism of actual speech
- **Reliably low latency, full duplex streaming**: Use LMNT to enable superior performance for conversational experiences, with consistently low latency and unmatched reliability

## Getting started

The Vercel  integration can be accessed through the **AI** tab on your [Vercel dashboard](/dashboard).

### Prerequisites

To follow this guide, you'll need the following:

- An existing [Vercel project](/docs/projects/overview#creating-a-project)
- The latest version of [Vercel CLI](/docs/cli#installing-vercel-cli)
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

### Add the provider to your project

#### Using the dashboard

1. Navigate to the **AI** tab in your [Vercel dashboard](/dashboard)
2. Select  from the list of providers, and press **Add**
3. Review the provider information, and press **Add Provider**
4. You can now select which projects the provider will have access to. You can choose from **All Projects** or **Specific Projects**
   - If you select **Specific Projects**, you'll be prompted to select the projects you want to connect to the provider. The list will display projects associated with your scoped team
   - Multiple projects can be selected during this step
5. Select the **Connect to Project** button
6. You'll be redirected to the provider's website to complete the connection process
7. Once the connection is complete, you'll be redirected back to the Vercel dashboard, and the provider integration dashboard page. From here you can manage your provider settings, view usage, and more
8. Pull the environment variables into your project using [Vercel CLI](/docs/cli/env)
   ```bash filename="terminal"
   vercel env pull
   ```
9. Install the providers package
10. Connect your project using the code below:

## More resources


