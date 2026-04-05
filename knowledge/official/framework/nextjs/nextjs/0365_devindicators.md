---
title: devIndicators
description: "Optimized pages include an indicator to let you know if it's being statically optimized. You can opt-out of it here."
url: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/devIndicators"
version: 16.2.2
router: Pages Router
---

# devIndicators

`devIndicators` allows you to configure the on-screen indicator that gives context about the current route you're viewing during development.

```ts filename="Types"
  devIndicators: false | {
    position?: 'bottom-right'
    | 'bottom-left'
    | 'top-right'
    | 'top-left', // defaults to 'bottom-left',
  },
```

Setting `devIndicators` to `false` will hide the indicator, however Next.js will continue to surface any build or runtime errors that were encountered.

## Troubleshooting

### Indicator not marking a route as static

If you expect a route to be static and the indicator has marked it as dynamic, it's likely the route has opted out of prerendering.

You can confirm if a route is [prerendered](/docs/app/glossary#prerendering) or [dynamically rendered](/docs/app/glossary#dynamic-rendering) by building your application using `next build --debug`, and checking the output in your terminal. Static (or prerendered) routes will display a `○` symbol, whereas dynamic routes will display a `ƒ` symbol. For example:

```bash filename="Build Output"
Route (app)
┌ ○ /_not-found
└ ƒ /products/[id]

○  (Static)   prerendered as static content
ƒ  (Dynamic)  server-rendered on demand
```

When exporting [`getServerSideProps`](/docs/pages/building-your-application/data-fetching/get-server-side-props) or [`getInitialProps`](/docs/pages/api-reference/functions/get-initial-props) from a page, it will be marked as dynamic.

## Version History

| Version   | Changes                                                                                                                                             |
| --------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `v16.0.0` | `appIsrStatus`, `buildActivity`, and `buildActivityPosition` options have been removed.                                                             |
| `v15.2.0` | Improved on-screen indicator with new `position` option. `appIsrStatus`, `buildActivity`, and `buildActivityPosition` options have been deprecated. |
| `v15.0.0` | Static on-screen indicator added with `appIsrStatus` option.                                                                                        |


