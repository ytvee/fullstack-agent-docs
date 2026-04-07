---
id: "vercel-0063"
title: "Video Editing"
description: "Edit existing videos using text prompts with Grok Imagine Video through AI Gateway."
category: "vercel-ai-gateway"
subcategory: "ai-gateway"
type: "guide"
source: "https://vercel.com/docs/ai-gateway/capabilities/video-generation/video-editing"
tags: ["video", "editing", "capabilities", "video-generation", "video-editing", "grok-imagine-video"]
related: ["0062-text-to-video-generation.md", "0060-video-generation.md", "0058-image-to-video-generation.md"]
last_updated: "2026-04-03T23:47:14.606Z"
---

# Video Editing

Edit existing videos using text prompts. Describe the changes you want and the model modifies the video accordingly.

## Grok Imagine Video

Grok Imagine Video (by xAI) can edit existing videos using text prompts. Provide a source video URL and describe the desired edits.

### Grok models

| Model                    | Max Input Duration | Output Resolution |
| ------------------------ | ------------------ | ----------------- |
| `xai/grok-imagine-video` | 8.7 seconds        | Up to 720p        |

> **Note:** Video editing output matches the input video's aspect ratio and resolution,
> capped at 720p. A 1080p input will be downsized to 720p. The `duration`,
> `aspectRatio`, and `resolution` parameters are not supported for editing.

### Grok parameters

| Parameter                            | Type     | Required | Description                                          |
| ------------------------------------ | -------- | -------- | ---------------------------------------------------- |
| `prompt`                             | `string` | Yes      | Description of the edits to apply to the video       |
| `providerOptions.xai.videoUrl`       | `string` | Yes      | URL of the source video to edit                      |
| `providerOptions.xai.pollIntervalMs` | `number` | No       | How often to check task status. Defaults to `5000`   |
| `providerOptions.xai.pollTimeoutMs`  | `number` | No       | Maximum wait time. Defaults to `600000` (10 minutes) |

### Grok example

```typescript filename="video-editing.ts"
import { experimental_generateVideo as generateVideo } from 'ai';
import fs from 'node:fs';

const result = await generateVideo({
  model: 'xai/grok-imagine-video',
  prompt: 'Give the person sunglasses and a hat',
  providerOptions: {
    xai: {
      videoUrl: 'https://example.com/source-video.mp4',
      pollTimeoutMs: 600000,
    },
  },
});

fs.writeFileSync('output.mp4', result.videos[0].uint8Array);
```

> **Note:** Video generation can take several minutes. Set `pollTimeoutMs` to at least 10
> minutes (600000ms) for reliable operation. Generated video URLs are ephemeral
> and should be downloaded promptly.

***

