--------------------------------------------------------------------------------
title: "Observability Plus"
description: "Learn about using Observability Plus and its limits."
last_updated: "2026-04-03T23:47:24.529Z"
source: "https://vercel.com/docs/observability/observability-plus"
--------------------------------------------------------------------------------

# Observability Plus

> **🔒 Permissions Required**: Observability Plus

## Using Observability Plus

### Disabling Observability Plus

1. From your [dashboard](/dashboard), navigate to [the **Observability** section in the sidebar](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fobservability).
2. Click the more options button () at the top right of the page, then select **Configure Observability Plus**.
3. This takes you to the [**Observability Plus** section of your project's **Billing** settings](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fsettings/billing#observability)
   - Click the toggle button to disable it
   - Click the **Confirm** button in the **Turn off Observability Plus** dialog

## Pricing

Users on all plans can use Observability at no additional cost, with some [limitations](#limitations). Observability is available for all projects in the team.

Paid Pro and Enterprise teams can use **Observability Plus** for additional features, higher limits, and increased retention. Vercel bills you based on usage at a per-event rate. See the table below for pricing details:

| Resource | Base Fee | Usage-based pricing |
| --- | --- | --- |
| Observability Plus | Pro: $10/month Enterprise: none | $1.20 per 1 million events |


## Limitations

| Feature                               | Observability                                                                            | Observability Plus                                                                                                                  |
| ------------------------------------- | ---------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| Data Retention                        | Hobby: 12 hours  Pro: 1 day  Enterprise: 3 days                                | 30 days                                                                                                                             |
| Query                                 | No access                                                                                | Author queries in the Vercel dashboard and save queries to notebooks                                                                |
| Vercel Functions                      | No Latency (p75) data, no breakdown by path                                              | Latency data, sort by p75, breakdown by path and routes                                                                             |
| External APIs                         | No ability to sort by error rate or p75 duration, only request totals for each hostname  | Sorting and filtering by requests, p75 duration, and duration. Latency, Requests, API Endpoint and function calls for each hostname |
| Edge Requests                         | No breakdown by path                                                                     | Full request data                                                                                                                   |
| Fast Data Transfer                    | No breakdown by path                                                                     | Full request data                                                                                                                   |
| ISR (Incremental Static Regeneration) | No access to average duration or revalidation data. Limited function data for each route | Access to sorting and filtering by duration and revalidation. Full function data for each route                                     |
| Build Diagnostics                     | Hobby: 12 hours  Pro: 1 day  Enterprise: 3 days                                | Full access                                                                                                                         |
| In-function Concurrency               | Full access when enabled                                                                 | Full access when enabled                                                                                                            |
| Runtime logs                          | Hobby: 1 hour  Pro: 1 day  Enterprise: 3 days                                  | 30 days, max selection window of 14 consecutive days                                                                                |

## Prorating


