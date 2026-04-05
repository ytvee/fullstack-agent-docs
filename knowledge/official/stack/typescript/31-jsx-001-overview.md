---
display: "JSX"
oneline: "Specify what JSX code is generated."
---

Controls how JSX constructs are emitted in JavaScript files.
This only affects output of JS files that started in `.tsx` files.

- `react-jsx`: Emit `.js` files with the JSX changed to `_jsx` calls optimized for production
- `react-jsxdev`: Emit `.js` files with the JSX changed to `_jsx` calls for development only
- `preserve`: Emit `.jsx` files with the JSX unchanged
- `react-native`: Emit `.js` files with the JSX unchanged
- `react`: Emit `.js` files with JSX changed to the equivalent `React.createElement` calls
