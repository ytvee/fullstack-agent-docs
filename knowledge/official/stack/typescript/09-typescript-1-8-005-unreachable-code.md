### Unreachable code

Statements guaranteed to not be executed at run time are now correctly flagged as unreachable code errors.
For instance, statements following unconditional `return`, `throw`, `break` or `continue` statements are considered unreachable.
Use [`allowUnreachableCode`](/tsconfig#allowUnreachableCode) to disable unreachable code detection and reporting.
