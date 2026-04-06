---
id: "vercel-0002"
title: "Using the Activity Log"
description: "Learn how to use the Activity Log, which provides a list of all events on a team, chronologically organized since its creation."
category: "vercel-observability"
subcategory: "observability"
type: "guide"
source: "https://vercel.com/docs/activity-log"
tags: ["activity-log", "audit-trail", "team-events", "monitoring"]
related: ["0130-audit-logs.md", "0163-vercel-activity.md", "0001-account-management.md"]
last_updated: "2026-04-03T23:47:13.538Z"
---

# Using the Activity Log

> **🔒 Permissions Required**: Activity Log

The [Activity Log](/dashboard/activity) provides a list of all events on a [team](/docs/accounts#teams), chronologically organized since its creation. These events include:

- User(s) involved with the event
- Type of event performed
- Type of account
- Time of the event (hover over the time to reveal the exact timestamp)

> **💡 Note:** Vercel does not emit any logs to third-party services. The Activity Log is
> only available to the account owner and team members.

![Image](`/front/docs/observability/activity-logs-light.png`)

*Example events list on the Activity page.*

## When to use the Activity log

Common use cases for viewing the Activity log include:

- If a user was removed or deleted by mistake, use the list to find when the event happened and who requested it
- A domain can be disconnected from your deployment. Use the list to see if a domain related event was recently triggered
- Check if a specific user was removed from a team

## CLI access

You can also view and filter activity events from the command line. See the [`vercel activity`](/docs/cli/activity) CLI reference for available options.

## Events logged

The table below shows a list of events logged on the Activity page.


