# Figma Profile

When a task includes a Figma URL or node reference:

1. Use the built-in Figma capabilities first to inspect the design.
2. Recreate the design with the repo's existing styling system:
    - CSS Modules for local styling
    - global tokens and CSS variables for shared values
3. Reuse existing layout and component patterns before creating one-off structures.
4. Match the visual intent closely, but adapt it to the current responsive system.

## Local Constraints

- Prefer token reuse over raw hardcoded values
- Respect the existing desktop/mobile layout patterns already used by the app
- If the design introduces a new reusable token or pattern, add it deliberately
  instead of hiding it inside a single CSS Module
- Document any unavoidable deviation from the design in the implementation summary
