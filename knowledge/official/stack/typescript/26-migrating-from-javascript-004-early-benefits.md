## Early Benefits

Even at this point you can get some great benefits from TypeScript understanding your project.
If you open up an editor like [VS Code](https://code.visualstudio.com) or [Visual Studio](https://visualstudio.com), you'll see that you can often get some tooling support like completion.
You can also catch certain bugs with options like:

- [`noImplicitReturns`](/tsconfig#noImplicitReturns) which prevents you from forgetting to return at the end of a function.
- [`noFallthroughCasesInSwitch`](/tsconfig#noFallthroughCasesInSwitch) which is helpful if you never want to forget a `break` statement between `case`s in a `switch` block.

TypeScript will also warn about unreachable code and labels, which you can disable with [`allowUnreachableCode`](/tsconfig#allowUnreachableCode) and [`allowUnusedLabels`](/tsconfig#allowUnusedLabels) respectively.
