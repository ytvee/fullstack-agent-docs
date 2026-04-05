### Reduced Calls into Scanner for JSDoc Parsing

When older versions of TypeScript parsed out a JSDoc comment, they would use the scanner/tokenizer to break the comment into fine-grained tokens and piece the contents back together.
This could be helpful for normalizing comment text, so that multiple spaces would just collapse into one;
but it was extremely "chatty" and meant the parser and scanner would jump back and forth very often, adding overhead to JSDoc parsing.

TypeScript 5.1 has moved more logic around breaking down JSDoc comments into the scanner/tokenizer.
The scanner now returns larger chunks of content directly to the parser to do as it needs.

[These changes](https://github.com/microsoft/TypeScript/pull/53081) have brought down the parse time of several 10Mb mostly-prose-comment JavaScript files by about half.
For a more realistic example, our performance suite's snapshot of [xstate](https://github.com/statelyai/xstate) dropped about 300ms of parse time, making it faster to load and analyze.
