---
id: "vercel-0003"
title: "Installation"
description: "Let AI automatically install Web Analytics and Speed Insights in your app"
category: "vercel-integrations"
subcategory: "integrations"
type: "guide"
source: "https://vercel.com/docs/agent/installation"
tags: ["web-analytics", "speed-insights", "ai-agent", "automated-setup", "pull-request"]
related: ["0005-vercel-agent.md", "0124-vercel-web-analytics.md", "0126-getting-started-with-vercel-web-analytics.md"]
last_updated: "2026-04-03T23:47:13.553Z"
---

# Installation

> **🔒 Permissions Required**: Agent Installation

Vercel Agent Installation helps add [Web Analytics](/docs/analytics) and [Speed Insights](/docs/speed-insights) to your project with AI. After you start the installation, Vercel Agent automatically:

1. Analyzes your project configuration and connected repository
2. Installs the relevant package
3. Writes the code to integrate the package
4. Creates a pull request with all changes

## Getting started

> **💡 Note:** Agent Installation currently only supports projects with a GitHub repository connected.

To have Vercel Agent install **Web Analytics** or **Speed Insights** to your project:

1. Go to your [Vercel dashboard](https://vercel.com/d?to=%2F%5Bteam%5D%2F%5Bproject%5D\&title=Open+Project) and select your GitHub-connected project.
2. Navigate to the **Analytics** or **Speed Insights** tab.
3. If needed, click **Enable** to turn on the feature.
4. Click the **Implement** button to start the agent.
5. Review the pull request and merge when ready.

Once the pull request is merged and deployed, tracking starts automatically. If you need to regenerate the pull request, click **Run Again**.

## Pricing

Vercel Agent Installation is free for all teams. There are no additional costs to use the agent itself.

Billing is based on usage of the underlying features. For example, after the agent installs Web Analytics, you will be charged for [Web Analytics usage](/docs/analytics/limits-and-pricing). The same applies to [Speed Insights usage](/docs/speed-insights/limits-and-pricing).


