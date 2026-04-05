--------------------------------------------------------------------------------
title: "Understanding Vercel"
description: "Learn all about Vercel"
last_updated: "2026-04-03T23:47:24.848Z"
source: "https://vercel.com/docs/plans/pro-plan/trials"
--------------------------------------------------------------------------------

# Understanding Vercel

Vercel offers three plan tiers: **Hobby**, **Pro**, and **Enterprise**.

The Pro trial offers an opportunity to explore [Pro features](/docs/plans/pro-plan) for free during the trial period. There are some [limitations](/docs/plans/pro-plan/trials#trial-limitations).

## Starting a trial

> **💡 Note:** There is a limit of one Pro plan trial per user account.

1. Select the team switcher from the dashboard. From the bottom of the list select **Create Team**. Alternatively, click this button:
2. Name your team
3. Select the **Pro Trial** option from the dialog. If this option does not appear, it means you have already reached your limit of one trial:

![Image](https://vercel.com/docs-assets/static/docs/concepts/teams/new-team-light.png)

## Trial Limitations

The trial plan includes a $20 credit and follows the same [general limits](/docs/limits#general-limits) as a regular plan but with specified usage restrictions. See how these compare to the [non-trial usage limits](/docs/limits#included-usage):

|                                                                                            | Pro Trial Limits     |
| ------------------------------------------------------------------------------------------ | -------------------- |
| Owner Members                                                                              | 1                    |
| Team Members (total, including Owners)                                                     | 10                   |
| Projects                                                                                   | 200                  |
| [Active CPU](/docs/functions/usage-and-pricing)                                            | 8 CPU-hrs            |
| [Provisioned Memory](/docs/functions/usage-and-pricing)                                    | 720 GB-hrs           |
| [Function Invocations](/docs/functions/usage-and-pricing)                                  | 1,000,000/month      |
| Build Execution                                                                            | Max. 200 Hrs         |
| [Image transformations](/docs/image-optimization/limits-and-pricing#image-transformations) | Max. 5K/month        |
| [Image cache reads](/docs/image-optimization/limits-and-pricing#image-cache-reads)         | Max. 300K/month      |
| [Image cache writes](/docs/image-optimization/limits-and-pricing#image-cache-writes)       | Max. 100K/month      |
| [Monitoring](/docs/observability/monitoring)                                               | Max. 125,000 metrics |
| Domains per Project                                                                        | 50                   |

To monitor the current usage of your Team's projects, see the [Usage](/docs/limits/usage) guide.

The following Pro features are **not available** on the trial:

- [Log drains](/docs/log-drains)
- [Account webhooks](/docs/webhooks#account-webhooks)
- Certain models (GPT-5 and Claude) on [Vercel AI Playground](https://sdk.vercel.ai/)

Once your usage of [Active CPU](/docs/fu