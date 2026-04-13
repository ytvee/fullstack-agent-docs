# Figma Profile

When a task includes a Figma URL or node reference:

1. Use the built-in Figma capabilities first to inspect the design.
2. Recreate the design with the repo's existing styling system:
    - CSS Modules for local styling
    - global tokens and CSS variables from `src/styles/tokens/` for shared values
3. Reuse existing layout and component patterns before creating one-off structures.
4. Match the visual intent closely, but adapt it to the current responsive system.

## Breakpoints

These are the breakpoints used throughout the codebase (mobile-first):

| Name | Value |
|---|---|
| sm | 640px |
| md | 768px |
| lg | 1024px |
| xl | 1280px |
| 2xl | 1536px |

Use `@media (min-width: Npx)` — the project is mobile-first. Avoid
`max-width` queries unless matching an existing local pattern.

## Token Files

- `src/styles/tokens/colors.css` — color palette (`--color-*`) and semantic
  color roles per theme (`light` / `dark` via `data-theme` attribute)
- `src/styles/tokens/typography.css` — font faces, `--font-*`, `--font-size-*`,
  `--line-height-*`, `--letter-spacing-*`, `--font-weight-*`

## Local Constraints

- Prefer token reuse over raw hardcoded values
- Respect the existing desktop/mobile layout patterns already used by the app
- If the design introduces a new reusable token or pattern, add it deliberately
  to the relevant token file instead of hiding it inside a single CSS Module
- Document any unavoidable deviation from the design in the implementation summary
