---
id: "vercel-0048"
title: "Image Generation"
description: "Generate and edit images using AI models through Vercel AI Gateway with support for multiple providers and modalities."
category: "vercel-ai-gateway"
subcategory: "ai-gateway"
type: "guide"
source: "https://vercel.com/docs/ai-gateway/capabilities/image-generation"
tags: ["generation", "capabilities", "image-generation", "integration-methods", "setup"]
related: ["0046-image-generation-with-ai-sdk.md", "0047-image-generation-with-chat-completions-api.md", "0061-reference-to-video-generation.md"]
last_updated: "2026-04-03T23:47:14.377Z"
---

# Image Generation

The Vercel [AI Gateway](/docs/ai-gateway) supports image generation and editing capabilities. You can generate new images from text prompts, edit existing images, and create variations with natural language instructions.

To see which models AI Gateway supports for image generation, use the **Image Gen** filter at the [AI Gateway Models
page](https://vercel.com/ai-gateway/models?type=image).

### Integration methods

To implement image generation with AI Gateway, use one of the following methods:

- **[AI SDK](/docs/ai-gateway/capabilities/image-generation/ai-sdk)**: Use the AI SDK for TypeScript/JavaScript applications with native support for streaming, multi-modal inputs, and type-safe model interactions
- **[Chat Completions API](/docs/ai-gateway/capabilities/image-generation/openai)**: Use the Chat Completions endpoints for compatibility with existing OpenAI integrations across any programming language

