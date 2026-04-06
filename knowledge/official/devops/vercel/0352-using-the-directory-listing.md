---
id: "vercel-0352"
title: "Using the Directory Listing"
description: "The Directory Listing is served when a particular path is a directory and does not contain an index file. Learn how to toggle and disable it in this guide."
category: "vercel-deployments"
subcategory: "directory-listing"
type: "guide"
source: "https://vercel.com/docs/directory-listing"
tags: ["using-the-directory-listing", "directory", "listing", "setup", "how-to", "troubleshooting"]
related: ["0336-deployment-retention.md", "0353-directory-sync.md", "0327-options-allowlist.md"]
last_updated: "2026-04-03T23:47:19.209Z"
---

# Using the Directory Listing

The Directory Listing setting enables you to display the contents of a directory when a user visits its path. For example, if you create a directory at the root of your project called `/assets`, then when people visit `https://your-site.com/assets`, they will see the files and folders within that directory, as shown in the example below:

![Image](`/front/docs/projects/directory-listing-page-light.png`)

You can enable or disable Directory Listing from **Advanced** in your project sidebar settings.

![Image](`/front/docs/projects/directory-listing-light.png`)

When enabled, the Directory Listing will be displayed. When disabled, a "Not Found" error will be displayed with status code `404`.

> **💡 Note:** If Directory Listing isn't working, navigate to your deployment in the
> dashboard and open  in the sidebar to view the contents of
> your project. Ensure the expected directory and files are listed.

### Disabling Directory Listing on a specific directory

To prevent Directory Listing for a specific path, you can either:

- Add an index file with any extension except `.css`, such as `index.html`. This file will be displayed instead of the Directory Listing
- Or, [set up a custom 404 error](/kb/guide/custom-404-page)


