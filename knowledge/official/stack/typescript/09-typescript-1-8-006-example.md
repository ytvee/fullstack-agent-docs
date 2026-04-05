##### Example

Here's a simple example of an unreachable code error:

```ts
function f(x) {
  if (x) {
    return true;
  } else {
    return false;
  }

  x = 0; // Error: Unreachable code detected.
}
```

A more common error that this feature catches is adding a newline after a `return` statement:

```ts
function f() {
  return; // Automatic Semicolon Insertion triggered at newline
  {
    x: "string"; // Error: Unreachable code detected.
  }
}
```

Since JavaScript automatically terminates the `return` statement at the end of the line, the object literal becomes a block.
