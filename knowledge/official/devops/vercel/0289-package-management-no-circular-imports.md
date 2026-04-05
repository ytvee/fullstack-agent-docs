--------------------------------------------------------------------------------
title: "PACKAGE_MANAGEMENT_NO_CIRCULAR_IMPORTS"
description: "Circular imports between two files are not allowed."
last_updated: "2026-04-03T23:47:18.384Z"
source: "https://vercel.com/docs/conformance/rules/PACKAGE_MANAGEMENT_NO_CIRCULAR_IMPORTS"
--------------------------------------------------------------------------------

# PACKAGE_MANAGEMENT_NO_CIRCULAR_IMPORTS

> **🔒 Permissions Required**: Conformance

This check ensures that there is no path through import statements back to the
original file. This helps to keep dependencies between files clean, which aids
in dependency analysis and refactoring.

## Example

```ts filename="component-a.ts"
import Badge from './component-b';

export function withHigherOrderComponent({ children }) {
  return <div>{children}</div>;
}

export function Page() {
  return (
    <div>
      <Badge />
    </div>
  );
}
```

```ts filename="component-b.ts"
import { withHigherOrderComponent } from './component-a';

function Badge() {
  return <div>Badge</div>;
}

export default withHigherOrderComponent(Badge);
```

## How to fix

The exports in the file that has a circular import should be refactored so that
the circular import doesn't exist anymore. This might be fixed by moving some
of the exports in a file to a separate file so that the imports don't cause a
circular import. In some cases, it may be necessary to refactor the code to
avoid the circular import.


