---
id: "vercel-0556"
title: "Edge Functions"
description: "Run minimal code at the network edge."
category: "vercel-functions"
subcategory: "functions"
type: "concept"
source: "https://vercel.com/docs/functions/runtimes/edge/edge-functions"
tags: ["streaming", "cron-jobs", "edge-config", "edge", "runtimes", "edge-functions"]
related: ["0557-edge-runtime.md", "0562-runtimes.md", "0563-using-the-python-runtime-with-vercel-functions.md"]
last_updated: "2026-04-03T23:47:22.055Z"
---

# Edge Functions

> **⚠️ Warning:** The standalone Edge Functions product is no longer available. You can use Vercel
> Functions with the `edge` runtime instead. However, we recommend migrating
> from edge to Node.js for improved performance and reliability. Both runtimes
> run on [Fluid compute](/docs/fluid-compute) with [Active CPU
> pricing](/docs/functions/usage-and-pricing).

Edge Functions are Vercel Functions that run on the Edge Runtime, a minimal JavaScript runtime that exposes a set of Web Standard APIs.

- **Lightweight runtime**: With a smaller API surface area and using V8 isolates, Edge runtime-powered functions have a slim runtime with only a subset of Node.js APIs are exposed
- **Globally distributed by default**: Vercel deploys all Edge Functions globally across its CDN, which means your site's visitors will get API responses from data centers geographically near them

> **⚠️ Warning:** We recommend migrating from edge to Node.js for improved performance and
> reliability. Both runtimes run on [Fluid compute](/docs/fluid-compute) with
> [Active CPU pricing](/docs/functions/usage-and-pricing).

## Edge Functions and your data source

**Edge Functions** execute in the region closest to the user, which could result in longer response times when the function relies on a database located far away. For example, if a visitor triggers an Edge Function in Japan, but it depends on a database in San Francisco, the Function will have to send requests to and wait for a response from San Francisco for each call.

To avoid these long roundtrips, you can limit your Edge Functions to [regions near your database](/docs/functions/configuring-functions/region#setting-your-default-region), or you could use a globally-distributed database. Vercel's [storage options](/docs/storage) allow you to determine the [best location for your database](/docs/storage#locate-your-data-close-to-your-functions).

## Feature support

| Feature                         | Support Status |
| ------------------------------- | -------------- |
| Secure Compute                  | Not Supported  |
| [Streaming](#streaming)         | Supported      |
| [Cron jobs](#cron-jobs)         | Supported      |
| [Vercel Storage](/docs/storage) | Supported      |
| [Edge Config](#edge-config)     | Supported      |
| OTEL                            | Not supported  |

### Streaming

Streaming refers to the ability to send or receive data in a continuous flow.

The [Edge runtime](/docs/functions/runtimes/edge) supports streaming by default.

Edge Functions **do not** have a maximum duration, but you **must** send an *initial* response within 25 seconds. You can continue [streaming a response](/docs/functions/streaming-functions) beyond that time.

Node.js and Edge runtime streaming functions support the [`waitUntil` method](/docs/functions/functions-api-reference/vercel-functions-package#waituntil), allowing you to perform an asynchronous task during the lifecycle of the request.

### Cron jobs

[Cron jobs](/docs/cron-jobs) are time-based scheduling tools used to automate repetitive tasks. When a cron job is triggered through the [cron expression](/docs/cron-jobs#cron-expressions), it calls a Vercel Function.

### Edge Config

An [Edge Config](/docs/edge-config) is a global data store that enables experimentation with feature flags, A/B testing, critical redirects, and IP blocking. It enables you to read data at the edge without querying an external database or hitting upstream servers.

## Location

Edge Functions are executed close to the end-users across Vercel's global network.

When you deploy Edge Functions, there are considerations you need to make about where it's deployed and executes. Edge Functions are executed globally and in a region close to the user's request. However, if your [data source](/docs/storage#locate-your-data-close-to-your-functions) is geographically far from this request, any response will be slow. Because of this you can opt to [execute your function closer to your data source](/docs/functions/configuring-functions/region).

## Failover mode

Vercel's [failover mode](/docs/security#failover-strategy) refers to the system's behavior when a function fails to execute because of data center downtime.

Vercel provides [redundancy](/docs/regions#outage-resiliency) and automatic failover for Edge Functions to ensure high availability.

## File system support

Edge Functions do not have filesystem access due to their ephemeral nature.

## Isolation boundary

In Vercel, the isolation boundary refers to the separation of individual instances of a function to ensure they don't interfere with each other. This provides a secure execution environment for each function.

As the Edge runtime is built on the [V8 engine](https://developers.google.com/apps-script/guides/v8-runtime), it uses V8 isolates to separate just the runtime context, allowing for quick startup times and high performance.

## Bundle size limits

Vercel places restrictions on the maximum size of the deployment bundle for functions to ensure that they execute in a timely manner. Edge Functions have plan-dependent size limits. This is the total, compressed size of your function and its dependencies after bundling.

## Memory size limits

Edge Functions have a fixed memory limit. When you exceeds this limit, the execution will be aborted and we will return a `502` error.

The maximum size for a Function includes your JavaScript code, imported libraries and files (such as fonts), and all files bundled in the function.

If you reach the limit, make sure the code you are importing in your function is used and is not too heavy. You can use a package size checker tool like [bundle](https://bundle.js.org/) to check the size of a package and search for a smaller alternative.

### Request body size

In Vercel, the request body size is the maximum amount of data that can be included in the body of a request to a function.

Edge Functions have the following limits applied to the request size:

| Name                              | Limit |
| --------------------------------- | ----- |
| Maximum URL length                | 14 KB |
| Maximum request body length       | 4 MB  |
| Maximum number of request headers | 64    |
| Maximum request headers length    | 16 KB |

## Edge Function API support

Edge Functions are neither Node.js nor browser applications, which means they don't have access to all browser and Node.js APIs. Currently, the Edge runtime offers [a subset of browser APIs](/docs/functions/runtimes/edge-runtime) and [some Node.js APIs](/docs/functions/runtimes/edge-runtime#unsupported-apis).

There are some restrictions when writing Edge Functions:

- Use ES modules
- Most libraries which use Node.js APIs as dependencies can't be used in Edge Functions yet. See [available APIs](/docs/functions/runtimes/edge#supported-apis) for a full list
- Dynamic code execution (such as `eval`) is not allowed for security reasons. You must ensure **libraries used in your Edge Functions don't rely on dynamic code execution** because it leads to a runtime error. For example, the following APIs cannot be used:
  | API | Description |
  | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
  | [`eval`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/eval) | Evaluates JavaScript code represented as a string |
  | [`new Function(evalString)`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Function) | Creates a new function with the code provided as an argument |
  | [`WebAssembly.instantiate`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/WebAssembly/instantiate) | Compiles and instantiates a WebAssembly module from a buffer source |

See the [Edge Runtime supported APIs](/docs/functions/runtimes/edge#edge-runtime-supported-apis) for more information.

### Limits on fetch API

- You cannot set non-standard port numbers in the fetch URL (e.g., `https://example.com:8080`). Only `80` and `443` are allowed. If you set a non-standard port number, the port number is ignored, and the request is sent to port `80` for `http://` URL, or port `443` for `https://` URL.
- The maximum number of requests from `fetch` API is **950** per Edge Function invocation.
- The maximum number of open connections is **6**.
  - Each function invocation can have up to 6 open connections. For example, if you try to send 10 simultaneous fetch requests, only 6 of them can be processed at a time. The remaining requests are put into a waiting queue and will be processed accordingly as those in-flight requests are completed.
- If in-flight requests have been waiting for a response for more than 15 seconds with no active reads/writes, the runtime may cancel them based on its LRU (Least Recently Used) logic.
  - If you attempt to use a canceled connection, the `Network connection lost.` exception will be thrown.
  - You can `catch` on the `fetch` promise to handle this exception gracefully (e.g. with retries). Additionally, you can use the [`AbortController`](https://developer.mozilla.org/en-US/docs/Web/API/AbortController) API to set timeouts for `fetch` requests.

### Limited Date API

To avoid CPU timing attacks, like Spectre, date and time functionality is not generally available. In particular, the time returned from `Date.now()` only advances after I/O operations, like `fetch`. For example:

```ts filename="app/api/date/route.ts" framework=all
export const runtime = 'edge';

export async function GET(request: Request) {
  const currentDate = () => new Date().toISOString();
  for (let i = 0; i < 500; i++) {
    console.log(`Current Date before fetch: ${currentDate()}`); // Prints the same value 1000 times.
  }

  await fetch('https://worldtimeapi.org/api/timezone/Etc/UTC');
  console.log(`Current Date after fetch: ${currentDate()}`); // Prints the new time

  return Response.json({ date: currentDate() });
}
```

```js filename="app/api/date/route.js" framework=all
export const runtime = 'edge';

export async function GET(request) {
  const currentDate = () => new Date().toISOString();
  for (let i = 0; i < 500; i++) {
    console.log(`Current Date before fetch: ${currentDate()}`); // Prints the same value 1000 times.
  }

  await fetch('https://worldtimeapi.org/api/timezone/Etc/UTC');
  console.log(`Current Date after fetch: ${currentDate()}`); // Prints the new time

  return Response.json({ date: currentDate() });
}
```

## Limits

The table below outlines the limits and restrictions of using Edge Functions on Vercel:

| Feature | Edge Runtime |
| --------------------------------------------------------------------------------Autoscaled concurrency | --------------------------------------------------------------------------------------------------------------------------- |
| [Maximum memory](/docs/functions/limitations#memory-size-limits) | 128 MB |
| [Maximum duration](/docs/functions/limitations#max-duration) | 25s (to begin returning a response, but can continue [streaming](/docs/functions/streaming-functions) data for up to 300s.) |
| [Size](/docs/functions/runtimes#bundle-size-limits) (after gzip compression) | Hobby: 1 MB, Pro: 2 MB, Ent: 4 MB |
| [Concurrency](/docs/functions/concurrency-scaling#automatic-concurrency-scaling) | Autoscaled concurrency based on your plan |
| [Cost](/docs/functions/usage-and-pricing) | Pay for CPU time |
| [Regions](/docs/functions/runtimes#location) | Executes global-first, [can specify a region](/docs/functions/configuring-functions/region) |
| [API Coverage](/docs/functions/limitations#api-support) | Limited API support |

### Routing Middleware CPU Limit

Routing Middleware can use no more than **50 ms** of CPU time on average.

This limitation refers to actual net CPU time, which is the time spent performing calculations, not the total elapsed execution or "wall clock" time. For example, when you are blocked talking to the network, the time spent waiting for a response does *not* count toward CPU time limitations.

## Logs

See the Vercel Functions [Logs](/docs/functions/logs) documentation for more information on how to debug and monitor your Edge Functions.

## Pricing

The Hobby plan offers functions for free, within [limits](/docs/limits). The Pro plan extends these limits, and charges CPU Time for Edge Functions.

Edge runtime-powered functions usage is based on [CPU Time](/docs/pricing/edge-functions#managing-cpu-time). CPU time is the time spent actually processing your code. This doesn't measure time spent waiting for data fetches to return. See "Managing usage and pricing for [Edge Functions](/docs/pricing/edge-functions)" for more information.

Functions using the Edge Runtime are measured in the number of [**execution units**](/docs/limits/usage#execution-units), which are the amount of CPU time — or time spent performing calculations — used when a function is invoked. CPU time does not include idle time spent waiting for data fetching.

A function can use up to 50 ms of CPU time per execution unit. If a function uses more than 50 ms, it will be divided into multiple 50 ms units for billing purposes.

See [viewing function usage](#viewing-function-usage) for more information on how to track your usage.

### Resource pricing

The following table outlines the price for each resource according to the plan you are on.

Edge Functions are available for free with the included usage limits. If you exceed the included usage and are on the Pro plan, you will be charged for the additional usage according to the on-demand costs:

| Resource | Pro Price |
| --- | --- |
| Edge Function Execution Units | $2.00 |
| Function Invocations | $0.60 |


### Hobby

Vercel will send you emails as you are nearing your usage limits. On the Hobby plan you **will not pay for any additional usage**. However, your account may be paused if you do exceed the limits.

When your [Hobby team](/docs/plans/hobby) is set to **paused**, it remains in this state indefinitely unless you take action. This means **all** new and existing [deployments](/docs/deployments) will be paused.

> **💡 Note:** If you have reached this state, your application is likely a good candidate
> for a [Pro account](/docs/plans/pro-plan).

To unpause your account, you have two main options:

- **Contact Support**: You can reach out to our [support team](/help) to discuss the reason for the pause and potential resolutions
- **Transfer to a Pro team**:
  If your Hobby team is paused, you won't have the option to initiate a [Pro trial](/docs/plans/pro-plan/trials). Instead, you can set up a Pro team:
  1. [Create a Pro team account](/docs/accounts/create-a-team)
  2. Add a valid credit card to this account. Open **Settings** in the sidebar, then select [**Billing**](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fsettings%2Fbilling\&title=Go+to+Billing) and **Payment Method**

Once set up, a transfer modal will appear, prompting you to [transfer your previous Hobby projects](/docs/projects/overview#transferring-a-project) to this new team. After transferring, you can continue with your projects as usual.

### Pro

For teams on a Pro trial, the [trial will end](/docs/plans/pro-plan/trials#post-trial-decision) when your team reaches the [trial limits](/docs/plans/pro-plan/trials#trial-limitations).

Once your team exceeds the included usage, you will continue to be charged the on-demand costs going forward.

Pro teams can [set up Spend Management](/docs/spend-management#managing-your-spend-amount) to get notified or to automatically take action, such as [using a webhook](/docs/spend-management#configuring-a-webhook) or pausing your projects when your usage hits a set spend amount.

### Enterprise

Enterprise agreements provide custom usage and pricing for Edge Functions, including:

- Custom [execution units](/docs/functions/runtimes/edge/edge-functions#managing-execution-units)
- Multi-region deployments

See [Vercel Enterprise plans](/docs/plans/enterprise) for more information.

### Viewing function usage

Usage metrics can be found in the [Usage section in the sidebar](/dashboard/usage) on your [dashboard](/dashboard). Functions are invoked for every request that is served.

You can see the usage for **functions using the Edge Runtime** on the **Edge Functions** section of the [Usage section in the sidebar](/docs/limits/usage#edge-functions). The dashboard tracks the usage values:

| Metric          | Description                                                                                               | Priced                                                                                                                             | Optimize                                       |
| --------------- | --------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| Invocations     | The number of times your Functions have been invoked                                                      |  | [Learn More](#optimizing-function-invocations) |
| Execution Units | The number of execution units that your Edge Functions have used. An execution unit is 50 ms of CPU time. | Yes                                                                                                                                | [Learn More](#optimizing-execution-units)      |
| CPU Time        | The time your Edge Functions have spent computing responses to requests                                   | No                                                                                                                                 | [Learn More](#optimizing-cpu-time)             |

## Managing Functions invocations

You are charged based on the number of times your [functions](/docs/functions) are invoked, including both successful and errored response status codes, and excluding cache hits.

When viewing your Invocations graph, you can group by **Count** to see the total of all invocations across your team's projects.

### Optimizing Function invocations

- Use the **Projects** option to see the total number of invocations for each project within your team. This can help you identify which projects are using the most invocations and where to optimize.
- Cache your responses using [the CDN](/docs/cdn-cache#using-vercel-functions) and [Cache-Control headers](/docs/headers#cache-control-header). This reduces invocations and speeds up responses for users.

## Managing execution units

You are charged based on number of **execution units** that your Edge Functions have used. Each invocation of an Edge Function has a **Total CPU time**, which is the time spent running your code (it doesn't include execution time such as spent waiting for data fetches to return).

Each execution unit is 50ms. Vercel will work out the number of execution units (**total CPU time of the invocation / 50ms**) used for each invocation. You will then be charged based on anything over the limit.

For example:

- If your function gets invoked *250,000* times and uses *350* ms of CPU time at each invocation, then the function will incur **(350 ms / 50 ms) = 7** execution units each time the function gets invoked.
- Your usage is: 250,000 \* 7 = **1,750,000** execution units
  Pro users have 1,000,000 execution units included in their plan, so you will be charged for the additional 750,000 execution units. The cost is $2000000.00 for each additional 1,000,000 execution units.

### Optimizing execution units

- Execution units are comprised of a calculation of invocation count and CPU time. You can optimize your Edge Functions by [reducing the number of invocations](/docs/functions/runtimes/edge/edge-functions#optimizing-function-invocations) through caching and the [CPU time](#optimizing-cpu-time) used per invocation.

## Managing CPU time

There is no time limit on the amount of CPU time your Edge Function can use during a single invocation. However, you are charged for each [execution unit](/docs/limits/usage#execution-units), which is based on the compute time. The compute time refers to the actual net CPU time used, not the execution time. Operations such as network access do not count towards the CPU time.

You can view CPU time by **Average** to show the average time for computation across all projects using Edge Functions within your team. This data point provides an idea of how long your Edge Functions are taking to compute responses to requests and can be used in combination with the invocation count to calculate execution units.

### Optimizing CPU time

- View the CPU time by **Project** to understand which Projects are using the most CPU time
- CPU time is calculated based on the actual time your function is running, not the time it takes to respond to a request. Therefore you should optimize your code to ensure it's as performant as possible and avoid heavy CPU-bound operations


