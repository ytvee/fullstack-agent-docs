--------------------------------------------------------------------------------
title: "Connectivity"
description: "Connect your Vercel projects to backend services with static IPs and secure networking options."
last_updated: "2026-04-03T23:47:18.509Z"
source: "https://vercel.com/docs/connectivity"
--------------------------------------------------------------------------------

# Connectivity

Connect your projects to backend services that require IP allowlisting or private network access.

## Static IPs (shared pool)

When your database or API needs to see traffic from known IP addresses, Static IPs give you shared static egress IPs that won't change. Perfect for Pro and Enterprise teams who need IP allowlisting without the complexity.

- **Use case**: IP allowlisting for databases, APIs, and legacy systems
- **Network**: Shared VPC with subnet-level isolation
- [**Pricing**](/docs/connectivity/static-ips#pricing): $100.00/month per project + [Private Data Transfer](/docs/pricing/regional-pricing) at regional rates

[Learn more about Static IPs](/docs/connectivity/static-ips)

## Secure Compute

For when you need your own private Virtual Private Cloud (VPC). Secure Compute gives you dedicated networks with VPC peering — your infrastructure stays completely isolated from other customers.

- **Use case**: Full network isolation and VPC peering
- **Network**: Dedicated VPC per customer

[Learn more about Secure Compute](/docs/connectivity/secure-compute)

## Pricing

Both connectivity options are billed on **Private Data Transfer** priced regionally based on the [regional pricing documentation](/docs/pricing/regional-pricing).

| Resource | Pro Price |
| --- | --- |
| Static IPs | $100.00 |


### Understanding data transfer costs

Data transfer costs kick in for all outbound traffic from your Vercel Functions to external services:

- Database queries and responses
- API calls to third-party services
- File uploads and downloads
- Any other outbound network traffic

Keep tabs on your usage in the **Team Settings** **Usage** tab under the **Private Data Transfer** section.


