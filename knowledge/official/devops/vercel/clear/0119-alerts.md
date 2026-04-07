---
id: "vercel-0119"
title: "Alerts"
description: "Get notified when something"
category: "vercel-observability"
subcategory: "alerts"
type: "concept"
source: "https://vercel.com/docs/alerts"
tags: ["alert-types", "usage-anomaly-metrics", "investigate-alerts-with-ai"]
related: ["0381-speed-insights-drains-reference.md", "0657-observability-insights.md", "0002-using-the-activity-log.md"]
last_updated: "2026-04-03T23:47:15.488Z"
---

# Alerts

> **Permissions Required**: Alerts

Alerts let you know when something's wrong with your Vercel projects, like a spike in failed function invocations or unusual usage patterns. You can get these alerts by email, through Slack, or set up a webhook so you can respond to issues.

By default, you'll be notified about:

- **Usage anomaly**: When your project's usage exceeds abnormal levels.
- **Error anomaly**: When your project's error rate of function invocations (those with a status code of 5xx) exceeds abnormal levels.

## Alert types

| Alert Type        | Triggered when                                                                                                                             | Grouping |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | -------- |
| **Error Anomaly** | Fires when your 5-minute error rate (5xx) is more than 4 standard deviations above your 24-hour average and exceeds the minimum threshold. | Route    |
| **Usage Anomaly** | Fires when your 5-minute usage is more than 4 standard deviations above your 24-hour average and exceeds the minimum threshold.            | Metric   |

### Usage anomaly metrics

Usage anomaly alerts support these metrics:

- [Function CPU duration](/docs/functions/usage-and-pricing#active-cpu)
- [Function duration](/docs/functions/usage-and-pricing)
- [Fast Data Transfer](/docs/manage-cdn-usage#fast-data-transfer)
- [Edge requests](/docs/manage-cdn-usage#cdn-requests)
- [Function invocations](/docs/functions/usage-and-pricing)

## Investigate alerts with AI

When you get an alert, [Agent Investigation](/docs/agent/investigation) can run on its own to help you debug. Instead of digging through logs and metrics yourself, AI analyzes what's happening and displays highlights of the anomaly in your dashboard.

When you view an alert in the dashboard, you can click **Enable Auto Run** to trigger an investigation. This takes you to the **Agents** section in the sidebar, where you can set up investigations to run on new alerts. You can also click **Rerun** to start a new investigation.

Learn more in the [Agent Investigation docs](/docs/agent/investigation).

## Error anomaly reference table

Error anomaly detection compares current error rates against a 24-hour baseline using statistical confidence intervals. These are the minimum error counts needed to trigger alerts at different traffic volumes:

| Traffic Volume                     | Avg Error Rate | Minimum Errors | Notes                                    |
| ---------------------------------- | -------------- | -------------- | ---------------------------------------- |
| Sparse (1 req/hour)                | 2%             | 51 errors      | or 5 with 2 consecutive 5-min intervals  |
| Low (10 req/min)                   | 1%             | 51 errors      | or 6 with 2 consecutive 5-min intervals  |
| Medium (100 req/min)               | 0.5%           | 51 errors      | or 18 with 2 consecutive 5-min intervals |
| High (1k req/min)                  | 0.5%           | 106 errors     |                                          |
| High (10k req/min)                 | 0.2%           | 361 errors     |                                          |
| Zero Error Baseline (1000 req/min) | 0%             | 51 errors      | or 5 with 2 consecutive 5-min intervals  |
| High Error Rate (100 req/min)      | 5%             | 106 errors     |                                          |

