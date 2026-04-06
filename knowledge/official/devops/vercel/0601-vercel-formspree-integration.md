---
id: "vercel-0601"
title: "Vercel Formspree Integration"
description: "Learn how to integrate Formspree with Vercel. Follow our tutorial to set up Formspree and manage form submissions on your static website without needing a server. "
category: "vercel-integrations"
subcategory: "integrations"
type: "integration"
source: "https://vercel.com/docs/integrations/cms/formspree"
tags: ["formspree", "cms", "getting-started", "integration"]
related: ["0602-vercel-makeswift-integration.md", "0598-vercel-buttercms-integration.md", "0600-vercel-datocms-integration.md"]
last_updated: "2026-04-03T23:47:23.343Z"
---

# Vercel Formspree Integration

Formspree is a form backend platform that handles form submissions on static websites. It allows developers to collect and manage form data without needing a server.

## Getting started

To get started with Formspree on Vercel, follow the steps below to install the integration:

- ### Install the Vercel CLI
  To pull in environment variables from  to your Vercel project, you need to install the [Vercel CLI](/docs/cli). Run the following command in your terminal:
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

- ### Install your CMS integration
  Navigate to the  and follow the steps to install the integration.

- ### Pull in environment variables
  Once you've installed the  integration, you can pull in environment variables from  to your Vercel project. In your terminal, run:
  ```bash
  vercel env pull
  ```

See your installed CMSs documentation for next steps on how to use the integration.


