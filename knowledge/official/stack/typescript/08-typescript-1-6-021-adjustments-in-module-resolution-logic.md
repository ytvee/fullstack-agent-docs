## Adjustments in module resolution logic

Starting from release 1.6 TypeScript compiler will use different set of rules to resolve module names when targeting 'commonjs'.
These [rules](https://github.com/Microsoft/TypeScript/issues/2338) attempted to model module lookup procedure used by Node.
This effectively mean that node modules can include information about its typings and TypeScript compiler will be able to find it.
User however can override module resolution rules picked by the compiler by using [`moduleResolution`](/tsconfig#moduleResolution) command line option. Possible values are:

- 'classic' - module resolution rules used by pre 1.6 TypeScript compiler
- 'node' - node-like module resolution
