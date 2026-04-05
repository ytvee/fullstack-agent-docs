--------------------------------------------------------------------------------
title: "Image Input"
description: "Send images for analysis using the OpenResponses API."
last_updated: "2026-04-03T23:47:15.317Z"
source: "https://vercel.com/docs/ai-gateway/sdks-and-apis/openresponses/image-input"
--------------------------------------------------------------------------------

# Image Input

The [OpenResponses API](/docs/ai-gateway/sdks-and-apis/openresponses) supports sending images alongside text for vision-capable models to analyze. Include an `image_url` object in your message content array with either a public URL or a base64-encoded data URI. The `detail` parameter controls the resolution used for analysis.

```typescript filename="image-input.ts"
const apiKey = process.env.AI_GATEWAY_API_KEY;

const response = await fetch('https://ai-gateway.vercel.sh/v1/responses', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    Authorization: `Bearer ${apiKey}`,
  },
  body: JSON.stringify({
    model: 'zai/glm-4.7',
    input: [
      {
        type: 'message',
        role: 'user',
        content: [
          { type: 'text', text: 'Describe this image in detail.' },
          {
            type: 'image_url',
            image_url: { url: 'https://example.com/image.jpg', detail: 'auto' },
          },
        ],
      },
    ],
  }),
});
```

## Base64-encoded images

You can also use base64-encoded images:

```typescript
{
  type: 'image_url',
  image_url: {
    url: `data:image/png;base64,${imageBase64}`,
    detail: 'high',
  },
}
```

## Detail parameter

The `detail` parameter controls image resolution:

- `auto` - Let the model decide the appropriate resolution
- `low` - Use lower resolution for faster processing
- `high` - Use higher resolution for more detailed analysis


