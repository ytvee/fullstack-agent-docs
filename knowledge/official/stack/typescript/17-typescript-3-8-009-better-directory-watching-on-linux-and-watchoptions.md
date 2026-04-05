## Better Directory Watching on Linux and `watchOptions`

TypeScript 3.8 ships a new strategy for watching directories, which is crucial for efficiently picking up changes to `node_modules`.

For some context, on operating systems like Linux, TypeScript installs directory watchers (as opposed to file watchers) on `node_modules` and many of its subdirectories to detect changes in dependencies.
This is because the number of available file watchers is often eclipsed by the number of files in `node_modules`, whereas there are way fewer directories to track.

Older versions of TypeScript would _immediately_ install directory watchers on folders, and at startup that would be fine; however, during an npm install, a lot of activity will take place within `node_modules` and that can overwhelm TypeScript, often slowing editor sessions to a crawl.
To prevent this, TypeScript 3.8 waits slightly before installing directory watchers to give these highly volatile directories some time to stabilize.

Because every project might work better under different strategies, and this new approach might not work well for your workflows, TypeScript 3.8 introduces a new `watchOptions` field in `tsconfig.json` and `jsconfig.json` which allows users to tell the compiler/language service which watching strategies should be used to keep track of files and directories.

```jsonc tsconfig
{
  // Some typical compiler options
  "compilerOptions": {
    "target": "es2020",
    "moduleResolution": "node"
    // ...
  },

  // NEW: Options for file/directory watching
  "watchOptions": {
    // Use native file system events for files and directories
    "watchFile": "useFsEvents",
    "watchDirectory": "useFsEvents",

    // Poll files for updates more frequently
    // when they're updated a lot.
    "fallbackPolling": "dynamicPriority"
  }
}
```

`watchOptions` contains 4 new options that can be configured:

- [`watchFile`](/tsconfig#watchFile): the strategy for how individual files are watched. This can be set to

  - `fixedPollingInterval`: Check every file for changes several times a second at a fixed interval.
  - `priorityPollingInterval`: Check every file for changes several times a second, but use heuristics to check certain types of files less frequently than others.
  - `dynamicPriorityPolling`: Use a dynamic queue where less-frequently modified files will be checked less often.
  - `useFsEvents` (the default): Attempt to use the operating system/file system's native events for file changes.
  - `useFsEventsOnParentDirectory`: Attempt to use the operating system/file system's native events to listen for changes on a file's containing directories. This can use fewer file watchers, but might be less accurate.

- [`watchDirectory`](/tsconfig#watchDirectory): the strategy for how entire directory trees are watched under systems that lack recursive file-watching functionality. This can be set to:

  - `fixedPollingInterval`: Check every directory for changes several times a second at a fixed interval.
  - `dynamicPriorityPolling`: Use a dynamic queue where less-frequently modified directories will be checked less often.
  - `useFsEvents` (the default): Attempt to use the operating system/file system's native events for directory changes.

- [`fallbackPolling`](/tsconfig#fallbackPolling): when using file system events, this option specifies the polling strategy that gets used when the system runs out of native file watchers and/or doesn't support native file watchers. This can be set to
  - `fixedPollingInterval`: _(See above.)_
  - `priorityPollingInterval`: _(See above.)_
  - `dynamicPriorityPolling`: _(See above.)_
  - `synchronousWatchDirectory`: Disable deferred watching on directories. Deferred watching is useful when lots of file changes might occur at once (e.g. a change in `node_modules` from running `npm install`), but you might want to disable it with this flag for some less-common setups.

For more information on these changes, [head over to GitHub to see the pull request](https://github.com/microsoft/TypeScript/pull/35615) to read more.
