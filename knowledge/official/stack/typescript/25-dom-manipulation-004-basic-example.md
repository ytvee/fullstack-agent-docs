## Basic Example

Given a simplified _index.html_ file:

```html
<!DOCTYPE html>
<html lang="en">
  <head><title>TypeScript Dom Manipulation</title></head>
  <body>
    <div id="app"></div>
    <!-- Assume index.js is the compiled output of index.ts -->
    <script src="index.js"></script>
  </body>
</html>
```

Let's explore a TypeScript script that adds a `<p>Hello, World!</p>` element to the `#app` element.

```ts
// 1. Select the div element using the id property
const app = document.getElementById("app");

// 2. Create a new <p></p> element programmatically
const p = document.createElement("p");

// 3. Add the text content
p.textContent = "Hello, World!";

// 4. Append the p element to the div element
app?.appendChild(p);
```

After compiling and running the _index.html_ page, the resulting HTML will be:

```html
<div id="app">
  <p>Hello, World!</p>
</div>
```
