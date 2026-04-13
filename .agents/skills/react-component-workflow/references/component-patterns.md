# Component Patterns

## Orchestration vs presentation

Separate orchestration from presentation when it makes the code easier to
reason about independently.

**Orchestration component** — owns data fetching, async state, business logic,
and conditional rendering decisions. Knows about the data model. Passes results
down as props.

**Presentation component** — receives fully resolved props and renders UI.
No fetching, no business logic, no conditional data wiring.

**When to split:**
- The component mixes data-loading and rendering concerns in a way that makes
  either harder to read or test.
- The presentation can be reused in a different context with different data.
- The component is large enough that reading both concerns together is fatiguing.

**When NOT to split:**
- The component is small and reads clearly as a unit.
- The "presentation" half would need so many props it becomes harder to follow.
- Splitting would create an abstraction with only one caller.

## Composition

- Keep props explicit; avoid hidden coupling through module state or magic imports.
- Prefer composition over wrapper pyramids.
- Extract helpers or child components only when readability or reuse genuinely
  improves — three similar lines of inline JSX is fine; a premature component
  abstraction is not.

## State ownership

- Own state at the lowest component that needs it.
- Lift state only when two sibling components genuinely need to share it.
- Derive values from existing state instead of creating parallel state that must
  be kept in sync.
