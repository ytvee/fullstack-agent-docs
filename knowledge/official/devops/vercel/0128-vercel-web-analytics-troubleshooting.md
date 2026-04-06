---
id: "vercel-0128"
title: "Vercel Web Analytics Troubleshooting"
description: "Learn how to troubleshoot common issues with Vercel Web Analytics."
category: "vercel-analytics"
subcategory: "analytics"
type: "guide"
source: "https://vercel.com/docs/analytics/troubleshooting"
tags: ["web-analytics", "web", "troubleshooting", "setup", "how-to"]
related: ["0127-redacting-sensitive-data-from-web-analytics-events.md", "0123-advanced-web-analytics-config-with-vercel-analytics.md", "0126-getting-started-with-vercel-web-analytics.md"]
last_updated: "2026-04-03T23:47:15.644Z"
---

# Vercel Web Analytics Troubleshooting

## No data visible in Web Analytics dashboard

**Issue**: If you are experiencing a situation where data is not visible in the analytics dashboard or a 404 error occurs while loading `script.js`, it could be due to deploying the tracking code before enabling Web Analytics.

**How to fix**:

1. Make sure that you have [enabled Analytics](/docs/analytics/quickstart#enable-web-analytics-in-vercel) in the dashboard.
2. Re-deploy your app to Vercel.
3. Promote your latest deployment to production. To do so, visit the project in your [dashboard](/dashboard), and open [**Deployments**](https://vercel.com/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Fdeployments\&title=Go+to+Deployments) in the sidebar. From there, select the three dots to the right of the most recent deployment and select **Promote to Production**.

## Web Analytics is not working with a proxy (e.g., Cloudflare)

**Issue**: Web Analytics may not function when using a proxy, such as Cloudflare.

**How to fix**:

1. Check your proxy configuration to make sure that all desired pages are correctly proxied to the deployment.
2. Additionally, forward all requests to `/_vercel/insights/*` and `/<unique-path>` to the deployments so Web Analytics works through the proxy.

## Routes are not visible in Web Analytics dashboard

**Issue**: Not all data is visible in the Web Analytics dashboard

**How to fix**:

1. Verify that you are using the latest version of the `@vercel/analytics` package.
2. Make sure you are using the correct import statement.

```tsx
import { Analytics } from '@vercel/analytics/next'; // Next.js import
```

```tsx
import { Analytics } from '@vercel/analytics/react'; // Generic React import
```


