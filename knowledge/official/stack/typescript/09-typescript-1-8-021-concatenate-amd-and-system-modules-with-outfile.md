## Concatenate `AMD` and `System` modules with `--outFile`

Specifying [`outFile`](/tsconfig#outFile) in conjunction with `--module amd` or `--module system` will concatenate all modules in the compilation into a single output file containing multiple module closures.

A module name will be computed for each module based on its relative location to [`rootDir`](/tsconfig#rootDir).
