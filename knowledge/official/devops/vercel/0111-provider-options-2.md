---
id: "vercel-0111"
title: "Provider Options"
description: "Configure provider routing, fallbacks, and restrictions using the OpenResponses API."
category: "vercel-ai-gateway"
subcategory: "ai-gateway"
type: "guide"
source: "https://vercel.com/docs/ai-gateway/sdks-and-apis/openresponses/provider-options"
tags: ["openresponses", "provider", "options", "sdks-and-apis", "provider-options", "model-fallbacks"]
related: ["0110-openresponses-api.md", "0114-tool-calling.md", "0090-provider-options.md"]
last_updated: "2026-04-03T23:47:15.339Z"
---

# Provider Options

The [OpenResponses API](/docs/ai-gateway/sdks-and-apis/openresponses) lets you configure AI Gateway behavior using `providerOptions`. The `gateway` namespace gives you control over provider routing, fallbacks, and restrictions.

## Model fallbacks

Set up automatic fallbacks so if your primary model is unavailable, requests route to backup models in order. Use the `models` array to specify the fallback chain.

```typescript filename="fallbacks.ts"
const apiKey = process.env.AI_GATEWAY_API_KEY;

const response = await fetch('https://ai-gateway.vercel.sh/v1/responses', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    Authorization: `Bearer ${apiKey}`,
  },
  body: JSON.stringify({
    model: 'anthropic/claude-opus-4.6',
    input: [{ type: 'message', role: 'user', content: 'Tell me a fun fact about octopuses.' }],
    providerOptions: {
      gateway: {
        models: ['anthropic/claude-opus-4.6', 'openai/gpt-5.4', 'google/gemini-3.1-pro-preview'],
      },
    },
  }),
});
```

## Provider routing

Control the order in which providers are tried using the `order` array. AI Gateway will attempt providers in the specified order until one succeeds.

```typescript filename="routing.ts"
const response = await fetch('https://ai-gateway.vercel.sh/v1/responses', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    Authorization: `Bearer ${apiKey}`,
  },
  body: JSON.stringify({
    model: 'google/gemini-3.1-pro-preview',
    input: [{ type: 'message', role: 'user', content: 'Explain quantum computing in one sentence.' }],
    providerOptions: {
      gateway: {
        order: ['google', 'openai', 'anthropic'],
      },
    },
  }),
});
```

## Provider restriction

Restrict requests to specific providers using the `only` array. This ensures your requests only go to approved providers, which can be useful for compliance or cost control.

```typescript filename="restriction.ts"
const response = await fetch('https://ai-gateway.vercel.sh/v1/responses', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    Authorization: `Bearer ${apiKey}`,
  },
  body: JSON.stringify({
    model: 'zai/glm-4.7',
    input: [{ type: 'message', role: 'user', content: 'What makes a great cup of coffee?' }],
    providerOptions: {
      gateway: {
        only: ['zai', 'deepseek'],
      },
    },
  }),
});
```

## Provider timeouts

You can set per-provider timeouts for BYOK credentials to trigger fast failover when a provider is slow to respond. Pass `providerTimeouts` in `providerOptions.gateway`:

```json
"providerOptions": {
  "gateway": {
    "providerTimeouts": {
      "byok": { "anthropic": 3000, "bedrock": 5000 }
    }
  }
}
```

For full details, limits, and response metadata, see [Provider Timeouts](/docs/ai-gateway/models-and-providers/provider-timeouts).

## Automatic caching

Use `caching: 'auto'` in the request body to let AI Gateway automatically add cache markers for providers that require them (like Anthropic). For full details, supported providers, and examples, see [Automatic Caching](/docs/ai-gateway/models-and-providers/automatic-caching).


