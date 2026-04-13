# Task Routing

## Recommended chains

### Feature / refactor / bugfix

1. `webapp-task-protocol`
2. Domain skill(s):
    - `nextjs-app-router` — routing, layouts, file conventions, server/client boundaries
    - `react-component-workflow` — component architecture, props, state, hooks
    - Use both when the task spans routing AND component concerns (see `classification-rules.md`)
3. Add `frontend-typescript-rules` when typing or refactors matter
4. Add `frontend-zod-schema` when boundary input is parsed or validated
5. Finish with `frontend-review-and-fix`

### Cross-domain feature

When a feature requires new routes AND new component architecture:

1. `webapp-task-protocol`
2. `nextjs-app-router` — establish route structure and boundaries
3. `react-component-workflow` — implement component internals
4. Add `frontend-typescript-rules` and `frontend-zod-schema` as needed
5. `frontend-review-and-fix`

### Review request

1. `webapp-task-protocol`
2. `frontend-review-and-fix`

### SEO request

1. `technical-seo-app`

### Security request

1. `frontend-security-inspector`

### Repo refresh request

1. `project-context-adapter`
