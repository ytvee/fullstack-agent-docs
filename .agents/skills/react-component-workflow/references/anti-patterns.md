# Anti-Patterns

## General

- Duplicated state that can be derived
- Effects used as routine control flow
- Deep wrapper stacks with unclear ownership
- Over-abstracted hooks for one component
- Styling or data concerns hidden inside otherwise presentational components

## React 19 specific

- Wrapping function components in `forwardRef` — refs are plain props in React 19;
  `forwardRef` is unnecessary and adds noise
- Using `useState` + `useEffect` to manage async action state when `useActionState`
  covers the same pattern more directly
- Ignoring `use()` for reading Promises in client components and falling back to
  `useEffect`-based fetching patterns that require more boilerplate
- Manually wiring up form pending state with `useState` when `useFormStatus`
  already provides `pending` from the parent `<form>`
