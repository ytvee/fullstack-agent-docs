# Styling Profile

## Current Styling System

- CSS Modules are the primary styling approach for routes and components
- Global resets and prose styles live in `src/app/globals.css`
- Shared tokens live in `src/styles/tokens/` and are imported globally
- CSS custom properties are the preferred token surface

## What to Preserve

- Keep styles colocated with the component or route they belong to
- Reuse existing tokens before introducing raw color or spacing values
- Preserve the established typography and spacing rhythm

## What to Avoid

- Do not assume Tailwind or shadcn/ui
- Do not introduce a second styling system without an explicit request
- Avoid one-off hardcoded values when an existing token or module pattern fits
