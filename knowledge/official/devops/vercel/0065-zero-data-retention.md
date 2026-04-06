---
id: "vercel-0065"
title: "Zero Data Retention"
description: "Learn about zero data retention policies and how to enforce ZDR on a per-request basis with AI Gateway."
category: "vercel-ai-gateway"
subcategory: "ai-gateway"
type: "guide"
source: "https://vercel.com/docs/ai-gateway/capabilities/zdr"
tags: ["zero-data-retention", "ai-sdk", "openresponses", "responses-api", "chat-completions", "anthropic"]
related: ["0045-disallow-prompt-training.md", "0044-custom-reporting.md", "0083-text-generation-quickstart.md"]
last_updated: "2026-04-03T23:47:14.663Z"
---

# Zero Data Retention

Zero data retention (ZDR) is available for Pro and Enterprise users on AI Gateway. There are two ways to enforce ZDR:

- **Team-wide**: Enable ZDR globally from the [AI Gateway Dashboard Settings tab](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fai-gateway\&title=AI+Gateway). Once enabled, all requests are routed to ZDR-compliant providers.
- **Per-request**: Set `zeroDataRetention: true` in `providerOptions` for individual requests. This gives you fine-grained control over which requests require ZDR.

These two methods work as an OR: if either is enabled, ZDR is enforced for that request.

ZDR is a superset of [disallowing prompt training](/docs/ai-gateway/capabilities/disallow-prompt-training). All ZDR-compliant providers also disallow prompt training, but not all providers that disallow prompt training offer full zero data retention.

> **💡 Note:** ZDR enforcement does not apply to [BYOK (Bring Your Own
> Key)](/docs/ai-gateway/byok) requests. When you use BYOK, ZDR is not
> enforced since the request uses your own API key, your
> configuration, and agreement with the provider. However, if AI Gateway falls
> back to AI Gateway system credentials, ZDR filters are honored on
> the failover request.

## Pricing

| Option                          | Cost                     | Availability       |
| ------------------------------- | ------------------------ | ------------------ |
| Per-request zero data retention | No additional cost       | Pro and Enterprise |
| Team-wide zero data retention   | $0.10 per 1,000 requests | Pro and Enterprise |

Team-wide ZDR is only charged on successful responses that return usage data. Requests that fail or return errors are not charged.

## Vercel

AI Gateway has a ZDR policy and does not retain prompts, outputs, or sensitive data. User data is immediately and permanently deleted after requests are completed. No action is needed on the user side.

## Providers

AI Gateway has agreements in place to offer ZDR with specific providers. A provider's default policy may not match with the status that AI Gateway has in place due to these agreements.

By default, AI Gateway does not route based on the data retention policy of providers.

> **💡 Note:** If we do not know a provider's ZDR stance or have not yet established an
> agreement with them, they are treated as not being ZDR-compliant. If ZDR is enabled
> for a request, it will not be routed through this provider.

## Team-wide zero data retention

Pro and Enterprise customers can enable ZDR globally for all requests from the [AI Gateway Dashboard](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fai-gateway\&title=AI+Gateway).

To enable team-wide ZDR:

1. Go to the [AI Gateway Dashboard](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fai-gateway)
2. Navigate to the [**Settings** tab](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fai-gateway%2Fsettings\&title=AI+Gateway+Settings)
3. Toggle on the **Zero Data Retention** option

Once enabled, team-wide ZDR applies to all your requests through the Vercel team you configured it for. However, ZDR enforcement does not apply to [BYOK](/docs/ai-gateway/authentication-and-byok/byok) requests since those use your own API key, configuration, and agreement with the provider. If AI Gateway falls back to AI Gateway system credentials, it honors ZDR filters on the failover request.

## Per-request zero data retention

You can enforce ZDR on individual requests using the `zeroDataRetention` parameter in `providerOptions`. Set `zeroDataRetention` to `true` to route the request only through providers that have zero data retention agreements with Vercel AI Gateway.

If no ZDR-compliant providers are available for the requested model, the request fails with an error:

```json
{
  "error": "No ZDR (Zero Data Retention) providers available for model: example/model-name. \
            Providers considered: provider-a, provider-b",
  "type": "no_providers_available",
  "statusCode": 400
}
```

When ZDR is enabled, the routing metadata in successful responses shows how AI Gateway filtered providers. The `planningReasoning` field indicates which providers were considered:

```json
{
  "gateway": {
    "routing": {
      "planningReasoning": "ZDR requested: 5 attempts → 2 ZDR attempts. \
                            ZDR execution order: anthropic(system) → bedrock(system)"
    }
  }
}
```

ZDR enforcement does not apply to [BYOK](/docs/ai-gateway/authentication-and-byok/byok) requests since those use your own API key, configuration, and agreement with the provider. If AI Gateway falls back to AI Gateway system credentials, it honors ZDR filters on the failover request.
ZDR enforcement also applies to any fallback providers.

ZDR enforcement does not apply to [BYOK](/docs/ai-gateway/authentication-and-byok/byok) requests since those use your own API key, configuration, and agreement with the provider. If AI Gateway falls back to AI Gateway system credentials, ZDR filters are honored on the failover request.

### Using AI SDK

Set `zeroDataRetention` to `true` in `providerOptions`:

#### streamText

```typescript filename="zdr.ts" {8-12}
import type { GatewayProviderOptions } from '@ai-sdk/gateway';
import { streamText } from 'ai';

export async function POST(request: Request) {
  const result = streamText({
    model: 'moonshotai/kimi-k2.5',
    prompt: 'Analyze this sensitive business data and provide insights.',
    providerOptions: {
      gateway: {
        zeroDataRetention: true,
      } satisfies GatewayProviderOptions,
    },
  });

  return result.toDataStreamResponse();
}
```

#### generateText

```typescript filename="zdr.ts" {8-12}
import type { GatewayProviderOptions } from '@ai-sdk/gateway';
import { generateText } from 'ai';

export async function POST(request: Request) {
  const { text } = await generateText({
    model: 'moonshotai/kimi-k2.5',
    prompt: 'Analyze this sensitive business data and provide insights.',
    providerOptions: {
      gateway: {
        zeroDataRetention: true,
      } satisfies GatewayProviderOptions,
    },
  });

  return Response.json({ text });
}
```

### Using the Chat Completions API

Set `zeroDataRetention` to `true` in `providerOptions`:

#### TypeScript

```typescript filename="zdr.ts" {19-23}
import OpenAI from 'openai';

const apiKey = process.env.AI_GATEWAY_API_KEY || process.env.VERCEL_OIDC_TOKEN;

const openai = new OpenAI({
  apiKey,
  baseURL: 'https://ai-gateway.vercel.sh/v1',
});

const completion = await openai.chat.completions.create({
  model: 'moonshotai/kimi-k2.5',
  messages: [
    {
      role: 'user',
      content:
        'Tell me the history of the San Francisco Mission-style burrito in two paragraphs.',
    },
  ],
  providerOptions: {
    gateway: {
      zeroDataRetention: true, // Request only ZDR compliant providers
    },
  },
});
```

#### Python

```python filename="zdr.py" {17-21}
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("AI_GATEWAY_API_KEY"),
    base_url="https://ai-gateway.vercel.sh/v1",
)

completion = client.chat.completions.create(
    model="moonshotai/kimi-k2.5",
    messages=[
        {
            "role": "user",
            "content": "Tell me the history of the San Francisco Mission-style burrito in two paragraphs.",
        }
    ],
    extra_body={
        "providerOptions": {
            "gateway": {"zeroDataRetention": True}  # Request only ZDR compliant providers
        }
    },
)
```

### Using the Responses API

Set `zeroDataRetention` to `true` in `providerOptions`:

#### TypeScript

```typescript filename="zdr.ts" {18-22}
const apiKey = process.env.AI_GATEWAY_API_KEY || process.env.VERCEL_OIDC_TOKEN;

const response = await fetch('https://ai-gateway.vercel.sh/v1/responses', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    Authorization: `Bearer ${apiKey}`,
  },
  body: JSON.stringify({
    model: 'moonshotai/kimi-k2.5',
    input: [
      {
        type: 'message',
        role: 'user',
        content: 'Analyze this sensitive business data and provide insights.',
      },
    ],
    providerOptions: {
      gateway: {
        zeroDataRetention: true,
      },
    },
  }),
});
```

#### Python

```python filename="zdr.py" {17-21}
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("AI_GATEWAY_API_KEY"),
    base_url="https://ai-gateway.vercel.sh/v1",
)

response = client.responses.create(
    model="moonshotai/kimi-k2.5",
    input=[
        {
            "role": "user",
            "content": "Analyze this sensitive business data and provide insights.",
        }
    ],
    extra_body={
        "providerOptions": {
            "gateway": {"zeroDataRetention": True}
        }
    },
)
```

### Using the Anthropic Messages API

Set `zeroDataRetention` to `true` in `providerOptions`:

#### TypeScript

```typescript filename="zdr.ts" {19-23}
import Anthropic from '@anthropic-ai/sdk';

const apiKey = process.env.AI_GATEWAY_API_KEY || process.env.VERCEL_OIDC_TOKEN;

const anthropic = new Anthropic({
  apiKey,
  baseURL: 'https://ai-gateway.vercel.sh/anthropic/v1',
});

const message = await anthropic.messages.create({
  model: 'anthropic/claude-sonnet-4.6',
  messages: [
    {
      role: 'user',
      content: 'Analyze this sensitive business data and provide insights.',
    },
  ],
  // @ts-expect-error -- providerOptions is not in the Anthropic SDK types
  providerOptions: {
    gateway: {
      zeroDataRetention: true,
    },
  },
});
```

#### Python

```python filename="zdr.py" {17-21}
import os
import anthropic

client = anthropic.Anthropic(
    api_key=os.getenv("AI_GATEWAY_API_KEY"),
    base_url="https://ai-gateway.vercel.sh/anthropic/v1",
)

message = client.messages.create(
    model="anthropic/claude-sonnet-4.6",
    messages=[
        {
            "role": "user",
            "content": "Analyze this sensitive business data and provide insights.",
        }
    ],
    extra_body={
        "providerOptions": {
            "gateway": {"zeroDataRetention": True}
        }
    },
)
```

### Using the OpenResponses API

Set `zeroDataRetention` to `true` in `providerOptions`:

#### TypeScript

```typescript filename="zdr.ts" {18-22}
const apiKey = process.env.AI_GATEWAY_API_KEY || process.env.VERCEL_OIDC_TOKEN;

const response = await fetch('https://ai-gateway.vercel.sh/openresponses/v1/responses', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    Authorization: `Bearer ${apiKey}`,
  },
  body: JSON.stringify({
    model: 'moonshotai/kimi-k2.5',
    input: [
      {
        type: 'message',
        role: 'user',
        content: 'Analyze this sensitive business data and provide insights.',
      },
    ],
    providerOptions: {
      gateway: {
        zeroDataRetention: true,
      },
    },
  }),
});
```

#### Python

```python filename="zdr.py" {17-21}
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("AI_GATEWAY_API_KEY"),
    base_url="https://ai-gateway.vercel.sh/openresponses/v1",
)

response = client.responses.create(
    model="moonshotai/kimi-k2.5",
    input=[
        {
            "role": "user",
            "content": "Analyze this sensitive business data and provide insights.",
        }
    ],
    extra_body={
        "providerOptions": {
            "gateway": {"zeroDataRetention": True}
        }
    },
)
```

## Using both account and request-level ZDR

Team-wide ZDR toggled to enabled overrides request-level `zeroDataRetention: false` since these options work together as an OR. If either option is enabled, ZDR is enforced on the request.

## Caching and zero data retention

When you use [prompt caching](/docs/ai-gateway/models-and-providers/automatic-caching) through AI Gateway, caching happens at the provider level. Whether that caching is ZDR-compliant depends on the provider.

## ZDR providers and policies

The following providers currently offer ZDR on AI Gateway. Please review each provider's ZDR policy and terms carefully. A provider's default policy may not match with the status that AI Gateway has in place due to negotiated agreements. We are constantly coordinating and revising agreements to be able to enforce stricter retention policies for customers. The full terms of service are available for each provider on the [model pages](/ai-gateway/models).

All ZDR-compliant providers also disallow prompt training, since ZDR is a superset of [disallowing prompt training](/docs/ai-gateway/capabilities/disallow-prompt-training). In some cases, certain models or functionalities may be excluded from a provider's ZDR policy. AI Gateway will not fail these requests if zero data retention is enabled, so review the provider's policy in the table below to understand the nuances of specific tools and how they affect data retention.

| Provider       | No prompt training | ZDR | Policy                                                                                                               |
| -------------- | ------------------ | --- | -------------------------------------------------------------------------------------------------------------------- |
| Amazon Bedrock | ✓                  | ✓   | [Data protection](https://docs.aws.amazon.com/bedrock/latest/userguide/data-protection.html)                         |
| Anthropic      | ✓                  | ✓   | [ZDR policy](https://platform.claude.com/docs/en/build-with-claude/zero-data-retention)                              |
| Azure          | ✓                  | ✓   | [Data privacy](https://learn.microsoft.com/en-us/azure/foundry/responsible-ai/openai/data-privacy?tabs=azure-portal) |
| Baseten        | ✓                  | ✓   | [Security](https://docs.baseten.co/observability/security)                                                           |
| Cerebras       | ✓                  | ✓   | [Privacy policy](https://www.cerebras.ai/privacy-policy)                                                             |
| DeepInfra      | ✓                  | ✓   | [Data handling](https://deepinfra.com/docs/data)                                                                     |
| Fireworks      | ✓                  | ✓   | [Data handling](https://docs.fireworks.ai/guides/security_compliance/data_handling)                                  |
| Google Vertex  | ✓                  | ✓   | [ZDR policy](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/vertex-ai-zero-data-retention)               |
| Groq           | ✓                  | ✓   | [ZDR policy](https://console.groq.com/docs/your-data#zero-data-retention)                                            |
| Mistral        | ✓                  | ✓   | [Terms of service](https://legal.mistral.ai/terms)                                                                   |
| Nebius         | ✓                  | ✓   | [Legal quick guide](https://docs.tokenfactory.nebius.com/legal/legal-quick-guide)                                    |
| Parasail       | ✓                  | ✓   | [Terms of service](https://parasail.io/legal/terms-of-service)                                                       |
| Together       | ✓                  | ✓   | [Terms of service](https://www.together.ai/terms-of-service)                                                         |


