--------------------------------------------------------------------------------
title: "Configuring In-function Concurrency"
description: "Learn how to allow multiple requests to share a single function instance."
last_updated: "2026-04-03T23:47:21.743Z"
source: "https://vercel.com/docs/functions/configuring-functions/concurrency"
--------------------------------------------------------------------------------

# Configuring In-function Concurrency

In-function concurrency allows multiple requests to share a single function instance and is available when using the Node.js or Python runtimes. To learn more, see the [Efficient serverless Node.js with in-function concurrency](/blog/serverless-servers-node-js-with-in-function-concurrency) blog post.

This feature is ideal for I/O-bound tasks like database operations or API requests, as it makes better use of system resources. However, enabling this feature may introduce latency for CPU-intensive tasks such as image processing, LLM training, or large matrix calculations, this is a beta constraint that we are working to improve.

## Enabling in-function concurrency

> **💡 Note:** You must have enabled at least 1vCPU of memory (i.e. **Standard** or
> **Performance**) in order to enable concurrency for your functions. To learn
> more, see [Setting your default function CPU
> size](/docs/functions/configuring-functions/memory#setting-your-default-function-memory-/-cpu-size).

To enable the feature:

1. Navigate to your project in the Vercel [dashboard](/dashboard).
2. Click on the **Settings** tab and select the [**Functions**](https://vercel.com/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Fsettings%2Ffunctions\&title=Go+to+Functions+Settings) section.
3. Scroll to the **In-function concurrency** section.
4. Toggle the switch to **Enabled**, and click **Save**.
5. Redeploy your project to apply the changes.

Concurrency is now enabled for all functions in that project.

## Viewing in-function concurrency metrics

Once enabled, you can view the [GB-Hours saved](https://vercel.com/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Fobservability%2Fserverless-functions%2Fadvanced\&title=View+GB-Hours+saved):

1. Choose your project from the [dashboard](/dashboard).
2. Click on the **Settings** tab and select the [**Functions**](https://vercel.com/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Fsettings%2Ffunctions\&title=Go+to+Functions+Settings) section and scroll to the **In-function concurrency** section.
3. Next to the toggle, click the **View in-function concurrency metrics** link.

From here, you'll be able to see total consumed and saved GB-Hours, and the ratio of the saved usage.


