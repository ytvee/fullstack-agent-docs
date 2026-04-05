##### Example

With [`noFallthroughCasesInSwitch`](/tsconfig#noFallthroughCasesInSwitch), this example will trigger an error:

```ts
switch (x % 2) {
  case 0: // Error: Fallthrough case in switch.
    console.log("even");

  case 1:
    console.log("odd");
    break;
}
```

However, in the following example, no error will be reported because the fall-through case is empty:

```ts
switch (x % 3) {
  case 0:
  case 1:
    console.log("Acceptable");
    break;

  case 2:
    console.log("This is *two much*!");
    break;
}
```
