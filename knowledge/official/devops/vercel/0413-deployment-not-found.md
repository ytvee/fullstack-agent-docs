---
id: "vercel-0413"
title: "DEPLOYMENT_NOT_FOUND"
description: "The deployment was not found. This is a deployment error."
category: "vercel-errors"
subcategory: "errors"
type: "guide"
source: "https://vercel.com/docs/errors/DEPLOYMENT_NOT_FOUND"
tags: ["not", "found", "deployment-not-found", "troubleshoot", "setup", "how-to"]
related: ["0458-not-found.md", "0470-resource-not-found.md", "0409-body-not-a-string-from-function.md"]
last_updated: "2026-04-03T23:47:20.341Z"
---

# DEPLOYMENT_NOT_FOUND

The `DEPLOYMENT_NOT_FOUND` error occurs when a request is made for a deployment that doesn't exist. This could happen if the deployment ID or URL is incorrect, or if the deployment has been deleted.

**Error Code:** `404`

**Name:** Not Found

## Troubleshoot

To troubleshoot this error, follow these steps:

1. **Check the deployment URL**: Ensure that the deployment URL you are using is correct and does not contain any typos or incorrect paths
2. **Check deployment existence:** Verify that the [deployment exists](/docs/deployments/managing-deployments) and has not been deleted
3. **Review deployment logs:** If the deployment exists, review the [deployment logs](/docs/deployments/logs) to identify any issues that might have caused the deployment to be unavailable
4. **Verify permissions:** Ensure you have the necessary [permissions](/docs/accounts/team-members-and-roles) to access the deployment
5. **Consult community resources:** Visit our [community post on debugging 404 errors](https://community.vercel.com/t/debugging-404-errors/437) for additional tips and solutions shared by other developers.
6. **Contact support:** If you've checked the above and are still unable to resolve the issue, [contact support](/help#issues) for further assistance


