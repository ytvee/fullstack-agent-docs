### Avoiding Unnecessary Type Instantiation

TypeScript 5.1 now avoids performing type instantiation within object types that are known not to contain references to outer type parameters.
This has the potential to cut down on many unnecessary computations, and reduced the type-checking time of [material-ui's docs directory](https://github.com/mui/material-ui/tree/b0351248fb396001a30330daac86d0e0794a0c1d/docs) by over 50%.

You can [see the changes involved for this change on GitHub](https://github.com/microsoft/TypeScript/pull/53246).
