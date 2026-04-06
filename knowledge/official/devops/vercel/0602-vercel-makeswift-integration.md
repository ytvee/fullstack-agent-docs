---
id: "vercel-0602"
title: "Vercel Makeswift Integration"
description: "Learn how to integrate Makeswift with Vercel. Makeswift is a no-code website builder designed for creating and managing React websites. Follow our tutorial to set up Makeswift and deploy your website on Vercel."
category: "vercel-integrations"
subcategory: "integrations"
type: "integration"
source: "https://vercel.com/docs/integrations/cms/makeswift"
tags: ["makeswift", "cms", "getting-started", "integration"]
related: ["0601-vercel-formspree-integration.md", "0598-vercel-buttercms-integration.md", "0600-vercel-datocms-integration.md"]
last_updated: "2026-04-03T23:47:23.348Z"
---

# Vercel Makeswift Integration

Makeswift is a no-code website builder designed for creating and managing React websites. It offers a drag-and-drop interface that allows users to design and build responsive web pages without writing code.

## Getting started

To get started with the Makeswift on Vercel deploy the template below:

Or, follow the steps below to install the integration:

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


