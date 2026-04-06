---
id: "vercel-0367"
title: "Assigning a domain to a Git branch"
description: "Learn how to assign a domain to a different Git branch with this guide."
category: "vercel-domains"
subcategory: "domains"
type: "guide"
source: "https://vercel.com/docs/domains/working-with-domains/assign-domain-to-a-git-branch"
tags: ["assigning", "domain", "git", "branch", "working-with-domains", "setup"]
related: ["0366-assigning-a-custom-domain-to-an-environment.md", "0371-removing-a-domain-from-a-project.md", "0372-managing-domain-renewals-and-redemptions.md"]
last_updated: "2026-04-03T23:47:19.429Z"
---

# Assigning a domain to a Git branch

Every commit pushed to the [Production Branch](/docs/git#production-branch) of your [connected Git repository](/docs/git) will be assigned the domains configured in your project.

To automatically assign a domain to a different branch:

1. From the [dashboard](/dashboard), pick the project to which you would like to assign your domain and open **Settings** in the sidebar.
2. Click on [**Domains**](https://vercel.com/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Fsettings%2Fdomains\&title=Go+to+Domains+Settings).
3. Select the **Edit** dropdown item for the domain to which you would like to assign your branch.
4. Select **Preview** from the **Connect to an environment** section
5. In the **Git Branch** field, enter the branch name to which you would like to assign the domain:

![Image](`/docs-assets/static/docs/domains/assign-domain-to-git-branch-light.png`)

Pro and Enterprise teams can also set branch tracking for their [custom environments](/docs/deployments/environments#custom-environments).

> **💡 Note:** If you prefer to do this using the Vercel REST API instead, you can use the
> ["Update a project
> domain"](/docs/rest-api/reference/endpoints/projects/update-a-project-domain)
> PATCH endpoint.


