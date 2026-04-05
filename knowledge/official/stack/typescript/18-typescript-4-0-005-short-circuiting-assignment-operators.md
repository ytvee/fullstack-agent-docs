## Short-Circuiting Assignment Operators

JavaScript, and a lot of other languages, support a set of operators called _compound assignment_ operators.
Compound assignment operators apply an operator to two arguments, and then assign the result to the left side.
You may have seen these before:

```ts
// Addition
// a = a + b
a += b;

// Subtraction
// a = a - b
a -= b;

// Multiplication
// a = a * b
a *= b;

// Division
// a = a / b
a /= b;

// Exponentiation
// a = a ** b
a **= b;

// Left Bit Shift
// a = a << b
a <<= b;
```

So many operators in JavaScript have a corresponding assignment operator!
Up until recently, however, there were three notable exceptions: logical _and_ (`&&`), logical _or_ (`||`), and nullish coalescing (`??`).

That's why TypeScript 4.0 supports a new ECMAScript feature to add three new assignment operators: `&&=`, `||=`, and `??=`.

These operators are great for substituting any example where a user might write code like the following:

```ts
a = a && b;
a = a || b;
a = a ?? b;
```

Or a similar `if` block like

```ts
// could be 'a ||= b'
if (!a) {
  a = b;
}
```

There are even some patterns we've seen (or, uh, written ourselves) to lazily initialize values, only if they'll be needed.

```ts
let values: string[];
(values ?? (values = [])).push("hello");

// After
(values ??= []).push("hello");
```

(look, we're not proud of _all_ the code we write...)

On the rare case that you use getters or setters with side-effects, it's worth noting that these operators only perform assignments if necessary.
In that sense, not only is the right side of the operator "short-circuited" - the assignment itself is too.

```ts
obj.prop ||= foo();

// roughly equivalent to either of the following

obj.prop || (obj.prop = foo());

if (!obj.prop) {
    obj.prop = foo();
}
```

[Try running the following example](https://www.typescriptlang.org/play?ts=next#code/MYewdgzgLgBCBGArGBeGBvAsAKBnmA5gKawAOATiKQBQCUGO+TMokIANkQHTsgHUAiYlChFyMABYBDCDHIBXMANoBuHI2Z4A9FpgAlIqXZTgRGAFsiAQg2byJeeTAwAslKgSu5KWAAmIczoYAB4YAAYuAFY1XHwAXwAaWxgIEhgKKmoAfQA3KXYALhh4EA4iH3osWM1WCDKePkFUkTFJGTlFZRimOJw4mJwAM0VgKABLcBhB0qCqplr63n4BcjGCCVgIMd8zIjz2eXciXy7k+yhHZygFIhje7BwFzgblgBUJMdlwM3yAdykAJ6yBSQGAeMzNUTkU7YBCILgZUioOBIBGUJEAHwxUxmqnU2Ce3CWgnenzgYDMACo6pZxpYIJSOqDwSkSFCYXC0VQYFi0NMQHQVEA) to see how that differs from _always_ performing the assignment.

```ts twoslash
const obj = {
    get prop() {
        console.log("getter has run");

        // Replace me!
        return Math.random() < 0.5;
    },
    set prop(_val: boolean) {
        console.log("setter has run");
    }
};

function foo() {
    console.log("right side evaluated");
    return true;
}

console.log("This one always runs the setter");
obj.prop = obj.prop || foo();

console.log("This one *sometimes* runs the setter");
obj.prop ||= foo();
```

We'd like to extend a big thanks to community member [Wenlu Wang](https://github.com/Kingwl) for this contribution!

For more details, you can [take a look at the pull request here](https://github.com/microsoft/TypeScript/pull/37727).
You can also [check out TC39's proposal repository for this feature](https://github.com/tc39/proposal-logical-assignment/).
