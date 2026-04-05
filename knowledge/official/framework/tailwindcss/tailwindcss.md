# React documentation sources


---

## Source: src/docs/detecting-classes-in-source-files.mdx

import { TipGood, TipBad, TipInfo } from "@/components/tips";
import { Iframe } from "@/components/iframe";
import { Example } from "@/components/example";
import { Figure } from "@/components/figure";
import { CodeExampleStack } from "@/components/code-example";

export const title = "Detecting classes in source files";
export const description = "Understanding and customizing how Tailwind scans your source files.";

## Overview

Tailwind works by scanning your project for utility classes, then generating all of the necessary CSS based on the classes you've actually used.

This makes sure your CSS is as small as possible, and is also what makes features like [arbitrary values](/docs/adding-custom-styles#using-arbitrary-values) possible.

### How classes are detected

Tailwind treats all of your source files as plain text, and doesn't attempt to actually parse your files as code in any way.

Instead it just looks for any tokens in your file that could be classes based on which characters Tailwind is expecting in class names:

```jsx
// [!code filename:JSX]
// [!code word:bg-blue-500]
// [!code word:rounded-full]
// [!code word:text-white]
// [!code word:text-black]
// [!code word:font-medium]
// [!code word:text-sm\/6]
// [!code word:font-sans]
// [!code word:bg-black]
// [!code word:bg-white]
// [!code word:className]
// [!code word:function]
// [!code word:children]
// [!code word:button]
// [!code word:shadow]
// [!code word:export]
// [!code word:colors]
// [!code word:color]
// [!code word:black]
// [!code word:white]
// [!code word:const]
// [!code word:blue]
// [!code word:return]
// [!code word:py-1.5]
// [!code word:px-2]
export function Button({ color, children }) {
  const colors = {
    black: "bg-black text-white",
    blue: "bg-blue-500 text-white",
    white: "bg-white text-black",
  };

  return (
    <button className={`${colors[color]} rounded-full px-2 py-1.5 font-sans text-sm/6 font-medium shadow`}>
      {children}
    </button>
  );
}
```

Then it tries to generate the CSS for all of these tokens, throwing away any tokens that don't map to a utility class the framework knows about.

### Dynamic class names

Since Tailwind scans your source files as plain text, it has no way of understanding string concatenation or interpolation in the programming language you're using.

<TipBad>{<>Don't construct class names dynamically</>}</TipBad>

```html
<!-- [!code filename:HTML] -->
<div class="text-{{ error ? 'red' : 'green' }}-600"></div>
```

In the example above, the strings `text-red-600` and `text-green-600` do not exist, so Tailwind will not generate those classes.

Instead, make sure any class names you’re using exist in full:

<TipGood>{<>Always use complete class names</>}</TipGood>

```html
<!-- [!code filename:HTML] -->
<!-- [!code word:text-red-600] -->
<!-- [!code word:text-green-600] -->
<div class="{{ error ? 'text-red-600' : 'text-green-600' }}"></div>
```

If you're using a component library like React or Vue, this means you shouldn't use props to dynamically construct classes:

<TipBad>Don't use props to build class names dynamically</TipBad>

```jsx
// [!code filename:JSX]
function Button({ color, children }) {
  return <button className={`bg-${color}-600 hover:bg-${color}-500 ...`}>{children}</button>;
}
```

Instead, map props to complete class names that are statically detectable at build-time:

<TipGood>Always map props to static class names</TipGood>

```jsx
// [!code filename:JSX]
function Button({ color, children }) {
  const colorVariants = {
    blue: "bg-blue-600 hover:bg-blue-500",
    red: "bg-red-600 hover:bg-red-500",
  };

  return <button className={`${colorVariants[color]} ...`}>{children}</button>;
}
```

This has the added benefit of letting you map different prop values to different color shades for example:

```jsx
// [!code filename:JSX]
function Button({ color, children }) {
  const colorVariants = {
    blue: "bg-blue-600 hover:bg-blue-500 text-white",
    red: "bg-red-500 hover:bg-red-400 text-white",
    yellow: "bg-yellow-300 hover:bg-yellow-400 text-black",
  };

  return <button className={`${colorVariants[color]} ...`}>{children}</button>;
}
```

As long as you always use complete class names in your code, Tailwind will generate all of your CSS perfectly every time.

### Which files are scanned

Tailwind will scan every file in your project for class names, except in the following cases:

- Files that are in your `.gitignore` file
- Files in the `node_modules` directory
- Binary files like images, videos, or zip files
- CSS files
- Common package manager lock files

If you need to scan any files that Tailwind is ignoring by default, you can [explicitly register](#explicitly-registering-sources) those sources.

## Explicitly registering sources

Use `@source` to explicitly register source paths relative to the stylesheet:

```css
/* [!code filename:CSS] */
@import "tailwindcss";
/* [!code highlight:2] */
@source "../node_modules/@acmecorp/ui-lib";
```

This is especially useful when you need to scan an external library that is built with Tailwind, since dependencies are usually listed in your `.gitignore` file and ignored by Tailwind by default.

### Setting your base path

Tailwind uses the current working directory as its starting point when scanning for class names by default.

To set the base path for source detection explicitly, use the `source()` function when importing Tailwind in your CSS:

```css
/* [!code filename:CSS] */
/* [!code word:source("../src")] */
@import "tailwindcss" source("../src");
```

This can be useful when working with monorepos where your build commands run from the root of the monorepo instead of the root of each project.

### Ignoring specific paths

Use `@source not` to ignore specific paths, relative to the stylesheet, when scanning for class names:

```css
/* [!code filename:CSS] */
@import "tailwindcss";
/* [!code highlight:2] */
@source not "../src/components/legacy";
```

This is useful when you have large directories in your project that you know don't use Tailwind classes, like legacy components or third-party libraries.

### Disabling automatic detection

Use `source(none)` to completely disable automatic source detection if you want to register all of your sources explicitly:

```css
/* [!code filename:CSS] */
/* [!code word:source("../src")] */
@import "tailwindcss" source(none);

@source "../admin";
@source "../shared";
```

This can be useful in projects that have multiple Tailwind stylesheets where you want to make sure each one only includes the classes each stylesheet needs.

## Safelisting specific utilities

If you need to make sure Tailwind generates certain class names that don’t exist in your content files, use `@source inline()` to force them to be generated:

<CodeExampleStack>
```css
/* [!code filename:CSS] */
@import "tailwindcss";
/* [!code highlight:2] */
@source inline("underline");
```

```css
/* [!code filename:Generated CSS] */
.underline {
  text-decoration-line: underline;
}
```

</CodeExampleStack>

### Safelisting variants

You can also use `@source inline()` to generate classes with variants. For example, to generate the `underline` class with hover and focus variants, add `{hover:,focus:,}` to the source input:

<CodeExampleStack>
```css
/* [!code filename:CSS] */
@import "tailwindcss";
/* [!code highlight:2] */
@source inline("{hover:,focus:,}underline");
```

```css
/* [!code filename:Generated CSS] */
.underline {
  text-decoration-line: underline;
}
@media (hover: hover) {
  .hover\:underline:hover {
    text-decoration-line: underline;
  }
}
@media (focus: focus) {
  .focus\:underline:focus {
    text-decoration-line: underline;
  }
}
```

</CodeExampleStack>

### Safelisting with ranges

The source input is [brace expanded](https://www.gnu.org/software/bash/manual/html_node/Brace-Expansion.html), so you can generate multiple classes at once. For example, to generate all the red background colors with hover variants, use a range:

<CodeExampleStack>
```css
/* [!code filename:CSS] */
@import "tailwindcss";
/* [!code highlight:2] */
@source inline("{hover:,}bg-red-{50,{100..900..100},950}");
```

```css
/* [!code filename:Generated CSS] */
.bg-red-50 {
  background-color: var(--color-red-50);
}
.bg-red-100 {
  background-color: var(--color-red-100);
}
.bg-red-200 {
  background-color: var(--color-red-200);
}

/* ... */

.bg-red-800 {
  background-color: var(--color-red-800);
}
.bg-red-900 {
  background-color: var(--color-red-900);
}
.bg-red-950 {
  background-color: var(--color-red-950);
}
@media (hover: hover) {
  .hover\:bg-red-50:hover {
    background-color: var(--color-red-50);
  }

  /* ... */

  .hover\:bg-red-950:hover {
    background-color: var(--color-red-950);
  }
}
```

</CodeExampleStack>

This generates red background colors from 100 to 900 in increments of 100, along with the first and last shades of 50 and 950. It also adds the `hover:` variant for each of those classes.

### Explicitly excluding classes

Use `@source not inline()` to prevent specific classes from being generated, even if they are detected in your source files:

```css
/* [!code filename:CSS] */
@import "tailwindcss";
/* [!code highlight:2] */
@source not inline("{hover:,focus:,}bg-red-{50,{100..900..100},950}");
```

This will explicitly exclude the red background utilities, along with their hover and focus variants, from being generated.


---

## Source: src/docs/styling-with-utility-classes.mdx

import { Example } from "@/components/example";
import { CodeExampleWrapper, CodeExampleStack } from "@/components/code-example";
import { Iframe } from "@/components/iframe.tsx";
import { Figure } from "@/components/figure";
import { TipGood, TipBad, TipCompat, TipInfo } from "@/components/tips";
import { MultiCursorAnimation, MultiCursorPreview } from "@/components/multi-cursor/animation.tsx";
import { MultiCursorCode } from "@/components/multi-cursor/example.tsx";
import erinLindford from "./img/erin-lindford.jpg";

export const title = "Styling with utility classes";
export const description = "Building complex components from a constrained set of primitive utilities.";

## Overview

You style things with Tailwind by combining many single-purpose presentational classes _(utility classes)_ directly in your markup:

<Figure>

<Example>
  {
    <div className="mx-auto flex max-w-sm items-center gap-x-4 rounded-xl bg-white p-6 shadow-lg outline outline-black/5 dark:bg-slate-800 dark:shadow-none dark:-outline-offset-1 dark:outline-white/10">
      <svg className="size-12 shrink-0" viewBox="0 0 40 40">
        <defs>
          <linearGradient x1="50%" y1="0%" x2="50%" y2="100%" id="a">
            <stop stopColor="#2397B3" offset="0%"></stop>
            <stop stopColor="#13577E" offset="100%"></stop>
          </linearGradient>
          <linearGradient x1="50%" y1="0%" x2="50%" y2="100%" id="b">
            <stop stopColor="#73DFF2" offset="0%"></stop>
            <stop stopColor="#47B1EB" offset="100%"></stop>
          </linearGradient>
        </defs>
        <g fill="none" fillRule="evenodd">
          <path
            d="M28.872 22.096c.084.622.128 1.258.128 1.904 0 7.732-6.268 14-14 14-2.176 0-4.236-.496-6.073-1.382l-6.022 2.007c-1.564.521-3.051-.966-2.53-2.53l2.007-6.022A13.944 13.944 0 0 1 1 24c0-7.331 5.635-13.346 12.81-13.95A9.967 9.967 0 0 0 13 14c0 5.523 4.477 10 10 10a9.955 9.955 0 0 0 5.872-1.904z"
            fill="url(#a)"
            transform="translate(1 1)"
          ></path>
          <path
            d="M35.618 20.073l2.007 6.022c.521 1.564-.966 3.051-2.53 2.53l-6.022-2.007A13.944 13.944 0 0 1 23 28c-7.732 0-14-6.268-14-14S15.268 0 23 0s14 6.268 14 14c0 2.176-.496 4.236-1.382 6.073z"
            fill="url(#b)"
            transform="translate(1 1)"
          ></path>
          <path
            d="M18 17a2 2 0 1 0 0-4 2 2 0 0 0 0 4zM24 17a2 2 0 1 0 0-4 2 2 0 0 0 0 4zM30 17a2 2 0 1 0 0-4 2 2 0 0 0 0 4z"
            fill="#FFF"
          ></path>
        </g>
      </svg>
      <div>
        <div className="text-xl font-medium text-black dark:text-white">ChitChat</div>
        <p className="text-gray-500 dark:text-gray-400">You have a new message!</p>
      </div>
    </div>
  }
</Example>

```html
<!-- prettier-ignore -->
<div class="mx-auto flex max-w-sm items-center gap-x-4 rounded-xl bg-white p-6 shadow-lg outline outline-black/5 dark:bg-slate-800 dark:shadow-none dark:-outline-offset-1 dark:outline-white/10">
  <img class="size-12 shrink-0" src="/img/logo.svg" alt="ChitChat Logo" />
  <div>
    <div class="text-xl font-medium text-black dark:text-white">ChitChat</div>
    <p class="text-gray-500 dark:text-gray-400">You have a new message!</p>
  </div>
</div>
```

</Figure>

For example, in the UI above we've used:

- The [display](/docs/display#flex) and [padding](/docs/padding) utilities (`flex`, `shrink-0`, and `p-6`) to control the overall layout
- The [max-width](/docs/max-width) and [margin](/docs/margin) utilities (`max-w-sm` and `mx-auto`) to constrain the card width and center it horizontally
- The [background-color](/docs/background-color), [border-radius](/docs/border-radius), and [box-shadow](/docs/box-shadow) utilities (`bg-white`, `rounded-xl`, and `shadow-lg`) to style the card's appearance
- The [width](/docs/width) and [height](/docs/height) utilities (`size-12`) to set the width and height of the logo image
- The [gap](/docs/gap) utilities (`gap-x-4`) to handle the spacing between the logo and the text
- The [font-size](/docs/font-size), [color](/docs/text-color), and [font-weight](/docs/font-weight) utilities (`text-xl`, `text-black`, `font-medium`, etc.) to style the card text

Styling things this way contradicts a lot of traditional best practices, but once you try it you'll quickly notice some really important benefits:

- **You get things done faster** — you don't spend any time coming up with class names, making decisions about selectors, or switching between HTML and CSS files, so your designs come together very fast.
- **Making changes feels safer** — adding or removing a utility class to an element only ever affects that element, so you never have to worry about accidentally breaking something another page that's using the same CSS.
- **Maintaining old projects is easier** — changing something just means finding that element in your project and changing the classes, not trying to remember how all of that custom CSS works that you haven't touched in six months.
- **Your code is more portable** — since both the structure and styling live in the same place, you can easily copy and paste entire chunks of UI around, even between different projects.
- **Your CSS stops growing** — since utility classes are so reusable, your CSS doesn't continue to grow linearly with every new feature you add to a project.

These benefits make a big difference on small projects, but they are even more valuable for teams working on long-running projects at scale.

### Why not just use inline styles?

A common reaction to this approach is wondering, “isn’t this just inline styles?” and in some ways it is — you’re applying styles directly to elements instead of assigning them a class name and then styling that class.

But using utility classes has many important advantages over inline styles, for example:

- **Designing with constraints** — using inline styles, every value is a magic number. With utilities, you’re choosing styles from a [predefined design system](/docs/theme), which makes it much easier to build visually consistent UIs.
- **Hover, focus, and other states** — inline styles can’t target states like hover or focus, but Tailwind’s [state variants](/docs/hover-focus-and-other-states) make it easy to style those states with utility classes.
- **Media queries** — you can’t use media queries in inline styles, but you can use Tailwind’s [responsive variants](/docs/responsive-design) to build fully responsive interfaces easily.

This component is fully responsive and includes a button with hover and active styles, and is built entirely with utility classes:

<Figure>

<Example resizable>
  {
    <div className="mx-auto max-w-sm space-y-2 rounded-xl bg-white px-8 py-8 shadow-lg ring ring-black/5 @sm:flex @sm:items-center @sm:space-y-0 @sm:gap-x-6 @sm:py-4">
      <img
        className="mx-auto block h-24 rounded-full @sm:mx-0 @sm:shrink-0"
        src={erinLindford.src}
        alt="Woman's Face"
      />
      <div className="space-y-2 text-center @sm:text-left">
        <div className="space-y-0.5">
          <p className="text-lg font-semibold text-black">Erin Lindford</p>
          <p className="font-medium text-gray-500">Product Engineer</p>
        </div>
        <button className="rounded-full border border-purple-200 px-4 py-1 text-sm font-semibold text-purple-600 hover:border-transparent hover:bg-purple-600 hover:text-white active:bg-purple-700">
          Message
        </button>
      </div>
    </div>
  }
</Example>

```html
<!-- [!code classes:sm:flex-row,sm:py-4,sm:gap-6,sm:mx-0,sm:shrink-0,sm:text-left,sm:items-center] -->
<!-- [!code classes:hover:text-white,hover:bg-purple-600,hover:border-transparent,active:bg-purple-700] -->
<div class="flex flex-col gap-2 p-8 sm:flex-row sm:items-center sm:gap-6 sm:py-4 ...">
  <img class="mx-auto block h-24 rounded-full sm:mx-0 sm:shrink-0" src="/img/erin-lindford.jpg" alt="" />
  <div class="space-y-2 text-center sm:text-left">
    <div class="space-y-0.5">
      <p class="text-lg font-semibold text-black">Erin Lindford</p>
      <p class="font-medium text-gray-500">Product Engineer</p>
    </div>
    <!-- prettier-ignore -->
    <button class="border-purple-200 text-purple-600 hover:border-transparent hover:bg-purple-600 hover:text-white active:bg-purple-700 ...">
      Message
    </button>
  </div>
</div>
```

</Figure>

## Thinking in utility classes

### Styling hover and focus states

To style an element on states like hover or focus, prefix any utility with the state you want to target, for example `hover:bg-sky-700`:

<Figure hint="Hover over this button to see the background color change">

<Example>
  {
    <div className="grid place-items-center">
      <button className="rounded-full bg-sky-500 px-5 py-2 text-sm leading-5 font-semibold text-white hover:bg-sky-700">
        Save changes
      </button>
    </div>
  }
</Example>

```html
<!-- [!code word:hover\:bg-sky-700] -->
<button class="bg-sky-500 hover:bg-sky-700 ...">Save changes</button>
```

</Figure>

These prefixes are called [variants](/docs/hover-focus-and-other-states) in Tailwind, and they only apply the styles from a utility class when the condition for that variant matches.

Here's what the generated CSS looks like for the `hover:bg-sky-700` class:

```css
/* [!code filename: Generated CSS] */
.hover\:bg-sky-700 {
  &:hover {
    background-color: var(--color-sky-700);
  }
}
```

Notice how this class does nothing _unless_ the element is hovered? Its _only_ job is to provide hover styles — nothing else.

This is different from how you'd write traditional CSS, where a single class would usually provide the styles for many states:

```html
/* [!code filename:HTML] */
<button class="btn">Save changes</button>

<style>
  .btn {
    background-color: var(--color-sky-500);
    &:hover {
      background-color: var(--color-sky-700);
    }
  }
</style>
```

You can even stack variants in Tailwind to apply a utility when multiple conditions match, like combining `hover:` and `disabled:`

```html
<!-- [!code classes:disabled:hover:bg-sky-500] -->
<button class="bg-sky-500 disabled:hover:bg-sky-500 ...">Save changes</button>
```

Learn more in the documentation styling elements on [hover, focus, and other states](/docs/hover-focus-and-other-states).

### Media queries and breakpoints

Just like hover and focus states, you can style elements at different breakpoints by prefixing any utility with the breakpoint where you want that style to apply:

<Figure hint="Resize this example to see the layout change">

<Example className="@container" resizable>
  {
    <div className="grid grid-cols-2 gap-4 text-center font-mono font-medium text-white @sm:grid-cols-3">
      <div className="rounded-lg bg-sky-500 p-4">01</div>
      <div className="rounded-lg bg-sky-500 p-4">02</div>
      <div className="rounded-lg bg-sky-500 p-4">03</div>
      <div className="rounded-lg bg-sky-500 p-4">04</div>
      <div className="rounded-lg bg-sky-500 p-4">05</div>
      <div className="rounded-lg bg-sky-500 p-4">06</div>
    </div>
  }
</Example>

```html
<!-- [!code classes:sm:grid-cols-3] -->
<div class="grid grid-cols-2 sm:grid-cols-3">
  <!-- ... -->
</div>
```

</Figure>

In the example above, the `sm:` prefix makes sure that `grid-cols-3` only triggers at the `sm` breakpoint and above, which is 40rem out of the box:

```css
/* [!code filename: Generated CSS] */
.sm\:grid-cols-3 {
  @media (width >= 40rem) {
    grid-template-columns: repeat(3, minmax(0, 1fr));
  }
}
```

Learn more in the [responsive design](/docs/responsive-design) documentation.

### Targeting dark mode

Styling an element in dark mode is just a matter of adding the `dark:` prefix to any utility you want to apply when dark mode is active:

<Figure>

<Example padding={false}>
  {
    <div className="grid grid-cols-1 sm:grid-cols-2">
      <div className="p-8 pt-7">
        <p className="mb-2 text-sm font-medium text-gray-500">Light mode</p>
        <div className="rounded-lg bg-white px-6 py-8 shadow-xl ring ring-gray-900/5">
          <div>
            <span className="inline-flex items-center justify-center rounded-md bg-indigo-500 p-2 shadow-lg">
              <svg
                className="h-6 w-6 text-white"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
                aria-hidden="true"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth="2"
                  d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"
                />
              </svg>
            </span>
          </div>
          <p className="mt-5 text-base font-medium tracking-tight text-gray-900">Writes upside-down</p>
          <p
            className="mt-2 text-sm text-gray-500"
            children={`The Zero Gravity Pen can be used to write in any orientation,
          including upside-down. It even works in outer space.`}
          />
        </div>
      </div>
      <div className="bg-gray-900 p-8 pt-7">
        <p className="mb-2 text-sm font-medium text-gray-400">Dark mode</p>
        <div className="rounded-lg bg-gray-800 px-6 py-8 shadow-xl ring ring-gray-900/5">
          <div>
            <span className="inline-flex items-center justify-center rounded-md bg-indigo-500 p-2 shadow-lg">
              <svg
                className="h-6 w-6 text-white"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
                aria-hidden="true"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth="2"
                  d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"
                />
              </svg>
            </span>
          </div>
          <p className="mt-5 text-base font-medium tracking-tight text-white">Writes upside-down</p>
          <p
            className="mt-2 text-sm text-gray-400"
            children={`The Zero Gravity Pen can be used to write in any orientation,
          including upside-down. It even works in outer space.`}
          />
        </div>
      </div>
    </div>
  }
</Example>

```html
<!-- [!code word:dark\:bg-gray-800] -->
<!-- prettier-ignore -->
<div class="bg-white dark:bg-gray-800 rounded-lg px-6 py-8 ring shadow-xl ring-gray-900/5">
  <div>
    <span class="inline-flex items-center justify-center rounded-md bg-indigo-500 p-2 shadow-lg">
      <svg
        class="h-6 w-6 text-white"

        fill="none"
        viewBox="0 0 24 24"
        stroke="currentColor"
        aria-hidden="true"
      >
        <!-- ... -->
      </svg>
    </span>
  </div>
  <!-- prettier-ignore -->
  <!-- [!code word:dark\:text-white] -->
  <h3 class="text-gray-900 dark:text-white mt-5 text-base font-medium tracking-tight ">Writes upside-down</h3>
  <!-- prettier-ignore -->
  <!-- [!code word:dark\:text-gray-400] -->
  <p class="text-gray-500 dark:text-gray-400 mt-2 text-sm ">
    The Zero Gravity Pen can be used to write in any orientation, including upside-down. It even works in outer space.
  </p>
</div>
```

</Figure>

Just like with hover states or media queries, the important thing to understand is that a single utility class will never include _both_ the light and dark styles — you style things in dark mode by using multiple classes, one for the light mode styles and another for the dark mode styles.

```css
/* [!code filename: Generated CSS] */
.dark\:bg-gray-800 {
  @media (prefers-color-scheme: dark) {
    background-color: var(--color-gray-800);
  }
}
```

Learn more in the [dark mode](/docs/dark-mode) documentation.

### Using class composition

A lot of the time with Tailwind you'll even use multiple classes to build up the value for a single CSS property, for example adding multiple filters to an element:

```html
<!-- [!code filename:HTML] -->
<!-- [!code classes:blur-sm,grayscale] -->
<div class="blur-sm grayscale">
  <!-- ... -->
</div>
```

Both of these effects rely on the `filter` property in CSS, so Tailwind uses CSS variables to make it possible to compose these effects together:

```css
/* [!code filename:Generated CSS] */
.blur-sm {
  --tw-blur: blur(var(--blur-sm));
  filter: var(--tw-blur,) var(--tw-brightness,) var(--tw-grayscale,);
}
.grayscale {
  --tw-grayscale: grayscale(100%);
  filter: var(--tw-blur,) var(--tw-brightness,) var(--tw-grayscale,);
}
```

The generated CSS above is slightly simplified, but the trick here is that each utility sets a CSS variable just for the effect it's meant to apply. Then the `filter` property looks at all of these variables, falling back to nothing if the variable hasn't been set.

Tailwind uses this same approach for [gradients](/docs/background-image#adding-a-linear-gradient), [shadow colors](/docs/box-shadow#setting-the-shadow-color), [transforms](/docs/translate), and more.

### Using arbitrary values

Many utilities in Tailwind are driven by [theme variables](/docs/theme), like `bg-blue-500`, `text-xl`, and `shadow-md`, which map to your underlying color palette, type scale, and shadows.

When you need to use a one-off value outside of your theme, use the special square bracket syntax for specifying arbitrary values:

```html
<!-- [!code filename:HTML] -->
<!-- [!code classes:bg-[#316ff6]] -->
<!-- prettier-ignore -->
<button class="bg-[#316ff6] ...">
  Sign in with Facebook
</button>
```

This can be useful for one-off colors outside of your color palette _(like the Facebook blue above)_, but also when you need a complex custom value like a very specific grid:

```html
<!-- [!code filename:HTML] -->
<!-- [!code classes:grid-cols-[24rem_2.5rem_minmax(0,1fr)]] -->
<div class="grid grid-cols-[24rem_2.5rem_minmax(0,1fr)]">
  <!-- ... -->
</div>
```

It's also useful when you need to use CSS features like `calc()`, even if you are using your theme values:

```html
<!-- [!code filename:HTML] -->
<!-- [!code classes:max-h-[calc(100dvh-(--spacing(6)))]] -->
<div class="max-h-[calc(100dvh-(--spacing(6)))]">
  <!-- ... -->
</div>
```

There's even a syntax for generating completely arbitrary CSS including an arbitrary property name, which can be useful for setting CSS variables:

```html
<!-- [!code filename:HTML] -->
<!-- [!code classes:[--gutter-width:1rem],lg:[--gutter-width:2rem]] -->
<div class="[--gutter-width:1rem] lg:[--gutter-width:2rem]">
  <!-- ... -->
</div>
```

Learn more in the documentation on [using arbitrary values](/docs/adding-custom-styles#using-arbitrary-values).

#### How does this even work?

Tailwind CSS isn't one big static stylesheet like you might be used to with other CSS frameworks — it generates the CSS needed based on the classes you're actually using when you compile your CSS.

It does this by scanning all of the files in your project looking for any symbol that looks like it could be a class name:

```jsx
// [!code filename:Button.jsx]
// [!code word:px-4]
// [!code word:py-2]
// [!code word:rounded-md]
// [!code word:text-base]
// [!code word:px-5]
// [!code word:py-3]
// [!code word:rounded-lg]
// [!code word:text-lg]
// [!code word:font-bold]
export default function Button({ size, children }) {
  let sizeClasses = {
    md: "px-4 py-2 rounded-md text-base",
    lg: "px-5 py-3 rounded-lg text-lg",
  }[size];

  return (
    <button type="button" className={`font-bold ${sizeClasses}`}>
      {children}
    </button>
  );
}
```

After it's found all of the potential classes, Tailwind generates the CSS for each one and compiles it all into one stylesheet of just the styles you actually need.

Since the CSS is generated based on the class name, Tailwind can recognize classes using arbitrary values like `bg-[#316ff6]` and generate the necessary CSS, even when the value isn't part of your theme.

Learn more about how this works in [detecting classes in source files](/docs/detecting-classes-in-source-files).

### Complex selectors

Sometimes you need to style an element under a combination of conditions, for example in dark mode, at a specific breakpoint, when hovered, and when the element has a specific data attribute.

Here's an example of what that looks like with Tailwind:

<CodeExampleStack>

```html
<!-- [!code filename:HTML] -->
<!-- [!code classes:dark:lg:data-current:hover:bg-indigo-600] -->
<button class="dark:lg:data-current:hover:bg-indigo-600 ...">
  <!-- ... -->
</button>
```

```css
/* [!code filename:Simplified CSS] */
@media (prefers-color-scheme: dark) and (width >= 64rem) {
  button[data-current]:hover {
    background-color: var(--color-indigo-600);
  }
}
```

</CodeExampleStack>

Tailwind also supports things like `group-hover`, which let you style an element when a specific parent is hovered:

<CodeExampleStack>

```html
<!-- [!code filename:HTML] -->
<!-- [!code classes:group,group-hover:underline] -->
<a href="#" class="group rounded-lg p-8">
  <!-- ... -->
  <span class="group-hover:underline">Read more…</span>
</a>
```

```css
/* [!code filename:Simplified CSS] */
@media (hover: hover) {
  a:hover span {
    text-decoration-line: underline;
  }
}
```

</CodeExampleStack>

This `group-*` syntax works with other variants too, like `group-focus`, `group-active`, and [many more](/docs/hover-focus-and-other-states#styling-based-on-parent-state).

For really complex scenarios _(especially when styling HTML you don't control)_, Tailwind supports [arbitrary variants](/docs/adding-custom-styles#arbitrary-variants) which let you write any selector you want, directly in a class name:

<CodeExampleStack>

```html
<!-- [!code filename:HTML] -->
<!-- [!code classes:[&>[data-active]+span]:text-blue-600] -->
<div class="[&>[data-active]+span]:text-blue-600 ...">
  <span data-active><!-- ... --></span>
  <!-- [!code highlight:2] -->
  <span>This text will be blue</span>
</div>
```

```css
/* [!code filename:Simplified CSS] */
div > [data-active] + span {
  color: var(--color-blue-600);
}
```

</CodeExampleStack>

### When to use inline styles

Inline styles are still very useful in Tailwind CSS projects, particularly when a value is coming from a dynamic source like a database or API:

```jsx
// [!code filename:branded-button.jsx]
export function BrandedButton({ buttonColor, textColor, children }) {
  return (
    <button
      style={{
        // [!code highlight:3]
        backgroundColor: buttonColor,
        color: textColor,
      }}
      className="rounded-md px-3 py-1.5 font-medium"
    >
      {children}
    </button>
  );
}
```

You might also reach for an inline style for very complicated arbitrary values that are difficult to read when formatted as a class name:

```html
<!-- [!code filename:HTML] -->
<!-- prettier-ignore -->
<div class="grid-[2fr_max(0,var(--gutter-width))_calc(var(--gutter-width)+10px)]"> <!-- [!code --] -->
<!-- prettier-ignore -->
<div style="grid-template-columns: 2fr max(0, var(--gutter-width)) calc(var(--gutter-width) + 10px)"> <!-- [!code ++] -->
  <!-- ... -->
</div>
```

Another useful pattern is setting CSS variables based on dynamic sources using inline styles, then referencing those variables with utility classes:

```jsx
// [!code filename:branded-button.jsx]
export function BrandedButton({ buttonColor, buttonColorHover, textColor, children }) {
  return (
    <button
      style={{
        // [!code highlight:4]
        "--bg-color": buttonColor,
        "--bg-color-hover": buttonColorHover,
        "--text-color": textColor,
      }}
      // [!code classes:bg-(--bg-color),text-(--text-color),hover:bg-(--bg-color-hover)]
      className="bg-(--bg-color) text-(--text-color) hover:bg-(--bg-color-hover) ..."
    >
      {children}
    </button>
  );
}
```

## Managing duplication

When you build entire projects with just utility classes, you'll inevitably find yourself repeating certain patterns to recreate the same design in different places.

For example, here the utility classes for each avatar image are repeated five separate times:

<Figure>

<Example padding={false}>
  <div className="bg-white">
    <div className="mx-auto w-72 px-8 py-6 sm:w-96 sm:px-12 sm:py-8">
      <div className="flex items-center space-x-2 text-base">
        <h4 className="text-base font-semibold text-slate-900">Contributors</h4>
        <span className="rounded-full bg-slate-100 px-2 py-1 text-xs font-semibold text-slate-700">204</span>
      </div>
      <div className="mt-3 flex -space-x-2 overflow-hidden">
        <img
          className="inline-block h-12 w-12 rounded-full ring-2 ring-white"
          src="https://images.unsplash.com/photo-1491528323818-fdd1faba62cc?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80"
          alt=""
        />
        <img
          className="inline-block h-12 w-12 rounded-full ring-2 ring-white"
          src="https://images.unsplash.com/photo-1550525811-e5869dd03032?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80"
          alt=""
        />
        <img
          className="inline-block h-12 w-12 rounded-full ring-2 ring-white"
          src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2.25&w=256&h=256&q=80"
          alt=""
        />
        <img
          className="inline-block h-12 w-12 rounded-full ring-2 ring-white"
          src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80"
          alt=""
        />
        <img
          className="inline-block h-12 w-12 rounded-full ring-2 ring-white"
          src="https://images.unsplash.com/photo-1517365830460-955ce3ccd263?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80"
          alt=""
        />
      </div>
      <div className="mt-3 text-sm font-medium">
        <a href="#" className="text-blue-500">
          + 198 others
        </a>
      </div>
    </div>
  </div>
</Example>

```html
<!-- [!code classes:inline-block,h-12,w-12,rounded-full,ring-2,ring-white] -->
<div>
  <div class="flex items-center space-x-2 text-base">
    <h4 class="font-semibold text-slate-900">Contributors</h4>
    <span class="bg-slate-100 px-2 py-1 text-xs font-semibold text-slate-700 ...">204</span>
  </div>
  <div class="mt-3 flex -space-x-2 overflow-hidden">
    <!-- prettier-ignore -->
    <img class="inline-block h-12 w-12 rounded-full ring-2 ring-white" src="https://images.unsplash.com/photo-1491528323818-fdd1faba62cc?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="" />
    <!-- prettier-ignore -->
    <img class="inline-block h-12 w-12 rounded-full ring-2 ring-white" src="https://images.unsplash.com/photo-1550525811-e5869dd03032?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="" />
    <!-- prettier-ignore -->
    <img class="inline-block h-12 w-12 rounded-full ring-2 ring-white" src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2.25&w=256&h=256&q=80" alt="" />
    <!-- prettier-ignore -->
    <img class="inline-block h-12 w-12 rounded-full ring-2 ring-white" src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="" />
    <!-- prettier-ignore -->
    <img class="inline-block h-12 w-12 rounded-full ring-2 ring-white" src="https://images.unsplash.com/photo-1517365830460-955ce3ccd263?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="" />
  </div>
  <div class="mt-3 text-sm font-medium">
    <a href="#" class="text-blue-500">+ 198 others</a>
  </div>
</div>
```

</Figure>

Don't panic! In practice this isn't the problem you might be worried it is, and the strategies for dealing with it are things you already do every day.

### Using loops

A lot of the time a design element that shows up more than once in the rendered page is only actually authored once because the actual markup is rendered in a loop.

For example, the duplicate avatars at the beginning of this guide would almost certainly be rendered in a loop in a real project:

<Figure>

<Example padding={false}>
  <div className="bg-white">
    <div className="mx-auto w-72 px-8 py-6 sm:w-96 sm:px-12 sm:py-8">
      <div className="flex items-center space-x-2 text-base">
        <h4 className="text-base font-semibold text-slate-900">Contributors</h4>
        <span className="rounded-full bg-slate-100 px-2 py-1 text-xs font-semibold text-slate-700">204</span>
      </div>
      <div className="mt-3 flex -space-x-2 overflow-hidden">
        <img
          className="inline-block h-12 w-12 rounded-full ring-2 ring-white"
          src="https://images.unsplash.com/photo-1491528323818-fdd1faba62cc?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80"
          alt=""
        />
        <img
          className="inline-block h-12 w-12 rounded-full ring-2 ring-white"
          src="https://images.unsplash.com/photo-1550525811-e5869dd03032?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80"
          alt=""
        />
        <img
          className="inline-block h-12 w-12 rounded-full ring-2 ring-white"
          src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2.25&w=256&h=256&q=80"
          alt=""
        />
        <img
          className="inline-block h-12 w-12 rounded-full ring-2 ring-white"
          src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80"
          alt=""
        />
        <img
          className="inline-block h-12 w-12 rounded-full ring-2 ring-white"
          src="https://images.unsplash.com/photo-1517365830460-955ce3ccd263?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80"
          alt=""
        />
      </div>
      <div className="mt-3 text-sm font-medium">
        <a href="#" className="text-blue-500">
          + 198 others
        </a>
      </div>
    </div>
  </div>
</Example>

```svelte
<div>
  <div class="flex items-center space-x-2 text-base">
    <h4 class="font-semibold text-slate-900">Contributors</h4>
    <span class="bg-slate-100 px-2 py-1 text-xs font-semibold text-slate-700 ...">204</span>
  </div>
  <div class="mt-3 flex -space-x-2 overflow-hidden">
    <!-- prettier-ignore -->
    <!-- [!code highlight:4] -->
    {#each contributors as user}
      <img class="inline-block h-12 w-12 rounded-full ring-2 ring-white" src={user.avatarUrl} alt={user.handle} />
    {/each}
  </div>
  <div class="mt-3 text-sm font-medium">
    <a href="#" class="text-blue-500">+ 198 others</a>
  </div>
</div>
```

</Figure>

When elements are rendered in a loop like this, the actual class list is only written once so there's no actual duplication problem to solve.

### Using multi-cursor editing

When duplication is localized to a group of elements in a single file, the easiest way to deal with it is to use [multi-cursor editing](https://code.visualstudio.com/docs/editor/codebasics#_multiple-selections-multicursor) to quickly select and edit the class list for each element at once:

<MultiCursorAnimation>
  <Figure>
    <Example>
      <MultiCursorPreview />
    </Example>
    <CodeExampleWrapper>
      <MultiCursorCode />
    </CodeExampleWrapper>
  </Figure>
</MultiCursorAnimation>

You'd be surprised at how often this ends up being the best solution. If you can quickly edit all of the duplicated class lists simultaneously, there's no benefit to introducing any additional abstraction.

### Using components

If you need to reuse some styles across multiple files, the best strategy is to create a _component_ if you're using a front-end framework like React, Svelte, or Vue, or a _template partial_ if you're using a templating language like Blade, ERB, Twig, or Nunjucks.

<Figure>

<Example padding={false}>
<div className="bg-white">
  <div className="mx-auto w-72 bg-white px-8 py-6  sm:w-96 sm:px-12 sm:py-8">
    <div>
      <img
        className="rounded-lg"
        src="https://images.unsplash.com/photo-1452784444945-3f422708fe5e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=512&q=80"
        width="512"
        height="341"
        alt="Beach"
      />
      <div className="mt-4">
          <div className="text-xs font-bold text-sky-500">Private Villa</div>
          <div className="mt-1 font-bold text-gray-700">
            <a href="#" className="hover:underline">Relaxing All-Inclusive Resort in Cancun</a>
          </div>
          <div className="mt-2 text-sm text-gray-600">$299 USD per night</div>
      </div>
    </div>
  </div>
</div>

</Example>

```jsx {{ filename: 'VacationCard.jsx' }}
export function VacationCard({ img, imgAlt, eyebrow, title, pricing, url }) {
  return (
    <div>
      <img className="rounded-lg" src={img} alt={imgAlt} />
      <div className="mt-4">
        <div className="text-xs font-bold text-sky-500">{eyebrow}</div>
        <div className="mt-1 font-bold text-gray-700">
          <a href={url} className="hover:underline">
            {title}
          </a>
        </div>
        <div className="mt-2 text-sm text-gray-600">{pricing}</div>
      </div>
    </div>
  );
}
```

</Figure>

Now you can use this component in as many places as you like, while still having a single source of truth for the styles so they can easily be updated together in one place.

### Using custom CSS

If you're using a templating language like ERB or Twig instead of something like React or Vue, creating a template partial for something as small as a button can feel like overkill compared to a simple CSS class like `btn`.

While it's highly recommended that you create proper template partials for more complex components, writing some custom CSS is totally fine when a template partial feels heavy-handed.

Here's what a `btn-primary` class might look like, using [theme variables](/docs/theme#with-custom-css) to keep the design consistent:

<Figure>

<Example>

<div className="text-center">
  <button
    type="button"
    className="rounded-full bg-violet-500 px-5 py-2 font-semibold text-white shadow-md hover:bg-violet-700"
  >
    Save changes
  </button>
</div>

</Example>

<CodeExampleStack>

```html
<!-- [!code filename:HTML] -->
<button class="btn-primary">Save changes</button>
```

```css
/* [!code filename:CSS] */
@import "tailwindcss";

@layer components {
  .btn-primary {
    border-radius: calc(infinity * 1px);
    background-color: var(--color-violet-500);
    padding-inline: --spacing(5);
    padding-block: --spacing(2);
    font-weight: var(--font-weight-semibold);
    color: var(--color-white);
    box-shadow: var(--shadow-md);
    &:hover {
      @media (hover: hover) {
        background-color: var(--color-violet-700);
      }
    }
  }
}
```

</CodeExampleStack>

</Figure>

Again though, for anything that's more complicated than just a single HTML element, we highly recommend using template partials so the styles and structure can be encapsulated in one place.

## Managing style conflicts

### Conflicting utility classes

When you add two classes that target the same CSS property, the class that appears later in the stylesheet wins. So in this example, the element will receive `display: grid` even though `flex` comes last in the actual `class` attribute:

<CodeExampleStack>

```html
<!-- [!code filename:HTML] -->
<!-- prettier-ignore -->
<div class="grid flex">
  <!-- ... -->
</div>
```

```css
/* [!code filename: CSS] */
.flex {
  display: flex;
}
.grid {
  display: grid;
}
```

</CodeExampleStack>

In general, you should just never add two conflicting classes to the same element — only ever add the one you actually want to take effect:

```jsx
// [!code filename:example.jsx]
// [!code word:gridLayout\ \?\ \"grid\"\ \:\ \"flex\"]
export function Example({ gridLayout }) {
  return <div className={gridLayout ? "grid" : "flex"}>{/* ... */}</div>;
}
```

Using component-based libraries like React or Vue, this often means exposing specific props for styling customizations instead of letting consumers add extra classes from outside of a component, since those styles will often conflict.

### Using the important modifier

When you really need to force a specific utility class to take effect and have no other means of managing the specificity, you can add `!` to the end of the class name to make all of the declarations `!important`:

<CodeExampleStack>

```html
<!-- [!code filename:HTML] -->
<!-- [!code classes:bg-red-500!] -->
<!-- prettier-ignore -->
<div class="bg-teal-500 bg-red-500!">
  <!-- ... -->
</div>
```

```css
/* [!code filename: Generated CSS] */
/* [!code word:!important] */
.bg-red-500\! {
  background-color: var(--color-red-500) !important;
}
.bg-teal-500 {
  background-color: var(--color-teal-500);
}
```

</CodeExampleStack>

### Using the important flag

If you're adding Tailwind to a project that has existing complex CSS with high specificity rules, you can use the `important` flag when importing Tailwind to mark _all_ utilities as `!important`:

<CodeExampleStack>

```css
/* [!code filename:app.css] */
/* [!code word:important] */
@import "tailwindcss" important;
```

```css
/* [!code filename:Compiled CSS] */
/* [!code word:!important] */
@layer utilities {
  .flex {
    display: flex !important;
  }
  .gap-4 {
    gap: 1rem !important;
  }
  .underline {
    text-decoration-line: underline !important;
  }
}
```

</CodeExampleStack>

### Using the prefix option

If your project has class names that conflict with Tailwind CSS utilities, you can prefix all Tailwind-generated classes and CSS variables using the `prefix` option:

<CodeExampleStack>

```css
/* [!code filename:app.css] */
/* [!code word:important] */
@import "tailwindcss" prefix(tw);
```

```css
/* [!code filename:Compiled CSS] */
/* [!code word:tw\:] */
@layer theme {
  :root {
    --tw-color-red-500: oklch(0.637 0.237 25.331);
  }
}

@layer utilities {
  .tw\:text-red-500 {
    color: var(--tw-color-red-500);
  }
}
```

</CodeExampleStack>


---

## Source: src/docs/theme.mdx

import { CodeExampleStack } from "@/components/code-example";
import { TipGood, TipBad, TipInfo } from "@/components/tips";
import { Iframe } from "@/components/iframe";
import { Example } from "@/components/example";
import { Figure } from "@/components/figure";

export const title = "Theme variables";
export const description = "Using utility classes as an API for your design tokens.";

## Overview

Tailwind is a framework for building custom designs, and different designs need different typography, colors, shadows, breakpoints, and more.

These low-level design decisions are often called _design tokens_, and in Tailwind projects you store those values in _theme variables_.

### What are theme variables?

Theme variables are special CSS variables defined using the `@theme` directive that influence which utility classes exist in your project.

For example, you can add a new color to your project by defining a theme variable like `--color-mint-500`:

```css
/* [!code filename:app.css] */
@import "tailwindcss";

/* [!code highlight:4] */
@theme {
  --color-mint-500: oklch(0.72 0.11 178);
}
```

Now you can use utility classes like `bg-mint-500`, `text-mint-500`, or `fill-mint-500` in your HTML:

```html
<!-- [!code filename:HTML] -->
<!-- [!code word:bg-mint-500] -->
<div class="bg-mint-500">
  <!-- ... -->
</div>
```

Tailwind also generates regular CSS variables for your theme variables so you can reference your design tokens in arbitrary values or inline styles:

```html
<!-- [!code filename:HTML] -->
<!-- [!code word:var(--color-mint-500)] -->
<div style="background-color: var(--color-mint-500)">
  <!-- ... -->
</div>
```

Learn more about how theme variables map to different utility classes in the [theme variable namespaces](#theme-variable-namespaces) documentation.

#### Why `@theme` instead of `:root`?

Theme variables aren't _just_ CSS variables — they also instruct Tailwind to create new utility classes that you can use in your HTML.

Since they do more than regular CSS variables, Tailwind uses special syntax so that defining theme variables is always explicit. Theme variables are also required to be defined top-level and not nested under other selectors or media queries, and using a special syntax makes it possible to enforce that.

Defining regular CSS variables with `:root` can still be useful in Tailwind projects when you want to define a variable that isn't meant to be connected to a utility class. Use `@theme` when you want a design token to map directly to a utility class, and use `:root` for defining regular CSS variables that shouldn't have corresponding utility classes.

### Relationship to utility classes

Some utility classes in Tailwind like `flex` and `object-cover` are static, and are always the same from project to project. But many others are driven by theme variables, and only exist because of the theme variables you've defined.

For example, theme variables defined in the `--font-*` namespace determine all of the `font-family` utilities that exist in a project:

```css
/* [!code filename:./node_modules/tailwindcss/theme.css] */
@theme {
  /* [!code highlight:4] */
  /* prettier-ignore */
  --font-sans: ui-sans-serif, system-ui, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";
  --font-serif: ui-serif, Georgia, Cambria, "Times New Roman", Times, serif;
  /* prettier-ignore */
  --font-mono: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
  /* ... */
}
```

The `font-sans`, `font-serif`, and `font-mono` utilities only exist by default because Tailwind's default theme defines the `--font-sans`, `--font-serif`, and `--font-mono` theme variables.

If another theme variable like `--font-poppins` were defined, a `font-poppins` utility class would become available to go with it:

```css
/* [!code filename:app.css] */
@import "tailwindcss";

@theme {
  /* [!code highlight:2] */
  --font-poppins: Poppins, sans-serif;
}
```

```html
<!-- [!code filename:HTML] -->
<!-- [!code word:font-poppins] -->
<h1 class="font-poppins">This headline will use Poppins.</h1>
```

You can name your theme variables whatever you want within these namespaces, and a corresponding utility with the same name will become available to use in your HTML.

#### Relationship to variants

Some theme variables are used to define variants rather than utilities. For example theme variables in the `--breakpoint-*` namespace determine which responsive breakpoint variants exist in your project:

```css
/* [!code filename:app.css] */
@import "tailwindcss";

@theme {
  /* [!code highlight:2] */
  --breakpoint-3xl: 120rem;
}
```

Now you can use the `3xl:*` variant to only trigger a utility when the viewport is 120rem or wider:

```html
<!-- [!code filename:HTML] -->
<!-- [!code word:3xl\:grid-cols-6] -->
<div class="3xl:grid-cols-6 grid grid-cols-2 md:grid-cols-4">
  <!-- ... -->
</div>
```

Learn more about how theme variables map to different utility classes and variants in the [theme variable namespaces](#theme-variable-namespaces) documentation.

### Theme variable namespaces

Theme variables are defined in _namespaces_ and each namespace corresponds to one or more utility class or variant APIs.

Defining new theme variables in these namespaces will make new corresponding utilities and variants available in your project:

{

<table>
  <thead>
    <tr>
      <th>Namespace</th>
      <th>Utility classes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td className="whitespace-nowrap">
        <code>--color-*</code>
      </td>
      <td>
        Color utilities like <code>bg-red-500</code>, <code>text-sky-300</code>, and many more
      </td>
    </tr>
    <tr>
      <td className="whitespace-nowrap">
        <code>--font-*</code>
      </td>
      <td>
        Font family utilities like <code>font-sans</code>
      </td>
    </tr>
    <tr>
      <td className="whitespace-nowrap">
        <code>--text-*</code>
      </td>
      <td>
        Font size utilities like <code>text-xl</code>
      </td>
    </tr>
    <tr>
      <td className="whitespace-nowrap">
        <code>--font-weight-*</code>
      </td>
      <td>
        Font weight utilities like <code>font-bold</code>
      </td>
    </tr>
    <tr>
      <td className="whitespace-nowrap">
        <code>--tracking-*</code>
      </td>
      <td>
        Letter spacing utilities like <code>tracking-wide</code>
      </td>
    </tr>
    <tr>
      <td className="whitespace-nowrap">
        <code>--leading-*</code>
      </td>
      <td>
        Line height utilities like <code>leading-tight</code>
      </td>
    </tr>
    <tr>
      <td className="whitespace-nowrap">
        <code>--breakpoint-*</code>
      </td>
      <td>
        Responsive breakpoint variants like <code>sm:*</code>
      </td>
    </tr>
    <tr>
      <td className="whitespace-nowrap">
        <code>--container-*</code>
      </td>
      <td>
        Container query variants like <code>@sm:*</code> and size utilities like <code>max-w-md</code>
      </td>
    </tr>
    <tr>
      <td className="whitespace-nowrap">
        <code>--spacing-*</code>
      </td>
      <td>
        Spacing and sizing utilities like <code>px-4</code>, <code>max-h-16</code>, and many more
      </td>
    </tr>
    <tr>
      <td className="whitespace-nowrap">
        <code>--radius-*</code>
      </td>
      <td>
        Border radius utilities like <code>rounded-sm</code>
      </td>
    </tr>
    <tr>
      <td className="whitespace-nowrap">
        <code>--shadow-*</code>
      </td>
      <td>
        Box shadow utilities like <code>shadow-md</code>
      </td>
    </tr>
    <tr>
      <td className="whitespace-nowrap">
        <code>--inset-shadow-*</code>
      </td>
      <td>
        Inset box shadow utilities like <code>inset-shadow-xs</code>
      </td>
    </tr>
    <tr>
      <td className="whitespace-nowrap">
        <code>--drop-shadow-*</code>
      </td>
      <td>
        Drop shadow filter utilities like <code>drop-shadow-md</code>
      </td>
    </tr>
    <tr>
      <td className="whitespace-nowrap">
        <code>--blur-*</code>
      </td>
      <td>
        Blur filter utilities like <code>blur-md</code>
      </td>
    </tr>
    <tr>
      <td className="whitespace-nowrap">
        <code>--perspective-*</code>
      </td>
      <td>
        Perspective utilities like <code>perspective-near</code>
      </td>
    </tr>
    <tr>
      <td className="whitespace-nowrap">
        <code>--aspect-*</code>
      </td>
      <td>
        Aspect ratio utilities like <code>aspect-video</code>
      </td>
    </tr>
    <tr>
      <td className="whitespace-nowrap">
        <code>--ease-*</code>
      </td>
      <td>
        Transition timing function utilities like <code>ease-out</code>
      </td>
    </tr>
    <tr>
      <td className="whitespace-nowrap">
        <code>--animate-*</code>
      </td>
      <td>
        Animation utilities like <code>animate-spin</code>
      </td>
    </tr>
  </tbody>
</table>
}

For a list of all of the default theme variables, see the [default theme variable reference](#default-theme-variable-reference).

### Default theme variables

When you import `tailwindcss` at the top of your CSS file, it includes a set of default theme variables to get you started.

Here's what you're actually importing when you import `tailwindcss`:

```css
/* [!code filename:node_modules/tailwindcss/index.css] */
@layer theme, base, components, utilities;

/* [!code highlight:2] */
@import "./theme.css" layer(theme);
@import "./preflight.css" layer(base);
@import "./utilities.css" layer(utilities);
```

That `theme.css` file includes the default color palette, type scale, shadows, fonts, and more:

```css
/* [!code filename:node_modules/tailwindcss/theme.css] */
@theme {
  /* prettier-ignore */
  --font-sans: ui-sans-serif, system-ui, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";
  --font-serif: ui-serif, Georgia, Cambria, "Times New Roman", Times, serif;
  --font-mono: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;

  --color-red-50: oklch(0.971 0.013 17.38);
  --color-red-100: oklch(0.936 0.032 17.717);
  --color-red-200: oklch(0.885 0.062 18.334);
  /* ... */

  --shadow-2xs: 0 1px rgb(0 0 0 / 0.05);
  --shadow-xs: 0 1px 2px 0 rgb(0 0 0 / 0.05);
  --shadow-sm: 0 1px 3px 0 rgb(0 0 0 / 0.1), 0 1px 2px -1px rgb(0 0 0 / 0.1);
  /* ... */
}
```

This is why utilities like `bg-red-200`, `font-serif`, and `shadow-sm` exist out of the box — they're driven by the default theme, not hardcoded into the framework like `flex-col` or `pointer-events-none`.

For a list of all of the default theme variables, see the [default theme variable reference](#default-theme-variable-reference).

## Customizing your theme

The default theme variables are very general purpose and suitable for building dramatically different designs, but they are still just a starting point. It's very common to customize things like the color palette, fonts, and shadows to build exactly the design you have in mind.

### Extending the default theme

Use `@theme` to define new theme variables and extend the default theme:

```css
/* [!code filename:app.css] */
@import "tailwindcss";

@theme {
  /* [!code highlight:2] */
  --font-script: Great Vibes, cursive;
}
```

This makes a new `font-script` utility class available that you can use in your HTML, just like the default `font-sans` or `font-mono` utilities:

```html
<!-- [!code filename:HTML] -->
<!-- [!code word:font-script] -->
<p class="font-script">This will use the Great Vibes font family.</p>
```

Learn more about how theme variables map to different utility classes and variants in the [theme variable namespaces](#theme-variable-namespaces) documentation.

### Overriding the default theme

Override a default theme variable value by redefining it within `@theme`:

```css
/* [!code filename:app.css] */
@import "tailwindcss";

@theme {
  /* [!code highlight:2] */
  --breakpoint-sm: 30rem;
}
```

Now the `sm:*` variant will trigger at 30rem instead of the default 40rem viewport size:

```html
<!-- [!code filename:HTML] -->
<!-- [!code word:sm\:grid-cols-3] -->
<div class="grid grid-cols-1 sm:grid-cols-3">
  <!-- ... -->
</div>
```

To completely override an entire namespace in the default theme, set the entire namespace to `initial` using the special asterisk syntax:

```css
/* [!code filename:app.css] */
@import "tailwindcss";

@theme {
  /* [!code highlight:2] */
  --color-*: initial;
  --color-white: #fff;
  --color-purple: #3f3cbb;
  --color-midnight: #121063;
  --color-tahiti: #3ab7bf;
  --color-bermuda: #78dcca;
}
```

When you do this, all of the default utilities that use that namespace _(like `bg-red-500`)_ will be removed, and only your custom values _(like `bg-midnight`)_ will be available.

Learn more about how theme variables map to different utility classes and variants in the [theme variable namespaces](#theme-variable-namespaces) documentation.

### Using a custom theme

To completely disable the default theme and use only custom values, set the global theme variable namespace to `initial`:

```css
/* [!code filename:app.css] */
@import "tailwindcss";

@theme {
  /* [!code highlight:2] */
  --*: initial;

  --spacing: 4px;

  --font-body: Inter, sans-serif;

  --color-lagoon: oklch(0.72 0.11 221.19);
  --color-coral: oklch(0.74 0.17 40.24);
  --color-driftwood: oklch(0.79 0.06 74.59);
  --color-tide: oklch(0.49 0.08 205.88);
  --color-dusk: oklch(0.82 0.15 72.09);
}
```

Now none of the default utility classes that are driven by theme variables will be available, and you'll only be able to use utility classes matching your custom theme variables like `font-body` and `text-dusk`.

### Defining animation keyframes

Define the `@keyframes` rules for your `--animate-*` theme variables within `@theme` to include them in your generated CSS:

```css
/* [!code filename:app.css] */
@import "tailwindcss";

@theme {
  --animate-fade-in-scale: fade-in-scale 0.3s ease-out;

  @keyframes fade-in-scale {
    0% {
      opacity: 0;
      transform: scale(0.95);
    }
    100% {
      opacity: 1;
      transform: scale(1);
    }
  }
}
```

If you want your custom `@keyframes` rules to always be included even when not adding an `--animate-*` theme variable, define them outside of `@theme` instead.

### Referencing other variables

When defining theme variables that reference other variables, use the `inline` option:

```css
/* [!code filename:app.css] */
@import "tailwindcss";

/* [!code word:inline] */
@theme inline {
  --font-sans: var(--font-inter);
}
```

Using the `inline` option, the utility class will use the theme variable _value_ instead of referencing the actual theme variable:

```css
/* [!code filename:dist.css] */
.font-sans {
  font-family: var(--font-inter);
}
```

Without using `inline`, your utility classes might resolve to unexpected values because of how variables are resolved in CSS.

For example, this text will fall back to `sans-serif` instead of using `Inter` like you might expect:

```html
<!-- [!code filename:HTML] -->
<!-- [!code word:--font-sans\: var(--font-inter, sans-serif);] -->
<div id="parent" style="--font-sans: var(--font-inter, sans-serif);">
  <!-- [!code word:--font-inter\: Inter; font-family\: var(--font-sans);] -->
  <div id="child" style="--font-inter: Inter; font-family: var(--font-sans);">
    This text will use the sans-serif font, not Inter.
  </div>
</div>
```

This happens because `var(--font-sans)` is resolved where `--font-sans` is defined _(on `#parent`)_, and `--font-inter` has no value there since it's not defined until deeper in the tree _(on `#child`)_.

### Generating all CSS variables

By default only used CSS variables will be generated in the final CSS output. If you want to always generate all CSS variables, you can use the `static` theme option:

```css
/* [!code filename:app.css] */
/* [!code word:static] */
@import "tailwindcss";

@theme static {
  --color-primary: var(--color-red-500);
  --color-secondary: var(--color-blue-500);
}
```

### Sharing across projects

Since theme variables are defined in CSS, sharing them across projects is just a matter of throwing them into their own CSS file that you can import in each project:

```css
/* [!code filename:./packages/brand/theme.css] */
@theme {
  --*: initial;

  --spacing: 4px;

  --font-body: Inter, sans-serif;

  --color-lagoon: oklch(0.72 0.11 221.19);
  --color-coral: oklch(0.74 0.17 40.24);
  --color-driftwood: oklch(0.79 0.06 74.59);
  --color-tide: oklch(0.49 0.08 205.88);
  --color-dusk: oklch(0.82 0.15 72.09);
}
```

Then you can use `@import` to include your theme variables in other projects:

```css
/* [!code filename:./packages/admin/app.css] */
@import "tailwindcss";
/* [!code highlight:2] */
@import "../brand/theme.css";
```

You can put shared theme variables like this in their own package in monorepo setups or even publish them to NPM and import them just like any other third-party CSS files.

## Using your theme variables

All of your theme variables are turned into regular CSS variables when you compile your CSS:

```css
/* [!code filename:dist.css] */
:root {
  /* prettier-ignore */
  --font-sans: ui-sans-serif, system-ui, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";
  --font-serif: ui-serif, Georgia, Cambria, "Times New Roman", Times, serif;
  --font-mono: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;

  --color-red-50: oklch(0.971 0.013 17.38);
  --color-red-100: oklch(0.936 0.032 17.717);
  --color-red-200: oklch(0.885 0.062 18.334);
  /* ... */

  --shadow-2xs: 0 1px rgb(0 0 0 / 0.05);
  --shadow-xs: 0 1px 2px 0 rgb(0 0 0 / 0.05);
  --shadow-sm: 0 1px 3px 0 rgb(0 0 0 / 0.1), 0 1px 2px -1px rgb(0 0 0 / 0.1);
  /* ... */
}
```

This makes it easy to reference all of your design tokens in any of your custom CSS or inline styles.

### With custom CSS

Use your theme variables to get access to your design tokens when you're writing custom CSS that needs to use the same values:

```css
/* [!code filename:app.css] */
/* [!code word:var(--text-base)] */
/* [!code word:var(--color-gray-700)] */
/* [!code word:var(--text-2xl)] */
/* [!code word:var(--font-weight-semibold)] */
/* [!code word:var(--color-gray-950)] */
/* [!code word:var(--text-xl)] */
@import "tailwindcss";

@layer components {
  .typography {
    p {
      font-size: var(--text-base);
      color: var(--color-gray-700);
    }

    h1 {
      font-size: var(--text-2xl--line-height);
      font-weight: var(--font-weight-semibold);
      color: var(--color-gray-950);
    }

    h2 {
      font-size: var(--text-xl);
      font-weight: var(--font-weight-semibold);
      color: var(--color-gray-950);
    }
  }
}
```

This is often useful when styling HTML you don't control, like Markdown content coming from a database or API and rendered to HTML.

### With arbitrary values

Using theme variables in arbitrary values can be useful, especially in combination with the `calc()` function.

```html
<!-- [!code filename:HTML] -->
<!-- [!code word:rounded-xl] -->
<div class="relative rounded-xl">
  <!-- [!code word:rounded-\[calc(var(--radius-xl)-1px)\]] -->
  <div class="absolute inset-px rounded-[calc(var(--radius-xl)-1px)]">
    <!-- ... -->
  </div>
  <!-- ... -->
</div>
```

In the above example, we're subtracting 1px from the `--radius-xl` value on a nested inset element to make sure it has a concentric border radius.

### Referencing in JavaScript

Most of the time when you need to reference your theme variables in JS you can just use the CSS variables directly, just like any other CSS value.

For example, the popular [Motion](https://motion.dev/docs/react-quick-start) library for React lets you animate to and from CSS variable values:

```jsx
// [!code filename:JSX]
// [!code word:var(--color-blue-500)]
<motion.div animate={{ backgroundColor: "var(--color-blue-500)" }} />
```

If you need access to a resolved CSS variable value in JS, you can use `getComputedStyle` to get the value of a theme variable on the document root:

```js
// [!code filename:spaghetti.js]
let styles = getComputedStyle(document.documentElement);
let shadow = styles.getPropertyValue("--shadow-xl");
```

## Default theme variable reference

For reference, here's a complete list of the theme variables included by default when you import Tailwind CSS into your project:

```css
/* [!code filename:tailwindcss/theme.css] */
@theme {
  /* prettier-ignore */
  --font-sans: ui-sans-serif, system-ui, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";
  --font-serif: ui-serif, Georgia, Cambria, "Times New Roman", Times, serif;
  --font-mono: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;

  --color-red-50: oklch(97.1% 0.013 17.38);
  --color-red-100: oklch(93.6% 0.032 17.717);
  --color-red-200: oklch(88.5% 0.062 18.334);
  --color-red-300: oklch(80.8% 0.114 19.571);
  --color-red-400: oklch(70.4% 0.191 22.216);
  --color-red-500: oklch(63.7% 0.237 25.331);
  --color-red-600: oklch(57.7% 0.245 27.325);
  --color-red-700: oklch(50.5% 0.213 27.518);
  --color-red-800: oklch(44.4% 0.177 26.899);
  --color-red-900: oklch(39.6% 0.141 25.723);
  --color-red-950: oklch(25.8% 0.092 26.042);

  --color-orange-50: oklch(98% 0.016 73.684);
  --color-orange-100: oklch(95.4% 0.038 75.164);
  --color-orange-200: oklch(90.1% 0.076 70.697);
  --color-orange-300: oklch(83.7% 0.128 66.29);
  --color-orange-400: oklch(75% 0.183 55.934);
  --color-orange-500: oklch(70.5% 0.213 47.604);
  --color-orange-600: oklch(64.6% 0.222 41.116);
  --color-orange-700: oklch(55.3% 0.195 38.402);
  --color-orange-800: oklch(47% 0.157 37.304);
  --color-orange-900: oklch(40.8% 0.123 38.172);
  --color-orange-950: oklch(26.6% 0.079 36.259);

  --color-amber-50: oklch(98.7% 0.022 95.277);
  --color-amber-100: oklch(96.2% 0.059 95.617);
  --color-amber-200: oklch(92.4% 0.12 95.746);
  --color-amber-300: oklch(87.9% 0.169 91.605);
  --color-amber-400: oklch(82.8% 0.189 84.429);
  --color-amber-500: oklch(76.9% 0.188 70.08);
  --color-amber-600: oklch(66.6% 0.179 58.318);
  --color-amber-700: oklch(55.5% 0.163 48.998);
  --color-amber-800: oklch(47.3% 0.137 46.201);
  --color-amber-900: oklch(41.4% 0.112 45.904);
  --color-amber-950: oklch(27.9% 0.077 45.635);

  --color-yellow-50: oklch(98.7% 0.026 102.212);
  --color-yellow-100: oklch(97.3% 0.071 103.193);
  --color-yellow-200: oklch(94.5% 0.129 101.54);
  --color-yellow-300: oklch(90.5% 0.182 98.111);
  --color-yellow-400: oklch(85.2% 0.199 91.936);
  --color-yellow-500: oklch(79.5% 0.184 86.047);
  --color-yellow-600: oklch(68.1% 0.162 75.834);
  --color-yellow-700: oklch(55.4% 0.135 66.442);
  --color-yellow-800: oklch(47.6% 0.114 61.907);
  --color-yellow-900: oklch(42.1% 0.095 57.708);
  --color-yellow-950: oklch(28.6% 0.066 53.813);

  --color-lime-50: oklch(98.6% 0.031 120.757);
  --color-lime-100: oklch(96.7% 0.067 122.328);
  --color-lime-200: oklch(93.8% 0.127 124.321);
  --color-lime-300: oklch(89.7% 0.196 126.665);
  --color-lime-400: oklch(84.1% 0.238 128.85);
  --color-lime-500: oklch(76.8% 0.233 130.85);
  --color-lime-600: oklch(64.8% 0.2 131.684);
  --color-lime-700: oklch(53.2% 0.157 131.589);
  --color-lime-800: oklch(45.3% 0.124 130.933);
  --color-lime-900: oklch(40.5% 0.101 131.063);
  --color-lime-950: oklch(27.4% 0.072 132.109);

  --color-green-50: oklch(98.2% 0.018 155.826);
  --color-green-100: oklch(96.2% 0.044 156.743);
  --color-green-200: oklch(92.5% 0.084 155.995);
  --color-green-300: oklch(87.1% 0.15 154.449);
  --color-green-400: oklch(79.2% 0.209 151.711);
  --color-green-500: oklch(72.3% 0.219 149.579);
  --color-green-600: oklch(62.7% 0.194 149.214);
  --color-green-700: oklch(52.7% 0.154 150.069);
  --color-green-800: oklch(44.8% 0.119 151.328);
  --color-green-900: oklch(39.3% 0.095 152.535);
  --color-green-950: oklch(26.6% 0.065 152.934);

  --color-emerald-50: oklch(97.9% 0.021 166.113);
  --color-emerald-100: oklch(95% 0.052 163.051);
  --color-emerald-200: oklch(90.5% 0.093 164.15);
  --color-emerald-300: oklch(84.5% 0.143 164.978);
  --color-emerald-400: oklch(76.5% 0.177 163.223);
  --color-emerald-500: oklch(69.6% 0.17 162.48);
  --color-emerald-600: oklch(59.6% 0.145 163.225);
  --color-emerald-700: oklch(50.8% 0.118 165.612);
  --color-emerald-800: oklch(43.2% 0.095 166.913);
  --color-emerald-900: oklch(37.8% 0.077 168.94);
  --color-emerald-950: oklch(26.2% 0.051 172.552);

  --color-teal-50: oklch(98.4% 0.014 180.72);
  --color-teal-100: oklch(95.3% 0.051 180.801);
  --color-teal-200: oklch(91% 0.096 180.426);
  --color-teal-300: oklch(85.5% 0.138 181.071);
  --color-teal-400: oklch(77.7% 0.152 181.912);
  --color-teal-500: oklch(70.4% 0.14 182.503);
  --color-teal-600: oklch(60% 0.118 184.704);
  --color-teal-700: oklch(51.1% 0.096 186.391);
  --color-teal-800: oklch(43.7% 0.078 188.216);
  --color-teal-900: oklch(38.6% 0.063 188.416);
  --color-teal-950: oklch(27.7% 0.046 192.524);

  --color-cyan-50: oklch(98.4% 0.019 200.873);
  --color-cyan-100: oklch(95.6% 0.045 203.388);
  --color-cyan-200: oklch(91.7% 0.08 205.041);
  --color-cyan-300: oklch(86.5% 0.127 207.078);
  --color-cyan-400: oklch(78.9% 0.154 211.53);
  --color-cyan-500: oklch(71.5% 0.143 215.221);
  --color-cyan-600: oklch(60.9% 0.126 221.723);
  --color-cyan-700: oklch(52% 0.105 223.128);
  --color-cyan-800: oklch(45% 0.085 224.283);
  --color-cyan-900: oklch(39.8% 0.07 227.392);
  --color-cyan-950: oklch(30.2% 0.056 229.695);

  --color-sky-50: oklch(97.7% 0.013 236.62);
  --color-sky-100: oklch(95.1% 0.026 236.824);
  --color-sky-200: oklch(90.1% 0.058 230.902);
  --color-sky-300: oklch(82.8% 0.111 230.318);
  --color-sky-400: oklch(74.6% 0.16 232.661);
  --color-sky-500: oklch(68.5% 0.169 237.323);
  --color-sky-600: oklch(58.8% 0.158 241.966);
  --color-sky-700: oklch(50% 0.134 242.749);
  --color-sky-800: oklch(44.3% 0.11 240.79);
  --color-sky-900: oklch(39.1% 0.09 240.876);
  --color-sky-950: oklch(29.3% 0.066 243.157);

  --color-blue-50: oklch(97% 0.014 254.604);
  --color-blue-100: oklch(93.2% 0.032 255.585);
  --color-blue-200: oklch(88.2% 0.059 254.128);
  --color-blue-300: oklch(80.9% 0.105 251.813);
  --color-blue-400: oklch(70.7% 0.165 254.624);
  --color-blue-500: oklch(62.3% 0.214 259.815);
  --color-blue-600: oklch(54.6% 0.245 262.881);
  --color-blue-700: oklch(48.8% 0.243 264.376);
  --color-blue-800: oklch(42.4% 0.199 265.638);
  --color-blue-900: oklch(37.9% 0.146 265.522);
  --color-blue-950: oklch(28.2% 0.091 267.935);

  --color-indigo-50: oklch(96.2% 0.018 272.314);
  --color-indigo-100: oklch(93% 0.034 272.788);
  --color-indigo-200: oklch(87% 0.065 274.039);
  --color-indigo-300: oklch(78.5% 0.115 274.713);
  --color-indigo-400: oklch(67.3% 0.182 276.935);
  --color-indigo-500: oklch(58.5% 0.233 277.117);
  --color-indigo-600: oklch(51.1% 0.262 276.966);
  --color-indigo-700: oklch(45.7% 0.24 277.023);
  --color-indigo-800: oklch(39.8% 0.195 277.366);
  --color-indigo-900: oklch(35.9% 0.144 278.697);
  --color-indigo-950: oklch(25.7% 0.09 281.288);

  --color-violet-50: oklch(96.9% 0.016 293.756);
  --color-violet-100: oklch(94.3% 0.029 294.588);
  --color-violet-200: oklch(89.4% 0.057 293.283);
  --color-violet-300: oklch(81.1% 0.111 293.571);
  --color-violet-400: oklch(70.2% 0.183 293.541);
  --color-violet-500: oklch(60.6% 0.25 292.717);
  --color-violet-600: oklch(54.1% 0.281 293.009);
  --color-violet-700: oklch(49.1% 0.27 292.581);
  --color-violet-800: oklch(43.2% 0.232 292.759);
  --color-violet-900: oklch(38% 0.189 293.745);
  --color-violet-950: oklch(28.3% 0.141 291.089);

  --color-purple-50: oklch(97.7% 0.014 308.299);
  --color-purple-100: oklch(94.6% 0.033 307.174);
  --color-purple-200: oklch(90.2% 0.063 306.703);
  --color-purple-300: oklch(82.7% 0.119 306.383);
  --color-purple-400: oklch(71.4% 0.203 305.504);
  --color-purple-500: oklch(62.7% 0.265 303.9);
  --color-purple-600: oklch(55.8% 0.288 302.321);
  --color-purple-700: oklch(49.6% 0.265 301.924);
  --color-purple-800: oklch(43.8% 0.218 303.724);
  --color-purple-900: oklch(38.1% 0.176 304.987);
  --color-purple-950: oklch(29.1% 0.149 302.717);

  --color-fuchsia-50: oklch(97.7% 0.017 320.058);
  --color-fuchsia-100: oklch(95.2% 0.037 318.852);
  --color-fuchsia-200: oklch(90.3% 0.076 319.62);
  --color-fuchsia-300: oklch(83.3% 0.145 321.434);
  --color-fuchsia-400: oklch(74% 0.238 322.16);
  --color-fuchsia-500: oklch(66.7% 0.295 322.15);
  --color-fuchsia-600: oklch(59.1% 0.293 322.896);
  --color-fuchsia-700: oklch(51.8% 0.253 323.949);
  --color-fuchsia-800: oklch(45.2% 0.211 324.591);
  --color-fuchsia-900: oklch(40.1% 0.17 325.612);
  --color-fuchsia-950: oklch(29.3% 0.136 325.661);

  --color-pink-50: oklch(97.1% 0.014 343.198);
  --color-pink-100: oklch(94.8% 0.028 342.258);
  --color-pink-200: oklch(89.9% 0.061 343.231);
  --color-pink-300: oklch(82.3% 0.12 346.018);
  --color-pink-400: oklch(71.8% 0.202 349.761);
  --color-pink-500: oklch(65.6% 0.241 354.308);
  --color-pink-600: oklch(59.2% 0.249 0.584);
  --color-pink-700: oklch(52.5% 0.223 3.958);
  --color-pink-800: oklch(45.9% 0.187 3.815);
  --color-pink-900: oklch(40.8% 0.153 2.432);
  --color-pink-950: oklch(28.4% 0.109 3.907);

  --color-rose-50: oklch(96.9% 0.015 12.422);
  --color-rose-100: oklch(94.1% 0.03 12.58);
  --color-rose-200: oklch(89.2% 0.058 10.001);
  --color-rose-300: oklch(81% 0.117 11.638);
  --color-rose-400: oklch(71.2% 0.194 13.428);
  --color-rose-500: oklch(64.5% 0.246 16.439);
  --color-rose-600: oklch(58.6% 0.253 17.585);
  --color-rose-700: oklch(51.4% 0.222 16.935);
  --color-rose-800: oklch(45.5% 0.188 13.697);
  --color-rose-900: oklch(41% 0.159 10.272);
  --color-rose-950: oklch(27.1% 0.105 12.094);

  --color-slate-50: oklch(98.4% 0.003 247.858);
  --color-slate-100: oklch(96.8% 0.007 247.896);
  --color-slate-200: oklch(92.9% 0.013 255.508);
  --color-slate-300: oklch(86.9% 0.022 252.894);
  --color-slate-400: oklch(70.4% 0.04 256.788);
  --color-slate-500: oklch(55.4% 0.046 257.417);
  --color-slate-600: oklch(44.6% 0.043 257.281);
  --color-slate-700: oklch(37.2% 0.044 257.287);
  --color-slate-800: oklch(27.9% 0.041 260.031);
  --color-slate-900: oklch(20.8% 0.042 265.755);
  --color-slate-950: oklch(12.9% 0.042 264.695);

  --color-gray-50: oklch(98.5% 0.002 247.839);
  --color-gray-100: oklch(96.7% 0.003 264.542);
  --color-gray-200: oklch(92.8% 0.006 264.531);
  --color-gray-300: oklch(87.2% 0.01 258.338);
  --color-gray-400: oklch(70.7% 0.022 261.325);
  --color-gray-500: oklch(55.1% 0.027 264.364);
  --color-gray-600: oklch(44.6% 0.03 256.802);
  --color-gray-700: oklch(37.3% 0.034 259.733);
  --color-gray-800: oklch(27.8% 0.033 256.848);
  --color-gray-900: oklch(21% 0.034 264.665);
  --color-gray-950: oklch(13% 0.028 261.692);

  --color-zinc-50: oklch(98.5% 0 0);
  --color-zinc-100: oklch(96.7% 0.001 286.375);
  --color-zinc-200: oklch(92% 0.004 286.32);
  --color-zinc-300: oklch(87.1% 0.006 286.286);
  --color-zinc-400: oklch(70.5% 0.015 286.067);
  --color-zinc-500: oklch(55.2% 0.016 285.938);
  --color-zinc-600: oklch(44.2% 0.017 285.786);
  --color-zinc-700: oklch(37% 0.013 285.805);
  --color-zinc-800: oklch(27.4% 0.006 286.033);
  --color-zinc-900: oklch(21% 0.006 285.885);
  --color-zinc-950: oklch(14.1% 0.005 285.823);

  --color-neutral-50: oklch(98.5% 0 0);
  --color-neutral-100: oklch(97% 0 0);
  --color-neutral-200: oklch(92.2% 0 0);
  --color-neutral-300: oklch(87% 0 0);
  --color-neutral-400: oklch(70.8% 0 0);
  --color-neutral-500: oklch(55.6% 0 0);
  --color-neutral-600: oklch(43.9% 0 0);
  --color-neutral-700: oklch(37.1% 0 0);
  --color-neutral-800: oklch(26.9% 0 0);
  --color-neutral-900: oklch(20.5% 0 0);
  --color-neutral-950: oklch(14.5% 0 0);

  --color-stone-50: oklch(98.5% 0.001 106.423);
  --color-stone-100: oklch(97% 0.001 106.424);
  --color-stone-200: oklch(92.3% 0.003 48.717);
  --color-stone-300: oklch(86.9% 0.005 56.366);
  --color-stone-400: oklch(70.9% 0.01 56.259);
  --color-stone-500: oklch(55.3% 0.013 58.071);
  --color-stone-600: oklch(44.4% 0.011 73.639);
  --color-stone-700: oklch(37.4% 0.01 67.558);
  --color-stone-800: oklch(26.8% 0.007 34.298);
  --color-stone-900: oklch(21.6% 0.006 56.043);
  --color-stone-950: oklch(14.7% 0.004 49.25);

  --color-mauve-50: oklch(98.5% 0 0);
  --color-mauve-100: oklch(96% 0.003 325.6);
  --color-mauve-200: oklch(92.2% 0.005 325.62);
  --color-mauve-300: oklch(86.5% 0.012 325.68);
  --color-mauve-400: oklch(71.1% 0.019 323.02);
  --color-mauve-500: oklch(54.2% 0.034 322.5);
  --color-mauve-600: oklch(43.5% 0.029 321.78);
  --color-mauve-700: oklch(36.4% 0.029 323.89);
  --color-mauve-800: oklch(26.3% 0.024 320.12);
  --color-mauve-900: oklch(21.2% 0.019 322.12);
  --color-mauve-950: oklch(14.5% 0.008 326);

  --color-olive-50: oklch(98.8% 0.003 106.5);
  --color-olive-100: oklch(96.6% 0.005 106.5);
  --color-olive-200: oklch(93% 0.007 106.5);
  --color-olive-300: oklch(88% 0.011 106.6);
  --color-olive-400: oklch(73.7% 0.021 106.9);
  --color-olive-500: oklch(58% 0.031 107.3);
  --color-olive-600: oklch(46.6% 0.025 107.3);
  --color-olive-700: oklch(39.4% 0.023 107.4);
  --color-olive-800: oklch(28.6% 0.016 107.4);
  --color-olive-900: oklch(22.8% 0.013 107.4);
  --color-olive-950: oklch(15.3% 0.006 107.1);

  --color-mist-50: oklch(98.7% 0.002 197.1);
  --color-mist-100: oklch(96.3% 0.002 197.1);
  --color-mist-200: oklch(92.5% 0.005 214.3);
  --color-mist-300: oklch(87.2% 0.007 219.6);
  --color-mist-400: oklch(72.3% 0.014 214.4);
  --color-mist-500: oklch(56% 0.021 213.5);
  --color-mist-600: oklch(45% 0.017 213.2);
  --color-mist-700: oklch(37.8% 0.015 216);
  --color-mist-800: oklch(27.5% 0.011 216.9);
  --color-mist-900: oklch(21.8% 0.008 223.9);
  --color-mist-950: oklch(14.8% 0.004 228.8);

  --color-taupe-50: oklch(98.6% 0.002 67.8);
  --color-taupe-100: oklch(96% 0.002 17.2);
  --color-taupe-200: oklch(92.2% 0.005 34.3);
  --color-taupe-300: oklch(86.8% 0.007 39.5);
  --color-taupe-400: oklch(71.4% 0.014 41.2);
  --color-taupe-500: oklch(54.7% 0.021 43.1);
  --color-taupe-600: oklch(43.8% 0.017 39.3);
  --color-taupe-700: oklch(36.7% 0.016 35.7);
  --color-taupe-800: oklch(26.8% 0.011 36.5);
  --color-taupe-900: oklch(21.4% 0.009 43.1);
  --color-taupe-950: oklch(14.7% 0.004 49.3);

  --color-black: #000;
  --color-white: #fff;

  --spacing: 0.25rem;

  --breakpoint-sm: 40rem;
  --breakpoint-md: 48rem;
  --breakpoint-lg: 64rem;
  --breakpoint-xl: 80rem;
  --breakpoint-2xl: 96rem;

  --container-3xs: 16rem;
  --container-2xs: 18rem;
  --container-xs: 20rem;
  --container-sm: 24rem;
  --container-md: 28rem;
  --container-lg: 32rem;
  --container-xl: 36rem;
  --container-2xl: 42rem;
  --container-3xl: 48rem;
  --container-4xl: 56rem;
  --container-5xl: 64rem;
  --container-6xl: 72rem;
  --container-7xl: 80rem;

  --text-xs: 0.75rem;
  --text-xs--line-height: calc(1 / 0.75);
  --text-sm: 0.875rem;
  --text-sm--line-height: calc(1.25 / 0.875);
  --text-base: 1rem;
  --text-base--line-height: calc(1.5 / 1);
  --text-lg: 1.125rem;
  --text-lg--line-height: calc(1.75 / 1.125);
  --text-xl: 1.25rem;
  --text-xl--line-height: calc(1.75 / 1.25);
  --text-2xl: 1.5rem;
  --text-2xl--line-height: calc(2 / 1.5);
  --text-3xl: 1.875rem;
  --text-3xl--line-height: calc(2.25 / 1.875);
  --text-4xl: 2.25rem;
  --text-4xl--line-height: calc(2.5 / 2.25);
  --text-5xl: 3rem;
  --text-5xl--line-height: 1;
  --text-6xl: 3.75rem;
  --text-6xl--line-height: 1;
  --text-7xl: 4.5rem;
  --text-7xl--line-height: 1;
  --text-8xl: 6rem;
  --text-8xl--line-height: 1;
  --text-9xl: 8rem;
  --text-9xl--line-height: 1;

  --font-weight-thin: 100;
  --font-weight-extralight: 200;
  --font-weight-light: 300;
  --font-weight-normal: 400;
  --font-weight-medium: 500;
  --font-weight-semibold: 600;
  --font-weight-bold: 700;
  --font-weight-extrabold: 800;
  --font-weight-black: 900;

  --tracking-tighter: -0.05em;
  --tracking-tight: -0.025em;
  --tracking-normal: 0em;
  --tracking-wide: 0.025em;
  --tracking-wider: 0.05em;
  --tracking-widest: 0.1em;

  --leading-tight: 1.25;
  --leading-snug: 1.375;
  --leading-normal: 1.5;
  --leading-relaxed: 1.625;
  --leading-loose: 2;

  --radius-xs: 0.125rem;
  --radius-sm: 0.25rem;
  --radius-md: 0.375rem;
  --radius-lg: 0.5rem;
  --radius-xl: 0.75rem;
  --radius-2xl: 1rem;
  --radius-3xl: 1.5rem;
  --radius-4xl: 2rem;

  --shadow-2xs: 0 1px rgb(0 0 0 / 0.05);
  --shadow-xs: 0 1px 2px 0 rgb(0 0 0 / 0.05);
  --shadow-sm: 0 1px 3px 0 rgb(0 0 0 / 0.1), 0 1px 2px -1px rgb(0 0 0 / 0.1);
  --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
  --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
  --shadow-xl: 0 20px 25px -5px rgb(0 0 0 / 0.1), 0 8px 10px -6px rgb(0 0 0 / 0.1);
  --shadow-2xl: 0 25px 50px -12px rgb(0 0 0 / 0.25);

  --inset-shadow-2xs: inset 0 1px rgb(0 0 0 / 0.05);
  --inset-shadow-xs: inset 0 1px 1px rgb(0 0 0 / 0.05);
  --inset-shadow-sm: inset 0 2px 4px rgb(0 0 0 / 0.05);

  --drop-shadow-xs: 0 1px 1px rgb(0 0 0 / 0.05);
  --drop-shadow-sm: 0 1px 2px rgb(0 0 0 / 0.15);
  --drop-shadow-md: 0 3px 3px rgb(0 0 0 / 0.12);
  --drop-shadow-lg: 0 4px 4px rgb(0 0 0 / 0.15);
  --drop-shadow-xl: 0 9px 7px rgb(0 0 0 / 0.1);
  --drop-shadow-2xl: 0 25px 25px rgb(0 0 0 / 0.15);

  --text-shadow-2xs: 0px 1px 0px rgb(0 0 0 / 0.15);
  --text-shadow-xs: 0px 1px 1px rgb(0 0 0 / 0.2);
  --text-shadow-sm: 0px 1px 0px rgb(0 0 0 / 0.075), 0px 1px 1px rgb(0 0 0 / 0.075), 0px 2px 2px rgb(0 0 0 / 0.075);
  --text-shadow-md: 0px 1px 1px rgb(0 0 0 / 0.1), 0px 1px 2px rgb(0 0 0 / 0.1), 0px 2px 4px rgb(0 0 0 / 0.1);
  --text-shadow-lg: 0px 1px 2px rgb(0 0 0 / 0.1), 0px 3px 2px rgb(0 0 0 / 0.1), 0px 4px 8px rgb(0 0 0 / 0.1);

  --blur-xs: 4px;
  --blur-sm: 8px;
  --blur-md: 12px;
  --blur-lg: 16px;
  --blur-xl: 24px;
  --blur-2xl: 40px;
  --blur-3xl: 64px;

  --perspective-dramatic: 100px;
  --perspective-near: 300px;
  --perspective-normal: 500px;
  --perspective-midrange: 800px;
  --perspective-distant: 1200px;

  --aspect-video: 16 / 9;

  --ease-in: cubic-bezier(0.4, 0, 1, 1);
  --ease-out: cubic-bezier(0, 0, 0.2, 1);
  --ease-in-out: cubic-bezier(0.4, 0, 0.2, 1);

  --animate-spin: spin 1s linear infinite;
  --animate-ping: ping 1s cubic-bezier(0, 0, 0.2, 1) infinite;
  --animate-pulse: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
  --animate-bounce: bounce 1s infinite;

  @keyframes spin {
    to {
      transform: rotate(360deg);
    }
  }

  @keyframes ping {
    75%,
    100% {
      transform: scale(2);
      opacity: 0;
    }
  }

  @keyframes pulse {
    50% {
      opacity: 0.5;
    }
  }

  @keyframes bounce {
    0%,
    100% {
      transform: translateY(-25%);
      animation-timing-function: cubic-bezier(0.8, 0, 1, 1);
    }

    50% {
      transform: none;
      animation-timing-function: cubic-bezier(0, 0, 0.2, 1);
    }
  }
}
```


---

## Source: src/docs/upgrade-guide.mdx

export const title = "Upgrade guide";
export const description = "Upgrading your Tailwind CSS projects from v3 to v4.";

Tailwind CSS v4.0 is a new major version of the framework, so while we've worked really hard to minimize breaking changes, some updates are necessary. This guide outlines all the steps required to upgrade your projects from v3 to v4.

**Tailwind CSS v4.0 is designed for Safari 16.4+, Chrome 111+, and Firefox 128+.** If you need to support older browsers, stick with v3.4 until your browser support requirements change.

## Using the upgrade tool

If you'd like to upgrade a project from v3 to v4, you can use our upgrade tool to do the vast majority of the heavy lifting for you:

```sh
  # [!code filename:Terminal]
$ npx @tailwindcss/upgrade
```

For most projects, the upgrade tool will automate the entire migration process including updating your dependencies, migrating your configuration file to CSS, and handling any changes to your template files.

The upgrade tool requires Node.js 20 or higher, so ensure your environment is updated before running it.

**We recommend running the upgrade tool in a new branch**, then carefully reviewing the diff and testing your project in the browser to make sure all of the changes look correct. You may need to tweak a few things by hand in complex projects, but the tool will save you a ton of time either way.

It's also a good idea to go over all of the [breaking changes](#changes-from-v3) in v4 and get a good understanding of what's changed, in case there are other things you need to update in your project that the upgrade tool doesn't catch.

## Upgrading manually

### Using PostCSS

In v3, the `tailwindcss` package was a PostCSS plugin, but in v4 the PostCSS plugin lives in a dedicated `@tailwindcss/postcss` package.

Additionally, in v4 imports and vendor prefixing is now handled for you automatically, so you can remove `postcss-import` and `autoprefixer` if they are in your project:

```js
// [!code filename:postcss.config.mjs]
export default {
  plugins: {
    // [!code --:4]
    "postcss-import": {},
    tailwindcss: {},
    autoprefixer: {},
    // [!code ++:2]
    "@tailwindcss/postcss": {},
  },
};
```

### Using Vite

If you're using Vite, we recommend migrating from the PostCSS plugin to our new dedicated Vite plugin for improved performance and the best developer experience:

```ts
// [!code filename:vite.config.ts]
import { defineConfig } from "vite";
// [!code highlight:2]
import tailwindcss from "@tailwindcss/vite";

export default defineConfig({
  plugins: [
    // [!code highlight:2]
    tailwindcss(),
  ],
});
```

### Using Tailwind CLI

In v4, Tailwind CLI lives in a dedicated `@tailwindcss/cli` package. Update any of your build commands to use the new package instead:

```sh
/* [!code filename:Terminal] */
  # [!code --:2]
npx tailwindcss -i input.css -o output.css
  # [!code ++:2]
npx @tailwindcss/cli -i input.css -o output.css
```

## Changes from v3

Here's a comprehensive list of all the breaking changes in Tailwind CSS v4.0.

Our [upgrade tool](#using-the-upgrade-tool) will handle most of these changes for you automatically, so we highly recommend using it if you can.

### Browser requirements

Tailwind CSS v4.0 is designed for modern browsers and targets Safari 16.4, Chrome 111, and Firefox 128. We depend on modern CSS features like `@property` and `color-mix()` for core framework features, and Tailwind CSS v4.0 will not work in older browsers.

If you need to support older browsers, we recommend sticking with v3.4 for now. We're actively exploring a compatibility mode to help people upgrade sooner that we hope to share more news on in the future.

### Removed @tailwind directives

In v4 you import Tailwind using a regular CSS `@import` statement, not using the `@tailwind` directives you used in v3:

```css
/* [!code filename:CSS] */
/* [!code --:4] */
@tailwind base;
@tailwind components;
@tailwind utilities;
/* [!code ++:2] */
@import "tailwindcss";
```

### Removed deprecated utilities

We've removed any utilities that were deprecated in v3 and have been undocumented for several years. Here's a list of what's been removed along with the modern alternative:

{

<table>
  <thead>
    <tr>
      <th>Deprecated</th>
      <th>Replacement</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <code className="whitespace-nowrap">bg-opacity-*</code>
      </td>
      <td>
        Use opacity modifiers like <code className="whitespace-nowrap">bg-black/50</code>
      </td>
    </tr>
    <tr>
      <td>
        <code className="whitespace-nowrap">text-opacity-*</code>
      </td>
      <td>
        Use opacity modifiers like <code className="whitespace-nowrap">text-black/50</code>
      </td>
    </tr>
    <tr>
      <td>
        <code className="whitespace-nowrap">border-opacity-*</code>
      </td>
      <td>
        Use opacity modifiers like <code className="whitespace-nowrap">border-black/50</code>
      </td>
    </tr>
    <tr>
      <td>
        <code className="whitespace-nowrap">divide-opacity-*</code>
      </td>
      <td>
        Use opacity modifiers like <code className="whitespace-nowrap">divide-black/50</code>
      </td>
    </tr>
    <tr>
      <td>
        <code className="whitespace-nowrap">ring-opacity-*</code>
      </td>
      <td>
        Use opacity modifiers like <code className="whitespace-nowrap">ring-black/50</code>
      </td>
    </tr>
    <tr>
      <td>
        <code className="whitespace-nowrap">placeholder-opacity-*</code>
      </td>
      <td>
        Use opacity modifiers like <code className="whitespace-nowrap">placeholder-black/50</code>
      </td>
    </tr>
    <tr>
      <td>
        <code className="whitespace-nowrap">flex-shrink-*</code>
      </td>
      <td>
        <code className="whitespace-nowrap">shrink-*</code>
      </td>
    </tr>
    <tr>
      <td>
        <code className="whitespace-nowrap">flex-grow-*</code>
      </td>
      <td>
        <code className="whitespace-nowrap">grow-*</code>
      </td>
    </tr>
    <tr>
      <td>
        <code className="whitespace-nowrap">overflow-ellipsis</code>
      </td>
      <td>
        <code className="whitespace-nowrap">text-ellipsis</code>
      </td>
    </tr>
    <tr>
      <td>
        <code className="whitespace-nowrap">decoration-slice</code>
      </td>
      <td>
        <code className="whitespace-nowrap">box-decoration-slice</code>
      </td>
    </tr>
    <tr>
      <td>
        <code className="whitespace-nowrap">decoration-clone</code>
      </td>
      <td>
        <code className="whitespace-nowrap">box-decoration-clone</code>
      </td>
    </tr>
  </tbody>
</table>

}

### Renamed utilities

We've renamed the following utilities in v4 to make them more consistent and predictable:

{

<table>
  <thead>
    <tr>
      <th>v3</th>
      <th>v4</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <code className="whitespace-nowrap">shadow-sm</code>
      </td>
      <td>
        <code className="whitespace-nowrap">shadow-xs</code>
      </td>
    </tr>
    <tr>
      <td>
        <code className="whitespace-nowrap">shadow</code>
      </td>
      <td>
        <code className="whitespace-nowrap">shadow-sm</code>
      </td>
    </tr>
    <tr>
      <td>
        <code className="whitespace-nowrap">drop-shadow-sm</code>
      </td>
      <td>
        <code className="whitespace-nowrap">drop-shadow-xs</code>
      </td>
    </tr>
    <tr>
      <td>
        <code className="whitespace-nowrap">drop-shadow</code>
      </td>
      <td>
        <code className="whitespace-nowrap">drop-shadow-sm</code>
      </td>
    </tr>
    <tr>
      <td>
        <code className="whitespace-nowrap">blur-sm</code>
      </td>
      <td>
        <code className="whitespace-nowrap">blur-xs</code>
      </td>
    </tr>
    <tr>
      <td>
        <code className="whitespace-nowrap">blur</code>
      </td>
      <td>
        <code className="whitespace-nowrap">blur-sm</code>
      </td>
    </tr>
    <tr>
      <td>
        <code className="whitespace-nowrap">backdrop-blur-sm</code>
      </td>
      <td>
        <code className="whitespace-nowrap">backdrop-blur-xs</code>
      </td>
    </tr>
    <tr>
      <td>
        <code className="whitespace-nowrap">backdrop-blur</code>
      </td>
      <td>
        <code className="whitespace-nowrap">backdrop-blur-sm</code>
      </td>
    </tr>
    <tr>
      <td>
        <code className="whitespace-nowrap">rounded-sm</code>
      </td>
      <td>
        <code className="whitespace-nowrap">rounded-xs</code>
      </td>
    </tr>
    <tr>
      <td>
        <code className="whitespace-nowrap">rounded</code>
      </td>
      <td>
        <code className="whitespace-nowrap">rounded-sm</code>
      </td>
    </tr>
    <tr>
      <td>
        <code className="whitespace-nowrap">outline-none</code>
      </td>
      <td>
        <code className="whitespace-nowrap">outline-hidden</code>
      </td>
    </tr>
    <tr>
      <td>
        <code className="whitespace-nowrap">ring</code>
      </td>
      <td>
        <code className="whitespace-nowrap">ring-3</code>
      </td>
    </tr>
  </tbody>
</table>

}

#### Updated shadow, radius, and blur scales

We've renamed the default shadow, radius and blur scales to make sure every utility has a named value. The "bare" versions still work for backward compatibility, but the <code><em>{'<utility>'}</em>-sm</code> utilities will look different unless updated to their respective <code><em>{'<utility>'}</em>-xs</code> versions.

To update your project for these changes, replace all the v3 utilities with their v4 versions:

```html
<!-- [!code filename:HTML] -->
<!-- [!code --:2] -->
<input class="shadow-sm" />
<!-- [!code ++:2] -->
<input class="shadow-xs" />

<!-- [!code --:2] -->
<input class="shadow" />
<!-- [!code ++:2] -->
<input class="shadow-sm" />
```

#### Renamed outline utility

The `outline` utility now sets `outline-width: 1px` by default to be more consistent with border and ring utilities. Furthermore all `outline-<number>` utilities default `outline-style` to `solid`, omitting the need to combine them with `outline`:

```html
<!-- [!code filename:HTML] -->
<!-- [!code --:2] -->
<input class="outline outline-2" />
<!-- [!code ++:2] -->
<input class="outline-2" />
```

The `outline-none` utility previously didn't actually set `outline-style: none`, and instead set an invisible outline that would still show up in forced colors mode for accessibility reasons.

To make this more clear we've renamed this utility to `outline-hidden` and added a new `outline-none` utility that actually sets `outline-style: none`.

To update your project for this change, replace any usage of `outline-none` with `outline-hidden`:

```html
<!-- [!code filename:HTML] -->
<!-- [!code --:2] -->
<input class="focus:outline-none" />
<!-- [!code ++:2] -->
<input class="focus:outline-hidden" />
```

#### Default ring width change

In v3, the `ring` utility added a `3px` ring. We've changed this in v4 to be `1px` to make it consistent with borders and outlines.

To update your project for this change, replace any usage of `ring` with `ring-3`:

```html
<!-- [!code filename:HTML] -->
<!-- [!code --:2] -->
<input class="ring ring-blue-500" />
<!-- [!code ++:2] -->
<input class="ring-3 ring-blue-500" />
```

### Space-between selector

We've changed the selector used by the [`space-x-*` and `space-y-*` utilities](/docs/margin#adding-space-between-children) to address serious performance issues on large pages:

```css
/* [!code filename:CSS] */
/* Before */
.space-y-4 > :not([hidden]) ~ :not([hidden]) {
  margin-top: 1rem;
}

/* Now */
.space-y-4 > :not(:last-child) {
  margin-bottom: 1rem;
}
```

You might see changes in your project if you were ever using these utilities with inline elements, or if you were adding other margins to child elements to tweak their spacing.

If this change causes any issues in your project, we recommend migrating to a flex or grid layout and using `gap` instead:

{/* prettier-ignore */}
```html
<!-- [!code filename:HTML] -->
<div class="space-y-4 p-4"> <!-- [!code --] -->
<div class="flex flex-col gap-4 p-4"> <!-- [!code ++] -->
  <label for="name">Name</label>
  <input type="text" name="name" />
</div>
```

### Divide selector

We've changed the selector used by the [`divide-x-*` and `divide-y-*` utilities](/docs/border-width#between-children) to address serious performance issues on large pages:

```css
/* [!code filename:CSS] */
/* Before */
.divide-y-4 > :not([hidden]) ~ :not([hidden]) {
  border-top-width: 4px;
}

/* Now */
.divide-y-4 > :not(:last-child) {
  border-bottom-width: 4px;
}
```

You might see changes in your project if you were ever using these utilities with inline elements, if you were adding other margins/padding to child elements to tweak their spacing, or adjusting the borders of specific child elements.

### Using variants with gradients

In v3, overriding part of a gradient with a variant would "reset" the entire gradient, so in this example the `to-*` color would be transparent in dark mode instead of yellow:

```html
<!-- [!code filename:HTML] -->
<!-- [!code classes:dark:from-blue-500] -->
<div class="bg-gradient-to-r from-red-500 to-yellow-400 dark:from-blue-500">
  <!-- ... -->
</div>
```

In v4, these values are preserved which is more consistent with how other utilities in Tailwind work.

This means you may need to explicitly use `via-none` if you want to "unset" a three-stop gradient back to a two-stop gradient in a specific state:

```html
<!-- [!code filename:HTML] -->
<!-- [!code classes:dark:via-none] -->
<div class="bg-linear-to-r from-red-500 via-orange-400 to-yellow-400 dark:via-none dark:from-blue-500 dark:to-teal-400">
  <!-- ... -->
</div>
```

### Container configuration

In v3, the `container` utility had several configuration options like `center` and `padding` that no longer exist in v4.

To customize the `container` utility in v4, extend it using the `@utility` directive:

```css
/* [!code filename:CSS] */
@utility container {
  margin-inline: auto;
  padding-inline: 2rem;
}
```

### Default border color

In v3, the `border-*` and `divide-*` utilities used your configured `gray-200` color by default. We've changed this to `currentColor` in v4 to make Tailwind less opinionated and match browser defaults.

To update your project for this change, make sure you specify a color anywhere you're using a `border-*` or `divide-*` utility:

```html
<!-- [!code classes:border-gray-200] -->
<div class="border border-gray-200 px-2 py-3 ...">
  <!-- ... -->
</div>
```

Alternatively, add these base styles to your project to preserve the v3 behavior:

```css
/* [!code filename:CSS] */
@layer base {
  *,
  ::after,
  ::before,
  ::backdrop,
  ::file-selector-button {
    border-color: var(--color-gray-200, currentColor);
  }
}
```

### Default ring width and color

We've changed the width of the `ring` utility from 3px to 1px and changed the default color from `blue-500` to `currentColor` to make things more consistent the `border-*`, `divide-*`, and `outline-*` utilities.

To update your project for these changes, replace any use of `ring` with `ring-3`:

```html
<!-- prettier-ignore -->
<button class="focus:ring ..."> <!-- [!code --] -->
<button class="focus:ring-3 ..."> <!-- [!code ++] -->
  <!-- ... -->
</button>
```

Then make sure to add `ring-blue-500` anywhere you were depending on the default ring color:

```html
<!-- [!code classes:focus:ring-blue-500] -->
<button class="focus:ring-3 focus:ring-blue-500 ...">
  <!-- ... -->
</button>
```

Alternatively, add these theme variables to your CSS to preserve the v3 behavior:

```css
/* [!code filename:CSS] */
@theme {
  --default-ring-width: 3px;
  --default-ring-color: var(--color-blue-500);
}
```

Note though that these variables are only supported for compatibility reasons, and are not considered idiomatic usage of Tailwind CSS v4.0.

### Preflight changes

We've made a couple small changes to the base styles in Preflight in v4:

#### New default placeholder color

In v3, placeholder text used your configured `gray-400` color by default. We've simplified this in v4 to just use the current text color at 50% opacity.

You probably won't even notice this change (it might even make your project look better), but if you want to preserve the v3 behavior, add this CSS to your project:

```css
/* [!code filename:CSS] */
@layer base {
  input::placeholder,
  textarea::placeholder {
    color: var(--color-gray-400);
  }
}
```

#### Buttons use the default cursor

Buttons now use `cursor: default` instead of `cursor: pointer` to match the default browser behavior.

If you'd like to continue using `cursor: pointer` by default, add these base styles to your CSS:

```css
/* [!code filename:CSS] */
@layer base {
  button:not(:disabled),
  [role="button"]:not(:disabled) {
    cursor: pointer;
  }
}
```

#### Dialog margins removed

Preflight now resets margins on `<dialog>` elements to be consistent with how other elements are reset.

If you still want dialogs to be centered by default, add this CSS to your project:

```css
/* [!code filename:CSS] */
@layer base {
  dialog {
    margin: auto;
  }
}
```

#### Hidden attribute takes priority

Display classes like `block` or `flex` no longer take priority over the `hidden` attribute on an element. Remove the `hidden` attribute if you want an element to be visible to the user. Note that this does not apply to `hidden="until-found"`.

### Using a prefix

Prefixes now look like variants and are always at the beginning of the class name:

```html
<!-- [!code classes:tw:bg-red-500,tw:flex,tw:hover:bg-red-600] -->
<div class="tw:flex tw:bg-red-500 tw:hover:bg-red-600">
  <!-- ... -->
</div>
```

When using a prefix, you should still configure your theme variables as if you aren't using a prefix:

```css {{ filename: "app.css" }}
@import "tailwindcss" prefix(tw);

@theme {
  --font-display: "Satoshi", "sans-serif";

  --breakpoint-3xl: 120rem;

  --color-avocado-100: oklch(0.99 0 0);
  --color-avocado-200: oklch(0.98 0.04 113.22);
  --color-avocado-300: oklch(0.94 0.11 115.03);

  /* ... */
}
```

The generated CSS variables _will_ include a prefix to avoid conflicts with any existing variables in your project:

```css {{ filename: "dist.css" }}
:root {
  --tw-font-display: "Satoshi", "sans-serif";

  --tw-breakpoint-3xl: 120rem;

  --tw-color-avocado-100: oklch(0.99 0 0);
  --tw-color-avocado-200: oklch(0.98 0.04 113.22);
  --tw-color-avocado-300: oklch(0.94 0.11 115.03);

  /* ... */
}
```

### The important modifier

In v3 you could mark a utility as important by placing an `!` at the beginning of the utility name (but after any variants). In v4 you should place the `!` at the very end of the class name instead:

```html
<!-- [!code classes:bg-red-500!,flex!,hover:bg-red-600/50!] -->
<div class="flex! bg-red-500! hover:bg-red-600/50!">
  <!-- ... -->
</div>
```

The old way is still supported for compatibility but is deprecated.

### Adding custom utilities

In v3, any custom classes you defined within `@layer utilities` or `@layer components` would get picked up by Tailwind as a true utility class and would automatically work with variants like `hover`, `focus`, or `lg` with the difference being that `@layer components` would always come first in the generated stylesheet.

In v4 we are using native cascade layers and no longer hijacking the `@layer` at-rule, so we've introduced the `@utility` API as a replacement:

```css
/* [!code filename:CSS] */
/* [!code --:6] */
@layer utilities {
  .tab-4 {
    tab-size: 4;
  }
}
/* [!code ++:4] */
@utility tab-4 {
  tab-size: 4;
}
```

Custom utilities are now also sorted based on the amount of properties they define. This means that component utilities like this `.btn` can be overwritten by other Tailwind utilities without additional configuration:

```css
/* [!code filename:CSS] */
/* [!code --:8] */
@layer components {
  .btn {
    border-radius: 0.5rem;
    padding: 0.5rem 1rem;
    background-color: ButtonFace;
  }
}
/* [!code ++:6] */
@utility btn {
  border-radius: 0.5rem;
  padding: 0.5rem 1rem;
  background-color: ButtonFace;
}
```

Learn more about registering custom utilities in the [adding custom utilities documentation](/docs/adding-custom-styles#adding-custom-utilities).

### Variant stacking order

In v3, stacked variants were applied from right to left, but in v4 we've updated them to apply left to right to look more like CSS syntax.

To update your project for this change, reverse the order of any order-sensitive stacked variants in your project:

```html
<!-- [!code filename:HTML] -->
<!-- [!code --:2] -->
<!-- prettier-ignore -->
<ul class="py-4 first:*:pt-0 last:*:pb-0">
<!-- [!code ++:2] -->
<ul class="py-4 *:first:pt-0 *:last:pb-0">
  <li>One</li>
  <li>Two</li>
  <li>Three</li>
</ul>
```

You likely have very few of these if any—the direct child variant (`*`) and any typography plugin variants (`prose-headings`) are the most likely ones you might be using, and even then it's only if you've stacked them with other variants.

### Variables in arbitrary values

In v3 you were able to use CSS variables as arbitrary values without `var()`, but recent updates to CSS mean that this can often be ambiguous, so we've changed the syntax for this in v4 to use parentheses instead of square brackets.

To update your project for this change, replace usage of the old variable shorthand syntax with the new variable shorthand syntax:

```html
<!-- [!code filename:HTML] -->
<!-- [!code --:2] -->
<div class="bg-[--brand-color]"></div>
<!-- [!code ++:2] -->
<div class="bg-(--brand-color)"></div>
```

### Arbitrary values in grid and object-position utilities

Commas were previously replaced with spaces in the `grid-cols-*`, `grid-rows-*`, and `object-*` utilities inside arbitrary values. This special behavior existed in Tailwind CSS v3 for compatibility with v2. This compatibility no longer exists in v4.0 and underscores must be used to represent spaces.

To update your project for this change, replace usage of commas that were intended to be spaces with underscores:

```html
<!-- [!code filename:HTML] -->
<!-- [!code --:2] -->
<div class="grid-cols-[max-content,auto]"></div>
<!-- [!code ++:2] -->
<div class="grid-cols-[max-content_auto]"></div>
```

### Hover styles on mobile

In v4 we've updated the `hover` variant to only apply when the primary input device supports hover:

```css
/* [!code filename:CSS] */
@media (hover: hover) {
  .hover\:underline:hover {
    text-decoration: underline;
  }
}
```

This can create problems if you've built your site in a way that depends on touch devices triggering hover on tap. If this is an issue for you, you can override the `hover` variant with your own variant that uses the old implementation:

```css
/* [!code filename:CSS] */
@custom-variant hover (&:hover);
```

Generally though we recommend treating hover functionality as an enhancement, and not depending on it for your site to work since touch devices don't truly have the ability to hover.

### Transitioning outline-color

The `transition` and `transition-colors` utilities now include the `outline-color` property.

This means if you were adding an outline with a custom color on focus, you will see the color transition from the default color. To avoid this, make sure you set the outline color unconditionally, or explicitly set it for both states:

```html
<!-- [!code filename:HTML] -->
<!-- [!code --:2] -->
<button class="transition hover:outline-2 hover:outline-cyan-500"></button>
<!-- [!code ++:2] -->
<button class="outline-cyan-500 transition hover:outline-2"></button>
```

### Individual transform properties

The `rotate-*`, `scale-*`, and `translate-*` utilities are now based on the individual `rotate`, `scale`, and `translate` properties in CSS. Normally this shouldn't affect the behavior but there's a couple of cases to look out for:

#### Resetting Transforms

You previously would've been able to "reset" your rotate, scale, and translate utilities via `transform-none`. This no longer works and you will need to reset the individual properties instead:

```html
<!-- [!code filename:HTML] -->
<!-- [!code --:2] -->
<button class="scale-150 focus:transform-none"></button>
<!-- [!code ++:2] -->
<button class="scale-150 focus:scale-none"></button>
```

#### Transitions

If you customize the list of transitioned properties and include `transform` (e.g. by writing `transition-[opacity,transform]`) then these utilities will no longer transition. To fix this, include the individual properties in the list. For example, if you want to transition changes when using `opacity-*` and `scale-*` utilities you should use `transition-[opacity,scale]` instead.

```html
<!-- [!code filename:HTML] -->
<!-- [!code --:2] -->
<button class="transition-[opacity,transform] hover:scale-150"></button>
<!-- [!code ++:2] -->
<button class="transition-[opacity,scale] hover:scale-150"></button>
```

### Disabling core plugins

In v3 there was a `corePlugins` option you could use to completely disable certain utilities in the framework. This is no longer supported in v4.

### Using the theme() function

Since v4 includes CSS variables for all of your theme values, we recommend using those variables instead of the `theme()` function whenever possible:

```css
/* [!code filename:CSS] */
.my-class {
  /* [!code --:2] */
  background-color: theme(colors.red.500);
  /* [!code ++:2] */
  background-color: var(--color-red-500);
}
```

For cases where you still need to use the `theme()` function (like in media queries where CSS variables aren't supported), you should use the CSS variable name instead of the old dot notation:

```css
/* [!code filename:CSS] */
@media (width >= theme(screens.xl)) { /* [!code --] */
@media (width >= theme(--breakpoint-xl)) { /* [!code ++] */
  /* ... */
}
```

### Using a JavaScript config file

JavaScript config files are still supported for backward compatibility, but they are no longer detected automatically in v4.

If you still need to use a JavaScript config file, you can load it explicitly using the `@config` directive:

```css
/* [!code filename:CSS] */
@config "../../tailwind.config.js";
```

The `corePlugins`, `safelist`, and `separator` options from the JavaScript-based config are not supported in v4.0. To safelist utilities in v4 use [`@source inline()`](/docs/detecting-classes-in-source-files#safelisting-specific-utilities).

### Theme values in JavaScript

In v3 we exported a `resolveConfig` function that you could use to turn your JavaScript-based config into a flat object that you could use in your other JavaScript.

We've removed this in v4 in hopes that people can use the CSS variables we generate directly instead, which is much simpler and will significantly reduce your bundle size.

For example, the popular [Motion](https://motion.dev/docs/react-quick-start) library for React lets you animate to and from CSS variable values:

```jsx
// [!code filename:JSX]
// [!code word:var(--color-blue-500)]
<motion.div animate={{ backgroundColor: "var(--color-blue-500)" }} />
```

If you need access to a resolved CSS variable value in JS, you can use `getComputedStyle` to get the value of a theme variable on the document root:

```js
// [!code filename:spaghetti.js]
let styles = getComputedStyle(document.documentElement);
let shadow = styles.getPropertyValue("--shadow-xl");
```

### Using @apply with Vue, Svelte, or CSS modules

In v4, stylesheets that are bundled separately from your main CSS file (e.g. CSS modules files, `<style>` blocks in Vue, Svelte, or Astro, etc.) do not have access to theme variables, custom utilities, and custom variants defined in other files.

To make these definitions available in these contexts, use [`@reference`](/docs/functions-and-directives#reference-directive) to import them without duplicating any CSS in your bundle:

```html
<!-- [!code filename:Vue] -->
<template>
  <h1>Hello world!</h1>
</template>

<style>
  /* [!code highlight:2] */
  @reference "../../app.css";

  h1 {
    @apply text-2xl font-bold text-red-500;
  }
</style>
```

Alternatively, you can use your CSS theme variables directly instead of using `@apply` at all, which will also improve performance since Tailwind won't need to process these styles:

```html
<!-- [!code filename:Vue] -->
<template>
  <h1>Hello world!</h1>
</template>

<style>
  h1 {
    /* [!code highlight:2] */
    color: var(--text-red-500);
  }
</style>
```

You can find more documentation on [using Tailwind with CSS modules](/docs/compatibility#css-modules).

### Using Sass, Less, and Stylus

Tailwind CSS v4.0 is not designed to be used with CSS preprocessors like Sass, Less, or Stylus. Think of Tailwind CSS itself as your preprocessor — you shouldn't use Tailwind with Sass for the same reason you wouldn't use Sass with Stylus. Because of this it is not possible to use Sass, Less, or Stylus for your stylesheets or `<style>` blocks in Vue, Svelte, Astro, etc.

Learn more in the [compatibility documentation](/docs/compatibility#sass-less-and-stylus).


---

## Source: src/app/(docs)/docs/installation/(tabs)/using-vite/page.tsx

import { Cta } from "@/components/cta";
import { type Step, Steps } from "@/components/installation-steps";
import dedent from "dedent";
import { Metadata } from "next";

export const metadata: Metadata = {
  title: "Installing Tailwind CSS with Vite",
  description:
    "Installing Tailwind CSS as a Vite plugin is the most seamless way to integrate it with frameworks like Laravel, SvelteKit, React Router, Nuxt, and SolidJS.",
  openGraph: {
    type: "article",
    title: "Installing with Vite",
    description: "Integrate Tailwind CSS with frameworks like Laravel, SvelteKit, React Router, and SolidJS.",
    images: "https://tailwindcss.com/api/og?path=/docs/installation/using-vite",
    url: "https://tailwindcss.com/docs/installation/using-vite",
  },
};

const steps: Step[] = [
  {
    title: "Create your project",
    body: (
      <p>
        Start by creating a new Vite project if you don’t have one set up already. The most common approach is to use{" "}
        <a href="https://vite.dev/guide/#scaffolding-your-first-vite-project">Create Vite</a>.
      </p>
    ),
    code: {
      name: "Terminal",
      lang: "shell",
      code: dedent`
        npm create vite@latest my-project
        cd my-project
      `,
    },
  },
  {
    title: "Install Tailwind CSS",
    body: (
      <p>
        Install <code>tailwindcss</code> and <code>@tailwindcss/vite</code> via npm.
      </p>
    ),
    code: {
      name: "Terminal",
      lang: "shell",
      code: dedent`
        npm install tailwindcss @tailwindcss/vite
      `,
    },
  },
  {
    title: "Configure the Vite plugin",
    body: (
      <p>
        Add the <code>@tailwindcss/vite</code> plugin to your Vite configuration.
      </p>
    ),
    code: {
      name: "vite.config.ts",
      lang: "js",
      code: dedent`
        import { defineConfig } from 'vite'
        // [!code highlight:2]
        import tailwindcss from '@tailwindcss/vite'

        export default defineConfig({
          plugins: [
            // [!code highlight:2]
            tailwindcss(),
          ],
        })
      `,
    },
  },
  {
    title: "Import Tailwind CSS",
    body: (
      <p>
        Add an <code>@import</code> to your CSS file that imports Tailwind CSS.
      </p>
    ),
    code: {
      name: "CSS",
      lang: "css",
      code: dedent`
        @import "tailwindcss";
      `,
    },
  },
  {
    title: "Start your build process",
    body: (
      <p>
        Run your build process with <code>npm run dev</code> or whatever command is configured in your{" "}
        <code>package.json</code> file.
      </p>
    ),
    code: {
      name: "Terminal",
      lang: "shell",
      code: dedent`
        npm run dev
      `,
    },
  },
  {
    title: "Start using Tailwind in your HTML",
    body: (
      <p>
        Make sure your compiled CSS is included in the <code>{"<head>"}</code>{" "}
        <em>(your framework might handle this for you)</em>, then start using Tailwind’s utility classes to style your
        content.
      </p>
    ),
    code: {
      name: "HTML",
      lang: "html",
      code: dedent`
        <!doctype html>
        <html>
        <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <!-- [!code highlight:2] -->
          <link href="/src/style.css" rel="stylesheet">
        </head>
        <body>
          <!-- [!code highlight:4] -->
          <h1 class="text-3xl font-bold underline">
            Hello world!
          </h1>
        </body>
        </html>
      `,
    },
  },
];

export default function Page() {
  return (
    <>
      <div id="content-wrapper" className="prose relative z-10 mb-10 max-w-3xl" data-content="true">
        <h3 data-title="true" className="sr-only">
          Installing Tailwind CSS as a Vite plugin
        </h3>
        <p>
          Installing Tailwind CSS as a Vite plugin is the most seamless way to integrate it with frameworks like
          Laravel, SvelteKit, React Router, Nuxt, and SolidJS.
        </p>
      </div>
      <Steps steps={steps} />
      <div className="my-4 md:my-16">
        <Cta label="Explore our framework guides" href="/docs/installation/framework-guides">
          <strong className="font-semibold text-gray-950 dark:text-white">Are you stuck?</strong> Setting up Tailwind
          with Vite can be a bit different across different build tools. Check our framework guides to see if we have
          more specific instructions for your particular setup.
        </Cta>
      </div>
    </>
  );
}


---

## Source: src/app/(docs)/docs/installation/framework-guides/adonisjs.tsx

import { css, js, shell, html, type Page, type Step, type Tile } from "./utils";
import Logo from "@/docs/img/guides/adonis.react.svg";
import LogoDark from "@/docs/img/guides/adonis-white.react.svg";

export let tile: Tile = {
  title: "AdonisJS",
  description: "A fully featured web framework for Node.js.",

  Logo,
  LogoDark,
};

export let page: Page = {
  title: "Install Tailwind CSS with AdonisJS",
  description: "Setting up Tailwind CSS in an AdonisJS project.",
};

export let steps: Step[] = [
  {
    title: "Create your project",
    body: (
      <p>
        Start by creating a new AdonisJS project if you don’t have one set up already. The most common approach is to
        use <a href="https://docs.adonisjs.com/guides/getting-started/installation">Create AdonisJS</a>.
      </p>
    ),
    code: {
      name: "Terminal",
      lang: "shell",
      code: shell`
        npm init adonisjs@latest my-project -- --kit=web
        cd my-project
      `,
    },
  },
  {
    title: "Install Tailwind CSS",
    body: (
      <p>
        Install <code>@tailwindcss/vite</code> and its peer dependencies via npm.
      </p>
    ),
    code: {
      name: "Terminal",
      lang: "shell",
      code: shell`
        npm install tailwindcss @tailwindcss/vite
      `,
    },
  },
  {
    title: "Configure Vite Plugin",
    body: (
      <p>
        Add the <code>@tailwindcss/vite</code> plugin to your Vite configuration.
      </p>
    ),
    code: {
      name: "vite.config.ts",
      lang: "ts",
      code: js`
        import { defineConfig } from 'vite'
        import adonisjs from '@adonisjs/vite/client'
        // [!code highlight:2]
        import tailwindcss from '@tailwindcss/vite'

        export default defineConfig({
          plugins: [
            // [!code highlight:2]
            tailwindcss(),
            adonisjs({
              // …
            }),
          ],
        })
      `,
    },
  },
  {
    title: "Import Tailwind CSS",
    body: (
      <p>
        Add an <code>@import</code> to <code>./resources/css/app.css</code> that imports Tailwind CSS's styles.
        Additionally, tell Tailwind CSS to scan your <code>resources/views</code> directory for utilities.
      </p>
    ),
    code: {
      name: "app.css",
      lang: "css",
      code: css`
        @import "tailwindcss";
        @source "../views";
      `,
    },
  },
  {
    title: "Start your build process",
    body: (
      <p>
        Run your build process with <code>npm run dev</code>.
      </p>
    ),
    code: {
      name: "Terminal",
      lang: "shell",
      code: "npm run dev",
    },
  },
  {
    title: "Start using Tailwind in your project",
    body: (
      <p>
        Make sure your compiled CSS is included in the <code>{"<head>"}</code> then start using Tailwind’s utility
        classes to style your content.
      </p>
    ),
    code: {
      name: "home.edge",
      lang: "edge",
      code: html`
        <!doctype html>
        <html>
          <head>
            <meta charset="utf-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <!-- [!code highlight:2] -->
            @vite(['resources/css/app.css', 'resources/js/app.js'])
          </head>
          <body>
            <!-- [!code highlight:4] -->
            <h1 class="text-3xl font-bold underline">
              <!-- prettier-ignore -->
              Hello world!
            </h1>
          </body>
        </html>
      `,
    },
  },
];


---

## Source: src/app/(docs)/docs/installation/framework-guides/angular.tsx

import { css, html, js, shell, Page, Step, Tile } from "./utils";
import Logo from "@/docs/img/guides/angular.react.svg";
import LogoDark from "@/docs/img/guides/angular-white.react.svg";

export let tile: Tile = {
  title: "Angular",
  description: "Platform for building mobile and desktop web applications.",
  Logo,
  LogoDark,
};

export let page: Page = {
  title: "Install Tailwind CSS with Angular",
  description: "Setting up Tailwind CSS in an Angular project.",
};

export let steps: Step[] = [
  {
    title: "Create your project",
    body: (
      <p>
        Start by creating a new Angular project if you don’t have one set up already. The most common approach is to use{" "}
        <a href="https://angular.dev/tools/cli/setup-local">Angular CLI</a>.
      </p>
    ),
    code: {
      name: "Terminal",
      lang: "shell",
      code: shell`
        ng new my-project --style css
        cd my-project
      `,
    },
  },
  {
    title: "Install Tailwind CSS",
    body: (
      <p>
        Install <code>@tailwindcss/postcss</code> and its peer dependencies via npm.
      </p>
    ),

    // NOTE: The `--force` flag is used to make sure the installation succeeds. Angular has a peer dependency on `tailwindcss` v3 which causes errors when installing `tailwindcss` v4.
    code: {
      name: "Terminal",
      lang: "shell",
      code: shell`
        npm install tailwindcss @tailwindcss/postcss postcss --force
      `,
    },
  },
  {
    title: "Configure PostCSS Plugins",
    body: (
      <p>
        Create a <code>.postcssrc.json</code> file in the root of your project and add the{" "}
        <code>@tailwindcss/postcss</code> plugin to your PostCSS configuration.
      </p>
    ),
    code: {
      name: ".postcssrc.json",
      lang: "js",
      code: js`
        {
          "plugins": {
            // [!code highlight:2]
            "@tailwindcss/postcss": {}
          }
        }
      `,
    },
  },
  {
    title: "Import Tailwind CSS",
    body: (
      <p>
        Add an <code>@import</code> to <code>./src/styles.css</code> that imports Tailwind CSS.
      </p>
    ),
    code: {
      name: "styles.css",
      lang: "css",
      code: css`
        @import "tailwindcss";
      `,
    },
  },
  {
    title: "Start your build process",
    body: (
      <p>
        Run your build process with <code>ng serve</code>.
      </p>
    ),
    code: {
      name: "Terminal",
      lang: "shell",
      code: shell`
        ng serve
      `,
    },
  },
  {
    title: "Start using Tailwind in your project",
    body: <p>Start using Tailwind’s utility classes to style your content.</p>,
    code: {
      name: "app.component.html",
      lang: "html",
      code: html`
        <!-- [!code highlight:4] -->
        <h1 class="text-3xl font-bold underline">
          <!-- prettier-ignore -->
          Hello world!
        </h1>
      `,
    },
  },
];


---

## Source: src/app/(docs)/docs/installation/framework-guides/astro.tsx

import { astro, css, js, Page, shell, Step, Tile } from "./utils";
import Logo from "@/docs/img/guides/astro.react.svg";
import LogoDark from "@/docs/img/guides/astro-white.react.svg";

export let tile: Tile = {
  title: "Astro",
  description: "The all-in-one web framework designed for speed.",
  Logo,
  LogoDark,
};

export let page: Page = {
  title: "Install Tailwind CSS with Astro",
  description: "Setting up Tailwind CSS in an Astro project.",
};

export let steps: Step[] = [
  {
    title: "Create your project",
    body: (
      <p>
        Start by creating a new Astro project if you don't have one set up already. The most common approach is to use{" "}
        <a href="https://docs.astro.build/en/install-and-setup/#install-from-the-cli-wizard">create astro</a>.
      </p>
    ),
    code: {
      name: "Terminal",
      lang: "shell",
      code: shell`
        npm create astro@latest my-project
        cd my-project
      `,
    },
  },
  {
    title: "Install Tailwind CSS",
    body: (
      <p>
        Install <code>@tailwindcss/vite</code> and its peer dependencies via npm.
      </p>
    ),
    code: {
      name: "Terminal",
      lang: "shell",
      code: shell`
        npm install tailwindcss @tailwindcss/vite
      `,
    },
  },
  {
    title: "Configure Vite Plugin",
    body: (
      <p>
        Add the <code>@tailwindcss/vite</code> plugin to your Vite plugins in your Astro config file.
      </p>
    ),
    code: {
      name: "astro.config.mjs",
      lang: "js",
      code: js`
        // @ts-check
        import { defineConfig } from "astro/config";
        // [!code highlight:2]
        import tailwindcss from "@tailwindcss/vite";

        // https://astro.build/config
        export default defineConfig({
          // [!code highlight:4]
          vite: {
            plugins: [tailwindcss()],
          },
        });
      `,
    },
  },
  {
    title: "Import Tailwind CSS",
    body: (
      <p>
        Create a <code>./src/styles/global.css</code> file and add an <code>@import</code> for Tailwind CSS.
      </p>
    ),
    code: {
      name: "global.css",
      lang: "css",
      code: css`
        @import "tailwindcss";
      `,
    },
  },
  {
    title: "Start your build process",
    body: (
      <p>
        Run your build process with <code>npm run dev</code>.
      </p>
    ),
    code: {
      name: "Terminal",
      lang: "shell",
      code: shell`
        npm run dev
      `,
    },
  },
  {
    title: "Start using Tailwind in your project",
    body: (
      <p>
        Start using Tailwind's utility classes to style your content while making sure to import the newly created CSS
        file.
      </p>
    ),
    code: {
      name: "index.astro",
      lang: "astro",
      code: astro`
        ---
        // [!code highlight:2]
        import "../styles/global.css";
        ---

        <!-- [!code highlight:4] -->
        <h1 class="text-3xl font-bold underline">
          Hello world!
        </h1>
      `,
    },
  },
];


---

## Source: src/app/(docs)/docs/installation/framework-guides/emberjs.tsx

import { css, handlebars, js, Page, shell, Step, Tile } from "./utils";
import Logo from "@/docs/img/guides/ember.react.svg";

export let tile: Tile = {
  title: "Ember.js",
  description: "A JavaScript framework for ambitious web developers.",
  Logo,
};

export let page: Page = {
  title: "Install Tailwind CSS with Ember.js",
  description: "Setting up Tailwind CSS in an Ember.js project.",
};

export let steps: Step[] = [
  {
    title: "Create your project",
    body: (
      <p>
        Start by creating a new Ember.js project if you don't have one set up already. The most common approach is to
        use{" "}
        <a href="https://guides.emberjs.com/release/getting-started/quick-start/#toc_create-a-new-application">
          Ember CLI
        </a>
        .
      </p>
    ),
    code: {
      name: "Terminal",
      lang: "shell",
      code: shell`
        npx ember-cli new my-project --embroider --no-welcome
        cd my-project
      `,
    },
  },
  {
    title: "Install Tailwind CSS",
    body: (
      <p>
        Using npm, install <code>@tailwindcss/postcss</code> and its peer dependencies, as well as{" "}
        <code>postcss-loader</code>.
      </p>
    ),
    code: {
      name: "Terminal",
      lang: "shell",
      code: shell`
        npm install tailwindcss @tailwindcss/postcss postcss postcss-loader
      `,
    },
  },
  {
    title: "Enable PostCSS support",
    body: (
      <p>
        In your <code>ember-cli-build.js</code> file, configure PostCSS to process your CSS files.
      </p>
    ),
    code: {
      name: "ember-cli-build.js",
      lang: "js",
      code: js`
        'use strict';

        const EmberApp = require('ember-cli/lib/broccoli/ember-app');

        module.exports = function (defaults) {
          const app = new EmberApp(defaults, {
            // Add options here
          });

          const { Webpack } = require('@embroider/webpack');
          return require('@embroider/compat').compatBuild(app, Webpack, {
            skipBabel: [
              {
                package: 'qunit',
              },
            ],
            // [!code highlight:22]
            packagerOptions: {
              webpackConfig: {
                module: {
                  rules: [
                    {
                      test: /\.css$/i,
                      use: ['postcss-loader'],
                    },
                  ],
                },
              },
            },
          });
        };
      `,
    },
  },
  {
    title: "Configure PostCSS Plugins",
    body: (
      <p>
        Create a <code>postcss.config.mjs</code> file in the root of your project and add the{" "}
        <code>@tailwindcss/postcss</code> plugin to your PostCSS configuration.
      </p>
    ),
    code: {
      name: "postcss.config.mjs",
      lang: "js",
      code: js`
        export default {
          plugins: {
            // [!code highlight:2]
            "@tailwindcss/postcss": {},
          },
        }
      `,
    },
  },
  {
    title: "Import Tailwind CSS",
    body: (
      <p>
        Create an <code>./app/app.css</code> file and add an <code>@import</code> for Tailwind CSS.
      </p>
    ),
    code: {
      name: "app.css",
      lang: "css",
      code: css`
        @import "tailwindcss";
      `,
    },
  },
  {
    title: "Import the CSS file",
    body: (
      <p>
        Import the newly-created <code>./app/app.css</code> file in your <code>./app/app.js</code> file.
      </p>
    ),
    code: {
      name: "app.js",
      lang: "js",
      code: js`
        import Application from '@ember/application';
        import Resolver from 'ember-resolver';
        import loadInitializers from 'ember-load-initializers';
        import config from 'my-project/config/environment';
        // [!code highlight:2]
        import 'my-project/app.css';

        export default class App extends Application {
          modulePrefix = config.modulePrefix;
          podModulePrefix = config.podModulePrefix;
          Resolver = Resolver;
        }

        loadInitializers(App, config.modulePrefix);
      `,
    },
  },
  {
    title: "Start your build process",
    body: (
      <p>
        Run your build process with <code>npm run start</code>.
      </p>
    ),
    code: {
      name: "Terminal",
      lang: "shell",
      code: shell`
        npm run start
      `,
    },
  },
  {
    title: "Start using Tailwind in your project",
    body: <p>Start using Tailwind's utility classes to style your content.</p>,
    code: {
      name: "application.hbs",
      lang: "hbs",
      code: handlebars`
        {{page-title "MyProject"}}

        <!-- [!code highlight:4] -->
        <h1 class="text-3xl font-bold underline">
          Hello world!
        </h1>

        {{outlet}}
      `,
    },
  },
];


---

## Source: src/app/(docs)/docs/installation/framework-guides/gatsby.tsx

import { astro, css, js, Page, shell, Step, Tile } from "./utils";
import Logo from "@/docs/img/guides/gatsby.react.svg";

export let tile: Tile = {
  title: "Gatsby",
  description: "Framework for building static sites with React and GraphQL.",
  Logo,
};

export let page: Page = {
  title: "Install Tailwind CSS with Gatsby",
  description: "Setting up Tailwind CSS in a Gatsby project.",
};

export let steps: Step[] = [
  {
    title: "Create your project",
    body: (
      <p>
        Start by creating a new Gatsby project if you don’t have one set up already. The most common approach is to use{" "}
        <a href="https://www.gatsbyjs.com/docs/reference/gatsby-cli/#how-to-use-gatsby-cli">Gatsby CLI</a>.
      </p>
    ),
    code: {
      name: "Terminal",
      lang: "shell",
      code: shell`
        gatsby new my-project
        cd my-project
      `,
    },
  },
  {
    title: "Install Tailwind CSS",
    body: (
      <p>
        Using npm, install <code>@tailwindcss/postcss</code>, its peer dependencies, and{" "}
        <code>gatsby-plugin-postcss</code>.
      </p>
    ),
    code: {
      name: "Terminal",
      lang: "shell",
      code: shell`
        npm install @tailwindcss/postcss tailwindcss postcss gatsby-plugin-postcss
      `,
    },
  },
  {
    title: "Enable the Gatsby PostCSS plugin",
    body: (
      <p>
        In your <code>gatsby-config.js</code> file, enable <code>gatsby-plugin-postcss</code>. See{" "}
        <a href="https://www.gatsbyjs.com/plugins/gatsby-plugin-postcss/">the plugin's documentation</a> for more
        information.
      </p>
    ),
    code: {
      name: "gatsby-config.js",
      lang: "js",
      code: js`
        module.exports = {
          plugins: [
            // [!code highlight:2]
            'gatsby-plugin-postcss',
            // ...
          ],
        }
      `,
    },
  },
  {
    title: "Configure PostCSS Plugins",
    body: (
      <p>
        Create a <code>postcss.config.js</code> file in the root of your project and add the{" "}
        <code>@tailwindcss/postcss</code> plugin to your PostCSS configuration.
      </p>
    ),
    code: {
      name: "postcss.config.js",
      lang: "js",
      code: js`
        module.exports = {
          plugins: {
            // [!code highlight:2]
            "@tailwindcss/postcss": {},
          },
        };
      `,
    },
  },
  {
    title: "Import Tailwind CSS",
    body: (
      <p>
        Create a <code>./src/styles/global.css</code> file and add an <code>@import</code> for Tailwind CSS.
      </p>
    ),
    code: {
      name: "global.css",
      lang: "css",
      code: css`
        @import "tailwindcss";
      `,
    },
  },
  {
    title: "Import the CSS file",
    body: (
      <p>
        Create a <code>gatsby-browser.js</code> file at the root of your project if it doesn’t already exist, and import
        your newly-created <code>./src/styles/global.css</code> file.
      </p>
    ),
    code: {
      name: "gatsby-browser.js",
      lang: "js",
      code: js`
        import './src/styles/global.css';
      `,
    },
  },
  {
    title: "Start your build process",
    body: (
      <p>
        Run your build process with <code>gatsby develop</code>.
      </p>
    ),
    code: {
      name: "Terminal",
      lang: "shell",
      code: shell`
        gatsby develop
      `,
    },
  },
  {
    title: "Start using Tailwind in your project",
    body: <p>Start using Tailwind’s utility classes to style your content.</p>,
    code: {
      name: "index.js",
      lang: "js",
      code: js`
        export default function IndexPage() {
          return (
            <Layout>
              /* [!code highlight:4] */
              <h1 className="text-3xl font-bold underline">
                Hello world!
              </h1>
            </Layout>
          )
        }
      `,
    },
  },
];


---

## Source: src/app/(docs)/docs/installation/framework-guides/laravel.tsx

import { css, html, js, Page, shell, Step, Tab, Tile } from "./utils";
import Logo from "@/docs/img/guides/laravel.react.svg";

export let tile: Tile = {
  title: "Laravel",
  description: "PHP web application framework with expressive, elegant syntax.",
  Logo,
};

export let page: Page = {
  title: "Install Tailwind CSS with Laravel",
  description: "Setting up Tailwind CSS in a Laravel project.",
};

export let tabs: Tab[] = [
  {
    slug: "vite",
    title: "Using Vite",
  },
  {
    slug: "mix",
    title: "Using Laravel Mix",
  },
];

export let steps: Step[] = [
  {
    tabs: ["vite"],
    title: "Create your project",
    body: (
      <p>
        Start by creating a new Laravel project if you don’t have one set up already. The most common approach is to use{" "}
        <a href="https://laravel.com/docs#creating-an-application">the Laravel installer</a>.
      </p>
    ),
    code: {
      name: "Terminal",
      lang: "shell",
      code: shell`
        laravel new my-project
        cd my-project
      `,
    },
  },

  {
    tabs: ["vite"],
    title: "Install Tailwind CSS",
    body: (
      <p>
        Install <code>@tailwindcss/vite</code> and its peer dependencies via npm.
      </p>
    ),
    code: {
      name: "Terminal",
      lang: "shell",
      code: shell`
        npm install tailwindcss @tailwindcss/vite
      `,
    },
  },
  {
    tabs: ["mix"],
    title: "Install Tailwind CSS",
    body: (
      <p>
        Install <code>@tailwindcss/postcss</code> and its peer dependencies via npm.
      </p>
    ),
    code: {
      name: "Terminal",
      lang: "shell",
      code: shell`
        npm install tailwindcss @tailwindcss/postcss postcss
      `,
    },
  },

  {
    tabs: ["vite"],
    title: "Configure Vite Plugin",
    body: (
      <p>
        Add the <code>@tailwindcss/vite</code> plugin to your Vite configuration.
      </p>
    ),
    code: {
      name: "vite.config.ts",
      lang: "ts",
      code: js`
        import { defineConfig } from 'vite'
        // [!code highlight:2]
        import tailwindcss from '@tailwindcss/vite'

        export default defineConfig({
          plugins: [
            // [!code highlight:2]
            tailwindcss(),
            // …
          ],
        })
      `,
    },
  },

  {
    tabs: ["mix"],
    title: "Add Tailwind to your Laravel Mix configuration",
    body: (
      <p>
        In your <code>webpack.mix.js</code> file, add <code>tailwindcss</code> as a PostCSS plugin.
      </p>
    ),
    code: {
      name: "webpack.mix.js",
      lang: "js",
      code: js`
        mix
          .js("resources/js/app.js", "public/js")
          .postCss("resources/css/app.css", "public/css", [
            // [!code highlight:2]
            require("@tailwindcss/postcss"),
          ]);
      `,
    },
  },

  {
    title: "Import Tailwind CSS",
    body: (
      <p>
        Add an <code>@import</code> to <code>./resources/css/app.css</code> that imports Tailwind CSS. Additionally,
        tell Tailwind CSS to scan some directories for utilities.
      </p>
    ),
    code: {
      name: "app.css",
      lang: "css",
      code: css`
        @import "tailwindcss";

        @source "../../vendor/laravel/framework/src/Illuminate/Pagination/resources/views/*.blade.php";
        @source "../../storage/framework/views/*.php";
        @source "../**/*.blade.php";
        @source "../**/*.js";
      `,
    },
  },

  {
    tabs: ["vite"],
    title: "Start your build process",
    body: (
      <p>
        Run your build process with <code>npm run dev</code>.
      </p>
    ),
    code: {
      name: "Terminal",
      lang: "shell",
      code: shell`
        npm run dev
      `,
    },
  },

  {
    tabs: ["mix"],
    title: "Start your build process",
    body: (
      <p>
        Run your build process with <code>npm run watch</code>.
      </p>
    ),
    code: {
      name: "Terminal",
      lang: "shell",
      code: shell`
        npm run watch
      `,
    },
  },

  {
    tabs: ["vite"],
    title: "Start using Tailwind in your project",
    body: (
      <p>
        Make sure your compiled CSS is included in the <code>{"<head>"}</code> then start using Tailwind’s utility
        classes to style your content.
      </p>
    ),
    code: {
      name: "app.blade.php",
      lang: "blade",
      code: html`
        <!doctype html>
        <html>
          <head>
            <meta charset="utf-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <!-- [!code highlight:2] -->
            @vite('resources/css/app.css')
          </head>
          <body>
            <!-- [!code highlight:4] -->
            <h1 class="text-3xl font-bold underline">
              <!-- prettier-ignore -->
              Hello world!
            </h1>
          </body>
        </html>
      `,
    },
  },
  {
    tabs: ["mix"],
    title: "Start using Tailwind in your project",
    body: (
      <p>
        Make sure your compiled CSS is included in the <code>{"<head>"}</code> then start using Tailwind’s utility
        classes to style your content.
      </p>
    ),
    code: {
      name: "app.blade.php",
      lang: "blade",
      code: html`
        <!doctype html>
        <html>
          <head>
            <meta charset="utf-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <!-- [!code highlight:2] -->
            <link href="{{ asset('css/app.css') }}" rel="stylesheet" />
          </head>
          <body>
            <!-- [!code highlight:4] -->
            <h1 class="text-3xl font-bold underline">
              <!-- prettier-ignore -->
              Hello world!
            </h1>
          </body>
        </html>
      `,
    },
  },
];


---

## Source: src/app/(docs)/docs/installation/framework-guides/meteor.tsx

import { css, js, Page, shell, Step, Tile } from "./utils";
import Logo from "@/docs/img/guides/meteor.react.svg";

export let tile: Tile = {
  title: "Meteor",
  description: "The full stack JavaScript framework for developing cross-platform apps.",
  Logo,
};

export let page: Page = {
  title: "Install Tailwind CSS with Meteor",
  description: "Setting up Tailwind CSS in a Meteor project.",
};

export let steps: Step[] = [
  {
    title: "Create your project",
    body: (
      <p>
        Start by creating a new Meteor project if you don't have one set up already. The most common approach is to use{" "}
        <a href="https://docs.meteor.com/about/install.html">the Meteor CLI</a>.
      </p>
    ),
    code: {
      name: "Terminal",
      lang: "shell",
      code: shell`
        npx meteor create my-project
        cd my-project
      `,
    },
  },
  {
    title: "Install Tailwind CSS",
    body: (
      <p>
        Install <code>@tailwindcss/postcss</code> and its peer dependencies via npm.
      </p>
    ),
    code: {
      name: "Terminal",
      lang: "shell",
      code: shell`
        npm install tailwindcss @tailwindcss/postcss postcss postcss-load-config
      `,
    },
  },
  {
    title: "Configure PostCSS Plugins",
    body: (
      <p>
        Create a <code>postcss.config.mjs</code> file in the root of your project and add the{" "}
        <code>@tailwindcss/postcss</code> plugin to your PostCSS configuration.
      </p>
    ),
    code: {
      name: "postcss.config.mjs",
      lang: "js",
      code: js`
        export default {
          plugins: {
            // [!code highlight:2]
            "@tailwindcss/postcss": {},
          },
        };
      `,
    },
  },
  {
    title: "Import Tailwind CSS",
    body: (
      <p>
        Add an <code>@import</code> for Tailwind CSS to your <code>./client/main.css</code> file.
      </p>
    ),
    code: {
      name: "main.css",
      lang: "css",
      code: css`
        @import "tailwindcss";
      `,
    },
  },
  {
    title: "Start your build process",
    body: (
      <p>
        Run your build process with <code>npm run start</code>.
      </p>
    ),
    code: {
      name: "Terminal",
      lang: "shell",
      code: shell`
        npm run start
      `,
    },
  },
  {
    title: "Start using Tailwind in your project",
    body: <p>Start using Tailwind’s utility classes to style your content.</p>,
    code: {
      name: "App.jsx",
      lang: "jsx",
      code: js`
        export const App = () => (
          // [!code highlight:4]
          <h1 className="text-3xl font-bold underline">
            Hello world!
          </h1>
        )
      `,
    },
  },
];


---

## Source: src/app/(docs)/docs/installation/framework-guides/nextjs.tsx

import { css, js, shell, Page, Step, Tile } from "./utils";
import Logo from "@/docs/img/guides/nextjs.react.svg";
import LogoDark from "@/docs/img/guides/nextjs-white.react.svg";

export let tile: Tile = {
  title: "Next.js",
  description: "Full-featured React framework with great developer experience.",
  Logo,
  LogoDark,
};

export let page: Page = {
  title: "Install Tailwind CSS with Next.js",
  description: "Setting up Tailwind CSS in a Next.js project.",
};

export let steps: Step[] = [
  {
    title: "Create your project",
    body: (
      <p>
        Start by creating a new Next.js project if you don’t have one set up already. The most common approach is to use{" "}
        <a href="https://nextjs.org/docs/api-reference/create-next-app">Create Next App</a>.
      </p>
    ),
    code: {
      name: "Terminal",
      lang: "shell",
      code: shell`
        npx create-next-app@latest my-project --typescript --eslint --app
        cd my-project
      `,
    },
  },
  {
    title: "Install Tailwind CSS",
    body: (
      <p>
        Install <code>@tailwindcss/postcss</code> and its peer dependencies via npm.
      </p>
    ),
    code: {
      name: "Terminal",
      lang: "shell",
      code: shell`
        npm install tailwindcss @tailwindcss/postcss postcss
      `,
    },
  },
  {
    title: "Configure PostCSS Plugins",
    body: (
      <p>
        Create a <code>postcss.config.mjs</code> file in the root of your project and add the{" "}
        <code>@tailwindcss/postcss</code> plugin to your PostCSS configuration.
      </p>
    ),
    code: {
      name: "postcss.config.mjs",
      lang: "js",
      code: js`
        const config = {
          plugins: {
            // [!code highlight:2]
            "@tailwindcss/postcss": {},
          },
        };

        export default config;
      `,
    },
  },
  {
    title: "Import Tailwind CSS",
    body: (
      <p>
        Add an <code>@import</code> to <code>./app/globals.css</code> that imports Tailwind CSS.
      </p>
    ),
    code: {
      name: "globals.css",
      lang: "css",
      code: css`
        @import "tailwindcss";
      `,
    },
  },
  {
    title: "Start your build process",
    body: (
      <p>
        Run your build process with <code>npm run dev</code>.
      </p>
    ),
    code: {
      name: "Terminal",
      lang: "shell",
      code: shell`
        npm run dev
      `,
    },
  },
  {
    title: "Start using Tailwind in your project",
    body: <p>Start using Tailwind’s utility classes to style your content.</p>,
    code: {
      name: "page.tsx",
      lang: "jsx",
      code: js`
        export default function Home() {
          return (
            // [!code highlight:4]
            <h1 className="text-3xl font-bold underline">
              Hello world!
            </h1>
          )
        }
      `,
    },
  },
];


---

## Source: src/app/(docs)/docs/installation/framework-guides/nuxtjs.tsx

import { css, html, js, Page, shell, Step, Tile } from "./utils";
import Logo from "@/docs/img/guides/nuxtjs.react.svg";

export let tile: Tile = {
  title: "Nuxt",
  description: "Intuitive Vue framework for building universal applications.",
  Logo,
};

export let page: Page = {
  title: "Install Tailwind CSS with Nuxt",
  description: "Setting up Tailwind CSS in a Nuxt project.",
};

export let steps: Step[] = [
  {
    title: "Create your project",
    body: (
      <p>
        Start by creating a new Nuxt project if you don’t have one set up already. The most common approach is to use{" "}
        <a href="https://nuxt.com/docs/4.x/getting-started/installation#new-project">Create Nuxt</a>.
      </p>
    ),
    code: {
      name: "Terminal",
      lang: "shell",
      code: shell`
        npm create nuxt my-project
        cd my-project
      `,
    },
  },
  {
    title: "Install Tailwind CSS",
    body: (
      <p>
        Install <code>@tailwindcss/vite</code> and its peer dependencies via npm.
      </p>
    ),
    code: {
      name: "Terminal",
      lang: "shell",
      code: shell`
        npm install tailwindcss @tailwindcss/vite
      `,
    },
  },
  {
    title: "Configure Vite Plugin",
    body: (
      <p>
        Add the <code>@tailwindcss/vite</code> plugin to your Nuxt configuration as a Vite plugin.
      </p>
    ),
    code: {
      name: "nuxt.config.ts",
      lang: "ts",
      code: js`
        // [!code highlight:2]
        import tailwindcss from "@tailwindcss/vite";

        export default defineNuxtConfig({
          compatibilityDate: "2025-07-15",
          devtools: { enabled: true },
          vite: {
            plugins: [
              // [!code highlight:2]
              tailwindcss(),
            ],
          },
        });
      `,
    },
  },
  {
    title: "Import Tailwind CSS",
    body: (
      <p>
        Create an <code>./app/assets/css/main.css</code> file and add an <code>@import</code> that imports Tailwind CSS.
      </p>
    ),
    code: {
      name: "main.css",
      lang: "css",
      code: css`
        @import "tailwindcss";
      `,
    },
  },
  {
    title: "Add the CSS file globally",
    body: (
      <p>
        Add your newly-created <code>./app/assets/css/main.css</code> to the <code>css</code> array in your{" "}
        <code>nuxt.config.ts</code> file.
      </p>
    ),
    code: {
      name: "nuxt.config.ts",
      lang: "ts",
      code: js`
        import tailwindcss from "@tailwindcss/vite";

        export default defineNuxtConfig({
          compatibilityDate: "2025-07-15",
          devtools: { enabled: true },
          // [!code highlight:2]
          css: ['./app/assets/css/main.css'],
          vite: {
            plugins: [
              tailwindcss(),
            ],
          },
        });
      `,
    },
  },
  {
    title: "Start your build process",
    body: (
      <p>
        Run your build process with <code>npm run dev</code>.
      </p>
    ),
    code: {
      name: "Terminal",
      lang: "shell",
      code: shell`
        npm run dev
      `,
    },
  },
  {
    title: "Start using Tailwind in your project",
    body: <p>Start using Tailwind’s utility classes to style your content.</p>,
    code: {
      name: "app.vue",
      lang: "vue",
      code: html`
        <template>
          <!-- [!code highlight:4] -->
          <h1 class="text-3xl font-bold underline">
            <!-- prettier-ignore -->
            Hello world!
          </h1>
        </template>
      `,
    },
  },
];


---

## Source: src/app/(docs)/docs/installation/framework-guides/parcel.tsx

import { css, html, js, Page, shell, Step, Tile } from "./utils";
import Logo from "@/docs/img/guides/parcel.react.svg";

export let tile: Tile = {
  title: "Parcel",
  description: "The zero-configuration build tool for the web.",
  Logo,
};

export let page: Page = {
  title: "Install Tailwind CSS with Parcel",
  description: "Setting up Tailwind CSS in a Parcel project.",
};

export let steps: Step[] = [
  {
    title: "Create your project",
    body: (
      <p>
        Start by creating a new Parcel project if you don’t have one set up already. The most common approach is to add
        Parcel as a dev-dependency to your project as outlined in their{" "}
        <a href="https://parceljs.org/getting-started/webapp/">getting started guide</a>.
      </p>
    ),
    code: {
      name: "Terminal",
      lang: "shell",
      code: shell`
        mkdir my-project
        cd my-project
        npm init -y
        npm install parcel
        mkdir src
        touch src/index.html
      `,
    },
  },
  {
    title: "Install Tailwind CSS",
    body: (
      <p>
        Install <code>@tailwindcss/postcss</code> and its peer dependencies via npm.
      </p>
    ),
    code: {
      name: "Terminal",
      lang: "shell",
      code: shell`
        npm install tailwindcss @tailwindcss/postcss
      `,
    },
  },
  {
    title: "Configure PostCSS",
    body: (
      <p>
        Create a <code>.postcssrc</code> file in your project root, and enable the <code>@tailwindcss/postcss</code>{" "}
        plugin.
      </p>
    ),
    code: {
      name: ".postcssrc",
      lang: "json",
      code: js`
        {
          "plugins": {
            "@tailwindcss/postcss": {}
          }
        }
      `,
    },
  },
  {
    title: "Import Tailwind CSS",
    body: (
      <p>
        Create a <code>./src/index.css</code> file and add an <code>@import</code> for Tailwind CSS.
      </p>
    ),
    code: {
      name: "index.css",
      lang: "css",
      code: css`
        @import "tailwindcss";
      `,
    },
  },
  {
    title: "Start your build process",
    body: (
      <p>
        Run your build process with <code>npx parcel src/index.html</code>.
      </p>
    ),
    code: {
      name: "Terminal",
      lang: "shell",
      code: shell`
        npx parcel src/index.html
      `,
    },
  },
  {
    title: "Start using Tailwind in your project",
    body: (
      <p>
        Add your CSS file to the <code>{"<head>"}</code> and start using Tailwind’s utility classes to style your
        content.
      </p>
    ),
    code: {
      name: "index.html",
      lang: "html",
      code: html`
        <!doctype html>
        <html>
          <head>
            <meta charset="UTF-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <!-- [!code highlight:2] -->
            <link href="./index.css" type="text/css" rel="stylesheet" />
          </head>
          <body>
            <!-- [!code highlight:4] -->
            <h1 class="text-3xl font-bold underline">
              <!-- prettier-ignore -->
              Hello world!
            </h1>
          </body>
        </html>
      `,
    },
  },
];


---

## Source: src/app/(docs)/docs/installation/framework-guides/phoenix.tsx

import { css, elixir, html, js, Page, shell, Step, Tile } from "./utils";
import Logo from "@/docs/img/guides/phoenix.react.svg";

export let tile: Tile = {
  title: "Phoenix",
  description: "A framework to build rich, interactive applications with Elixir.",
  Logo,
};

export let page: Page = {
  title: "Install Tailwind CSS with Phoenix",
  description: "Setting up Tailwind CSS in a Phoenix project.",
};

export let steps: Step[] = [
  {
    title: "Create your project",
    body: (
      <p>
        Start by creating a new Phoenix project if you don't have one set up already. You can follow their{" "}
        <a href="https://hexdocs.pm/phoenix/installation.html">installation guide</a> to get up and running.
      </p>
    ),
    code: {
      name: "Terminal",
      lang: "shell",
      code: shell`
        mix phx.new myproject
        cd myproject
      `,
    },
  },
  {
    title: "Install the Tailwind plugin",
    body: (
      <p>
        Add the Tailwind plugin to your dependencies and run <code>mix deps.get</code> to install it.
      </p>
    ),
    code: {
      name: "mix.exs",
      lang: "elixir",
      code: elixir`
        defp deps do
          [
            # …
            # [!code highlight:2]
            {:tailwind, "~> 0.3", runtime: Mix.env() == :dev},
          ]
        end
      `,
    },
  },
  {
    title: "Configure the Tailwind plugin",
    body: (
      <p>
        In your <code>config/config.exs</code> file you can set which version of Tailwind CSS you want to use and
        customize your asset paths.
      </p>
    ),
    code: {
      name: "config.exs",
      lang: "elixir",
      code: elixir`
        config :tailwind,
          # [!code highlight:2]
          version: "4.1.10",
          myproject: [
            args: ~w(
              # [!code highlight:3]
              --input=assets/css/app.css
              --output=priv/static/assets/app.css
            ),
            # [!code highlight:2]
            cd: Path.expand("..", __DIR__)
          ]
      `,
    },
  },
  {
    title: "Update your deployment script",
    body: (
      <p>
        Configure your <code>assets.deploy</code> alias to build your CSS on deployment.
      </p>
    ),
    code: {
      name: "mix.exs",
      lang: "elixir",
      code: elixir`
        defp aliases do
          [
            # …
            "assets.deploy": [
              # [!code highlight:2]
              "tailwind myproject --minify",
              "esbuild myproject --minify",
              "phx.digest"
            ]
          ]
        end
      `,
    },
  },
  {
    title: "Enable watcher in development",
    body: (
      <p>
        Add Tailwind to your list of watchers in your <code>./config/dev.exs</code> file.
      </p>
    ),
    code: {
      name: "dev.exs",
      lang: "elixir",
      code: elixir`
        watchers: [
          # Start the esbuild watcher by calling Esbuild.install_and_run(:default, args)
          esbuild: {Esbuild, :install_and_run, [:myproject, ~w(--sourcemap=inline --watch)]},
          # [!code highlight:2]
          tailwind: {Tailwind, :install_and_run, [:myproject, ~w(--watch)]}
        ]
      `,
    },
  },
  {
    title: "Install Tailwind CSS",
    body: <p>Run the install command to download the standalone Tailwind CLI.</p>,
    code: {
      name: "Terminal",
      lang: "shell",
      code: shell`
        mix tailwind.install
      `,
    },
  },
  {
    title: "Import Tailwind CSS",
    body: (
      <p>
        Add an <code>@import</code> to <code>./assets/css/app.css</code> that imports Tailwind CSS.
      </p>
    ),
    code: {
      name: "app.css",
      lang: "css",
      code: css`
        @import "tailwindcss";
      `,
    },
  },
  {
    title: "Remove the default CSS import",
    body: (
      <p>
        Remove the CSS import from <code>./assets/js/app.js</code>, as Tailwind is now handling this for you.
      </p>
    ),
    code: {
      name: "app.js",
      lang: "js",
      code: js`
        // [!code --:3]
        // Remove this line if you add your own CSS build pipeline (e.g postcss).
        import "../css/app.css"
      `,
    },
  },
  {
    title: "Start your build process",
    body: (
      <p>
        Run your build process with <code>mix phx.server</code>.
      </p>
    ),
    code: {
      name: "Terminal",
      lang: "shell",
      code: shell`
        mix phx.server
      `,
    },
  },
  {
    title: "Start using Tailwind in your project",
    body: <p>Start using Tailwind’s utility classes to style your content.</p>,
    code: {
      name: "index.html.heex",
      lang: "html",
      code: html`
        <!-- [!code highlight:4] -->
        <h1 class="text-3xl font-bold underline">
          <!-- prettier-ignore -->
          Hello world!
        </h1>
      `,
    },
  },
];


---

## Source: src/app/(docs)/docs/installation/framework-guides/qwik.tsx

import { css, js, Page, shell, Step, Tile } from "./utils";
import Logo from "@/docs/img/guides/qwik.react.svg";

export let tile: Tile = {
  title: "Qwik",
  description: "Build instantly-interactive web apps without effort.",
  Logo,
};

export let page: Page = {
  title: "Install Tailwind CSS with Qwik",
  description: "Setting up Tailwind CSS in an Qwik project.",
};

export let steps: Step[] = [
  {
    title: "Create your project",
    body: (
      <p>
        Start by creating a new Qwik project if you don't have one set up already. The most common approach is to use{" "}
        <a href="https://qwik.dev/docs/getting-started/#create-an-app-using-the-cli">Create Qwik</a>.
      </p>
    ),
    code: {
      name: "Terminal",
      lang: "shell",
      code: shell`
        npm create qwik@latest empty my-project
        cd my-project
      `,
    },
  },
  {
    title: "Install Tailwind CSS",
    body: (
      <p>
        Install <code>@tailwindcss/vite</code> and its peer dependencies via npm.
      </p>
    ),
    code: {
      name: "Terminal",
      lang: "shell",
      code: shell`
        npm install tailwindcss @tailwindcss/vite
      `,
    },
  },
  {
    title: "Configure Vite Plugin",
    body: (
      <p>
        Add the <code>@tailwindcss/vite</code> plugin to your Vite configuration.
      </p>
    ),
    code: {
      name: "vite.config.ts",
      lang: "ts",
      code: js`
        import { defineConfig } from 'vite'
        import { qwikVite } from "@builder.io/qwik/optimizer";
        import { qwikCity } from "@builder.io/qwik-city/vite";
        // …

        // [!code highlight:2]
        import tailwindcss from '@tailwindcss/vite'

        export default defineConfig(({ command, mode }): UserConfig => {
          return {
            plugins: [
              // [!code highlight:2]
              tailwindcss(),
              qwikCity(),
              qwikVite(),
              tsconfigPaths(),
            ],

            // …
          }
        })
      `,
    },
  },
  {
    title: "Import Tailwind CSS",
    body: (
      <p>
        Add an <code>@import</code> to <code>./src/global.css</code> that imports Tailwind CSS.
      </p>
    ),
    code: {
      name: "global.css",
      lang: "css",
      code: css`
        @import "tailwindcss";
      `,
    },
  },
  {
    title: "Start your build process",
    body: (
      <p>
        Run your build process with <code>npm run dev</code>.
      </p>
    ),
    code: {
      name: "Terminal",
      lang: "shell",
      code: shell`
        npm run dev
      `,
    },
  },
  {
    title: "Start using Tailwind in your project",
    body: <p>Start using Tailwind’s utility classes to style your content.</p>,
    code: {
      name: "index.tsx",
      lang: "tsx",
      code: js`
        import { component$ } from '@builder.io/qwik'

        export default component$(() => {
          return (
            // [!code highlight:4]
            <h1 class="text-3xl font-bold underline">
              Hello World!
            </h1>
          )
        })
      `,
    },
  },
];


---

## Source: src/app/(docs)/docs/installation/framework-guides/react-router.tsx

import { css, js, Page, shell, Step, Tile } from "./utils";
import Logo from "@/docs/img/guides/react-router.react.svg";
import LogoDark from "@/docs/img/guides/react-router-white.react.svg";

export let tile: Tile = {
  title: "React Router",
  description: "A standards‑focused router you can deploy anywhere.",
  Logo,
  LogoDark,
};

export let page: Page = {
  title: "Install Tailwind CSS with React Router",
  description: "Setting up Tailwind CSS in a React Router project.",
};

export let steps: Step[] = [
  {
    title: "Create your project",
    body: (
      <p>
        Start by creating a new React Router project if you don’t have one set up already. The most common approach is
        to use <a href="https://reactrouter.com/start/framework/installation">Create React Router</a>.
      </p>
    ),
    code: {
      name: "Terminal",
      lang: "shell",
      code: shell`
        npx create-react-router@latest my-project
        cd my-project
      `,
    },
  },
  {
    title: "Install Tailwind CSS",
    body: (
      <p>
        Install <code>@tailwindcss/vite</code> and its peer dependencies via npm.
      </p>
    ),
    code: {
      name: "Terminal",
      lang: "shell",
      code: shell`
        npm install tailwindcss @tailwindcss/vite
      `,
    },
  },
  {
    title: "Configure Vite Plugin",
    body: (
      <p>
        Add the <code>@tailwindcss/vite</code> plugin to your Vite configuration.
      </p>
    ),
    code: {
      name: "vite.config.ts",
      lang: "ts",
      code: js`
        import { reactRouter } from "@react-router/dev/vite";
        import { defineConfig } from "vite";
        import tsconfigPaths from "vite-tsconfig-paths";
        // [!code highlight:2]
        import tailwindcss from "@tailwindcss/vite";

        export default defineConfig({
          plugins: [
            // [!code highlight:2]
            tailwindcss(),
            reactRouter(),
            tsconfigPaths(),
          ],
        });
      `,
    },
  },
  {
    title: "Import Tailwind CSS",
    body: (
      <p>
        Add an <code>@import</code> to <code>./app/app.css</code> that imports Tailwind CSS.
      </p>
    ),
    code: {
      name: "app.css",
      lang: "css",
      code: css`
        @import "tailwindcss";
      `,
    },
  },
  {
    title: "Start your build process",
    body: (
      <p>
        Run your build process with <code>npm run dev</code>.
      </p>
    ),
    code: {
      name: "Terminal",
      lang: "shell",
      code: shell`
        npm run dev
      `,
    },
  },
  {
    title: "Start using Tailwind in your project",
    body: <p>Start using Tailwind’s utility classes to style your content.</p>,
    code: {
      name: "home.tsx",
      lang: "tsx",
      code: js`
        export default function Home() {
          return (
            // [!code highlight:4]
            <h1 className="text-3xl font-bold underline">
              Hello world!
            </h1>
          )
        }
      `,
    },
  },
];


---

## Source: src/app/(docs)/docs/installation/framework-guides/rspack.tsx

import { css, html, js, Page, shell, Step, Tab, Tile } from "./utils";
import Logo from "@/docs/img/guides/rspack.react.svg";

export let tile: Tile = {
  title: "Rspack",
  description: "A fast Rust-based web bundler.",
  Logo,
};

export let page: Page = {
  title: "Install Tailwind CSS with Rspack",
  description: "Setting up Tailwind CSS in a Rspack project.",
};

export let tabs: Tab[] = [
  {
    slug: "react",
    title: "Using React",
  },
  {
    slug: "vue",
    title: "Using Vue",
  },
];

export let steps: Step[] = [
  {
    title: "Create your project",
    body: (
      <p>
        Start by creating a new Rspack project if you don’t have one set up already. The most common approach is to use{" "}
        <a href="https://rspack.dev/guide/start/quick-start#using-the-rspack-cli">Rspack CLI</a>.
      </p>
    ),
    code: {
      name: "Terminal",
      lang: "shell",
      code: shell`
        npm create rspack@latest
      `,
    },
  },

  {
    title: "Install Tailwind CSS",
    body: (
      <p>
        Install <code>@tailwindcss/postcss</code> and its peer dependencies.
      </p>
    ),
    code: {
      name: "Terminal",
      lang: "shell",
      code: shell`
        npm install tailwindcss @tailwindcss/postcss postcss postcss-loader
      `,
    },
  },
  {
    title: "Enable PostCSS support",
    body: (
      <p>
        In your <code>rspack.config.js</code> file, enable the PostCSS loader. See{" "}
        <a href="https://rspack.dev/guide/tech/css#tailwind-css">the documentation</a> for more information.
      </p>
    ),
    code: {
      name: "rspack.config.ts",
      lang: "ts",
      code: js`
        export default defineConfig({
          // ...
          module: {
            rules: [
              // [!code highlight:6]
              {
                test: /\.css$/,
                use: ["postcss-loader"],
                type: "css",
              },
              // ...
            ],
          },
        }
      `,
    },
  },
  {
    title: "Configure PostCSS Plugins",
    body: (
      <p>
        Create a <code>postcss.config.mjs</code> file in the root of your project and add the{" "}
        <code>@tailwindcss/postcss</code> plugin to your PostCSS configuration.
      </p>
    ),
    code: {
      name: "postcss.config.mjs",
      lang: "js",
      code: js`
        export default {
          plugins: {
            // [!code highlight:2]
            "@tailwindcss/postcss": {},
          },
        };
      `,
    },
  },
  {
    tabs: ["react"],
    title: "Import Tailwind CSS",
    body: (
      <p>
        Add an <code>@import</code> to <code>./src/index.css</code> that imports Tailwind CSS.
      </p>
    ),
    code: {
      name: "index.css",
      lang: "css",
      code: css`
        @import "tailwindcss";
      `,
    },
  },
  {
    tabs: ["vue"],
    title: "Import Tailwind CSS",
    body: (
      <p>
        Add an <code>@import</code> to <code>./src/style.css</code> that imports Tailwind CSS.
      </p>
    ),
    code: {
      name: "style.css",
      lang: "css",
      code: css`
        @import "tailwindcss";
      `,
    },
  },
  {
    title: "Start your build process",
    body: (
      <p>
        Run your build process with <code>npm run dev</code>.
      </p>
    ),
    code: {
      name: "Terminal",
      lang: "shell",
      code: shell`
        npm run dev
      `,
    },
  },
  {
    tabs: ["react"],
    title: "Start using Tailwind in your project",
    body: <p>Start using Tailwind’s utility classes to style your content.</p>,
    code: {
      name: "App.jsx",
      lang: "jsx",
      code: js`
        export default function App() {
          return (
            // [!code highlight:4]
            <h1 className="text-3xl font-bold underline">
              Hello world!
            </h1>
          )
        }
      `,
    },
  },
  {
    tabs: ["vue"],
    title: "Start using Tailwind in your project",
    body: <p>Start using Tailwind’s utility classes to style your content.</p>,
    code: {
      name: "App.vue",
      lang: "vue",
      code: html`
        <template>
          <!-- [!code highlight:4] -->
          <h1 class="text-3xl font-bold underline">
            <!-- prettier-ignore -->
            Hello world!
          </h1>
        </template>
      `,
    },
  },
];

// let tabs = [
//       {
//   {
//     name: "Using Vue",
//     href: "#vue",
//     steps: [
//       {
//         title: "Start your build process",
//         body: (
//           <p>
//             Run your build process with <code>npm run dev</code>.
//           </p>
//         ),
//         code: {
//           name: "Terminal",
//           lang: "shell",
//           code: "npm run dev",
//         },
//       },
//       {
//         title: "Start using Tailwind in your project",
//         body: (
//           <p>Start using Tailwind’s utility classes to style your content.</p>
//         ),
//         code: {
//           name: "App.vue",
//           lang: "html",
//           code: `  <template>
// >   <h1 class="text-3xl font-bold underline">
// >     Hello world!
// >   </h1>
//   </template>`,
//         },
//       },
//     ],
//   },
// ];


---

## Source: src/app/(docs)/docs/installation/framework-guides/ruby-on-rails.tsx

import { css, html, Page, shell, Step, Tile } from "./utils";
import Logo from "@/docs/img/guides/rails.react.svg";
import LogoDark from "@/docs/img/guides/rails-white.react.svg";

export let tile: Tile = {
  title: "Ruby on Rails",
  description: "Full-stack framework with all the tools needed to build amazing web apps.",
  Logo,
  LogoDark,
};

export let page: Page = {
  title: "Install Tailwind CSS with Ruby on Rails",
  description: "Setting up Tailwind CSS in Ruby on Rails v8+ project.",

  // NOTE: This intro is not used currently but is here for reference as we'll want to bring it back once the rails gem is updated for a stable v4 release.
  intro: (
    <div className="prose prose-slate dark:prose-dark relative z-10 mb-16 max-w-3xl">
      <p>
        The quickest way to start using Tailwind CSS in your Rails project is to use{" "}
        <a href="https://github.com/rails/tailwindcss-rails">Tailwind CSS for Rails</a> by running{" "}
        <code>rails new my-project --css tailwind</code>. This will automatically configure your Tailwind setup based on
        the official Rails example. If you'd like to configure Tailwind manually, continue with the rest of this guide.
      </p>
    </div>
  ),
};

export let steps: Step[] = [
  {
    title: "Create your project",
    body: (
      <p>
        Start by creating a new Rails project if you don't have one set up already. The most common approach is to use
        the <a href="https://guides.rubyonrails.org/command_line.html">Rails Command Line</a>.
      </p>
    ),
    code: {
      name: "Terminal",
      lang: "shell",
      code: shell`
        rails new my-project
        cd my-project
      `,
    },
  },
  {
    title: "Install Tailwind CSS",
    body: (
      <p>
        Install the <code>tailwindcss-rails</code> gem then run the install command to set up Tailwind CSS in your
        project.
      </p>
    ),

    code: {
      name: "Terminal",
      lang: "shell",
      code: shell`
        bundle add tailwindcss-rails
        ./bin/rails tailwindcss:install
      `,
    },
  },
  {
    title: "Start your build process",
    body: (
      <p>
        Run your build process with <code>./bin/dev</code>.
      </p>
    ),
    code: {
      name: "Terminal",
      lang: "shell",
      code: shell`
        ./bin/dev
      `,
    },
  },
  {
    title: "Start using Tailwind in your project",
    body: <p>Start using Tailwind's utility classes to style your content.</p>,
    code: {
      name: "index.html.erb",
      lang: "html",
      code: html`
        <!-- [!code highlight:4] -->
        <h1 class="text-3xl font-bold underline">
          <!-- prettier-ignore -->
          Hello world!
        </h1>
      `,
    },
  },
];


---

## Source: src/app/(docs)/docs/installation/framework-guides/solidjs.tsx

import { js, css, shell, type Page, type Step, type Tile } from "./utils";
import Logo from "@/docs/img/guides/solidjs.react.svg";

export let tile: Tile = {
  title: "SolidJS",
  description: "A tool for building simple, performant, and reactive user interfaces.",
  Logo,
};

export let page: Page = {
  title: "Install Tailwind CSS with SolidJS",
  description: "Setting up Tailwind CSS in a SolidJS project.",
};

export let steps: Step[] = [
  {
    title: "Create your project",
    body: (
      <p>
        Start by creating a new SolidJS project if you don't have one set up already. The most common approach is to use{" "}
        <a href="https://www.solidjs.com/guides/getting-started">the SolidJS Vite template</a>.
      </p>
    ),
    code: {
      name: "Terminal",
      lang: "shell",
      code: shell`
        npx degit solidjs/templates/js my-project
        cd my-project
      `,
    },
  },
  {
    title: "Install Tailwind CSS",
    body: (
      <p>
        Install <code>@tailwindcss/vite</code> and its peer dependencies via npm.
      </p>
    ),
    code: {
      name: "Terminal",
      lang: "shell",
      code: shell`
        npm install tailwindcss @tailwindcss/vite
      `,
    },
  },
  {
    title: "Configure Vite Plugin",
    body: (
      <p>
        Add the <code>@tailwindcss/vite</code> plugin to your Vite configuration.
      </p>
    ),
    code: {
      name: "vite.config.ts",
      lang: "ts",
      code: js`
        import { defineConfig } from 'vite';
        import solidPlugin from 'vite-plugin-solid';
        // [!code highlight:2]
        import tailwindcss from '@tailwindcss/vite';

        export default defineConfig({
          plugins: [
            // [!code highlight:2]
            tailwindcss(),
            solidPlugin(),
          ],
          server: {
            port: 3000,
          },
          build: {
            target: 'esnext',
          },
        });
      `,
    },
  },
  {
    title: "Import Tailwind CSS",
    body: (
      <p>
        Add an <code>@import</code> to <code>./src/index.css</code> that imports Tailwind CSS.
      </p>
    ),
    code: {
      name: "index.css",
      lang: "css",
      code: css`
        @import "tailwindcss";
      `,
    },
  },
  {
    title: "Start your build process",
    body: (
      <p>
        Run your build process with <code>npm run dev</code>.
      </p>
    ),
    code: {
      name: "Terminal",
      lang: "shell",
      code: shell`
        npm run dev
      `,
    },
  },
  {
    title: "Start using Tailwind in your project",
    body: <p>Start using Tailwind’s utility classes to style your content.</p>,
    code: {
      name: "App.jsx",
      lang: "jsx",
      code: js`
        export default function App() {
          return (
            // [!code highlight:4]
            <h1 class="text-3xl font-bold underline">
              Hello world!
            </h1>
          )
        }
      `,
    },
  },
];


---

## Source: src/app/(docs)/docs/installation/framework-guides/sveltekit.tsx

import { css, js, html, shell, Page, Step, Tile } from "./utils";
import Logo from "@/docs/img/guides/svelte.react.svg";

export let tile: Tile = {
  title: "SvelteKit",
  description: "The fastest way to build apps of all sizes with Svelte.js.",
  Logo,
};

export let page: Page = {
  title: "Install Tailwind CSS with SvelteKit",
  description: "Setting up Tailwind CSS in a SvelteKit project.",
};

export let steps: Step[] = [
  {
    title: "Create your project",
    body: (
      <p>
        Start by creating a new SvelteKit project if you don't have one set up already. The most common approach is
        outlined in the <a href="https://svelte.dev/docs/kit/creating-a-project">SvelteKit</a> documentation.
      </p>
    ),
    code: {
      name: "Terminal",
      lang: "shell",
      code: shell`
        npx sv create my-project
        cd my-project
      `,
    },
  },
  {
    title: "Install Tailwind CSS",
    body: (
      <p>
        Install <code>@tailwindcss/vite</code> and its peer dependencies via npm.
      </p>
    ),
    code: {
      name: "Terminal",
      lang: "shell",
      code: shell`
        npm install tailwindcss @tailwindcss/vite
      `,
    },
  },
  {
    title: "Configure Vite Plugin",
    body: (
      <p>
        Add the <code>@tailwindcss/vite</code> plugin to your Vite configuration.
      </p>
    ),
    code: {
      name: "vite.config.ts",
      lang: "ts",
      code: js`
        import { sveltekit } from '@sveltejs/kit/vite';
        import { defineConfig } from 'vite';
        // [!code highlight:2]
        import tailwindcss from '@tailwindcss/vite';

        export default defineConfig({
          plugins: [
            // [!code highlight:2]
            tailwindcss(),
            sveltekit(),
          ],
        });
      `,
    },
  },
  {
    title: "Import Tailwind CSS",
    body: (
      <p>
        Create a <code>./src/app.css</code> file and add an <code>@import</code> that imports Tailwind CSS.
      </p>
    ),
    code: {
      name: "app.css",
      lang: "css",
      code: css`
        @import "tailwindcss";
      `,
    },
  },
  {
    title: "Import the CSS file",
    body: (
      <p>
        Create a <code>./src/routes/+layout.svelte</code> file and import the newly-created <code>app.css</code> file.
      </p>
    ),
    code: {
      name: "+layout.svelte",
      lang: "svelte",
      code: html`
        <script>
          let { children } = $props();
          // [!code highlight:2]
          import "../app.css";
        </script>

        {@render children()}
      `,
    },
  },
  {
    title: "Start your build process",
    body: (
      <p>
        Run your build process with <code>npm run dev</code>.
      </p>
    ),
    code: {
      name: "Terminal",
      lang: "shell",
      code: shell`
        npm run dev
      `,
    },
  },
  {
    title: "Start using Tailwind in your project",
    body: (
      <p>
        Start using Tailwind’s utility classes to style your content, making sure to import your Tailwind CSS theme for
        any <code>&lt;style&gt;</code> blocks that need to be processed by Tailwind.
      </p>
    ),
    code: {
      name: "+page.svelte",
      lang: "svelte",
      code: html`
        <!-- [!code highlight:4] -->
        <h1 class="text-3xl font-bold underline">
          <!-- prettier-ignore -->
          Hello world!
        </h1>

        <style lang="postcss">
          /* [!code highlight:2] */
          @reference "tailwindcss";

          :global(html) {
            background-color: theme(--color-gray-100);
          }
        </style>
      `,
    },
  },
];


---

## Source: src/app/(docs)/docs/installation/framework-guides/symfony.tsx

import { css, html, js, Page, shell, Step, Tile, twig } from "./utils";
import Logo from "@/docs/img/guides/symfony.react.svg";
import LogoDark from "@/docs/img/guides/symfony-white.react.svg";

export let tile: Tile = {
  title: "Symfony",
  description: "A PHP framework to create websites and web applications.",
  Logo,
  LogoDark,
};

export let page: Page = {
  title: "Install Tailwind CSS with Symfony",
  description: "Setting up Tailwind CSS in a Symfony project.",
};

export let steps: Step[] = [
  {
    title: "Create your project",
    body: (
      <p>
        Start by creating a new Symfony project if you don’t have one set up already. The most common approach is to use{" "}
        <a href="https://symfony.com/download">the Symfony Installer</a>.
      </p>
    ),
    code: {
      name: "Terminal",
      lang: "shell",
      code: shell`
        symfony new --webapp my-project
        cd my-project
      `,
    },
  },
  {
    title: "Install Webpack Encore",
    body: (
      <p>
        Install Webpack Encore, which handles building your assets. See{" "}
        <a href="https://symfony.com/doc/current/frontend.html">the documentation</a> for more information.
      </p>
    ),
    code: {
      name: "Terminal",
      lang: "shell",
      code: shell`
        composer remove symfony/ux-turbo symfony/asset-mapper symfony/stimulus-bundle
        composer require symfony/webpack-encore-bundle symfony/ux-turbo symfony/stimulus-bundle
      `,
    },
  },
  {
    title: "Install Tailwind CSS",
    body: (
      <p>
        Using npm, install <code>@tailwindcss/postcss</code> and its peer dependencies, as well as{" "}
        <code>postcss-loader</code>.
      </p>
    ),
    code: {
      name: "Terminal",
      lang: "shell",
      code: shell`
        npm install tailwindcss @tailwindcss/postcss postcss postcss-loader
      `,
    },
  },
  {
    title: "Enable PostCSS support",
    body: (
      <p>
        In your <code>webpack.config.js</code> file, enable the PostCSS Loader. See{" "}
        <a href="https://symfony.com/doc/current/frontend/encore/postcss.html">the documentation</a> for more
        information.
      </p>
    ),
    code: {
      name: "webpack.config.js",
      lang: "js",
      code: js`
        Encore
          .enablePostCssLoader()
        ;
      `,
    },
  },
  {
    title: "Configure PostCSS Plugins",
    body: (
      <p>
        Create a <code>postcss.config.mjs</code> file in the root of your project and add the{" "}
        <code>@tailwindcss/postcss</code> plugin to your PostCSS configuration.
      </p>
    ),
    code: {
      name: "postcss.config.mjs",
      lang: "js",
      code: js`
        export default {
          plugins: {
            // [!code highlight:2]
            "@tailwindcss/postcss": {},
          },
        };
      `,
    },
  },
  {
    title: "Import Tailwind CSS",
    body: (
      <p>
        Add an <code>@import</code> to <code>./assets/styles/app.css</code> that imports Tailwind CSS and an{" "}
        <code>@source</code> that ignores the public dir to prevent recompile loops in watch mode.
      </p>
    ),
    code: {
      name: "app.css",
      lang: "css",
      code: css`
        @import "tailwindcss";
        @source not "../../public";
      `,
    },
  },
  {
    title: "Start your build process",
    body: (
      <p>
        Run your build process with <code>npm run watch</code>.
      </p>
    ),
    code: {
      name: "Terminal",
      lang: "shell",
      code: shell`
        npm run watch
      `,
    },
  },
  {
    title: "Start using Tailwind in your project",
    body: (
      <p>
        Make sure your compiled CSS is included in the <code>{"<head>"}</code> then start using Tailwind’s utility
        classes to style your content.
      </p>
    ),
    code: {
      name: "base.html.twig",
      lang: "twig",
      code: twig`
        <!doctype html>
        <html>
          <head>
            <meta charset="utf-8" />
            <meta
              name="viewport"
              content="width=device-width, initial-scale=1.0"
            />
            <!-- [!code highlight:4] -->
            {% block stylesheets %}
              {{ encore_entry_link_tags('app') }}
            {% endblock %}
          </head>
          <body>
            <!-- [!code highlight:4] -->
            <h1 class="text-3xl font-bold underline">
              <!-- prettier-ignore -->
              Hello world!
            </h1>
          </body>
        </html>
      `,
    },
  },
];


---

## Source: src/app/(docs)/docs/installation/framework-guides/tanstack-start.tsx

import { css, js, Page, shell, Step, Tile } from "./utils";
import Logo from "@/docs/img/guides/tanstack.react.svg";
import LogoDark from "@/docs/img/guides/tanstack-white.react.svg";

export let tile: Tile = {
  title: "TanStack Start",
  description: "Full-stack Framework powered by TanStack Router for React and Solid.",
  Logo,
  LogoDark,
};

export let page: Page = {
  title: "Install Tailwind CSS with TanStack Start",
  description: "Setting up Tailwind CSS in a TanStack Start project.",
};

export let steps: Step[] = [
  {
    title: "Create project",
    body: (
      <p>
        Start by creating a new TanStack Start project if you don’t have one set up already. The most common approach is
        to use <a href="https://tanstack.com/start/latest/docs/framework/react/overview">Create Start App</a>.
      </p>
    ),
    code: {
      name: "Terminal",
      lang: "shell",
      code: shell`
        npx create-start-app@latest my-project
        cd my-project
      `,
    },
  },
  {
    title: "Install Tailwind CSS",
    body: (
      <p>
        Install <code>@tailwindcss/vite</code> and its peer dependencies via npm.
      </p>
    ),
    code: {
      name: "Terminal",
      lang: "shell",
      code: shell`
        npm install tailwindcss @tailwindcss/vite
      `,
    },
  },
  {
    title: "Configure Vite Plugin",
    body: (
      <p>
        Add the <code>@tailwindcss/vite</code> plugin to your Vite configuration.
      </p>
    ),
    code: {
      name: "vite.config.ts",
      lang: "ts",
      code: js`
        import { tanstackStart } from '@tanstack/react-start/plugin/vite';
        import { defineConfig } from 'vite';
        import tsConfigPaths from 'vite-tsconfig-paths';
        // [!code highlight:2]
        import tailwindcss from '@tailwindcss/vite'

        export default defineConfig({
          plugins: [
            // [!code highlight:2]
            tailwindcss()
            tanstackStart(),
            tsConfigPaths(),
          ]
        });
      `,
    },
  },
  {
    title: "Import Tailwind CSS",
    body: (
      <p>
        Add an <code>@import</code> to <code>./src/styles.css</code> that imports Tailwind CSS.
      </p>
    ),
    code: {
      name: "src/styles.css",
      lang: "css",
      code: css`
        @import "tailwindcss";
      `,
    },
  },
  {
    title: "Import the CSS file in your root route",
    body: (
      <p>
        Import the CSS file in your <code>__root.tsx</code> file with the <code>?url</code> query.
      </p>
    ),
    code: {
      name: "src/routes/__root.tsx",
      lang: "tsx",
      code: js`
        // other imports...

        // [!code highlight:2]
        import appCss from '../styles.css?url'

        export const Route = createRootRoute({
          head: () => ({
            meta: [
              // your meta tags and site config
            ],
            // [!code highlight:2]
            links: [{ rel: 'stylesheet', href: appCss }],
            // other head config
          }),
          component: RootComponent,
        })
      `,
    },
  },
  {
    title: "Start using Tailwind in your project",
    body: <p>Start using Tailwind’s utility classes to style your content.</p>,
    code: {
      name: "src/routes/index.tsx",
      lang: "tsx",
      code: js`
        import { createFileRoute } from '@tanstack/react-router'

        export const Route = createFileRoute('/')({
          component: App,
        })

        function App() {
          return (
            // [!code highlight:4]
            <h1 class="text-3xl font-bold underline">
              Hello World!
            </h1>
          )
        }
      `,
    },
  },
];

