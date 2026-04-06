---
id: "vercel-0331"
title: "Methods to Protect Deployments"
description: "Vercel offers three methods to protect your deployments: Vercel Authentication, Password Protection, and Trusted IPs."
category: "vercel-deployments"
subcategory: "deployment-protection"
type: "concept"
source: "https://vercel.com/docs/deployment-protection/methods-to-protect-deployments"
tags: ["methods", "protect", "password-protection", "trusted-ips", "related-resources"]
related: ["0333-restrict-deployment-access-by-ip-address.md", "0332-password-protection.md", "0334-restrict-access-to-deployments-with-vercel-authentication.md"]
last_updated: "2026-04-03T23:47:18.869Z"
---

# Methods to Protect Deployments

Vercel offers three methods for protecting your deployments. Depending on your use case, you can choose to protect a single environment, or multiple environments. See [Understanding Deployment Protection by environment](/docs/security/deployment-protection#understanding-deployment-protection-by-environment) for more information.

To see an overview of your projects' protections:

1. Open **Settings** in the sidebar of your [dashboard](/dashboard) and select [**Deployment Protection**](https://vercel.com/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Fsettings%2Fdeployment-protection\&title=Go+to+Deployment+Protection+settings)

![Image](`/docs-assets/static/docs/concepts/deployments/preview-deployments/deployment-protection-projects-view.png`)

## Vercel Authentication

> **🔒 Permissions Required**: Vercel Authentication

With Vercel Authentication you can restrict access to all deployments (including non-public deployments), meaning only team members with a Vercel account, or users you share a [Sharable Link](/docs/security/deployment-protection/methods-to-bypass-deployment-protection#sharable-links) with, can access non-public URLs, such as `my-project-1234-your-name.vercel.app`.

When a Vercel user visits your protected deployment but doesn't have permission to access it, they can [request access](/docs/security/deployment-protection/methods-to-protect-deployments/vercel-authentication#access-requests) for their Vercel account. This request triggers an email and Vercel notification to the branch authors.

Learn more about [Vercel Authentication](/docs/security/deployment-protection/methods-to-protect-deployments/vercel-authentication) and how to enable it.

## Password Protection

> **🔒 Permissions Required**: Password Protection

Password Protection on Vercel lets you restrict access to both non-public, and public deployments depending on the type of [environment protection](/docs/security/deployment-protection#understanding-deployment-protection-by-environment) you choose.

Learn more about [Password Protection](/docs/security/deployment-protection/methods-to-protect-deployments/password-protection) and how to enable it.

## Trusted IPs

> **🔒 Permissions Required**: Trusted IPs

Trusted IPs restrict deployment access to specified IPv4 addresses and [CIDR ranges](https://www.ipaddressguide.com/cidr "What are CIDR ranges?"), returning a 404 for unauthorized IPs. This protection feature is suitable for limiting access through specific paths like VPNs or external proxies.

Learn more about [Trusted IPs](/docs/security/deployment-protection/methods-to-protect-deployments/trusted-ips) and how to enable it.

## Related resources

- [Understanding Deployment Protection by environment](/docs/deployment-protection#understanding-deployment-protection-by-environment)
- [Methods to bypass deployment protection](/docs/deployment-protection/methods-to-bypass-deployment-protection)


