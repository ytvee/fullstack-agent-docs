---
id: "vercel-0258"
title: "NEXTJS_NO_SELF_HOSTED_VIDEOS"
description: "Prevent video files from being added to Next.js applications."
category: "vercel-conformance"
subcategory: "conformance"
type: "concept"
source: "https://vercel.com/docs/conformance/rules/NEXTJS_NO_SELF_HOSTED_VIDEOS"
tags: ["nextjs", "no", "self", "hosted", "videos", "rules"]
related: ["0255-nextjs-no-fetch-in-server-props.md", "0263-nextjs-safe-url-imports.md", "0259-nextjs-no-turbo-cache.md"]
last_updated: "2026-04-03T23:47:18.201Z"
---

# NEXTJS_NO_SELF_HOSTED_VIDEOS

Video files, which are typically large, can consume a lot of bandwidth for
your Next.js application. Video files are better served from a dedicated video
CDN that is optimized for serving videos.

## How to fix

Vercel Blob can be used for storing and serving large files such as videos.

You can use either [server uploads or client uploads](/docs/storage/vercel-blob#server-and-client-uploads) depending on the file size:

- [Server uploads](/docs/storage/vercel-blob/server-upload) are suitable for files up to **4.5 MB**
- [Client uploads](/docs/storage/vercel-blob/client-upload) allow for uploading larger files directly from the browser to Vercel Blob, supporting files up to **5 TB (5,000 GB)**

See the [best practices for hosting videos on Vercel](/kb/guide/best-practices-for-hosting-videos-on-vercel-nextjs-mp4-gif) guide to learn more about various other options for hosting videos.


