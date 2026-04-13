# Styling Profile

## Current Styling System

- CSS Modules are the primary styling approach for routes and components
- Global resets and prose styles live in `src/app/globals.css`
- Shared design tokens live in:
  - `src/styles/tokens/colors.css` — color palette and semantic color variables
  - `src/styles/tokens/typography.css` — font faces, font-size scale, line-height,
    letter-spacing, and font-weight variables
- CSS custom properties are the preferred token surface

## CSS Custom Property Prefixes

| Prefix | Covers |
|---|---|
| `--color-*` | Color palette and semantic color roles |
| `--font-family-*` / `--font-*` | Font families and type scale |
| `--font-size-*` | Size scale (xs, sm, base, lg, xl, 2xl, 3xl, h1–h3) |
| `--line-height-*` | Line height scale (tight, snug, normal, relaxed, loose) |
| `--letter-spacing-*` | Letter spacing (tight, normal, wide) |
| `--font-weight-*` | Weight scale (normal, medium, semibold, bold) |

## What to Preserve

- Keep styles colocated with the component or route they belong to
- Reuse existing tokens before introducing raw color or spacing values
- Preserve the established typography and spacing rhythm

## What to Avoid

- Do not assume Tailwind or shadcn/ui
- Do not introduce a second styling system without an explicit request
- Avoid one-off hardcoded values when an existing token or module pattern fits
