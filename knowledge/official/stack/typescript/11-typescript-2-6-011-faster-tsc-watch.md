## Faster `tsc --watch`

TypeScript 2.6 brings a faster `--watch` implementation.
The new version optimizes code generation and checking for code bases using ES modules.
Changes detected in a module file will result in _only_ regenerating the changed module, and files that depend on it, instead of the whole project.
Projects with a large number of files should reap the most benefit from this change.

The new implementation also brings performance enhancements to watching in tsserver.
The watcher logic has been completely rewritten to respond faster to change events.
