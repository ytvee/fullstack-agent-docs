---
id: "vercel-0653"
title: "Vercel for Platforms"
description: "Build multi-tenant applications that serve multiple customers from a single codebase with custom domains and subdomains."
category: "vercel-domains"
subcategory: "multi-tenant"
type: "concept"
source: "https://vercel.com/docs/multi-tenant"
tags: ["custom-domains", "platforms", "why-build-multi-tenant-apps", "getting-started", "next-steps"]
related: ["0651-domain-management-for-multi-tenant.md", "0652-multi-tenant-limits.md", "0361-setting-up-a-custom-domain.md"]
last_updated: "2026-04-03T23:47:24.431Z"
---

# Vercel for Platforms

A **multi-tenant application** serves multiple customers (tenants) from a single codebase.

Each tenant gets its own domain or subdomain, but you only have one Next.js (or similar) deployment running on Vercel. This approach simplifies your infrastructure, scales well, and keeps your branding consistent across all tenant sites.

Get started with our [detailed docs](/platforms/docs), [multi-tenant Next.js example](https://vercel.com/templates/next.js/platforms-starter-kit), or learn more about customizing domains.

## Why build multi-tenant apps?

Some popular multi-tenant apps on Vercel include:

- **Content platforms**: [Hashnode](https://townhall.hashnode.com/powerful-and-superfast-hashnode-blogs-now-powered-by-nextjs-11-and-vercel), [Dub](https://dub.co/)
- **Documentation platforms:** [Mintlify](https://mintlify.com/), [Fern](https://buildwithfern.com/), [Plain](https://www.plain.com/channels/help-center)
- **Website and ecommerce store builders**: [Super](https://vercel.com/blog/super-serves-thousands-of-domains-on-one-project-with-next-js-and-vercel), [Typedream](https://typedream.com/), [Universe](https://univer.se/)
- **B2B SaaS platforms**: [Zapier](https://zapier.com/interfaces), [Instatus](https://instatus.com/), [Cal](http://cal.com/)

For example, you might have:

- A root domain for your platform: `acme.com`
- Subdomains for tenants: `tenant1.acme.com`, `tenant2.acme.com`
- Fully custom domains for certain customers: `tenantcustomdomain.com`

Vercel's platform automatically issues [SSL certificates](https://vercel.com/docs/domains/working-with-ssl), handles DNS routing via its Anycast network, and ensures each of your tenants gets low-latency responses from the closest CDN region.

## Getting started

The fastest way to get started is with our [multi-tenant Next.js starter kit](https://vercel.com/templates/next.js/platforms-starter-kit). This template includes:

- Custom subdomain routing with Next.js middleware
- Tenant-specific content and pages
- Redis for tenant data storage
- Admin interface for managing tenants
- Compatible with Vercel preview deployments

## Multi-tenant features on Vercel

- Unlimited custom domains
- Unlimited `*.yourdomain.com` subdomains
- Automatic SSL certificate issuance and renewal
- Domain management through REST API or SDK
- Low-latency responses globally with the Vercel CDN
- Preview environment support to test changes
- Support for 35+ frontend and backend frameworks

## Next steps

- [Full Vercel for Platforms docs](/platforms/docs)
- [Learn about limits and features](/docs/multi-tenant/limits)
- [Set up domain management](/docs/multi-tenant/domain-management)
- [Deploy the starter template](https://vercel.com/templates/next.js/platforms-starter-kit)


