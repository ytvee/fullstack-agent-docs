---
id: "vercel-0264"
title: "NEXTJS_UNNEEDED_GET_SERVER_SIDE_PROPS"
description: "Catches usages of getServerSideProps that could use static rendering instead, improving the performance of those pages."
category: "vercel-conformance"
subcategory: "conformance"
type: "concept"
source: "https://vercel.com/docs/conformance/rules/NEXTJS_UNNEEDED_GET_SERVER_SIDE_PROPS"
tags: ["nextjs", "unneeded", "get", "server", "side", "props"]
related: ["0256-nextjs-no-get-initial-props.md", "0255-nextjs-no-fetch-in-server-props.md", "0242-eslint-next-rules-required.md"]
last_updated: "2026-04-03T23:47:18.229Z"
---

# NEXTJS_UNNEEDED_GET_SERVER_SIDE_PROPS

> **🔒 Permissions Required**: Conformance

This rule will analyze each Next.js page's `getServerSideProps` to see if the context parameter is being used and if not
then it will fail.

When using `getServerSideProps` to render a Next.js page on the server, if the page doesn't require any information
from the request, consider using [SSG](https://nextjs.org/docs/basic-features/data-fetching/get-static-props) with
`getStaticProps`. If you are using `getServerSideProps` to refresh the data on each page load, consider using
[ISR](https://nextjs.org/docs/basic-features/data-fetching/incremental-static-regeneration) instead with a `revalidate`
property to control how often the page is regenerated. If you are using `getServerSideProps` to randomize the data on
each page load, consider moving that logic to the client instead and use `getStaticProps` to reuse the statically generated
page.

## Example

An example of when this check would fail:

```tsx filename="src/pages/index.tsx"
import { type GetServerSideProps } from 'next';

export const getServerSideProps: GetServerSideProps = async () => {
  const res = await fetch('https://api.github.com/repos/vercel/next.js');
  const json = await res.json();
  return {
    props: { stargazersCount: json.stargazers_count },
  };
};

function Home({ stargazersCount }) {
  return <h1>The Next.js repo has {stargazersCount} stars.</h1>;
}

export default Home;
```

In this example, the `getServerSideProps` function is used to pass data from an API to the page,
but it isn't using any information from the context argument so `getServerSideProps` is unnecessary.

## How to fix

Instead, we can convert the page to use [SSG](https://nextjs.org/docs/basic-features/data-fetching/get-static-props)
with `getStaticProps`. This will generate the page at build time and serve it statically. If you need the page to
be updated more frequently, then you can also use [ISR](https://nextjs.org/docs/basic-features/data-fetching/incremental-static-regeneration)
with the revalidate option:

```tsx filename="src/pages/index.tsx"
import { type GetStaticProps } from 'next';

export const getStaticProps: GetStaticProps = async () => {
  const res = await fetch('https://api.github.com/repos/vercel/next.js');
  const json = await res.json();
  return {
    props: { stargazersCount: json.stargazers_count },
    revalidate: 60, // Using ISR, regenerate the page every 60 seconds
  };
};

function Home({ stargazersCount }) {
  return <h1>The Next.js repo has {stargazersCount} stars.</h1>;
}

export default Home;
```

Or, you can use information from the context argument to customize the page:

```tsx filename="src/pages/index.tsx"
import { type GetServerSideProps } from 'next';

export const getServerSideProps: GetServerSideProps = async (context) => {
  const res = await fetch(
    `https://api.github.com/repos/vercel/${context.query.repoName}`,
  );
  const json = await res.json();
  return {
    props: {
      repoName: context.query.repoName,
      stargazersCount: json.stargazers_count,
    },
  };
};

function Home({ repoName, stargazersCount }) {
  return (
    <h1>
      The {repoName} repo has {stargazersCount} stars.
    </h1>
  );
}

export default Home;
```


