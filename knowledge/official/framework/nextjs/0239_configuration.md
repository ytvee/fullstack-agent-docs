---
title: Configuration
description: "Configure `adapterPath` or `NEXT_ADAPTER_PATH` to use a custom deployment adapter."
url: "https://nextjs.org/docs/app/api-reference/adapters/configuration"
version: 16.2.2
---

# Configuration

To use an adapter, specify the path to your adapter module in `adapterPath`:

```js filename="next.config.js"
/** @type {import('next').NextConfig} */
const nextConfig = {
  adapterPath: require.resolve('./my-adapter.js'),
}

module.exports = nextConfig
```

Alternatively `NEXT_ADAPTER_PATH` can be set to enable zero-config usage in deployment platforms.


