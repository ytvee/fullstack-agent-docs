# React Documentation Aggregate

Source: all markdown docs in `packages/*/copy/en` containing the word `react` (case-insensitive).

---

## Source: `packages/documentation/copy/en/handbook-v2/The Handbook.md`

---
title: The TypeScript Handbook
layout: docs
permalink: /docs/handbook/intro.html
oneline: Your first step to learn TypeScript
handbook: "true"
---

## About this Handbook

Over 20 years after its introduction to the programming community, JavaScript is now one of the most widespread cross-platform languages ever created. Starting as a small scripting language for adding trivial interactivity to webpages, JavaScript has grown to be a language of choice for both frontend and backend applications of every size. While the size, scope, and complexity of programs written in JavaScript has grown exponentially, the ability of the JavaScript language to express the relationships between different units of code has not. Combined with JavaScript's rather peculiar runtime semantics, this mismatch between language and program complexity has made JavaScript development a difficult task to manage at scale.

The most common kinds of errors that programmers write can be described as type errors: a certain kind of value was used where a different kind of value was expected. This could be due to simple typos, a failure to understand the API surface of a library, incorrect assumptions about runtime behavior, or other errors. The goal of TypeScript is to be a static typechecker for JavaScript programs - in other words, a tool that runs before your code runs (static) and ensures that the types of the program are correct (typechecked).

If you are coming to TypeScript without a JavaScript background, with the intention of TypeScript being your first language, we recommend you first start reading the documentation on either the [Microsoft Learn JavaScript tutorial](https://developer.microsoft.com/javascript/) or read [JavaScript at the Mozilla Web Docs](https://developer.mozilla.org/docs/Web/JavaScript/Guide).
If you have experience in other languages, you should be able to pick up JavaScript syntax quite quickly by reading the handbook.

## How is this Handbook Structured

The handbook is split into two sections:

- **The Handbook**

  The TypeScript Handbook is intended to be a comprehensive document that explains TypeScript to everyday programmers. You can read the handbook by going from top to bottom in the left-hand navigation.

  You should expect each chapter or page to provide you with a strong understanding of the given concepts. The TypeScript Handbook is not a complete language specification, but it is intended to be a comprehensive guide to all of the language's features and behaviors.

  A reader who completes the walkthrough should be able to:

  - Read and understand commonly-used TypeScript syntax and patterns
  - Explain the effects of important compiler options
  - Correctly predict type system behavior in most cases

  In the interests of clarity and brevity, the main content of the Handbook will not explore every edge case or minutiae of the features being covered. You can find more details on particular concepts in the reference articles.

- **Reference Files**

  The reference section below the handbook in the navigation is built to provide a richer understanding of how a particular part of TypeScript works. You can read it top-to-bottom, but each section aims to provide a deeper explanation of a single concept - meaning there is no aim for continuity.

### Non-Goals

The Handbook is also intended to be a concise document that can be comfortably read in a few hours. Certain topics won't be covered in order to keep things short.

Specifically, the Handbook does not fully introduce core JavaScript basics like functions, classes, and closures. Where appropriate, we'll include links to background reading that you can use to read up on those concepts.

The Handbook also isn't intended to be a replacement for a language specification. In some cases, edge cases or formal descriptions of behavior will be skipped in favor of high-level, easier-to-understand explanations. Instead, there are separate reference pages that more precisely and formally describe many aspects of TypeScript's behavior. The reference pages are not intended for readers unfamiliar with TypeScript, so they may use advanced terminology or reference topics you haven't read about yet.

Finally, the Handbook won't cover how TypeScript interacts with other tools, except where necessary. Topics like how to configure TypeScript with webpack, rollup, parcel, react, babel, closure, lerna, rush, bazel, preact, vue, angular, svelte, jquery, yarn, or npm are out of scope - you can find these resources elsewhere on the web.

## Get Started

Before getting started with [The Basics](/docs/handbook/2/basic-types.html), we recommend reading one of the following introductory pages. These introductions are intended to highlight key similarities and differences between TypeScript and your favored programming language, and clear up common misconceptions specific to those languages.

- [TypeScript for the New Programmer](/docs/handbook/typescript-from-scratch.html)
- [TypeScript for JavaScript Programmers](/docs/handbook/typescript-in-5-minutes.html)
- [TypeScript for Java/C# Programmers](/docs/handbook/typescript-in-5-minutes-oop.html)
- [TypeScript for Functional Programmers](/docs/handbook/typescript-in-5-minutes-func.html)

Otherwise, jump to [The Basics](/docs/handbook/2/basic-types.html).

---

## Source: `packages/documentation/copy/en/handbook-v2/Type Declarations.md`

---
title: Type Declarations
layout: docs
permalink: /docs/handbook/2/type-declarations.html
oneline: "How TypeScript provides types for un-typed JavaScript."
---

Throughout the sections you've read so far, we've been demonstrating basic TypeScript concepts using the built-in functions present in all JavaScript runtimes.
However, almost all JavaScript today includes many libraries to accomplish common tasks.
Having types for the parts of your application that _aren't_ your code will greatly improve your TypeScript experience.
Where do these types come from?

## What Do Type Declarations Look Like?

Let's say you write some code like this:

```ts twoslash
// @errors: 2339
const k = Math.max(5, 6);
const j = Math.mix(7, 8);
```

How did TypeScript know that `max` was present but not `mix`, even though `Math`'s implementation wasn't part of your code?

The answer is that there are _declaration files_ describing these built-in objects.
A declaration file provides a way to _declare_ the existence of some types or values without actually providing implementations for those values.

## `.d.ts` files

TypeScript has two main kinds of files.
`.ts` files are _implementation_ files that contain types and executable code.
These are the files that produce `.js` outputs, and are where you'd normally write your code.

`.d.ts` files are _declaration_ files that contain _only_ type information.
These files don't produce `.js` outputs; they are only used for typechecking.
We'll learn more about how to write our own declaration files later.

## Built-in Type Definitions

TypeScript includes declaration files for all of the standardized built-in APIs available in JavaScript runtimes.
This includes things like methods and properties of built-in types like `string` or `function`, top-level names like `Math` and `Object`, and their associated types.
By default, TypeScript also includes types for things available when running inside the browser, such as `window` and `document`; these are collectively referred to as the DOM APIs.

TypeScript names these declaration files with the pattern `lib.[something].d.ts`.
If you navigate into a file with that name, you can know that you're dealing with some built-in part of the platform, not user code.

### `target` setting

The methods, properties, and functions available to you actually vary based on the _version_ of JavaScript your code is running on.
For example, the `startsWith` method of strings is available only starting with the version of JavaScript referred as _ECMAScript 6_.

Being aware of what version of JavaScript your code ultimately runs on is important because you don't want to use APIs that are from a newer version than the platform you deploy to.
This is one function of the [`target`](/tsconfig#target) compiler setting.

TypeScript helps with this problem by varying which `lib` files are included by default based on your [`target`](/tsconfig#target) setting.
For example, if [`target`](/tsconfig#target) is `ES5`, you will see an error if trying to use the `startsWith` method, because that method is only available in `ES6` or later.

### `lib` setting

The [`lib`](/tsconfig#lib) setting allows more fine-grained control of which built-in declaration files are considered available in your program.
See the documentation page on [`lib`](/tsconfig#lib) for more information.

## External Definitions

For non-built-in APIs, there are a variety of ways you can get declaration files.
How you do this depends on exactly which library you're getting types for.

### Bundled Types

If a library you're using is published as an npm package, it may include type declaration files as part of its distribution already.
You can read the project's documentation to find out, or simply try importing the package and see if TypeScript is able to automatically resolve the types for you.

If you're a package author considering bundling type definitions with your package, you can read our guide on [bundling type definitions](/docs/handbook/declaration-files/publishing.html#including-declarations-in-your-npm-package).

### DefinitelyTyped / `@types`

The [DefinitelyTyped repository](https://github.com/DefinitelyTyped/DefinitelyTyped/) is a centralized repo storing declaration files for thousands of libraries.
The vast majority of commonly-used libraries have declaration files available on DefinitelyTyped.

Definitions on DefinitelyTyped are also automatically published to npm under the `@types` scope.
The name of the types package is always the same as the name of the underlying package itself.
For example, if you installed the `react` npm package, you can install its corresponding types by running

```sh
npm install --save-dev @types/react
```

TypeScript automatically finds type definitions under `node_modules/@types`, so there's no other step needed to get these types available in your program.

### Your Own Definitions

In the uncommon event that a library didn't bundle its own types and didn't have a definition on DefinitelyTyped, you can write a declaration file yourself.
See the appendix [Writing Declaration Files](/docs/handbook/declaration-files/introduction.html) for a guide.

If you want to silence warnings about a particular module without writing a declaration file, you can also quick declare the module as type `any` by putting an empty declaration for it in a `.d.ts` file in your project.
For example, if you wanted to use a module named `some-untyped-module` without having definitions for it, you would write:

```ts twoslash
declare module "some-untyped-module";
```

---

## Source: `packages/documentation/copy/en/javascript/JSDoc Reference.md`

---
title: JSDoc Reference
layout: docs
permalink: /docs/handbook/jsdoc-supported-types.html
oneline: What JSDoc does TypeScript-powered JavaScript support?
translatable: true
---

The list below outlines which constructs are currently supported
when using JSDoc annotations to provide type information in JavaScript files.

Note:
- Any tags which are not explicitly listed below (such as `@async`) are not yet supported.
- Only documentation tags are supported in TypeScript files. The rest of the tags are only supported in JavaScript files.

#### Types

- [`@type`](#type)
- [`@import`](#import)
- [`@param`](#param-and-returns) (or [`@arg`](#param-and-returns) or [`@argument`](#param-and-returns))
- [`@returns`](#param-and-returns) (or [`@return`](#param-and-returns))
- [`@typedef`](#typedef-callback-and-param)
- [`@callback`](#typedef-callback-and-param)
- [`@template`](#template)
- [`@satisfies`](#satisfies)


#### Classes

- [Property Modifiers](#property-modifiers) `@public`, `@private`, `@protected`, `@readonly`
- [`@override`](#override)
- [`@extends`](#extends) (or [`@augments`](#extends))
- [`@implements`](#implements)
- [`@class`](#constructor) (or [`@constructor`](#constructor))
- [`@this`](#this)

#### Documentation

Documentation tags work in both TypeScript and JavaScript.

- [`@deprecated`](#deprecated)
- [`@see`](#see)
- [`@link`](#link)

#### Other

- [`@enum`](#enum)
- [`@author`](#author)
- [Other supported patterns](#other-supported-patterns)
- [Unsupported patterns](#unsupported-patterns)
- [Unsupported tags](#unsupported-tags)

The meaning is usually the same, or a superset, of the meaning of the tag given at [jsdoc.app](https://jsdoc.app).
The code below describes the differences and gives some example usage of each tag.

**Note:** You can use [the playground to explore JSDoc support](/play?useJavaScript=truee=4#example/jsdoc-support).

## Types

### `@type`

You can reference types with the "@type" tag. The type can be:

1. Primitive, like `string` or `number`.
2. Declared in a TypeScript declaration, either global or imported.
3. Declared in a JSDoc [`@typedef`](#typedef-callback-and-param) tag.

You can use most JSDoc type syntax and any TypeScript syntax, from [the most basic like `string`](/docs/handbook/2/basic-types.html) to [the most advanced, like conditional types](/docs/handbook/2/conditional-types.html).

```js twoslash
/**
 * @type {string}
 */
var s;

/** @type {Window} */
var win;

/** @type {PromiseLike<string>} */
var promisedString;

// You can specify an HTML Element with DOM properties
/** @type {HTMLElement} */
var myElement = document.querySelector(selector);
element.dataset.myData = "";
```

`@type` can specify a union type &mdash; for example, something can be either a string or a boolean.

```js twoslash
/**
 * @type {string | boolean}
 */
var sb;
```

You can specify array types using a variety of syntaxes:

```js twoslash
/** @type {number[]} */
var ns;
/** @type {Array.<number>} */
var jsdoc;
/** @type {Array<number>} */
var nas;
```

You can also specify object literal types.
For example, an object with properties 'a' (string) and 'b' (number) uses the following syntax:

```js twoslash
/** @type {{ a: string, b: number }} */
var var9;
```

You can specify map-like and array-like objects using string and number index signatures, using either standard JSDoc syntax or TypeScript syntax.

```js twoslash
/**
 * A map-like object that maps arbitrary `string` properties to `number`s.
 *
 * @type {Object.<string, number>}
 */
var stringToNumber;

/** @type {Object.<number, object>} */
var arrayLike;
```

The preceding two types are equivalent to the TypeScript types `{ [x: string]: number }` and `{ [x: number]: any }`. The compiler understands both syntaxes.

You can specify function types using either TypeScript or Google Closure syntax:

```js twoslash
/** @type {function(string, boolean): number} Closure syntax */
var sbn;
/** @type {(s: string, b: boolean) => number} TypeScript syntax */
var sbn2;
```

Or you can just use the unspecified `Function` type:

```js twoslash
/** @type {Function} */
var fn7;
/** @type {function} */
var fn6;
```

Other types from Closure also work:

```js twoslash
/**
 * @type {*} - can be 'any' type
 */
var star;
/**
 * @type {?} - unknown type (same as 'any')
 */
var question;
```

#### Casts

TypeScript borrows cast syntax from Google Closure.
This lets you cast types to other types by adding a `@type` tag before any parenthesized expression.

```js twoslash
/**
 * @type {number | string}
 */
var numberOrString = Math.random() < 0.5 ? "hello" : 100;
var typeAssertedNumber = /** @type {number} */ (numberOrString);
```

You can even cast to `const` just like TypeScript:

```js twoslash
let one = /** @type {const} */(1);
```

#### Import types

You can import declarations from other files using import types.
This syntax is TypeScript-specific and differs from the JSDoc standard:

```js twoslash
// @filename: types.d.ts
export type Pet = {
  name: string,
};

// @filename: main.js
/**
 * @param {import("./types").Pet} p
 */
function walk(p) {
  console.log(`Walking ${p.name}...`);
}
```

import types can be used to get the type of a value from a module if you don't know the type, or if it has a large type that is annoying to type:

```js twoslash
// @types: node
// @filename: accounts.d.ts
export const userAccount = {
  name: "Name",
  address: "An address",
  postalCode: "",
  country: "",
  planet: "",
  system: "",
  galaxy: "",
  universe: "",
};
// @filename: main.js
// ---cut---
/**
 * @type {typeof import("./accounts").userAccount}
 */
var x = require("./accounts").userAccount;
```

### `@import`

The `@import` tag can let us reference exports from other files.

```js twoslash
// @filename: types.d.ts
export type Pet = {
  name: string,
};
// @filename: main.js
// ---cut---
/**
 * @import {Pet} from "./types"
 */

/**
 * @type {Pet}
 */
var myPet;
myPet.name;
```

These tags don't actually import files at runtime, and the symbols they bring into scope can only be used within JSDoc comments for type-checking.

```js twoslash
// @filename: dog.js
export class Dog {
  woof() {
    console.log("Woof!");
  }
}

// @filename: main.js
/** @import { Dog } from "./dog.js" */

const d = new Dog(); // error!
```

### `@param` and `@returns`

`@param` uses the same type syntax as `@type`, but adds a parameter name.
The parameter may also be declared optional by surrounding the name with square brackets:

```js twoslash
// Parameters may be declared in a variety of syntactic forms
/**
 * @param {string}  p1 - A string param.
 * @param {string=} p2 - An optional param (Google Closure syntax)
 * @param {string} [p3] - Another optional param (JSDoc syntax).
 * @param {string} [p4="test"] - An optional param with a default value
 * @returns {string} This is the result
 */
function stringsStringStrings(p1, p2, p3, p4) {
  // TODO
}
```

Likewise, for the return type of a function:

```js twoslash
/**
 * @return {PromiseLike<string>}
 */
function ps() {}

/**
 * @returns {{ a: string, b: number }} - May use '@returns' as well as '@return'
 */
function ab() {}
```

### `@typedef`, `@callback`, and `@param`

You can define complex types with `@typedef`.
Similar syntax works with `@param`.

```js twoslash
/**
 * @typedef {Object} SpecialType - creates a new type named 'SpecialType'
 * @property {string} prop1 - a string property of SpecialType
 * @property {number} prop2 - a number property of SpecialType
 * @property {number=} prop3 - an optional number property of SpecialType
 * @prop {number} [prop4] - an optional number property of SpecialType
 * @prop {number} [prop5=42] - an optional number property of SpecialType with default
 */

/** @type {SpecialType} */
var specialTypeObject;
specialTypeObject.prop3;
```

You can use either `object` or `Object` on the first line.

```js twoslash
/**
 * @typedef {object} SpecialType1 - creates a new type named 'SpecialType1'
 * @property {string} prop1 - a string property of SpecialType1
 * @property {number} prop2 - a number property of SpecialType1
 * @property {number=} prop3 - an optional number property of SpecialType1
 */

/** @type {SpecialType1} */
var specialTypeObject1;
```

`@param` allows a similar syntax for one-off type specifications.
Note that the nested property names must be prefixed with the name of the parameter:

```js twoslash
/**
 * @param {Object} options - The shape is the same as SpecialType above
 * @param {string} options.prop1
 * @param {number} options.prop2
 * @param {number=} options.prop3
 * @param {number} [options.prop4]
 * @param {number} [options.prop5=42]
 */
function special(options) {
  return (options.prop4 || 1001) + options.prop5;
}
```

`@callback` is similar to `@typedef`, but it specifies a function type instead of an object type:

```js twoslash
/**
 * @callback Predicate
 * @param {string} data
 * @param {number} [index]
 * @returns {boolean}
 */

/** @type {Predicate} */
const ok = (s) => !(s.length % 2);
```

Of course, any of these types can be declared using TypeScript syntax in a single-line `@typedef`:

```js
/** @typedef {{ prop1: string, prop2: string, prop3?: number }} SpecialType */
/** @typedef {(data: string, index?: number) => boolean} Predicate */
```

### `@template`

You can declare type parameters with the `@template` tag.
This lets you make functions, classes, or types that are generic:

```js twoslash
/**
 * @template T
 * @param {T} x - A generic parameter that flows through to the return type
 * @returns {T}
 */
function id(x) {
  return x;
}

const a = id("string");
const b = id(123);
const c = id({});
```

Use comma or multiple tags to declare multiple type parameters:

```js
/**
 * @template T,U,V
 * @template W,X
 */
```

You can also specify a type constraint before the type parameter name.
Only the first type parameter in a list is constrained:

```js twoslash
/**
 * @template {string} K - K must be a string or string literal
 * @template {{ serious(): string }} Seriousalizable - must have a serious method
 * @param {K} key
 * @param {Seriousalizable} object
 */
function seriousalize(key, object) {
  // ????
}
```

Finally, you can specify a default for a type parameter:

```js twoslash
/** @template [T=object] */
class Cache {
    /** @param {T} initial */
    constructor(initial) {
    }
}
let c = new Cache()
```

### `@satisfies`

`@satisfies` provides access to the postfix [operator `satisfies`](/docs/handbook/release-notes/typescript-4-9.html) in TypeScript. Satisfies is used to declare that a value implements a type but does not affect the type of the value. 

```js twoslash
// @errors: 1360
// @ts-check
/**
 * @typedef {"hello world" | "Hello, world"} WelcomeMessage
 */

/** @satisfies {WelcomeMessage} */
const message = "hello world"
//     ^?

/** @satisfies {WelcomeMessage} */
const failingMessage = "Hello world!"

/** @type {WelcomeMessage} */
const messageUsingType = "hello world"
//     ^?
```


## Classes

Classes can be declared as ES6 classes.

```js twoslash
class C {
  /**
   * @param {number} data
   */
  constructor(data) {
    // property types can be inferred
    this.name = "foo";

    // or set explicitly
    /** @type {string | null} */
    this.title = null;

    // or simply annotated, if they're set elsewhere
    /** @type {number} */
    this.size;

    this.initialize(data); // Should error, initializer expects a string
  }
  /**
   * @param {string} s
   */
  initialize = function (s) {
    this.size = s.length;
  };
}

var c = new C(0);

// C should only be called with new, but
// because it is JavaScript, this is allowed and
// considered an 'any'.
var result = C(1);
```

They can also be declared as constructor functions; use [`@constructor`](#constructor) along with [`@this`](#this) for this.

### Property Modifiers
<div id="jsdoc-property-modifiers"></div>


`@public`, `@private`, and `@protected` work exactly like `public`, `private`, and `protected` in TypeScript:

```js twoslash
// @errors: 2341
// @ts-check

class Car {
  constructor() {
    /** @private */
    this.identifier = 100;
  }

  printIdentifier() {
    console.log(this.identifier);
  }
}

const c = new Car();
console.log(c.identifier);
```

- `@public` is always implied and can be left off, but means that a property can be reached from anywhere.
- `@private` means that a property can only be used within the containing class.
- `@protected` means that a property can only be used within the containing class, and all derived subclasses, but not on dissimilar instances of the containing class.

`@public`, `@private`, and `@protected` do not work in constructor functions.

### `@readonly`

The `@readonly` modifier ensures that a property is only ever written to during initialization.

```js twoslash
// @errors: 2540
// @ts-check

class Car {
  constructor() {
    /** @readonly */
    this.identifier = 100;
  }

  printIdentifier() {
    console.log(this.identifier);
  }
}

const c = new Car();
console.log(c.identifier);
```

### `@override`

`@override` works the same way as in TypeScript; use it on methods that override a method from a base class:

```js twoslash
export class C {
  m() { }
}
class D extends C {
  /** @override */
  m() { }
}
```

Set `noImplicitOverride: true` in tsconfig to check overrides.

### `@extends`

When JavaScript classes extend a generic base class, there is no JavaScript syntax for passing a type argument. The `@extends` tag allows this:

```js twoslash
/**
 * @template T
 * @extends {Set<T>}
 */
class SortableSet extends Set {
  // ...
}
```

Note that `@extends` only works with classes. Currently, there is no way for a constructor function to extend a class.

### `@implements`

In the same way, there is no JavaScript syntax for implementing a TypeScript interface. The `@implements` tag works just like in TypeScript:

```js twoslash
/** @implements {Print} */
class TextBook {
  print() {
    // TODO
  }
}
```

### `@constructor`

The compiler infers constructor functions based on this-property assignments, but you can make checking stricter and suggestions better if you add a `@constructor` tag:

```js twoslash
// @checkJs
// @errors: 2345 2348
/**
 * @constructor
 * @param {number} data
 */
function C(data) {
  // property types can be inferred
  this.name = "foo";

  // or set explicitly
  /** @type {string | null} */
  this.title = null;

  // or simply annotated, if they're set elsewhere
  /** @type {number} */
  this.size;

  this.initialize(data);
}
/**
 * @param {string} s
 */
C.prototype.initialize = function (s) {
  this.size = s.length;
};

var c = new C(0);
c.size;

var result = C(1);
```

> Note: Error messages only show up in JS codebases with [a JSConfig](/docs/handbook/tsconfig-json.html) and [`checkJs`](/tsconfig#checkJs) enabled.

With `@constructor`, `this` is checked inside the constructor function `C`, so you will get suggestions for the `initialize` method and an error if you pass it a number. Your editor may also show warnings if you call `C` instead of constructing it.

Unfortunately, this means that constructor functions that are also callable cannot use `@constructor`.

### `@this`

The compiler can usually figure out the type of `this` when it has some context to work with. When it doesn't, you can explicitly specify the type of `this` with `@this`:

```js twoslash
/**
 * @this {HTMLElement}
 * @param {*} e
 */
function callbackForLater(e) {
  this.clientHeight = parseInt(e); // should be fine!
}
```

## Documentation

### `@deprecated`
<div id="deprecated-comments"></div>

When a function, method, or property is deprecated you can let users know by marking it with a `/** @deprecated */` JSDoc comment. That information is surfaced in completion lists and as a suggestion diagnostic that editors can handle specially. In an editor like VS Code, deprecated values are typically displayed in a strike-through style ~~like this~~.

```js twoslash
// @noErrors
/** @deprecated */
const apiV1 = {};
const apiV2 = {};

apiV;
// ^|


```

### `@see`

`@see` lets you link to other names in your program:

```ts twoslash
type Box<T> = { t: T }
/** @see Box for implementation details */
type Boxify<T> = { [K in keyof T]: Box<T> };
```

Some editors will turn `Box` into a link to make it easy to jump there and back.

### `@link`

`@link` is like `@see`, except that it can be used inside other tags:

```ts twoslash
type Box<T> = { t: T }
/** @returns A {@link Box} containing the parameter. */
function box<U>(u: U): Box<U> {
  return { t: u };
}
```

You can also link a property:

```ts twoslash 
type Pet = {
  name: string
  hello: () => string
}

/**
 * Note: you should implement the {@link Pet.hello} method of Pet.
 */
function hello(p: Pet) {
  p.hello()
}
```

Or with an optional name:

```ts twoslash
type Pet = {
  name: string
  hello: () => string
}

/**
 * Note: you should implement the {@link Pet.hello | hello} method of Pet.
 */
function hello(p: Pet) {
  p.hello()
}
```

## Other

### `@enum`

The `@enum` tag allows you to create an object literal whose members are all of a specified type. Unlike most object literals in JavaScript, it does not allow other members.
`@enum` is intended for compatibility with Google Closure's `@enum` tag.

```js twoslash
/** @enum {number} */
const JSDocState = {
  BeginningOfLine: 0,
  SawAsterisk: 1,
  SavingComments: 2,
};

JSDocState.SawAsterisk;
```

Note that `@enum` is quite different from, and much simpler than, TypeScript's `enum`. However, unlike TypeScript's enums, `@enum` can have any type:

```js twoslash
/** @enum {function(number): number} */
const MathFuncs = {
  add1: (n) => n + 1,
  id: (n) => -n,
  sub1: (n) => n - 1,
};

MathFuncs.add1;
```

### `@author`

You can specify the author of an item with `@author`:

```ts twoslash
/**
 * Welcome to awesome.ts
 * @author Ian Awesome <i.am.awesome@example.com>
 */
```

Remember to surround the email address with angle brackets.
Otherwise, `@example` will be parsed as a new tag.

### Other supported patterns

```js twoslash
// @types: react
class Foo {}
// ---cut---
var someObj = {
  /**
   * @param {string} param1 - JSDocs on property assignments work
   */
  x: function (param1) {},
};

/**
 * As do jsdocs on variable assignments
 * @return {Window}
 */
let someFunc = function () {};

/**
 * And class methods
 * @param {string} greeting The greeting to use
 */
Foo.prototype.sayHi = (greeting) => console.log("Hi!");

/**
 * And arrow function expressions
 * @param {number} x - A multiplier
 */
let myArrow = (x) => x * x;

/**
 * Which means it works for function components in JSX too
 * @param {{a: string, b: number}} props - Some param
 */
var fc = (props) => <div>{props.a.charAt(0)}</div>;

/**
 * A parameter can be a class constructor, using Google Closure syntax.
 *
 * @param {{new(...args: any[]): object}} C - The class to register
 */
function registerClass(C) {}

/**
 * @param {...string} p1 - A 'rest' arg (array) of strings. (treated as 'any')
 */
function fn10(p1) {}

/**
 * @param {...string} p1 - A 'rest' arg (array) of strings. (treated as 'any')
 */
function fn9(p1) {
  return p1.join();
}
```

### Unsupported patterns

Postfix equals on a property type in an object literal type doesn't specify an optional property:

```js twoslash
/**
 * @type {{ a: string, b: number= }}
 */
var wrong;
/**
 * Use postfix question on the property name instead:
 * @type {{ a: string, b?: number }}
 */
var right;
```

Nullable types only have meaning if [`strictNullChecks`](/tsconfig#strictNullChecks) is on:

```js twoslash
/**
 * @type {?number}
 * With strictNullChecks: true  -- number | null
 * With strictNullChecks: false -- number
 */
var nullable;
```

The TypeScript-native syntax is a union type:

```js twoslash
/**
 * @type {number | null}
 * With strictNullChecks: true  -- number | null
 * With strictNullChecks: false -- number
 */
var unionNullable;
```

Non-nullable types have no meaning and are treated just as their original type:

```js twoslash
/**
 * @type {!number}
 * Just has type number
 */
var normal;
```

Unlike JSDoc's type system, TypeScript only allows you to mark types as containing null or not.
There is no explicit non-nullability -- if strictNullChecks is on, then `number` is not nullable.
If it is off, then `number` is nullable.

### Unsupported tags

TypeScript ignores any unsupported JSDoc tags.

The following tags have open issues to support them:

- `@memberof` ([issue #7237](https://github.com/Microsoft/TypeScript/issues/7237))
- `@yields` ([issue #23857](https://github.com/Microsoft/TypeScript/issues/23857))
- `@member` ([issue #56674](https://github.com/microsoft/TypeScript/issues/56674))

### Legacy type synonyms

A number of common types are given aliases for compatibility with old JavaScript code.
Some of the aliases are the same as existing types, although most of those are rarely used.
For example, `String` is treated as an alias for `string`.
Even though `String` is a type in TypeScript, old JSDoc often uses it to mean `string`.
Besides, in TypeScript, the capitalized versions of primitive types are wrapper types -- almost always a mistake to use.
So the compiler treats these types as synonyms based on usage in old JSDoc:

- `String -> string`
- `Number -> number`
- `Boolean -> boolean`
- `Void -> void`
- `Undefined -> undefined`
- `Null -> null`
- `function -> Function`
- `array -> Array<any>`
- `promise -> Promise<any>`
- `Object -> any`
- `object -> any`

The last four aliases are turned off when `noImplicitAny: true`:

- `object` and `Object` are built-in types, although `Object` is rarely used.
- `array` and `promise` are not built-in, but might be declared somewhere in your program.

---

## Source: `packages/documentation/copy/en/javascript/Type Checking JavaScript Files.md`

---
title: Type Checking JavaScript Files
layout: docs
permalink: /docs/handbook/type-checking-javascript-files.html
oneline: How to add type checking to JavaScript files using TypeScript
---

Here are some notable differences on how checking works in `.js` files compared to `.ts` files.

## Properties are inferred from assignments in class bodies

ES2015 does not have a means for declaring properties on classes. Properties are dynamically assigned, just like object literals.

In a `.js` file, the compiler infers properties from property assignments inside the class body.
The type of a property is the type given in the constructor, unless it's not defined there, or the type in the constructor is undefined or null.
In that case, the type is the union of the types of all the right-hand values in these assignments.
Properties defined in the constructor are always assumed to exist, whereas ones defined just in methods, getters, or setters are considered optional.

```js twoslash
// @checkJs
// @errors: 2322
class C {
  constructor() {
    this.constructorOnly = 0;
    this.constructorUnknown = undefined;
  }
  method() {
    this.constructorOnly = false;
    this.constructorUnknown = "plunkbat"; // ok, constructorUnknown is string | undefined
    this.methodOnly = "ok"; // ok, but methodOnly could also be undefined
  }
  method2() {
    this.methodOnly = true; // also, ok, methodOnly's type is string | boolean | undefined
  }
}
```

If properties are never set in the class body, they are considered unknown.
If your class has properties that are only read from, add and then annotate a declaration in the constructor with JSDoc to specify the type.
You don't even have to give a value if it will be initialized later:

```js twoslash
// @checkJs
// @errors: 2322
class C {
  constructor() {
    /** @type {number | undefined} */
    this.prop = undefined;
    /** @type {number | undefined} */
    this.count;
  }
}

let c = new C();
c.prop = 0; // OK
c.count = "string";
```

## Constructor functions are equivalent to classes

Before ES2015, JavaScript used constructor functions instead of classes.
The compiler supports this pattern and understands constructor functions as equivalent to ES2015 classes.
The property inference rules described above work exactly the same way.

```js twoslash
// @checkJs
// @errors: 2683 2322
function C() {
  this.constructorOnly = 0;
  this.constructorUnknown = undefined;
}
C.prototype.method = function () {
  this.constructorOnly = false;
  this.constructorUnknown = "plunkbat"; // OK, the type is string | undefined
};
```

## CommonJS modules are supported

In a `.js` file, TypeScript understands the CommonJS module format.
Assignments to `exports` and `module.exports` are recognized as export declarations.
Similarly, `require` function calls are recognized as module imports. For example:

```js
// same as `import module "fs"`
const fs = require("fs");

// same as `export function readFile`
module.exports.readFile = function (f) {
  return fs.readFileSync(f);
};
```

The module support in JavaScript is much more syntactically forgiving than TypeScript's module support.
Most combinations of assignments and declarations are supported.

## Classes, functions, and object literals are namespaces

Classes are namespaces in `.js` files.
This can be used to nest classes, for example:

```js twoslash
class C {}
C.D = class {};
```

And, for pre-ES2015 code, it can be used to simulate static methods:

```js twoslash
function Outer() {
  this.y = 2;
}

Outer.Inner = function () {
  this.yy = 2;
};

Outer.Inner();
```

It can also be used to create simple namespaces:

```js twoslash
var ns = {};
ns.C = class {};
ns.func = function () {};

ns;
```

Other variants are allowed as well:

```js twoslash
// IIFE
var ns = (function (n) {
  return n || {};
})();
ns.CONST = 1;

// defaulting to global
var assign =
  assign ||
  function () {
    // code goes here
  };
assign.extra = 1;
```

## Object literals are open-ended

In a `.ts` file, an object literal that initializes a variable declaration gives its type to the declaration.
No new members can be added that were not specified in the original literal.
This rule is relaxed in a `.js` file; object literals have an open-ended type (an index signature) that allows adding and looking up properties that were not defined originally.
For instance:

```js twoslash
var obj = { a: 1 };
obj.b = 2; // Allowed
```

Object literals behave as if they have an index signature `[x:string]: any` that allows them to be treated as open maps instead of closed objects.

Like other special JS checking behaviors, this behavior can be changed by specifying a JSDoc type for the variable. For example:

```js twoslash
// @checkJs
// @errors: 2339
/** @type {{a: number}} */
var obj = { a: 1 };
obj.b = 2;
```

## null, undefined, and empty array initializers are of type any or any[]

Any variable, parameter or property that is initialized with null or undefined will have type any, even if strict null checks is turned on.
Any variable, parameter or property that is initialized with [] will have type any[], even if strict null checks is turned on.
The only exception is for properties that have multiple initializers as described above.

```js twoslash
function Foo(i = null) {
  if (!i) i = 1;
  var j = undefined;
  j = 2;
  this.l = [];
}

var foo = new Foo();
foo.l.push(foo.i);
foo.l.push("end");
```

## Function parameters are optional by default

Since there is no way to specify optionality on parameters in pre-ES2015 JavaScript, all function parameters in `.js` file are considered optional.
Calls with fewer arguments than the declared number of parameters are allowed.

It is important to note that it is an error to call a function with too many arguments.

For instance:

```js twoslash
// @checkJs
// @strict: false
// @errors: 7006 7006 2554
function bar(a, b) {
  console.log(a + " " + b);
}

bar(1); // OK, second argument considered optional
bar(1, 2);
bar(1, 2, 3); // Error, too many arguments
```

JSDoc annotated functions are excluded from this rule.
Use JSDoc optional parameter syntax (`[` `]`) to express optionality. e.g.:

```js twoslash
/**
 * @param {string} [somebody] - Somebody's name.
 */
function sayHello(somebody) {
  if (!somebody) {
    somebody = "John Doe";
  }
  console.log("Hello " + somebody);
}

sayHello();
```

## Var-args parameter declaration inferred from use of `arguments`

A function whose body has a reference to the `arguments` reference is implicitly considered to have a var-arg parameter (i.e. `(...arg: any[]) => any`). Use JSDoc var-arg syntax to specify the type of the arguments.

```js twoslash
/** @param {...number} args */
function sum(/* numbers */) {
  var total = 0;
  for (var i = 0; i < arguments.length; i++) {
    total += arguments[i];
  }
  return total;
}
```

## Unspecified type parameters default to `any`

Since there is no natural syntax for specifying generic type parameters in JavaScript, an unspecified type parameter defaults to `any`.

### In extends clause

For instance, `React.Component` is defined to have two type parameters, `Props` and `State`.
In a `.js` file, there is no legal way to specify these in the extends clause. By default the type arguments will be `any`:

```js
import { Component } from "react";

class MyComponent extends Component {
  render() {
    this.props.b; // Allowed, since this.props is of type any
  }
}
```

Use JSDoc `@augments` to specify the types explicitly. for instance:

```js
import { Component } from "react";

/**
 * @augments {Component<{a: number}, State>}
 */
class MyComponent extends Component {
  render() {
    this.props.b; // Error: b does not exist on {a:number}
  }
}
```

### In JSDoc references

An unspecified type argument in JSDoc defaults to any:

```js twoslash
/** @type{Array} */
var x = [];

x.push(1); // OK
x.push("string"); // OK, x is of type Array<any>

/** @type{Array.<number>} */
var y = [];

y.push(1); // OK
y.push("string"); // Error, string is not assignable to number
```

### In function calls

A call to a generic function uses the arguments to infer the type parameters. Sometimes this process fails to infer any types, mainly because of lack of inference sources; in these cases, the type parameters will default to `any`. For example:

```js
var p = new Promise((resolve, reject) => {
  reject();
});

p; // Promise<any>;
```

To learn all of the features available in JSDoc, see [the reference](/docs/handbook/jsdoc-supported-types.html).

---

## Source: `packages/documentation/copy/en/project-config/Compiler Options in MSBuild.md`

---
title: Compiler Options in MSBuild
layout: docs
permalink: /docs/handbook/compiler-options-in-msbuild.html
oneline: Which compiler options are available in MSBuild projects.
---

## Overview

When you have an MSBuild based project which utilizes TypeScript such as an ASP.NET Core project, you can configure TypeScript in two ways. Either via a `tsconfig.json` or via the project settings.

## Using a `tsconfig.json`

We recommend using a `tsconfig.json` for your project when possible. To add one to an existing project, add a new item to your project which is called a "TypeScript JSON Configuration File" in modern versions of Visual Studio.

The new `tsconfig.json` will then be used as the source of truth for TypeScript-specific build information like files and configuration. You can learn [about how TSConfigs works here](/docs/handbook/tsconfig-json.html) and there is a [comprehensive reference here](/tsconfig).

## Using Project Settings

You can also define the configuration for TypeScript inside you project's settings. This is done by editing the XML in your `.csproj` to define `PropertyGroups` which describe how the build can work:

```xml
<PropertyGroup>
  <TypeScriptNoEmitOnError>true</TypeScriptNoEmitOnError>
  <TypeScriptNoImplicitReturns>true</TypeScriptNoImplicitReturns>
</PropertyGroup>
```

There is a series of mappings for common TypeScript settings, these are settings which map directly to [TypeScript cli options](/docs/handbook/compiler-options.html) and are used to help you write a more understandable project file. You can use the [TSConfig reference](/tsconfig) to get more information on what values and defaults are for each mapping.

<!-- Start of replacement  --><h3>CLI Mappings</h3>

  <table class='cli-option' width="100%">
    <thead>
    <tr>
    <th>MSBuild Config Name</th>
    <th>TSC Flag</th>
    </tr>
  </thead>
  <tbody>

<tr class='odd' name='allowJs'>
<td><code>&#x3C;TypeScriptAllowJS&#x3E;</code></td>
<td><code><a href='/tsconfig/#allowJs'>--allowJs</a></code></td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Allow JavaScript files to be a part of your program. Use the <code>checkJS</code> option to get errors from these files.</p>

</tr></td>
<tr class='even' name='removeComments'>
<td><code>&#x3C;TypeScriptRemoveComments&#x3E;</code></td>
<td><code><a href='/tsconfig/#removeComments'>--removeComments</a></code></td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Disable emitting comments.</p>

</tr></td>
<tr class='odd' name='noImplicitAny'>
<td><code>&#x3C;TypeScriptNoImplicitAny&#x3E;</code></td>
<td><code><a href='/tsconfig/#noImplicitAny'>--noImplicitAny</a></code></td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Enable error reporting for expressions and declarations with an implied <code>any</code> type..</p>

</tr></td>
<tr class='even' name='declaration'>
<td><code>&#x3C;TypeScriptGeneratesDeclarations&#x3E;</code></td>
<td><code><a href='/tsconfig/#declaration'>--declaration</a></code></td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Generate .d.ts files from TypeScript and JavaScript files in your project.</p>

</tr></td>
<tr class='odd' name='module'>
<td><code>&#x3C;TypeScriptModuleKind&#x3E;</code></td>
<td><code><a href='/tsconfig/#module'>--module</a></code></td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Specify what module code is generated.</p>

</tr></td>
<tr class='even' name='jsx'>
<td><code>&#x3C;TypeScriptJSXEmit&#x3E;</code></td>
<td><code><a href='/tsconfig/#jsx'>--jsx</a></code></td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Specify what JSX code is generated.</p>

</tr></td>
<tr class='odd' name='outDir'>
<td><code>&#x3C;TypeScriptOutDir&#x3E;</code></td>
<td><code><a href='/tsconfig/#outDir'>--outDir</a></code></td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Specify an output folder for all emitted files.</p>

</tr></td>
<tr class='even' name='sourcemap'>
<td><code>&#x3C;TypeScriptSourceMap&#x3E;</code></td>
<td><code><a href='/tsconfig/#sourcemap'>--sourcemap</a></code></td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Create source map files for emitted JavaScript files.</p>

</tr></td>
<tr class='odd' name='target'>
<td><code>&#x3C;TypeScriptTarget&#x3E;</code></td>
<td><code><a href='/tsconfig/#target'>--target</a></code></td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Set the JavaScript language version for emitted JavaScript and include compatible library declarations.</p>

</tr></td>
<tr class='even' name='noResolve'>
<td><code>&#x3C;TypeScriptNoResolve&#x3E;</code></td>
<td><code><a href='/tsconfig/#noResolve'>--noResolve</a></code></td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Disallow <code>import</code>s, <code>require</code>s or <code>&#x3C;reference></code>s from expanding the number of files TypeScript should add to a project.</p>

</tr></td>
<tr class='odd' name='mapRoot'>
<td><code>&#x3C;TypeScriptMapRoot&#x3E;</code></td>
<td><code><a href='/tsconfig/#mapRoot'>--mapRoot</a></code></td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Specify the location where debugger should locate map files instead of generated locations.</p>

</tr></td>
<tr class='even' name='sourceRoot'>
<td><code>&#x3C;TypeScriptSourceRoot&#x3E;</code></td>
<td><code><a href='/tsconfig/#sourceRoot'>--sourceRoot</a></code></td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Specify the root path for debuggers to find the reference source code.</p>

</tr></td>
<tr class='odd' name='charset'>
<td><code>&#x3C;TypeScriptCharset&#x3E;</code></td>
<td><code><a href='/tsconfig/#charset'>--charset</a></code></td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>No longer supported. In early versions, manually set the text encoding for reading files.</p>

</tr></td>
<tr class='even' name='emitBOM'>
<td><code>&#x3C;TypeScriptEmitBOM&#x3E;</code></td>
<td><code><a href='/tsconfig/#emitBOM'>--emitBOM</a></code></td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Emit a UTF-8 Byte Order Mark (BOM) in the beginning of output files.</p>

</tr></td>
<tr class='odd' name='noLib'>
<td><code>&#x3C;TypeScriptNoLib&#x3E;</code></td>
<td><code><a href='/tsconfig/#noLib'>--noLib</a></code></td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Disable including any library files, including the default lib.d.ts.</p>

</tr></td>
<tr class='even' name='preserveConstEnums'>
<td><code>&#x3C;TypeScriptPreserveConstEnums&#x3E;</code></td>
<td><code><a href='/tsconfig/#preserveConstEnums'>--preserveConstEnums</a></code></td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Disable erasing <code>const enum</code> declarations in generated code.</p>

</tr></td>
<tr class='odd' name='suppressImplicitAnyIndexErrors'>
<td><code>&#x3C;TypeScriptSuppressImplicitAnyIndexErrors&#x3E;</code></td>
<td><code><a href='/tsconfig/#suppressImplicitAnyIndexErrors'>--suppressImplicitAnyIndexErrors</a></code></td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Suppress <code>noImplicitAny</code> errors when indexing objects that lack index signatures.</p>

</tr></td>
<tr class='even' name='noEmitHelpers'>
<td><code>&#x3C;TypeScriptNoEmitHelpers&#x3E;</code></td>
<td><code><a href='/tsconfig/#noEmitHelpers'>--noEmitHelpers</a></code></td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Disable generating custom helper functions like <code>__extends</code> in compiled output.</p>

</tr></td>
<tr class='odd' name='inlineSourceMap'>
<td><code>&#x3C;TypeScriptInlineSourceMap&#x3E;</code></td>
<td><code><a href='/tsconfig/#inlineSourceMap'>--inlineSourceMap</a></code></td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Include sourcemap files inside the emitted JavaScript.</p>

</tr></td>
<tr class='even' name='inlineSources'>
<td><code>&#x3C;TypeScriptInlineSources&#x3E;</code></td>
<td><code><a href='/tsconfig/#inlineSources'>--inlineSources</a></code></td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Include source code in the sourcemaps inside the emitted JavaScript.</p>

</tr></td>
<tr class='odd' name='newLine'>
<td><code>&#x3C;TypeScriptNewLine&#x3E;</code></td>
<td><code><a href='/tsconfig/#newLine'>--newLine</a></code></td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Set the newline character for emitting files.</p>

</tr></td>
<tr class='even' name='isolatedModules'>
<td><code>&#x3C;TypeScriptIsolatedModules&#x3E;</code></td>
<td><code><a href='/tsconfig/#isolatedModules'>--isolatedModules</a></code></td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Ensure that each file can be safely transpiled without relying on other imports.</p>

</tr></td>
<tr class='odd' name='emitDecoratorMetadata'>
<td><code>&#x3C;TypeScriptEmitDecoratorMetadata&#x3E;</code></td>
<td><code><a href='/tsconfig/#emitDecoratorMetadata'>--emitDecoratorMetadata</a></code></td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Emit design-type metadata for decorated declarations in source files.</p>

</tr></td>
<tr class='even' name='rootDir'>
<td><code>&#x3C;TypeScriptRootDir&#x3E;</code></td>
<td><code><a href='/tsconfig/#rootDir'>--rootDir</a></code></td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Specify the root folder within your source files.</p>

</tr></td>
<tr class='odd' name='experimentalDecorators'>
<td><code>&#x3C;TypeScriptExperimentalDecorators&#x3E;</code></td>
<td><code><a href='/tsconfig/#experimentalDecorators'>--experimentalDecorators</a></code></td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Enable experimental support for TC39 stage 2 draft decorators.</p>

</tr></td>
<tr class='even' name='moduleResolution'>
<td><code>&#x3C;TypeScriptModuleResolution&#x3E;</code></td>
<td><code><a href='/tsconfig/#moduleResolution'>--moduleResolution</a></code></td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Specify how TypeScript looks up a file from a given module specifier.</p>

</tr></td>
<tr class='odd' name='suppressExcessPropertyErrors'>
<td><code>&#x3C;TypeScriptSuppressExcessPropertyErrors&#x3E;</code></td>
<td><code><a href='/tsconfig/#suppressExcessPropertyErrors'>--suppressExcessPropertyErrors</a></code></td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Disable reporting of excess property errors during the creation of object literals.</p>

</tr></td>
<tr class='even' name='reactNamespace'>
<td><code>&#x3C;TypeScriptReactNamespace&#x3E;</code></td>
<td><code><a href='/tsconfig/#reactNamespace'>--reactNamespace</a></code></td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Specify the object invoked for <code>createElement</code>. This only applies when targeting <code>react</code> JSX emit.</p>

</tr></td>
<tr class='odd' name='skipDefaultLibCheck'>
<td><code>&#x3C;TypeScriptSkipDefaultLibCheck&#x3E;</code></td>
<td><code><a href='/tsconfig/#skipDefaultLibCheck'>--skipDefaultLibCheck</a></code></td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Skip type checking .d.ts files that are included with TypeScript.</p>

</tr></td>
<tr class='even' name='allowUnusedLabels'>
<td><code>&#x3C;TypeScriptAllowUnusedLabels&#x3E;</code></td>
<td><code><a href='/tsconfig/#allowUnusedLabels'>--allowUnusedLabels</a></code></td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Disable error reporting for unused labels.</p>

</tr></td>
<tr class='odd' name='noImplicitReturns'>
<td><code>&#x3C;TypeScriptNoImplicitReturns&#x3E;</code></td>
<td><code><a href='/tsconfig/#noImplicitReturns'>--noImplicitReturns</a></code></td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Enable error reporting for codepaths that do not explicitly return in a function.</p>

</tr></td>
<tr class='even' name='noFallthroughCasesInSwitch'>
<td><code>&#x3C;TypeScriptNoFallthroughCasesInSwitch&#x3E;</code></td>
<td><code><a href='/tsconfig/#noFallthroughCasesInSwitch'>--noFallthroughCasesInSwitch</a></code></td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Enable error reporting for fallthrough cases in switch statements.</p>

</tr></td>
<tr class='odd' name='allowUnreachableCode'>
<td><code>&#x3C;TypeScriptAllowUnreachableCode&#x3E;</code></td>
<td><code><a href='/tsconfig/#allowUnreachableCode'>--allowUnreachableCode</a></code></td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Disable error reporting for unreachable code.</p>

</tr></td>
<tr class='even' name='forceConsistentCasingInFileNames'>
<td><code>&#x3C;TypeScriptForceConsistentCasingInFileNames&#x3E;</code></td>
<td><code><a href='/tsconfig/#forceConsistentCasingInFileNames'>--forceConsistentCasingInFileNames</a></code></td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Ensure that casing is correct in imports.</p>

</tr></td>
<tr class='odd' name='allowSyntheticDefaultImports'>
<td><code>&#x3C;TypeScriptAllowSyntheticDefaultImports&#x3E;</code></td>
<td><code><a href='/tsconfig/#allowSyntheticDefaultImports'>--allowSyntheticDefaultImports</a></code></td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Allow 'import x from y' when a module doesn't have a default export.</p>

</tr></td>
<tr class='even' name='noImplicitUseStrict'>
<td><code>&#x3C;TypeScriptNoImplicitUseStrict&#x3E;</code></td>
<td><code><a href='/tsconfig/#noImplicitUseStrict'>--noImplicitUseStrict</a></code></td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Disable adding 'use strict' directives in emitted JavaScript files.</p>

</tr></td>
<tr class='odd' name='lib'>
<td><code>&#x3C;TypeScriptLib&#x3E;</code></td>
<td><code><a href='/tsconfig/#lib'>--lib</a></code></td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Specify a set of bundled library declaration files that describe the target runtime environment.</p>

</tr></td>
<tr class='even' name='baseUrl'>
<td><code>&#x3C;TypeScriptBaseUrl&#x3E;</code></td>
<td><code><a href='/tsconfig/#baseUrl'>--baseUrl</a></code></td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Specify the base directory to resolve bare specifier module names.</p>

</tr></td>
<tr class='odd' name='declarationDir'>
<td><code>&#x3C;TypeScriptDeclarationDir&#x3E;</code></td>
<td><code><a href='/tsconfig/#declarationDir'>--declarationDir</a></code></td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Specify the output directory for generated declaration files.</p>

</tr></td>
<tr class='even' name='noImplicitThis'>
<td><code>&#x3C;TypeScriptNoImplicitThis&#x3E;</code></td>
<td><code><a href='/tsconfig/#noImplicitThis'>--noImplicitThis</a></code></td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Enable error reporting when <code>this</code> is given the type <code>any</code>.</p>

</tr></td>
<tr class='odd' name='skipLibCheck'>
<td><code>&#x3C;TypeScriptSkipLibCheck&#x3E;</code></td>
<td><code><a href='/tsconfig/#skipLibCheck'>--skipLibCheck</a></code></td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Skip type checking all .d.ts files.</p>

</tr></td>
<tr class='even' name='strictNullChecks'>
<td><code>&#x3C;TypeScriptStrictNullChecks&#x3E;</code></td>
<td><code><a href='/tsconfig/#strictNullChecks'>--strictNullChecks</a></code></td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>When type checking, take into account <code>null</code> and <code>undefined</code>.</p>

</tr></td>
<tr class='odd' name='noUnusedLocals'>
<td><code>&#x3C;TypeScriptNoUnusedLocals&#x3E;</code></td>
<td><code><a href='/tsconfig/#noUnusedLocals'>--noUnusedLocals</a></code></td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Enable error reporting when a local variables aren't read.</p>

</tr></td>
<tr class='even' name='noUnusedParameters'>
<td><code>&#x3C;TypeScriptNoUnusedParameters&#x3E;</code></td>
<td><code><a href='/tsconfig/#noUnusedParameters'>--noUnusedParameters</a></code></td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Raise an error when a function parameter isn't read</p>

</tr></td>
<tr class='odd' name='alwaysStrict'>
<td><code>&#x3C;TypeScriptAlwaysStrict&#x3E;</code></td>
<td><code><a href='/tsconfig/#alwaysStrict'>--alwaysStrict</a></code></td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Ensure 'use strict' is always emitted.</p>

</tr></td>
<tr class='even' name='importHelpers'>
<td><code>&#x3C;TypeScriptImportHelpers&#x3E;</code></td>
<td><code><a href='/tsconfig/#importHelpers'>--importHelpers</a></code></td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Allow importing helper functions from tslib once per project, instead of including them per-file.</p>

</tr></td>
<tr class='odd' name='jsxFactory'>
<td><code>&#x3C;TypeScriptJSXFactory&#x3E;</code></td>
<td><code><a href='/tsconfig/#jsxFactory'>--jsxFactory</a></code></td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Specify the JSX factory function used when targeting React JSX emit, e.g. 'React.createElement' or 'h'</p>

</tr></td>
<tr class='even' name='stripInternal'>
<td><code>&#x3C;TypeScriptStripInternal&#x3E;</code></td>
<td><code><a href='/tsconfig/#stripInternal'>--stripInternal</a></code></td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Disable emitting declarations that have <code>@internal</code> in their JSDoc comments.</p>

</tr></td>
<tr class='odd' name='checkJs'>
<td><code>&#x3C;TypeScriptCheckJs&#x3E;</code></td>
<td><code><a href='/tsconfig/#checkJs'>--checkJs</a></code></td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Enable error reporting in type-checked JavaScript files.</p>

</tr></td>
<tr class='even' name='downlevelIteration'>
<td><code>&#x3C;TypeScriptDownlevelIteration&#x3E;</code></td>
<td><code><a href='/tsconfig/#downlevelIteration'>--downlevelIteration</a></code></td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Emit more compliant, but verbose and less performant JavaScript for iteration.</p>

</tr></td>
<tr class='odd' name='strict'>
<td><code>&#x3C;TypeScriptStrict&#x3E;</code></td>
<td><code><a href='/tsconfig/#strict'>--strict</a></code></td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Enable all strict type checking options.</p>

</tr></td>
<tr class='even' name='noStrictGenericChecks'>
<td><code>&#x3C;TypeScriptNoStrictGenericChecks&#x3E;</code></td>
<td><code><a href='/tsconfig/#noStrictGenericChecks'>--noStrictGenericChecks</a></code></td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Disable strict checking of generic signatures in function types.</p>

</tr></td>
<tr class='odd' name='preserveSymlinks'>
<td><code>&#x3C;TypeScriptPreserveSymlinks&#x3E;</code></td>
<td><code><a href='/tsconfig/#preserveSymlinks'>--preserveSymlinks</a></code></td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Disable resolving symlinks to their realpath. This correlates to the same flag in node.</p>

</tr></td>
<tr class='even' name='strictFunctionTypes'>
<td><code>&#x3C;TypeScriptStrictFunctionTypes&#x3E;</code></td>
<td><code><a href='/tsconfig/#strictFunctionTypes'>--strictFunctionTypes</a></code></td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>When assigning functions, check to ensure parameters and the return values are subtype-compatible.</p>

</tr></td>
<tr class='odd' name='strictPropertyInitialization'>
<td><code>&#x3C;TypeScriptStrictPropertyInitialization&#x3E;</code></td>
<td><code><a href='/tsconfig/#strictPropertyInitialization'>--strictPropertyInitialization</a></code></td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Check for class properties that are declared but not set in the constructor.</p>

</tr></td>
<tr class='even' name='esModuleInterop'>
<td><code>&#x3C;TypeScriptESModuleInterop&#x3E;</code></td>
<td><code><a href='/tsconfig/#esModuleInterop'>--esModuleInterop</a></code></td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Emit additional JavaScript to ease support for importing CommonJS modules. This enables <code>allowSyntheticDefaultImports</code> for type compatibility.</p>

</tr></td>
<tr class='odd' name='emitDeclarationOnly'>
<td><code>&#x3C;TypeScriptEmitDeclarationOnly&#x3E;</code></td>
<td><code><a href='/tsconfig/#emitDeclarationOnly'>--emitDeclarationOnly</a></code></td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Only output d.ts files and not JavaScript files.</p>

</tr></td>
<tr class='even' name='keyofStringsOnly'>
<td><code>&#x3C;TypeScriptKeyofStringsOnly&#x3E;</code></td>
<td><code><a href='/tsconfig/#keyofStringsOnly'>--keyofStringsOnly</a></code></td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Make keyof only return strings instead of string, numbers or symbols. Legacy option.</p>

</tr></td>
<tr class='odd' name='useDefineForClassFields'>
<td><code>&#x3C;TypeScriptUseDefineForClassFields&#x3E;</code></td>
<td><code><a href='/tsconfig/#useDefineForClassFields'>--useDefineForClassFields</a></code></td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Emit ECMAScript-standard-compliant class fields.</p>

</tr></td>
<tr class='even' name='declarationMap'>
<td><code>&#x3C;TypeScriptDeclarationMap&#x3E;</code></td>
<td><code><a href='/tsconfig/#declarationMap'>--declarationMap</a></code></td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Create sourcemaps for d.ts files.</p>

</tr></td>
<tr class='odd' name='resolveJsonModule'>
<td><code>&#x3C;TypeScriptResolveJsonModule&#x3E;</code></td>
<td><code><a href='/tsconfig/#resolveJsonModule'>--resolveJsonModule</a></code></td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Enable importing .json files</p>

</tr></td>
<tr class='even' name='strictBindCallApply'>
<td><code>&#x3C;TypeScriptStrictBindCallApply&#x3E;</code></td>
<td><code><a href='/tsconfig/#strictBindCallApply'>--strictBindCallApply</a></code></td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Check that the arguments for <code>bind</code>, <code>call</code>, and <code>apply</code> methods match the original function.</p>

</tr></td>
<tr class='odd' name='noEmitOnError'>
<td><code>&#x3C;TypeScriptNoEmitOnError&#x3E;</code></td>
<td><code><a href='/tsconfig/#noEmitOnError'>--noEmitOnError</a></code></td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Disable emitting files if any type checking errors are reported.</p>

</tr></td>
</tbody></table>
<!-- End of replacement  -->

### Additional Flags

Because the MSBuild system passes arguments directly to the TypeScript CLI, you can use the option `TypeScriptAdditionalFlags` to provide specific flags which don't have a mapping above.

For example, this would turn on [`noPropertyAccessFromIndexSignature`](/tsconfig#noPropertyAccessFromIndexSignature):

```xml
<TypeScriptAdditionalFlags> $(TypeScriptAdditionalFlags) --noPropertyAccessFromIndexSignature</TypeScriptAdditionalFlags>
```

### Debug and Release Builds

You can use PropertyGroup conditions to define different sets of configurations. For example, a common task is stripping comments and sourcemaps in production. In this example, we define a debug and release property group which have different TypeScript configurations:

```xml
<PropertyGroup Condition="'$(Configuration)' == 'Debug'">
  <TypeScriptRemoveComments>false</TypeScriptRemoveComments>
  <TypeScriptSourceMap>true</TypeScriptSourceMap>
</PropertyGroup>

<PropertyGroup Condition="'$(Configuration)' == 'Release'">
  <TypeScriptRemoveComments>true</TypeScriptRemoveComments>
  <TypeScriptSourceMap>false</TypeScriptSourceMap>
</PropertyGroup>

<Import
    Project="$(MSBuildExtensionsPath32)\Microsoft\VisualStudio\v$(VisualStudioVersion)\TypeScript\Microsoft.TypeScript.targets"
    Condition="Exists('$(MSBuildExtensionsPath32)\Microsoft\VisualStudio\v$(VisualStudioVersion)\TypeScript\Microsoft.TypeScript.targets')" />
```

### ToolsVersion

The value of `<TypeScriptToolsVersion>1.7</TypeScriptToolsVersion>` property in the project file identifies the compiler version to use to build (1.7 in this example).
This allows a project to build against the same versions of the compiler on different machines.

If `TypeScriptToolsVersion` is not specified, the latest compiler version installed on the machine will be used to build.

Users using newer versions of TS, will see a prompt to upgrade their project on first load.

### TypeScriptCompileBlocked

If you are using a different build tool to build your project (e.g. gulp, grunt , etc.) and VS for the development and debugging experience, set `<TypeScriptCompileBlocked>true</TypeScriptCompileBlocked>` in your project.
This should give you all the editing support, but not the build when you hit F5.

### TypeScriptEnableIncrementalMSBuild (TypeScript 4.2 Beta and later)

By default, MSBuild will attempt to only run the TypeScript compiler when the project's source files have been updated since the last compilation.
However, if this behavior is causing issues, such as when TypeScript's [`incremental`](/tsconfig#incremental) option is enabled, set `<TypeScriptEnableIncrementalMSBuild>false</TypeScriptEnableIncrementalMSBuild>` to ensure the TypeScript compiler is invoked with every run of MSBuild.

---

## Source: `packages/documentation/copy/en/project-config/Compiler Options.md`

---
title: tsc CLI Options
layout: docs
permalink: /docs/handbook/compiler-options.html
oneline: A very high-level overview of the CLI compiler options for tsc
disable_toc: true
---

## Using the CLI

Running `tsc` locally will compile the closest project defined by a `tsconfig.json`, or you can compile a set of TypeScript
files by passing in a glob of files you want. When input files are specified on the command line, `tsconfig.json` files are
ignored.

```sh
# Run a compile based on a backwards look through the fs for a tsconfig.json
tsc

# Emit JS for just the index.ts with the compiler defaults
tsc index.ts

# Emit JS for any .ts files in the folder src, with the default settings
tsc src/*.ts

# Emit files referenced in with the compiler settings from tsconfig.production.json
tsc --project tsconfig.production.json

# Emit d.ts files for a js file with showing compiler options which are booleans
tsc index.js --declaration --emitDeclarationOnly

# Emit a single .js file from two files via compiler options which take string arguments
tsc app.ts util.ts --target esnext --outfile index.js
```

## Compiler Options

**If you're looking for more information about the compiler options in a tsconfig, check out the [TSConfig Reference](/tsconfig)**

<!-- Start of replacement  --><h3>CLI Commands</h3>
<table class="cli-option" width="100%">
  <thead>
    <tr>
      <th>Flag</th>
      <th>Type</th>
    </tr>
  </thead>
  <tbody>
<tr class='odd' name='all'>
  <td><code>--all</code></td>
  <td><p><code>boolean</code></p>
</td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Show all compiler options.</p>
</td></tr>

<tr class='even' name='help'>
  <td><code>--help</code></td>
  <td><p><code>boolean</code></p>
</td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Gives local information for help on the CLI.</p>
</td></tr>

<tr class='odd' name='ignoreConfig'>
  <td><code>--ignoreConfig</code></td>
  <td><p><code>boolean</code></p>
</td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Ignore the tsconfig found and build with commandline options and files.</p>
</td></tr>

<tr class='even' name='init'>
  <td><code>--init</code></td>
  <td><p><code>boolean</code></p>
</td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Initializes a TypeScript project and creates a tsconfig.json file.</p>
</td></tr>

<tr class='odd' name='listFilesOnly'>
  <td><code>--listFilesOnly</code></td>
  <td><p><code>boolean</code></p>
</td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Print names of files that are part of the compilation and then stop processing.</p>
</td></tr>

<tr class='even' name='locale'>
  <td><code>--locale</code></td>
  <td><p><code>string</code></p>
</td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Set the language of the messaging from TypeScript. This does not affect emit.</p>
</td></tr>

<tr class='odd' name='project'>
  <td><code>--project</code></td>
  <td><p><code>string</code></p>
</td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Compile the project given the path to its configuration file, or to a folder with a 'tsconfig.json'.</p>
</td></tr>

<tr class='even' name='showConfig'>
  <td><code>--showConfig</code></td>
  <td><p><code>boolean</code></p>
</td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Print the final configuration instead of building.</p>
</td></tr>

<tr class='odd' name='version'>
  <td><code>--version</code></td>
  <td><p><code>boolean</code></p>
</td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Print the compiler's version.</p>
</td></tr>

</tbody></table>

<h3>Build Options</h3>
<table class="cli-option" width="100%">
  <thead>
    <tr>
      <th>Flag</th>
      <th>Type</th>
    </tr>
  </thead>
  <tbody>
<tr class='odd' name='build'>
  <td><code>--build</code></td>
  <td><p><code>boolean</code></p>
</td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Build one or more projects and their dependencies, if out of date</p>
</td></tr>

<tr class='even' name='clean'>
  <td><code>--clean</code></td>
  <td><p><code>boolean</code></p>
</td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Delete the outputs of all projects.</p>
</td></tr>

<tr class='odd' name='dry'>
  <td><code>--dry</code></td>
  <td><p><code>boolean</code></p>
</td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Show what would be built (or deleted, if specified with '--clean')</p>
</td></tr>

<tr class='even' name='force'>
  <td><code><a href='/tsconfig/#force'>--force</a></code></td>
  <td><p><code>boolean</code></p>
</td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Build all projects, including those that appear to be up to date.</p>
</td></tr>

<tr class='odd' name='verbose'>
  <td><code><a href='/tsconfig/#verbose'>--verbose</a></code></td>
  <td><p><code>boolean</code></p>
</td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Enable verbose logging.</p>
</td></tr>

</tbody></table>

<h3>Watch Options</h3>
<table class="cli-option" width="100%">
  <thead>
    <tr>
      <th>Flag</th>
      <th>Type</th>
    </tr>
  </thead>
  <tbody>
<tr class='odd' name='excludeDirectories'>
  <td><code><a href='/tsconfig/#excludeDirectories'>--excludeDirectories</a></code></td>
  <td><p><code>list</code></p>
</td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Remove a list of directories from the watch process.</p>
</td></tr>

<tr class='even' name='excludeFiles'>
  <td><code><a href='/tsconfig/#excludeFiles'>--excludeFiles</a></code></td>
  <td><p><code>list</code></p>
</td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Remove a list of files from the watch mode's processing.</p>
</td></tr>

<tr class='odd' name='fallbackPolling'>
  <td><code><a href='/tsconfig/#fallbackPolling'>--fallbackPolling</a></code></td>
  <td><p><code>fixedinterval</code>, <code>priorityinterval</code>, <code>dynamicpriority</code>, or <code>fixedchunksize</code></p>
</td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Specify what approach the watcher should use if the system runs out of native file watchers.</p>
</td></tr>

<tr class='even' name='synchronousWatchDirectory'>
  <td><code><a href='/tsconfig/#synchronousWatchDirectory'>--synchronousWatchDirectory</a></code></td>
  <td><p><code>boolean</code></p>
</td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Synchronously call callbacks and update the state of directory watchers on platforms that don`t support recursive watching natively.</p>
</td></tr>

<tr class='odd' name='watch'>
  <td><code>--watch</code></td>
  <td><p><code>boolean</code></p>
</td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Watch input files.</p>
</td></tr>

<tr class='even' name='watchDirectory'>
  <td><code><a href='/tsconfig/#watchDirectory'>--watchDirectory</a></code></td>
  <td><p><code>usefsevents</code>, <code>fixedpollinginterval</code>, <code>dynamicprioritypolling</code>, or <code>fixedchunksizepolling</code></p>
</td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Specify how directories are watched on systems that lack recursive file-watching functionality.</p>
</td></tr>

<tr class='odd' name='watchFile'>
  <td><code><a href='/tsconfig/#watchFile'>--watchFile</a></code></td>
  <td><p><code>fixedpollinginterval</code>, <code>prioritypollinginterval</code>, <code>dynamicprioritypolling</code>, <code>fixedchunksizepolling</code>, <code>usefsevents</code>, or <code>usefseventsonparentdirectory</code></p>
</td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Specify how the TypeScript watch mode works.</p>
</td></tr>

</tbody></table>

<h3>Compiler Flags</h3>
<table class="cli-option" width="100%">
  <thead>
    <tr>
      <th>Flag</th>
      <th>Type</th>
      <th>Default</th>
    </tr>
  </thead>
  <tbody>
<tr class='odd' name='allowArbitraryExtensions'>
  <td><code><a href='/tsconfig/#allowArbitraryExtensions'>--allowArbitraryExtensions</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>false</code></p>
</td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Enable importing files with any extension, provided a declaration file is present.</p>
</td></tr>

<tr class='even' name='allowImportingTsExtensions'>
  <td><code><a href='/tsconfig/#allowImportingTsExtensions'>--allowImportingTsExtensions</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>true</code> if <a href="#rewriteRelativeImportExtensions"><code>rewriteRelativeImportExtensions</code></a>; <code>false</code> otherwise.</p>
</td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Allow imports to include TypeScript file extensions.</p>
</td></tr>

<tr class='odd' name='allowJs'>
  <td><code><a href='/tsconfig/#allowJs'>--allowJs</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>false</code>, unless <code>checkJs</code> is set</p>
</td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Allow JavaScript files to be a part of your program. Use the <code>checkJS</code> option to get errors from these files.</p>
</td></tr>

<tr class='even' name='allowSyntheticDefaultImports'>
  <td><code><a href='/tsconfig/#allowSyntheticDefaultImports'>--allowSyntheticDefaultImports</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>true</code> if <a href="#esModuleInterop"><code>esModuleInterop</code></a> is enabled, <a href="#module"><code>module</code></a> is <code>system</code>, or <a href="#module-resolution"><code>moduleResolution</code></a> is <code>bundler</code>; <code>false</code> otherwise.</p>
</td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Allow 'import x from y' when a module doesn't have a default export.</p>
</td></tr>

<tr class='odd' name='allowUmdGlobalAccess'>
  <td><code><a href='/tsconfig/#allowUmdGlobalAccess'>--allowUmdGlobalAccess</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>false</code></p>
</td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Allow accessing UMD globals from modules.</p>
</td></tr>

<tr class='even' name='allowUnreachableCode'>
  <td><code><a href='/tsconfig/#allowUnreachableCode'>--allowUnreachableCode</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td></td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Disable error reporting for unreachable code.</p>
</td></tr>

<tr class='odd' name='allowUnusedLabels'>
  <td><code><a href='/tsconfig/#allowUnusedLabels'>--allowUnusedLabels</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td></td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Disable error reporting for unused labels.</p>
</td></tr>

<tr class='even' name='alwaysStrict'>
  <td><code><a href='/tsconfig/#alwaysStrict'>--alwaysStrict</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>true</code> if <a href="#strict"><code>strict</code></a>; <code>false</code> otherwise.</p>
</td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Ensure 'use strict' is always emitted.</p>
</td></tr>

<tr class='odd' name='assumeChangesOnlyAffectDirectDependencies'>
  <td><code><a href='/tsconfig/#assumeChangesOnlyAffectDirectDependencies'>--assumeChangesOnlyAffectDirectDependencies</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>false</code></p>
</td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Have recompiles in projects that use <a href="#incremental"><code>incremental</code></a> and <code>watch</code> mode assume that changes within a file will only affect files directly depending on it.</p>
</td></tr>

<tr class='even' name='baseUrl'>
  <td><code><a href='/tsconfig/#baseUrl'>--baseUrl</a></code></td>
  <td><p><code>string</code></p>
</td>
  <td></td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Specify the base directory to resolve bare specifier module names.</p>
</td></tr>

<tr class='odd' name='charset'>
  <td><code><a href='/tsconfig/#charset'>--charset</a></code></td>
  <td><p><code>string</code></p>
</td>
  <td><p><code>utf8</code></p>
</td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>No longer supported. In early versions, manually set the text encoding for reading files.</p>
</td></tr>

<tr class='even' name='checkJs'>
  <td><code><a href='/tsconfig/#checkJs'>--checkJs</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>false</code></p>
</td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Enable error reporting in type-checked JavaScript files.</p>
</td></tr>

<tr class='odd' name='composite'>
  <td><code><a href='/tsconfig/#composite'>--composite</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>false</code></p>
</td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Enable constraints that allow a TypeScript project to be used with project references.</p>
</td></tr>

<tr class='even' name='customConditions'>
  <td><code><a href='/tsconfig/#customConditions'>--customConditions</a></code></td>
  <td><p><code>list</code></p>
</td>
  <td></td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Conditions to set in addition to the resolver-specific defaults when resolving imports.</p>
</td></tr>

<tr class='odd' name='declaration'>
  <td><code><a href='/tsconfig/#declaration'>--declaration</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>true</code> if <a href="#composite"><code>composite</code></a>; <code>false</code> otherwise.</p>
</td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Generate .d.ts files from TypeScript and JavaScript files in your project.</p>
</td></tr>

<tr class='even' name='declarationDir'>
  <td><code><a href='/tsconfig/#declarationDir'>--declarationDir</a></code></td>
  <td><p><code>string</code></p>
</td>
  <td></td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Specify the output directory for generated declaration files.</p>
</td></tr>

<tr class='odd' name='declarationMap'>
  <td><code><a href='/tsconfig/#declarationMap'>--declarationMap</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>false</code></p>
</td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Create sourcemaps for d.ts files.</p>
</td></tr>

<tr class='even' name='diagnostics'>
  <td><code><a href='/tsconfig/#diagnostics'>--diagnostics</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>false</code></p>
</td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Output compiler performance information after building.</p>
</td></tr>

<tr class='odd' name='disableReferencedProjectLoad'>
  <td><code><a href='/tsconfig/#disableReferencedProjectLoad'>--disableReferencedProjectLoad</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>false</code></p>
</td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Reduce the number of projects loaded automatically by TypeScript.</p>
</td></tr>

<tr class='even' name='disableSizeLimit'>
  <td><code><a href='/tsconfig/#disableSizeLimit'>--disableSizeLimit</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>false</code></p>
</td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Remove the 20mb cap on total source code size for JavaScript files in the TypeScript language server.</p>
</td></tr>

<tr class='odd' name='disableSolutionSearching'>
  <td><code><a href='/tsconfig/#disableSolutionSearching'>--disableSolutionSearching</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>false</code></p>
</td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Opt a project out of multi-project reference checking when editing.</p>
</td></tr>

<tr class='even' name='disableSourceOfProjectReferenceRedirect'>
  <td><code><a href='/tsconfig/#disableSourceOfProjectReferenceRedirect'>--disableSourceOfProjectReferenceRedirect</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>false</code></p>
</td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Disable preferring source files instead of declaration files when referencing composite projects.</p>
</td></tr>

<tr class='odd' name='downlevelIteration'>
  <td><code><a href='/tsconfig/#downlevelIteration'>--downlevelIteration</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>false</code></p>
</td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Emit more compliant, but verbose and less performant JavaScript for iteration.</p>
</td></tr>

<tr class='even' name='emitBOM'>
  <td><code><a href='/tsconfig/#emitBOM'>--emitBOM</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>false</code></p>
</td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Emit a UTF-8 Byte Order Mark (BOM) in the beginning of output files.</p>
</td></tr>

<tr class='odd' name='emitDeclarationOnly'>
  <td><code><a href='/tsconfig/#emitDeclarationOnly'>--emitDeclarationOnly</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>false</code></p>
</td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Only output d.ts files and not JavaScript files.</p>
</td></tr>

<tr class='even' name='emitDecoratorMetadata'>
  <td><code><a href='/tsconfig/#emitDecoratorMetadata'>--emitDecoratorMetadata</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>false</code></p>
</td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Emit design-type metadata for decorated declarations in source files.</p>
</td></tr>

<tr class='odd' name='erasableSyntaxOnly'>
  <td><code><a href='/tsconfig/#erasableSyntaxOnly'>--erasableSyntaxOnly</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>false</code></p>
</td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Do not allow runtime constructs that are not part of ECMAScript.</p>
</td></tr>

<tr class='even' name='esModuleInterop'>
  <td><code><a href='/tsconfig/#esModuleInterop'>--esModuleInterop</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>true</code> if <a href="#module"><code>module</code></a> is <code>node16</code>, <code>nodenext</code>, or <code>preserve</code>; <code>false</code> otherwise.</p>
</td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Emit additional JavaScript to ease support for importing CommonJS modules. This enables <a href="#allowSyntheticDefaultImports"><code>allowSyntheticDefaultImports</code></a> for type compatibility.</p>
</td></tr>

<tr class='odd' name='exactOptionalPropertyTypes'>
  <td><code><a href='/tsconfig/#exactOptionalPropertyTypes'>--exactOptionalPropertyTypes</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>false</code></p>
</td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Interpret optional property types as written, rather than adding <code>undefined</code>.</p>
</td></tr>

<tr class='even' name='experimentalDecorators'>
  <td><code><a href='/tsconfig/#experimentalDecorators'>--experimentalDecorators</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>false</code></p>
</td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Enable experimental support for TC39 stage 2 draft decorators.</p>
</td></tr>

<tr class='odd' name='explainFiles'>
  <td><code><a href='/tsconfig/#explainFiles'>--explainFiles</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>false</code></p>
</td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Print files read during the compilation including why it was included.</p>
</td></tr>

<tr class='even' name='extendedDiagnostics'>
  <td><code><a href='/tsconfig/#extendedDiagnostics'>--extendedDiagnostics</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>false</code></p>
</td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Output more detailed compiler performance information after building.</p>
</td></tr>

<tr class='odd' name='forceConsistentCasingInFileNames'>
  <td><code><a href='/tsconfig/#forceConsistentCasingInFileNames'>--forceConsistentCasingInFileNames</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>true</code></p>
</td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Ensure that casing is correct in imports.</p>
</td></tr>

<tr class='even' name='generateCpuProfile'>
  <td><code><a href='/tsconfig/#generateCpuProfile'>--generateCpuProfile</a></code></td>
  <td><p><code>string</code></p>
</td>
  <td><p><code>profile.cpuprofile</code></p>
</td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Emit a v8 CPU profile of the compiler run for debugging.</p>
</td></tr>

<tr class='odd' name='generateTrace'>
  <td><code><a href='/tsconfig/#generateTrace'>--generateTrace</a></code></td>
  <td><p><code>string</code></p>
</td>
  <td></td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Generates an event trace and a list of types.</p>
</td></tr>

<tr class='even' name='importHelpers'>
  <td><code><a href='/tsconfig/#importHelpers'>--importHelpers</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>false</code></p>
</td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Allow importing helper functions from tslib once per project, instead of including them per-file.</p>
</td></tr>

<tr class='odd' name='importsNotUsedAsValues'>
  <td><code><a href='/tsconfig/#importsNotUsedAsValues'>--importsNotUsedAsValues</a></code></td>
  <td><p><code>remove</code>, <code>preserve</code>, or <code>error</code></p>
</td>
  <td><p><code>remove</code></p>
</td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Specify emit/checking behavior for imports that are only used for types.</p>
</td></tr>

<tr class='even' name='incremental'>
  <td><code><a href='/tsconfig/#incremental'>--incremental</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>true</code> if <a href="#composite"><code>composite</code></a>; <code>false</code> otherwise.</p>
</td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Save .tsbuildinfo files to allow for incremental compilation of projects.</p>
</td></tr>

<tr class='odd' name='inlineSourceMap'>
  <td><code><a href='/tsconfig/#inlineSourceMap'>--inlineSourceMap</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>false</code></p>
</td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Include sourcemap files inside the emitted JavaScript.</p>
</td></tr>

<tr class='even' name='inlineSources'>
  <td><code><a href='/tsconfig/#inlineSources'>--inlineSources</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>false</code></p>
</td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Include source code in the sourcemaps inside the emitted JavaScript.</p>
</td></tr>

<tr class='odd' name='isolatedDeclarations'>
  <td><code><a href='/tsconfig/#isolatedDeclarations'>--isolatedDeclarations</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>false</code></p>
</td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Require sufficient annotation on exports so other tools can trivially generate declaration files.</p>
</td></tr>

<tr class='even' name='isolatedModules'>
  <td><code><a href='/tsconfig/#isolatedModules'>--isolatedModules</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>true</code> if <a href="#verbatimModuleSyntax"><code>verbatimModuleSyntax</code></a>; <code>false</code> otherwise.</p>
</td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Ensure that each file can be safely transpiled without relying on other imports.</p>
</td></tr>

<tr class='odd' name='jsx'>
  <td><code><a href='/tsconfig/#jsx'>--jsx</a></code></td>
  <td><p><code>preserve</code>, <code>react</code>, <code>react-native</code>, <code>react-jsx</code>, or <code>react-jsxdev</code></p>
</td>
  <td></td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Specify what JSX code is generated.</p>
</td></tr>

<tr class='even' name='jsxFactory'>
  <td><code><a href='/tsconfig/#jsxFactory'>--jsxFactory</a></code></td>
  <td><p><code>string</code></p>
</td>
  <td><p><code>React.createElement</code></p>
</td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Specify the JSX factory function used when targeting React JSX emit, e.g. 'React.createElement' or 'h'.</p>
</td></tr>

<tr class='odd' name='jsxFragmentFactory'>
  <td><code><a href='/tsconfig/#jsxFragmentFactory'>--jsxFragmentFactory</a></code></td>
  <td><p><code>string</code></p>
</td>
  <td><p><code>React.Fragment</code></p>
</td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Specify the JSX Fragment reference used for fragments when targeting React JSX emit e.g. 'React.Fragment' or 'Fragment'.</p>
</td></tr>

<tr class='even' name='jsxImportSource'>
  <td><code><a href='/tsconfig/#jsxImportSource'>--jsxImportSource</a></code></td>
  <td><p><code>string</code></p>
</td>
  <td><p><code>react</code></p>
</td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Specify module specifier used to import the JSX factory functions when using <code>jsx: react-jsx*</code>.</p>
</td></tr>

<tr class='odd' name='keyofStringsOnly'>
  <td><code><a href='/tsconfig/#keyofStringsOnly'>--keyofStringsOnly</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>false</code></p>
</td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Make keyof only return strings instead of string, numbers or symbols. Legacy option.</p>
</td></tr>

<tr class='even' name='lib'>
  <td><code><a href='/tsconfig/#lib'>--lib</a></code></td>
  <td><p><code>list</code></p>
</td>
  <td></td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Specify a set of bundled library declaration files that describe the target runtime environment.</p>
</td></tr>

<tr class='odd' name='libReplacement'>
  <td><code><a href='/tsconfig/#libReplacement'>--libReplacement</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>false</code></p>
</td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Enable substitution of default <code>lib</code> files with custom ones.</p>
</td></tr>

<tr class='even' name='listEmittedFiles'>
  <td><code><a href='/tsconfig/#listEmittedFiles'>--listEmittedFiles</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>false</code></p>
</td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Print the names of emitted files after a compilation.</p>
</td></tr>

<tr class='odd' name='listFiles'>
  <td><code><a href='/tsconfig/#listFiles'>--listFiles</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>false</code></p>
</td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Print all of the files read during the compilation.</p>
</td></tr>

<tr class='even' name='mapRoot'>
  <td><code><a href='/tsconfig/#mapRoot'>--mapRoot</a></code></td>
  <td><p><code>string</code></p>
</td>
  <td></td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Specify the location where debugger should locate map files instead of generated locations.</p>
</td></tr>

<tr class='odd' name='maxNodeModuleJsDepth'>
  <td><code><a href='/tsconfig/#maxNodeModuleJsDepth'>--maxNodeModuleJsDepth</a></code></td>
  <td><p><code>number</code></p>
</td>
  <td><p><code>0</code></p>
</td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Specify the maximum folder depth used for checking JavaScript files from <code>node_modules</code>. Only applicable with <a href="#allowJs"><code>allowJs</code></a>.</p>
</td></tr>

<tr class='even' name='module'>
  <td><code><a href='/tsconfig/#module'>--module</a></code></td>
  <td><p><code>none</code>, <code>commonjs</code>, <code>amd</code>, <code>umd</code>, <code>system</code>, <code>es6</code>/<code>es2015</code>, <code>es2020</code>, <code>es2022</code>, <code>esnext</code>, <code>node16</code>, <code>node18</code>, <code>node20</code>, <code>nodenext</code>, or <code>preserve</code></p>
</td>
  <td><p><code>CommonJS</code> if <a href="#target"><code>target</code></a> is <code>ES5</code>; <code>ES6</code>/<code>ES2015</code> otherwise.</p>
</td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Specify what module code is generated.</p>
</td></tr>

<tr class='odd' name='moduleDetection'>
  <td><code><a href='/tsconfig/#moduleDetection'>--moduleDetection</a></code></td>
  <td><p><code>legacy</code>, <code>auto</code>, or <code>force</code></p>
</td>
  <td><p>"auto": Treat files with imports, exports, import.meta, jsx (with jsx: react-jsx), or esm format (with module: node16+) as modules.</p>
</td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Specify what method is used to detect whether a file is a script or a module.</p>
</td></tr>

<tr class='even' name='moduleResolution'>
  <td><code><a href='/tsconfig/#moduleResolution'>--moduleResolution</a></code></td>
  <td><p><code>classic</code>, <code>node10</code>/<code>node</code>, <code>node16</code>, <code>nodenext</code>, or <code>bundler</code></p>
</td>
  <td><p><code>Node10</code> if <a href="#module"><code>module</code></a> is <code>CommonJS</code>; <code>Node16</code> if <a href="#module"><code>module</code></a> is <code>Node16</code>, <code>Node18</code>, or <code>Node20</code>; <code>NodeNext</code> if <a href="#module"><code>module</code></a> is <code>NodeNext</code>; <code>Bundler</code> if <a href="#module"><code>module</code></a> is <code>Preserve</code>; <code>Classic</code> otherwise.</p>
</td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Specify how TypeScript looks up a file from a given module specifier.</p>
</td></tr>

<tr class='odd' name='moduleSuffixes'>
  <td><code><a href='/tsconfig/#moduleSuffixes'>--moduleSuffixes</a></code></td>
  <td><p><code>list</code></p>
</td>
  <td></td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>List of file name suffixes to search when resolving a module.</p>
</td></tr>

<tr class='even' name='newLine'>
  <td><code><a href='/tsconfig/#newLine'>--newLine</a></code></td>
  <td><p><code>crlf</code> or <code>lf</code></p>
</td>
  <td><p><code>lf</code></p>
</td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Set the newline character for emitting files.</p>
</td></tr>

<tr class='odd' name='noCheck'>
  <td><code><a href='/tsconfig/#noCheck'>--noCheck</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>false</code></p>
</td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Disable full type checking (only critical parse and emit errors will be reported).</p>
</td></tr>

<tr class='even' name='noEmit'>
  <td><code><a href='/tsconfig/#noEmit'>--noEmit</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>false</code></p>
</td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Disable emitting files from a compilation.</p>
</td></tr>

<tr class='odd' name='noEmitHelpers'>
  <td><code><a href='/tsconfig/#noEmitHelpers'>--noEmitHelpers</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>false</code></p>
</td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Disable generating custom helper functions like <code>__extends</code> in compiled output.</p>
</td></tr>

<tr class='even' name='noEmitOnError'>
  <td><code><a href='/tsconfig/#noEmitOnError'>--noEmitOnError</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>false</code></p>
</td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Disable emitting files if any type checking errors are reported.</p>
</td></tr>

<tr class='odd' name='noErrorTruncation'>
  <td><code><a href='/tsconfig/#noErrorTruncation'>--noErrorTruncation</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>false</code></p>
</td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Disable truncating types in error messages.</p>
</td></tr>

<tr class='even' name='noFallthroughCasesInSwitch'>
  <td><code><a href='/tsconfig/#noFallthroughCasesInSwitch'>--noFallthroughCasesInSwitch</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>false</code></p>
</td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Enable error reporting for fallthrough cases in switch statements.</p>
</td></tr>

<tr class='odd' name='noImplicitAny'>
  <td><code><a href='/tsconfig/#noImplicitAny'>--noImplicitAny</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>true</code> if <a href="#strict"><code>strict</code></a>; <code>false</code> otherwise.</p>
</td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Enable error reporting for expressions and declarations with an implied <code>any</code> type.</p>
</td></tr>

<tr class='even' name='noImplicitOverride'>
  <td><code><a href='/tsconfig/#noImplicitOverride'>--noImplicitOverride</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>false</code></p>
</td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Ensure overriding members in derived classes are marked with an override modifier.</p>
</td></tr>

<tr class='odd' name='noImplicitReturns'>
  <td><code><a href='/tsconfig/#noImplicitReturns'>--noImplicitReturns</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>false</code></p>
</td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Enable error reporting for codepaths that do not explicitly return in a function.</p>
</td></tr>

<tr class='even' name='noImplicitThis'>
  <td><code><a href='/tsconfig/#noImplicitThis'>--noImplicitThis</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>true</code> if <a href="#strict"><code>strict</code></a>; <code>false</code> otherwise.</p>
</td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Enable error reporting when <code>this</code> is given the type <code>any</code>.</p>
</td></tr>

<tr class='odd' name='noImplicitUseStrict'>
  <td><code><a href='/tsconfig/#noImplicitUseStrict'>--noImplicitUseStrict</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>false</code></p>
</td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Disable adding 'use strict' directives in emitted JavaScript files.</p>
</td></tr>

<tr class='even' name='noLib'>
  <td><code><a href='/tsconfig/#noLib'>--noLib</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>false</code></p>
</td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Disable including any library files, including the default lib.d.ts.</p>
</td></tr>

<tr class='odd' name='noPropertyAccessFromIndexSignature'>
  <td><code><a href='/tsconfig/#noPropertyAccessFromIndexSignature'>--noPropertyAccessFromIndexSignature</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>false</code></p>
</td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Enforces using indexed accessors for keys declared using an indexed type.</p>
</td></tr>

<tr class='even' name='noResolve'>
  <td><code><a href='/tsconfig/#noResolve'>--noResolve</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>false</code></p>
</td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Disallow <code>import</code>s, <code>require</code>s or <code>&#x3C;reference></code>s from expanding the number of files TypeScript should add to a project.</p>
</td></tr>

<tr class='odd' name='noStrictGenericChecks'>
  <td><code><a href='/tsconfig/#noStrictGenericChecks'>--noStrictGenericChecks</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>false</code></p>
</td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Disable strict checking of generic signatures in function types.</p>
</td></tr>

<tr class='even' name='noUncheckedIndexedAccess'>
  <td><code><a href='/tsconfig/#noUncheckedIndexedAccess'>--noUncheckedIndexedAccess</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>false</code></p>
</td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Add <code>undefined</code> to a type when accessed using an index.</p>
</td></tr>

<tr class='odd' name='noUncheckedSideEffectImports'>
  <td><code><a href='/tsconfig/#noUncheckedSideEffectImports'>--noUncheckedSideEffectImports</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>true</code></p>
</td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Check side effect imports.</p>
</td></tr>

<tr class='even' name='noUnusedLocals'>
  <td><code><a href='/tsconfig/#noUnusedLocals'>--noUnusedLocals</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>false</code></p>
</td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Enable error reporting when local variables aren't read.</p>
</td></tr>

<tr class='odd' name='noUnusedParameters'>
  <td><code><a href='/tsconfig/#noUnusedParameters'>--noUnusedParameters</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>false</code></p>
</td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Raise an error when a function parameter isn't read.</p>
</td></tr>

<tr class='even' name='out'>
  <td><code><a href='/tsconfig/#out'>--out</a></code></td>
  <td><p><code>string</code></p>
</td>
  <td></td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Deprecated setting. Use <a href="#outFile"><code>outFile</code></a> instead.</p>
</td></tr>

<tr class='odd' name='outDir'>
  <td><code><a href='/tsconfig/#outDir'>--outDir</a></code></td>
  <td><p><code>string</code></p>
</td>
  <td></td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Specify an output folder for all emitted files.</p>
</td></tr>

<tr class='even' name='outFile'>
  <td><code><a href='/tsconfig/#outFile'>--outFile</a></code></td>
  <td><p><code>string</code></p>
</td>
  <td></td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Specify a file that bundles all outputs into one JavaScript file. If <a href="#declaration"><code>declaration</code></a> is true, also designates a file that bundles all .d.ts output.</p>
</td></tr>

<tr class='odd' name='paths'>
  <td><code><a href='/tsconfig/#paths'>--paths</a></code></td>
  <td><p><code>object</code></p>
</td>
  <td></td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Specify a set of entries that re-map imports to additional lookup locations.</p>
</td></tr>

<tr class='even' name='plugins'>
  <td><code><a href='/tsconfig/#plugins'>--plugins</a></code></td>
  <td><p><code>list</code></p>
</td>
  <td></td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Specify a list of language service plugins to include.</p>
</td></tr>

<tr class='odd' name='preserveConstEnums'>
  <td><code><a href='/tsconfig/#preserveConstEnums'>--preserveConstEnums</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>true</code> if <a href="#isolatedModules"><code>isolatedModules</code></a>; <code>false</code> otherwise.</p>
</td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Disable erasing <code>const enum</code> declarations in generated code.</p>
</td></tr>

<tr class='even' name='preserveSymlinks'>
  <td><code><a href='/tsconfig/#preserveSymlinks'>--preserveSymlinks</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>false</code></p>
</td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Disable resolving symlinks to their realpath. This correlates to the same flag in node.</p>
</td></tr>

<tr class='odd' name='preserveValueImports'>
  <td><code><a href='/tsconfig/#preserveValueImports'>--preserveValueImports</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>false</code></p>
</td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Preserve unused imported values in the JavaScript output that would otherwise be removed.</p>
</td></tr>

<tr class='even' name='preserveWatchOutput'>
  <td><code><a href='/tsconfig/#preserveWatchOutput'>--preserveWatchOutput</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>false</code></p>
</td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Disable wiping the console in watch mode.</p>
</td></tr>

<tr class='odd' name='pretty'>
  <td><code><a href='/tsconfig/#pretty'>--pretty</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>true</code></p>
</td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Enable color and formatting in TypeScript's output to make compiler errors easier to read.</p>
</td></tr>

<tr class='even' name='reactNamespace'>
  <td><code><a href='/tsconfig/#reactNamespace'>--reactNamespace</a></code></td>
  <td><p><code>string</code></p>
</td>
  <td><p><code>React</code></p>
</td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Specify the object invoked for <code>createElement</code>. This only applies when targeting <code>react</code> JSX emit.</p>
</td></tr>

<tr class='odd' name='removeComments'>
  <td><code><a href='/tsconfig/#removeComments'>--removeComments</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>false</code></p>
</td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Disable emitting comments.</p>
</td></tr>

<tr class='even' name='resolveJsonModule'>
  <td><code><a href='/tsconfig/#resolveJsonModule'>--resolveJsonModule</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>false</code></p>
</td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Enable importing .json files.</p>
</td></tr>

<tr class='odd' name='resolvePackageJsonExports'>
  <td><code><a href='/tsconfig/#resolvePackageJsonExports'>--resolvePackageJsonExports</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>true</code> when <a href="#moduleResolution"><code>moduleResolution</code></a> is <code>node16</code>, <code>nodenext</code>, or <code>bundler</code>; otherwise <code>false</code></p>
</td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Use the package.json 'exports' field when resolving package imports.</p>
</td></tr>

<tr class='even' name='resolvePackageJsonImports'>
  <td><code><a href='/tsconfig/#resolvePackageJsonImports'>--resolvePackageJsonImports</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>true</code> when <a href="#moduleResolution"><code>moduleResolution</code></a> is <code>node16</code>, <code>nodenext</code>, or <code>bundler</code>; otherwise <code>false</code></p>
</td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Use the package.json 'imports' field when resolving imports.</p>
</td></tr>

<tr class='odd' name='rewriteRelativeImportExtensions'>
  <td><code><a href='/tsconfig/#rewriteRelativeImportExtensions'>--rewriteRelativeImportExtensions</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>false</code></p>
</td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Rewrite <code>.ts</code>, <code>.tsx</code>, <code>.mts</code>, and <code>.cts</code> file extensions in relative import paths to their JavaScript equivalent in output files.</p>
</td></tr>

<tr class='even' name='rootDir'>
  <td><code><a href='/tsconfig/#rootDir'>--rootDir</a></code></td>
  <td><p><code>string</code></p>
</td>
  <td><p>Computed from the list of input files.</p>
</td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Specify the root folder within your source files.</p>
</td></tr>

<tr class='odd' name='rootDirs'>
  <td><code><a href='/tsconfig/#rootDirs'>--rootDirs</a></code></td>
  <td><p><code>list</code></p>
</td>
  <td><p>Computed from the list of input files.</p>
</td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Allow multiple folders to be treated as one when resolving modules.</p>
</td></tr>

<tr class='even' name='skipDefaultLibCheck'>
  <td><code><a href='/tsconfig/#skipDefaultLibCheck'>--skipDefaultLibCheck</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>false</code></p>
</td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Skip type checking .d.ts files that are included with TypeScript.</p>
</td></tr>

<tr class='odd' name='skipLibCheck'>
  <td><code><a href='/tsconfig/#skipLibCheck'>--skipLibCheck</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>false</code></p>
</td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Skip type checking all .d.ts files.</p>
</td></tr>

<tr class='even' name='sourceMap'>
  <td><code><a href='/tsconfig/#sourceMap'>--sourceMap</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>false</code></p>
</td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Create source map files for emitted JavaScript files.</p>
</td></tr>

<tr class='odd' name='sourceRoot'>
  <td><code><a href='/tsconfig/#sourceRoot'>--sourceRoot</a></code></td>
  <td><p><code>string</code></p>
</td>
  <td></td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Specify the root path for debuggers to find the reference source code.</p>
</td></tr>

<tr class='even' name='stableTypeOrdering'>
  <td><code><a href='/tsconfig/#stableTypeOrdering'>--stableTypeOrdering</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>false</code></p>
</td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Ensure types are ordered stably and deterministically across compilations.</p>
</td></tr>

<tr class='odd' name='stopBuildOnErrors'>
  <td><code><a href='/tsconfig/#stopBuildOnErrors'>--stopBuildOnErrors</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td></td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Skip building downstream projects on error in upstream project.</p>
</td></tr>

<tr class='even' name='strict'>
  <td><code><a href='/tsconfig/#strict'>--strict</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>true</code></p>
</td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Enable all strict type-checking options.</p>
</td></tr>

<tr class='odd' name='strictBindCallApply'>
  <td><code><a href='/tsconfig/#strictBindCallApply'>--strictBindCallApply</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>true</code> if <a href="#strict"><code>strict</code></a>; <code>false</code> otherwise.</p>
</td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Check that the arguments for <code>bind</code>, <code>call</code>, and <code>apply</code> methods match the original function.</p>
</td></tr>

<tr class='even' name='strictBuiltinIteratorReturn'>
  <td><code><a href='/tsconfig/#strictBuiltinIteratorReturn'>--strictBuiltinIteratorReturn</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>true</code> if <a href="#strict"><code>strict</code></a>; <code>false</code> otherwise.</p>
</td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Built-in iterators are instantiated with a TReturn type of undefined instead of any.</p>
</td></tr>

<tr class='odd' name='strictFunctionTypes'>
  <td><code><a href='/tsconfig/#strictFunctionTypes'>--strictFunctionTypes</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>true</code> if <a href="#strict"><code>strict</code></a>; <code>false</code> otherwise.</p>
</td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>When assigning functions, check to ensure parameters and the return values are subtype-compatible.</p>
</td></tr>

<tr class='even' name='strictNullChecks'>
  <td><code><a href='/tsconfig/#strictNullChecks'>--strictNullChecks</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>true</code> if <a href="#strict"><code>strict</code></a>; <code>false</code> otherwise.</p>
</td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>When type checking, take into account <code>null</code> and <code>undefined</code>.</p>
</td></tr>

<tr class='odd' name='strictPropertyInitialization'>
  <td><code><a href='/tsconfig/#strictPropertyInitialization'>--strictPropertyInitialization</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>true</code> if <a href="#strict"><code>strict</code></a>; <code>false</code> otherwise.</p>
</td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Check for class properties that are declared but not set in the constructor.</p>
</td></tr>

<tr class='even' name='stripInternal'>
  <td><code><a href='/tsconfig/#stripInternal'>--stripInternal</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>false</code></p>
</td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Disable emitting declarations that have <code>@internal</code> in their JSDoc comments.</p>
</td></tr>

<tr class='odd' name='suppressExcessPropertyErrors'>
  <td><code><a href='/tsconfig/#suppressExcessPropertyErrors'>--suppressExcessPropertyErrors</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>false</code></p>
</td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Disable reporting of excess property errors during the creation of object literals.</p>
</td></tr>

<tr class='even' name='suppressImplicitAnyIndexErrors'>
  <td><code><a href='/tsconfig/#suppressImplicitAnyIndexErrors'>--suppressImplicitAnyIndexErrors</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>false</code></p>
</td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Suppress <a href="#noImplicitAny"><code>noImplicitAny</code></a> errors when indexing objects that lack index signatures.</p>
</td></tr>

<tr class='odd' name='target'>
  <td><code><a href='/tsconfig/#target'>--target</a></code></td>
  <td><p><code>es3</code>, <code>es5</code>, <code>es6</code>/<code>es2015</code>, <code>es2016</code>, <code>es2017</code>, <code>es2018</code>, <code>es2019</code>, <code>es2020</code>, <code>es2021</code>, <code>es2022</code>, <code>es2023</code>, <code>es2024</code>, <code>es2025</code>, or <code>esnext</code></p>
</td>
  <td><p><code>es2023</code> if <a href="#module"><code>module</code></a> is <code>node20</code>; <code>esnext</code> if <a href="#module"><code>module</code></a> is <code>nodenext</code>; <code>ES5</code> otherwise.</p>
</td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Set the JavaScript language version for emitted JavaScript and include compatible library declarations.</p>
</td></tr>

<tr class='even' name='traceResolution'>
  <td><code><a href='/tsconfig/#traceResolution'>--traceResolution</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>false</code></p>
</td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Log paths used during the <a href="#moduleResolution"><code>moduleResolution</code></a> process.</p>
</td></tr>

<tr class='odd' name='tsBuildInfoFile'>
  <td><code><a href='/tsconfig/#tsBuildInfoFile'>--tsBuildInfoFile</a></code></td>
  <td><p><code>string</code></p>
</td>
  <td><p><code>.tsbuildinfo</code></p>
</td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>The file to store <code>.tsbuildinfo</code> incremental build information in.</p>
</td></tr>

<tr class='even' name='typeRoots'>
  <td><code><a href='/tsconfig/#typeRoots'>--typeRoots</a></code></td>
  <td><p><code>list</code></p>
</td>
  <td></td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Specify multiple folders that act like <code>./node_modules/@types</code>.</p>
</td></tr>

<tr class='odd' name='types'>
  <td><code><a href='/tsconfig/#types'>--types</a></code></td>
  <td><p><code>list</code></p>
</td>
  <td></td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Specify type package names to be included without being referenced in a source file.</p>
</td></tr>

<tr class='even' name='useDefineForClassFields'>
  <td><code><a href='/tsconfig/#useDefineForClassFields'>--useDefineForClassFields</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>true</code> if <a href="#target"><code>target</code></a> is <code>ES2022</code> or higher, including <code>ESNext</code>; <code>false</code> otherwise.</p>
</td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Emit ECMAScript-standard-compliant class fields.</p>
</td></tr>

<tr class='odd' name='useUnknownInCatchVariables'>
  <td><code><a href='/tsconfig/#useUnknownInCatchVariables'>--useUnknownInCatchVariables</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>true</code> if <a href="#strict"><code>strict</code></a>; <code>false</code> otherwise.</p>
</td>
</tr>
<tr class="option-description odd"><td colspan="3">
<p>Default catch clause variables as <code>unknown</code> instead of <code>any</code>.</p>
</td></tr>

<tr class='even' name='verbatimModuleSyntax'>
  <td><code><a href='/tsconfig/#verbatimModuleSyntax'>--verbatimModuleSyntax</a></code></td>
  <td><p><code>boolean</code></p>
</td>
  <td><p><code>false</code></p>
</td>
</tr>
<tr class="option-description even"><td colspan="3">
<p>Do not transform or elide any imports or exports not marked as type-only, ensuring they are written in the output file's format based on the 'module' setting.</p>
</td></tr>

</tbody></table>
<!-- End of replacement  -->

## Related

- Every option is fully explained in the [TSConfig Reference](/tsconfig).
- Learn how to use a [`tsconfig.json`](/docs/handbook/tsconfig-json.html) file.
- Learn how to work in an [MSBuild project](/docs/handbook/compiler-options-in-msbuild.html).

---

## Source: `packages/documentation/copy/en/reference/JSX.md`

---
title: JSX
layout: docs
permalink: /docs/handbook/jsx.html
oneline: Using JSX with TypeScript
translatable: true
---

[JSX](https://facebook.github.io/jsx/) is an embeddable XML-like syntax.
It is meant to be transformed into valid JavaScript, though the semantics of that transformation are implementation-specific.
JSX rose to popularity with the [React](https://reactjs.org/) framework, but has since seen other implementations as well.
TypeScript supports embedding, type checking, and compiling JSX directly to JavaScript.

## Basic usage

In order to use JSX you must do two things.

1. Name your files with a `.tsx` extension
2. Enable the [`jsx`](/tsconfig#jsx) option

TypeScript ships with several JSX modes: `preserve`, `react` (classic runtime), `react-jsx` (automatic runtime), `react-jsxdev` (automatic development runtime), and `react-native`.
The `preserve` mode will keep the JSX as part of the output to be further consumed by another transform step (e.g. [Babel](https://babeljs.io/)).
Additionally the output will have a `.jsx` file extension.
The `react` mode will emit `React.createElement`, does not need to go through a JSX transformation before use, and the output will have a `.js` file extension.
The `react-native` mode is the equivalent of `preserve` in that it keeps all JSX, but the output will instead have a `.js` file extension.

| Mode           | Input     | Output                                            | Output File Extension |
| -------------- | --------- | ------------------------------------------------- | --------------------- |
| `preserve`     | `<div />` | `<div />`                                         | `.jsx`                |
| `react`        | `<div />` | `React.createElement("div")`                      | `.js`                 |
| `react-native` | `<div />` | `<div />`                                         | `.js`                 |
| `react-jsx`    | `<div />` | `_jsx("div", {}, void 0);`                        | `.js`                 |
| `react-jsxdev` | `<div />` | `_jsxDEV("div", {}, void 0, false, {...}, this);` | `.js`                 |

You can specify this mode using either the [`jsx`](/tsconfig#jsx) command line flag or the corresponding option [`jsx` in your tsconfig.json](/tsconfig#jsx) file.

> \*Note: You can specify the JSX factory function to use when targeting react JSX emit with [`jsxFactory`](/tsconfig#jsxFactory) option (defaults to `React.createElement`)

## The `as` operator

Recall how to write a type assertion:

```ts
const foo = <Foo>bar;
```

This asserts the variable `bar` to have the type `Foo`.
Since TypeScript also uses angle brackets for type assertions, combining it with JSX's syntax would introduce certain parsing difficulties. As a result, TypeScript disallows angle bracket type assertions in `.tsx` files.

Since the above syntax cannot be used in `.tsx` files, an alternate type assertion operator should be used: `as`.
The example can easily be rewritten with the `as` operator.

```ts
const foo = bar as Foo;
```

The `as` operator is available in both `.ts` and `.tsx` files, and is identical in behavior to the angle-bracket type assertion style.

## Type Checking

In order to understand type checking with JSX, you must first understand the difference between intrinsic elements and value-based elements.
Given a JSX expression `<expr />`, `expr` may either refer to something intrinsic to the environment (e.g. a `div` or `span` in a DOM environment) or to a custom component that you've created.
This is important for two reasons:

1. For React, intrinsic elements are emitted as strings (`React.createElement("div")`), whereas a component you've created is not (`React.createElement(MyComponent)`).
2. The types of the attributes being passed in the JSX element should be looked up differently.
   Intrinsic element attributes should be known _intrinsically_ whereas components will likely want to specify their own set of attributes.

TypeScript uses the [same convention that React does](http://facebook.github.io/react/docs/jsx-in-depth.html#html-tags-vs.-react-components) for distinguishing between these.
An intrinsic element always begins with a lowercase letter, and a value-based element always begins with an uppercase letter.

### The `JSX` namespace

JSX in TypeScript is typed by the `JSX` namespace. The `JSX` namespace may be defined in various places, depending on the `jsx` compiler option.

The `jsx` options `preserve`, `react`, and `react-native` use the type definitions for classic runtime. This means a variable needs to be in scope that’s determined by the `jsxFactory` compiler option. The `JSX` namespace should be specified on the top-most identifier of the JSX factory. For example, React uses the default factory `React.createElement`. This means its `JSX` namespace should be defined as `React.JSX`.

```ts
export function createElement(): any;

export namespace JSX {
  // …
}
```

And the user should always import React as `React`.

```ts
import * as React from 'react';
```

Preact uses the JSX factory `h`. That means its types should be defined as the `h.JSX`.

```ts
export function h(props: any): any;

export namespace h.JSX {
  // …
}
```

The user should use a named import to import `h`.

```ts
import { h } from 'preact';
```

For the `jsx` options `react-jsx` and `react-jsxdev`, the `JSX` namespace should be exported from the matching entry points. For `react-jsx` this is `${jsxImportSource}/jsx-runtime`. For `react-jsxdev`, this is `${jsxImportSource}/jsx-dev-runtime`. Since these don’t use a file extension, you must use the [`exports`](https://nodejs.org/api/packages.html#exports) field in `package.json` map in order to support ESM users.

```json 
{
  "exports": {
    "./jsx-runtime": "./jsx-runtime.js",
    "./jsx-dev-runtime": "./jsx-dev-runtime.js",
  }
}
```

Then in `jsx-runtime.d.ts` and `jsx-dev-runtime.d.ts`:

```ts
export namespace JSX {
  // …
}
```

Note that while exporting the `JSX` namespace is sufficient for type checking, the production runtime needs the `jsx`, `jsxs`, and `Fragment` exports at runtime, and the development runtime needs `jsxDEV` and `Fragment`. Ideally you add types for those too.

If the `JSX` namespace isn’t available in the appropriate location, both the classic and the automatic runtime fall back to the global `JSX` namespace.

### Intrinsic elements

Intrinsic elements are looked up on the special interface `JSX.IntrinsicElements`.
By default, if this interface is not specified, then anything goes and intrinsic elements will not be type checked.
However, if this interface _is_ present, then the name of the intrinsic element is looked up as a property on the `JSX.IntrinsicElements` interface.
For example:

```tsx
declare namespace JSX {
  interface IntrinsicElements {
    foo: any;
  }
}

<foo />; // ok
<bar />; // error
```

In the above example, `<foo />` will work fine but `<bar />` will result in an error since it has not been specified on `JSX.IntrinsicElements`.

> Note: You can also specify a catch-all string indexer on `JSX.IntrinsicElements` as follows:

```ts
declare namespace JSX {
  interface IntrinsicElements {
    [elemName: string]: any;
  }
}
```

### Value-based elements

Value-based elements are simply looked up by identifiers that are in scope.

```tsx
import MyComponent from "./myComponent";

<MyComponent />; // ok
<SomeOtherComponent />; // error
```

There are two ways to define a value-based element:

1. Function Component (FC)
2. Class Component

Because these two types of value-based elements are indistinguishable from each other in a JSX expression, first TS tries to resolve the expression as a Function Component using overload resolution. If the process succeeds, then TS finishes resolving the expression to its declaration. If the value fails to resolve as a Function Component, TS will then try to resolve it as a class component. If that fails, TS will report an error.

#### Function Component

As the name suggests, the component is defined as a JavaScript function where its first argument is a `props` object.
TS enforces that its return type must be assignable to `JSX.Element`.

```tsx
interface FooProp {
  name: string;
  X: number;
  Y: number;
}

declare function AnotherComponent(prop: { name: string });
function ComponentFoo(prop: FooProp) {
  return <AnotherComponent name={prop.name} />;
}

const Button = (prop: { value: string }, context: { color: string }) => (
  <button />
);
```

Because a Function Component is simply a JavaScript function, function overloads may be used here as well:

```ts twoslash
// @noErrors
declare module JSX {
  interface Element {}
  interface IntrinsicElements {
    [s: string]: any;
  }
}
// ---cut---
interface ClickableProps {
  children: JSX.Element[] | JSX.Element;
}

interface HomeProps extends ClickableProps {
  home: JSX.Element;
}

interface SideProps extends ClickableProps {
  side: JSX.Element | string;
}

function MainButton(prop: HomeProps): JSX.Element;
function MainButton(prop: SideProps): JSX.Element;
function MainButton(prop: ClickableProps): JSX.Element {
  // ...
}
```

> Note: Function Components were formerly known as Stateless Function Components (SFC). As Function Components can no longer be considered stateless in recent versions of react, the type `SFC` and its alias `StatelessComponent` were deprecated.

#### Class Component

It is possible to define the type of a class component.
However, to do so it is best to understand two new terms: the _element class type_ and the _element instance type_.

Given `<Expr />`, the _element class type_ is the type of `Expr`.
So in the example above, if `MyComponent` was an ES6 class the class type would be that class's constructor and statics.
If `MyComponent` was a factory function, the class type would be that function.

Once the class type is established, the instance type is determined by the union of the return types of the class type's construct or call signatures (whichever is present).
So again, in the case of an ES6 class, the instance type would be the type of an instance of that class, and in the case of a factory function, it would be the type of the value returned from the function.

```ts
class MyComponent {
  render() {}
}

// use a construct signature
const myComponent = new MyComponent();

// element class type => MyComponent
// element instance type => { render: () => void }

function MyFactoryFunction() {
  return {
    render: () => {},
  };
}

// use a call signature
const myComponent = MyFactoryFunction();

// element class type => MyFactoryFunction
// element instance type => { render: () => void }
```

The element instance type is interesting because it must be assignable to `JSX.ElementClass` or it will result in an error.
By default `JSX.ElementClass` is `{}`, but it can be augmented to limit the use of JSX to only those types that conform to the proper interface.

```tsx
declare namespace JSX {
  interface ElementClass {
    render: any;
  }
}

class MyComponent {
  render() {}
}
function MyFactoryFunction() {
  return { render: () => {} };
}

<MyComponent />; // ok
<MyFactoryFunction />; // ok

class NotAValidComponent {}
function NotAValidFactoryFunction() {
  return {};
}

<NotAValidComponent />; // error
<NotAValidFactoryFunction />; // error
```

### Attribute type checking

The first step to type checking attributes is to determine the _element attributes type_.
This is slightly different between intrinsic and value-based elements.

For intrinsic elements, it is the type of the property on `JSX.IntrinsicElements`

```tsx
declare namespace JSX {
  interface IntrinsicElements {
    foo: { bar?: boolean };
  }
}

// element attributes type for 'foo' is '{bar?: boolean}'
<foo bar />;
```

For value-based elements, it is a bit more complex.
It is determined by the type of a property on the _element instance type_ that was previously determined.
Which property to use is determined by `JSX.ElementAttributesProperty`.
It should be declared with a single property.
The name of that property is then used.
As of TypeScript 2.8, if `JSX.ElementAttributesProperty` is not provided, the type of first parameter of the class element's constructor or Function Component's call will be used instead.

```tsx
declare namespace JSX {
  interface ElementAttributesProperty {
    props; // specify the property name to use
  }
}

class MyComponent {
  // specify the property on the element instance type
  props: {
    foo?: string;
  };
}

// element attributes type for 'MyComponent' is '{foo?: string}'
<MyComponent foo="bar" />;
```

The element attribute type is used to type check the attributes in the JSX.
Optional and required properties are supported.

```tsx
declare namespace JSX {
  interface IntrinsicElements {
    foo: { requiredProp: string; optionalProp?: number };
  }
}

<foo requiredProp="bar" />; // ok
<foo requiredProp="bar" optionalProp={0} />; // ok
<foo />; // error, requiredProp is missing
<foo requiredProp={0} />; // error, requiredProp should be a string
<foo requiredProp="bar" unknownProp />; // error, unknownProp does not exist
<foo requiredProp="bar" some-unknown-prop />; // ok, because 'some-unknown-prop' is not a valid identifier
```

> Note: If an attribute name is not a valid JS identifier (like a `data-*` attribute), it is not considered to be an error if it is not found in the element attributes type.

Additionally, the `JSX.IntrinsicAttributes` interface can be used to specify extra properties used by the JSX framework which are not generally used by the components' props or arguments - for instance `key` in React. Specializing further, the generic `JSX.IntrinsicClassAttributes<T>` type may also be used to specify the same kind of extra attributes just for class components (and not Function Components). In this type, the generic parameter corresponds to the class instance type. In React, this is used to allow the `ref` attribute of type `Ref<T>`. Generally speaking, all of the properties on these interfaces should be optional, unless you intend that users of your JSX framework need to provide some attribute on every tag.

The spread operator also works:

```tsx
const props = { requiredProp: "bar" };
<foo {...props} />; // ok

const badProps = {};
<foo {...badProps} />; // error
```

### Children Type Checking

In TypeScript 2.3, TS introduced type checking of _children_. _children_ is a special property in an _element attributes type_ where child *JSXExpression*s are taken to be inserted into the attributes.
Similar to how TS uses `JSX.ElementAttributesProperty` to determine the name of _props_, TS uses `JSX.ElementChildrenAttribute` to determine the name of _children_ within those props.
`JSX.ElementChildrenAttribute` should be declared with a single property.

```ts
declare namespace JSX {
  interface ElementChildrenAttribute {
    children: {}; // specify children name to use
  }
}
```

```tsx
<div>
  <h1>Hello</h1>
</div>;

<div>
  <h1>Hello</h1>
  World
</div>;

const CustomComp = (props) => <div>{props.children}</div>
<CustomComp>
  <div>Hello World</div>
  {"This is just a JS expression..." + 1000}
</CustomComp>
```

You can specify the type of _children_ like any other attribute. This will override the default type from, e.g. the [React typings](https://github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/react) if you use them.

```tsx
interface PropsType {
  children: JSX.Element
  name: string
}

class Component extends React.Component<PropsType, {}> {
  render() {
    return (
      <h2>
        {this.props.children}
      </h2>
    )
  }
}

// OK
<Component name="foo">
  <h1>Hello World</h1>
</Component>

// Error: children is of type JSX.Element not array of JSX.Element
<Component name="bar">
  <h1>Hello World</h1>
  <h2>Hello World</h2>
</Component>

// Error: children is of type JSX.Element not array of JSX.Element or string.
<Component name="baz">
  <h1>Hello</h1>
  World
</Component>
```

## The JSX result type

By default the result of a JSX expression is typed as `any`.
You can customize the type by specifying the `JSX.Element` interface.
However, it is not possible to retrieve type information about the element, attributes or children of the JSX from this interface.
It is a black box.

## The JSX function return type

By default, function components must return `JSX.Element | null`. However, this doesn’t always represent runtime behaviour. As of TypeScript 5.1, you can specify `JSX.ElementType` to override what is a valid JSX component type. Note that this doesn’t define what props are valid. The type of props is always defined by the first argument of the component that’s passed. The default looks something like this:

```ts
namespace JSX {
    export type ElementType =
        // All the valid lowercase tags
        | keyof IntrinsicElements
        // Function components
        | (props: any) => Element
        // Class components
        | new (props: any) => ElementClass;
    export interface IntrinsicAttributes extends /*...*/ {}
    export type Element = /*...*/;
    export type ElementClass = /*...*/;
}
```

## Embedding Expressions

JSX allows you to embed expressions between tags by surrounding the expressions with curly braces (`{ }`).

```tsx
const a = (
  <div>
    {["foo", "bar"].map((i) => (
      <span>{i / 2}</span>
    ))}
  </div>
);
```

The above code will result in an error since you cannot divide a string by a number.
The output, when using the `preserve` option, looks like:

```tsx
const a = (
  <div>
    {["foo", "bar"].map(function (i) {
      return <span>{i / 2}</span>;
    })}
  </div>
);
```

## React integration

To use JSX with React you should use the [React typings](https://github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/react).
These typings define the `JSX` namespace appropriately for use with React.

```tsx
/// <reference path="react.d.ts" />

interface Props {
  foo: string;
}

class MyComponent extends React.Component<Props, {}> {
  render() {
    return <span>{this.props.foo}</span>;
  }
}

<MyComponent foo="bar" />; // ok
<MyComponent foo={0} />; // error
```

### Configuring JSX

There are multiple compiler flags which can be used to customize your JSX, which work as both a compiler flag and via inline per-file pragmas. To learn more see their tsconfig reference pages:

- [`jsxFactory`](/tsconfig#jsxFactory)
- [`jsxFragmentFactory`](/tsconfig#jsxFragmentFactory)
- [`jsxImportSource`](/tsconfig#jsxImportSource)

---

## Source: `packages/documentation/copy/en/release-notes/TypeScript 1.6.md`

---
title: TypeScript 1.6
layout: docs
permalink: /docs/handbook/release-notes/typescript-1-6.html
oneline: TypeScript 1.6 Release Notes
---

## JSX support

JSX is an embeddable XML-like syntax.
It is meant to be transformed into valid JavaScript, but the semantics of that transformation are implementation-specific.
JSX came to popularity with the React library but has since seen other applications.
TypeScript 1.6 supports embedding, type checking, and optionally compiling JSX directly into JavaScript.

#### New `.tsx` file extension and `as` operator

TypeScript 1.6 introduces a new `.tsx` file extension.
This extension does two things: it enables JSX inside of TypeScript files, and it makes the new `as` operator the default way to cast (removing any ambiguity between JSX expressions and the TypeScript prefix cast operator).
For example:

```ts
var x = <any>foo;
// is equivalent to:
var x = foo as any;
```

#### Using React

To use JSX-support with React you should use the [React typings](https://github.com/borisyankov/DefinitelyTyped/tree/master/react). These typings define the `JSX` namespace so that TypeScript can correctly check JSX expressions for React. For example:

```ts
/// <reference path="react.d.ts" />

interface Props {
  name: string;
}

class MyComponent extends React.Component<Props, {}> {
  render() {
    return <span>{this.props.name}</span>;
  }
}

<MyComponent name="bar" />; // OK
<MyComponent name={0} />; // error, `name` is not a number
```

#### Using other JSX frameworks

JSX element names and properties are validated against the `JSX` namespace.
Please see the [[JSX]] wiki page for defining the `JSX` namespace for your framework.

#### Output generation

TypeScript ships with two JSX modes: `preserve` and `react`.

- The `preserve` mode will keep JSX expressions as part of the output to be further consumed by another transform step. _Additionally the output will have a `.jsx` file extension._
- The `react` mode will emit `React.createElement`, does not need to go through a JSX transformation before use, and the output will have a `.js` file extension.

See the [[JSX]] wiki page for more information on using JSX in TypeScript.

## Intersection types

TypeScript 1.6 introduces intersection types, the logical complement of union types.
A union type `A | B` represents an entity that is either of type `A` or type `B`, whereas an intersection type `A & B` represents an entity that is both of type `A` _and_ type `B`.

##### Example

```ts
function extend<T, U>(first: T, second: U): T & U {
  let result = <T & U>{};
  for (let id in first) {
    result[id] = first[id];
  }
  for (let id in second) {
    if (!result.hasOwnProperty(id)) {
      result[id] = second[id];
    }
  }
  return result;
}

var x = extend({ a: "hello" }, { b: 42 });
var s = x.a;
var n = x.b;
```

```ts
type LinkedList<T> = T & { next: LinkedList<T> };

interface Person {
  name: string;
}

var people: LinkedList<Person>;
var s = people.name;
var s = people.next.name;
var s = people.next.next.name;
var s = people.next.next.next.name;
```

```ts
interface A {
  a: string;
}
interface B {
  b: string;
}
interface C {
  c: string;
}

var abc: A & B & C;
abc.a = "hello";
abc.b = "hello";
abc.c = "hello";
```

See [issue #1256](https://github.com/Microsoft/TypeScript/issues/1256) for more information.

## Local type declarations

Local class, interface, enum, and type alias declarations can now appear inside function declarations. Local types are block scoped, similar to variables declared with `let` and `const`. For example:

```ts
function f() {
  if (true) {
    interface T {
      x: number;
    }
    let v: T;
    v.x = 5;
  } else {
    interface T {
      x: string;
    }
    let v: T;
    v.x = "hello";
  }
}
```

The inferred return type of a function may be a type declared locally within the function. It is not possible for callers of the function to reference such a local type, but it can of course be matched structurally. For example:

```ts
interface Point {
  x: number;
  y: number;
}

function getPointFactory(x: number, y: number) {
  class P {
    x = x;
    y = y;
  }
  return P;
}

var PointZero = getPointFactory(0, 0);
var PointOne = getPointFactory(1, 1);
var p1 = new PointZero();
var p2 = new PointZero();
var p3 = new PointOne();
```

Local types may reference enclosing type parameters and local class and interfaces may themselves be generic. For example:

```ts
function f3() {
  function f<X, Y>(x: X, y: Y) {
    class C {
      public x = x;
      public y = y;
    }
    return C;
  }
  let C = f(10, "hello");
  let v = new C();
  let x = v.x; // number
  let y = v.y; // string
}
```

## Class expressions

TypeScript 1.6 adds support for ES6 class expressions. In a class expression, the class name is optional and, if specified, is only in scope in the class expression itself. This is similar to the optional name of a function expression. It is not possible to refer to the class instance type of a class expression outside the class expression, but the type can of course be matched structurally. For example:

```ts
let Point = class {
  constructor(public x: number, public y: number) {}
  public length() {
    return Math.sqrt(this.x * this.x + this.y * this.y);
  }
};
var p = new Point(3, 4); // p has anonymous class type
console.log(p.length());
```

## Extending expressions

TypeScript 1.6 adds support for classes extending arbitrary expression that computes a constructor function. This means that built-in types can now be extended in class declarations.

The `extends` clause of a class previously required a type reference to be specified. It now accepts an expression optionally followed by a type argument list. The type of the expression must be a constructor function type with at least one construct signature that has the same number of type parameters as the number of type arguments specified in the `extends` clause. The return type of the matching construct signature(s) is the base type from which the class instance type inherits. Effectively, this allows both real classes and "class-like" expressions to be specified in the `extends` clause.

Some examples:

```ts
// Extend built-in types

class MyArray extends Array<number> {}
class MyError extends Error {}

// Extend computed base class

class ThingA {
  getGreeting() {
    return "Hello from A";
  }
}

class ThingB {
  getGreeting() {
    return "Hello from B";
  }
}

interface Greeter {
  getGreeting(): string;
}

interface GreeterConstructor {
  new (): Greeter;
}

function getGreeterBase(): GreeterConstructor {
  return Math.random() >= 0.5 ? ThingA : ThingB;
}

class Test extends getGreeterBase() {
  sayHello() {
    console.log(this.getGreeting());
  }
}
```

## `abstract` classes and methods

TypeScript 1.6 adds support for `abstract` keyword for classes and their methods. An abstract class is allowed to have methods with no implementation, and cannot be constructed.

##### Examples

```ts
abstract class Base {
  abstract getThing(): string;
  getOtherThing() {
    return "hello";
  }
}

let x = new Base(); // Error, 'Base' is abstract

// Error, must either be 'abstract' or implement concrete 'getThing'
class Derived1 extends Base {}

class Derived2 extends Base {
  getThing() {
    return "hello";
  }
  foo() {
    super.getThing(); // Error: cannot invoke abstract members through 'super'
  }
}

var x = new Derived2(); // OK
var y: Base = new Derived2(); // Also OK
y.getThing(); // OK
y.getOtherThing(); // OK
```

## Generic type aliases

With TypeScript 1.6, type aliases can be generic. For example:

```ts
type Lazy<T> = T | (() => T);

var s: Lazy<string>;
s = "eager";
s = () => "lazy";

interface Tuple<A, B> {
  a: A;
  b: B;
}

type Pair<T> = Tuple<T, T>;
```

## Stricter object literal assignment checks

TypeScript 1.6 enforces stricter object literal assignment checks for the purpose of catching excess or misspelled properties. Specifically, when a fresh object literal is assigned to a variable or passed as an argument for a non-empty target type, it is an error for the object literal to specify properties that don't exist in the target type.

##### Examples

```ts
var x: { foo: number };
x = { foo: 1, baz: 2 }; // Error, excess property `baz`

var y: { foo: number; bar?: number };
y = { foo: 1, baz: 2 }; // Error, excess or misspelled property `baz`
```

A type can include an index signature to explicitly indicate that excess properties are permitted:

```ts
var x: { foo: number; [x: string]: any };
x = { foo: 1, baz: 2 }; // Ok, `baz` matched by index signature
```

## ES6 generators

TypeScript 1.6 adds support for generators when targeting ES6.

A generator function can have a return type annotation, just like a function. The annotation represents the type of the generator returned by the function. Here is an example:

```ts
function* g(): Iterable<string> {
  for (var i = 0; i < 100; i++) {
    yield ""; // string is assignable to string
  }
  yield* otherStringGenerator(); // otherStringGenerator must be iterable and element type assignable to string
}
```

A generator function with no type annotation can have the type annotation inferred.
So in the following case, the type will be inferred from the yield statements:

```ts
function* g() {
  for (var i = 0; i < 100; i++) {
    yield ""; // infer string
  }
  yield* otherStringGenerator(); // infer element type of otherStringGenerator
}
```

## Experimental support for `async` functions

TypeScript 1.6 introduces experimental support of `async` functions when targeting ES6.
Async functions are expected to invoke an asynchronous operation and await its result without blocking normal execution of the program.
This accomplished through the use of an ES6-compatible `Promise` implementation, and transposition of the function body into a compatible form to resume execution when the awaited asynchronous operation completes.

An _async function_ is a function or method that has been prefixed with the `async` modifier. This modifier informs the compiler that function body transposition is required, and that the keyword `await` should be treated as a unary expression instead of an identifier.
An _Async Function_ must provide a return type annotation that points to a compatible `Promise` type. Return type inference can only be used if there is a globally defined, compatible `Promise` type.

##### Example

```ts
var p: Promise<number> = /* ... */;
async function fn(): Promise<number> {
  var i = await p; // suspend execution until 'p' is settled. 'i' has type "number"
  return 1 + i;
}

var a = async (): Promise<number> => 1 + await p; // suspends execution.
var a = async () => 1 + await p; // suspends execution. return type is inferred as "Promise<number>" when compiling with --target ES6
var fe = async function(): Promise<number> {
  var i = await p; // suspend execution until 'p' is settled. 'i' has type "number"
  return 1 + i;
}

class C {
  async m(): Promise<number> {
    var i = await p; // suspend execution until 'p' is settled. 'i' has type "number"
    return 1 + i;
  }

  async get p(): Promise<number> {
    var i = await p; // suspend execution until 'p' is settled. 'i' has type "number"
    return 1 + i;
  }
}
```

## Nightly builds

While not strictly a language change, nightly builds are now available by installing with the following command:

```Shell
npm install -g typescript@next
```

## Adjustments in module resolution logic

Starting from release 1.6 TypeScript compiler will use different set of rules to resolve module names when targeting 'commonjs'.
These [rules](https://github.com/Microsoft/TypeScript/issues/2338) attempted to model module lookup procedure used by Node.
This effectively mean that node modules can include information about its typings and TypeScript compiler will be able to find it.
User however can override module resolution rules picked by the compiler by using [`moduleResolution`](/tsconfig#moduleResolution) command line option. Possible values are:

- 'classic' - module resolution rules used by pre 1.6 TypeScript compiler
- 'node' - node-like module resolution

## Merging ambient class and interface declaration

The instance side of an ambient class declaration can be extended using an interface declaration The class constructor object is unmodified.
For example:

```ts
declare class Foo {
  public x: number;
}

interface Foo {
  y: string;
}

function bar(foo: Foo) {
  foo.x = 1; // OK, declared in the class Foo
  foo.y = "1"; // OK, declared in the interface Foo
}
```

## User-defined type guard functions

TypeScript 1.6 adds a new way to narrow a variable type inside an `if` block, in addition to `typeof` and `instanceof`.
A user-defined type guard functions is one with a return type annotation of the form `x is T`, where `x` is a declared parameter in the signature, and `T` is any type.
When a user-defined type guard function is invoked on a variable in an `if` block, the type of the variable will be narrowed to `T`.

##### Examples

```ts
function isCat(a: any): a is Cat {
  return a.name === "kitty";
}

var x: Cat | Dog;
if (isCat(x)) {
  x.meow(); // OK, x is Cat in this block
}
```

## `exclude` property support in tsconfig.json

A tsconfig.json file that doesn't specify a files property (and therefore implicitly references all \*.ts files in all subdirectories) can now contain an exclude property that specifies a list of files and/or directories to exclude from the compilation.
The exclude property must be an array of strings that each specify a file or folder name relative to the location of the tsconfig.json file.
For example:

```json tsconfig
{
  "compilerOptions": {
    "out": "test.js"
  },
  "exclude": ["node_modules", "test.ts", "utils/t2.ts"]
}
```

The [`exclude`](/tsconfig#exclude) list does not support wildcards. It must simply be a list of files and/or directories.

## `--init` command line option

Run `tsc --init` in a directory to create an initial `tsconfig.json` in this directory with preset defaults.
Optionally pass command line arguments along with `--init` to be stored in your initial tsconfig.json on creation.

---

## Source: `packages/documentation/copy/en/release-notes/TypeScript 1.8.md`

---
title: TypeScript 1.8
layout: docs
permalink: /docs/handbook/release-notes/typescript-1-8.html
oneline: TypeScript 1.8 Release Notes
---

## Type parameters as constraints

With TypeScript 1.8 it becomes possible for a type parameter constraint to reference type parameters from the same type parameter list.
Previously this was an error.
This capability is usually referred to as [F-Bounded Polymorphism](https://wikipedia.org/wiki/Bounded_quantification#F-bounded_quantification).

##### Example

```ts
function assign<T extends U, U>(target: T, source: U): T {
  for (let id in source) {
    target[id] = source[id];
  }
  return target;
}

let x = { a: 1, b: 2, c: 3, d: 4 };
assign(x, { b: 10, d: 20 });
assign(x, { e: 0 }); // Error
```

## Control flow analysis errors

TypeScript 1.8 introduces control flow analysis to help catch common errors that users tend to run into.
Read on to get more details, and check out these errors in action:

![cfa](https://cloud.githubusercontent.com/assets/8052307/5210657/c5ae0f28-7585-11e4-97d8-86169ef2a160.gif)

### Unreachable code

Statements guaranteed to not be executed at run time are now correctly flagged as unreachable code errors.
For instance, statements following unconditional `return`, `throw`, `break` or `continue` statements are considered unreachable.
Use [`allowUnreachableCode`](/tsconfig#allowUnreachableCode) to disable unreachable code detection and reporting.

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

### Unused labels

Unused labels are also flagged.
Just like unreachable code checks, these are turned on by default;
use [`allowUnusedLabels`](/tsconfig#allowUnusedLabels) to stop reporting these errors.

##### Example

```ts
loop: while (x > 0) {
  // Error: Unused label.
  x++;
}
```

### Implicit returns

Functions with code paths that do not return a value in JS implicitly return `undefined`.
These can now be flagged by the compiler as implicit returns.
The check is turned _off_ by default; use [`noImplicitReturns`](/tsconfig#noImplicitReturns) to turn it on.

##### Example

```ts
function f(x) {
  // Error: Not all code paths return a value.
  if (x) {
    return false;
  }

  // implicitly returns `undefined`
}
```

### Case clause fall-throughs

TypeScript can reports errors for fall-through cases in switch statement where the case clause is non-empty.
This check is turned _off_ by default, and can be enabled using [`noFallthroughCasesInSwitch`](/tsconfig#noFallthroughCasesInSwitch).

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

## Function Components in React

TypeScript now supports [Function components](https://reactjs.org/docs/components-and-props.html#functional-and-class-components).
These are lightweight components that easily compose other components:

```ts
// Use parameter destructuring and defaults for easy definition of 'props' type
const Greeter = ({ name = "world" }) => <div>Hello, {name}!</div>;

// Properties get validated
let example = <Greeter name="TypeScript 1.8" />;
```

For this feature and simplified props, be sure to use the [latest version of react.d.ts](https://github.com/DefinitelyTyped/DefinitelyTyped/blob/master/types/react/index.d.ts).

## Simplified `props` type management in React

In TypeScript 1.8 with the latest version of react.d.ts (see above), we've also greatly simplified the declaration of `props` types.

Specifically:

- You no longer need to either explicitly declare `ref` and `key` or `extend React.Props`
- The `ref` and `key` properties will appear with correct types on all components
- The `ref` property is correctly disallowed on instances of Stateless Function components

## Augmenting global/module scope from modules

Users can now declare any augmentations that they want to make, or that any other consumers already have made, to an existing module.
Module augmentations look like plain old ambient module declarations (i.e. the `declare module "foo" { }` syntax), and are directly nested either your own modules, or in another top level ambient external module.

Furthermore, TypeScript also has the notion of _global_ augmentations of the form `declare global { }`.
This allows modules to augment global types such as `Array` if necessary.

The name of a module augmentation is resolved using the same set of rules as module specifiers in `import` and `export` declarations.
The declarations in a module augmentation are merged with any existing declarations the same way they would if they were declared in the same file.

Neither module augmentations nor global augmentations can add new items to the top level scope - they can only "patch" existing declarations.

##### Example

Here `map.ts` can declare that it will internally patch the `Observable` type from `observable.ts` and add the `map` method to it.

```ts
// observable.ts
export class Observable<T> {
  // ...
}
```

```ts
// map.ts
import { Observable } from "./observable";

// Create an augmentation for "./observable"
declare module "./observable" {

    // Augment the 'Observable' class definition with interface merging
    interface Observable<T> {
        map<U>(proj: (el: T) => U): Observable<U>;
    }

}

Observable.prototype.map = /*...*/;
```

```ts
// consumer.ts
import { Observable } from "./observable";
import "./map";

let o: Observable<number>;
o.map((x) => x.toFixed());
```

Similarly, the global scope can be augmented from modules using a `declare global` declarations:

##### Example

```ts
// Ensure this is treated as a module.
export {};

declare global {
  interface Array<T> {
    mapToNumbers(): number[];
  }
}

Array.prototype.mapToNumbers = function () {
  /* ... */
};
```

## String literal types

It's not uncommon for an API to expect a specific set of strings for certain values.
For instance, consider a UI library that can move elements across the screen while controlling the ["easing" of the animation.](https://wikipedia.org/wiki/Inbetweening)

```ts
declare class UIElement {
  animate(options: AnimationOptions): void;
}

interface AnimationOptions {
  deltaX: number;
  deltaY: number;
  easing: string; // Can be "ease-in", "ease-out", "ease-in-out"
}
```

However, this is error prone - there is nothing stopping a user from accidentally misspelling one of the valid easing values:

```ts
// No errors
new UIElement().animate({ deltaX: 100, deltaY: 100, easing: "ease-inout" });
```

With TypeScript 1.8, we've introduced string literal types.
These types are written the same way string literals are, but in type positions.

Users can now ensure that the type system will catch such errors.
Here's our new `AnimationOptions` using string literal types:

```ts
interface AnimationOptions {
  deltaX: number;
  deltaY: number;
  easing: "ease-in" | "ease-out" | "ease-in-out";
}

// Error: Type '"ease-inout"' is not assignable to type '"ease-in" | "ease-out" | "ease-in-out"'
new UIElement().animate({ deltaX: 100, deltaY: 100, easing: "ease-inout" });
```

## Improved union/intersection type inference

TypeScript 1.8 improves type inference involving source and target sides that are both union or intersection types.
For example, when inferring from `string | string[]` to `string | T`, we reduce the types to `string[]` and `T`, thus inferring `string[]` for `T`.

##### Example

```ts
type Maybe<T> = T | void;

function isDefined<T>(x: Maybe<T>): x is T {
  return x !== undefined && x !== null;
}

function isUndefined<T>(x: Maybe<T>): x is void {
  return x === undefined || x === null;
}

function getOrElse<T>(x: Maybe<T>, defaultValue: T): T {
  return isDefined(x) ? x : defaultValue;
}

function test1(x: Maybe<string>) {
  let x1 = getOrElse(x, "Undefined"); // string
  let x2 = isDefined(x) ? x : "Undefined"; // string
  let x3 = isUndefined(x) ? "Undefined" : x; // string
}

function test2(x: Maybe<number>) {
  let x1 = getOrElse(x, -1); // number
  let x2 = isDefined(x) ? x : -1; // number
  let x3 = isUndefined(x) ? -1 : x; // number
}
```

## Concatenate `AMD` and `System` modules with `--outFile`

Specifying [`outFile`](/tsconfig#outFile) in conjunction with `--module amd` or `--module system` will concatenate all modules in the compilation into a single output file containing multiple module closures.

A module name will be computed for each module based on its relative location to [`rootDir`](/tsconfig#rootDir).

##### Example

```ts
// file src/a.ts
import * as B from "./lib/b";
export function createA() {
  return B.createB();
}
```

```ts
// file src/lib/b.ts
export function createB() {
  return {};
}
```

Results in:

```js
define("lib/b", ["require", "exports"], function (require, exports) {
  "use strict";
  function createB() {
    return {};
  }
  exports.createB = createB;
});
define("a", ["require", "exports", "lib/b"], function (require, exports, B) {
  "use strict";
  function createA() {
    return B.createB();
  }
  exports.createA = createA;
});
```

## Support for `default` import interop with SystemJS

Module loaders like SystemJS wrap CommonJS modules and expose them as a `default` ES6 import. This makes it impossible to share the definition files between the SystemJS and CommonJS implementation of the module as the module shape looks different based on the loader.

Setting the new compiler flag [`allowSyntheticDefaultImports`](/tsconfig#allowSyntheticDefaultImports) indicates that the module loader performs some kind of synthetic default import member creation not indicated in the imported .ts or .d.ts. The compiler will infer the existence of a `default` export that has the shape of the entire module itself.

System modules have this flag on by default.

## Allow captured `let`/`const` in loops

Previously an error, now supported in TypeScript 1.8.
`let`/`const` declarations within loops and captured in functions are now emitted to correctly match `let`/`const` freshness semantics.

##### Example

```ts
let list = [];
for (let i = 0; i < 5; i++) {
  list.push(() => i);
}

list.forEach((f) => console.log(f()));
```

is compiled to:

```js
var list = [];
var _loop_1 = function (i) {
  list.push(function () {
    return i;
  });
};
for (var i = 0; i < 5; i++) {
  _loop_1(i);
}
list.forEach(function (f) {
  return console.log(f());
});
```

And results in

```cmd
0
1
2
3
4
```

## Improved checking for `for..in` statements

Previously the type of a `for..in` variable is inferred to `any`; that allowed the compiler to ignore invalid uses within the `for..in` body.

Starting with TypeScript 1.8:

- The type of a variable declared in a `for..in` statement is implicitly `string`.
- When an object with a numeric index signature of type `T` (such as an array) is indexed by a `for..in` variable of a containing `for..in` statement for an object _with_ a numeric index signature and _without_ a string index signature (again such as an array), the value produced is of type `T`.

##### Example

```ts
var a: MyObject[];
for (var x in a) {
  // Type of x is implicitly string
  var obj = a[x]; // Type of obj is MyObject
}
```

## Modules are now emitted with a `"use strict";` prologue

Modules were always parsed in strict mode as per ES6, but for non-ES6 targets this was not respected in the generated code. Starting with TypeScript 1.8, emitted modules are always in strict mode. This shouldn't have any visible changes in most code as TS considers most strict mode errors as errors at compile time, but it means that some things which used to silently fail at runtime in your TS code, like assigning to `NaN`, will now loudly fail. You can reference the [MDN Article](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Strict_mode) on strict mode for a detailed list of the differences between strict mode and non-strict mode.

## Including `.js` files with `--allowJs`

Often there are external source files in your project that may not be authored in TypeScript.
Alternatively, you might be in the middle of converting a JS code base into TS, but still want to bundle all your JS code into a single file with the output of your new TS code.

`.js` files are now allowed as input to `tsc`.
The TypeScript compiler checks the input `.js` files for syntax errors, and emits valid output based on the [`target`](/tsconfig#target) and [`module`](/tsconfig#module) flags.
The output can be combined with other `.ts` files as well.
Source maps are still generated for `.js` files just like with `.ts` files.

## Custom JSX factories using `--reactNamespace`

Passing `--reactNamespace <JSX factory Name>` along with `--jsx react` allows for using a different JSX factory from the default `React`.

The new factory name will be used to call `createElement` and `__spread` functions.

##### Example

```ts
import { jsxFactory } from "jsxFactory";

var div = <div>Hello JSX!</div>;
```

Compiled with:

```shell
tsc --jsx react --reactNamespace jsxFactory --m commonJS
```

Results in:

```js
"use strict";
var jsxFactory_1 = require("jsxFactory");
var div = jsxFactory_1.jsxFactory.createElement("div", null, "Hello JSX!");
```

## `this`-based type guards

TypeScript 1.8 extends [user-defined type guard functions](./typescript-1.6.html#user-defined-type-guard-functions) to class and interface methods.

`this is T` is now valid return type annotation for methods in classes and interfaces.
When used in a type narrowing position (e.g. `if` statement), the type of the call expression target object would be narrowed to `T`.

##### Example

```ts
class FileSystemObject {
  isFile(): this is File {
    return this instanceof File;
  }
  isDirectory(): this is Directory {
    return this instanceof Directory;
  }
  isNetworked(): this is Networked & this {
    return this.networked;
  }
  constructor(public path: string, private networked: boolean) {}
}

class File extends FileSystemObject {
  constructor(path: string, public content: string) {
    super(path, false);
  }
}
class Directory extends FileSystemObject {
  children: FileSystemObject[];
}
interface Networked {
  host: string;
}

let fso: FileSystemObject = new File("foo/bar.txt", "foo");
if (fso.isFile()) {
  fso.content; // fso is File
} else if (fso.isDirectory()) {
  fso.children; // fso is Directory
} else if (fso.isNetworked()) {
  fso.host; // fso is networked
}
```

## Official TypeScript NuGet package

Starting with TypeScript 1.8, official NuGet packages are available for the TypeScript Compiler (`tsc.exe`) as well as the MSBuild integration (`Microsoft.TypeScript.targets` and `Microsoft.TypeScript.Tasks.dll`).

Stable packages are available here:

- [Microsoft.TypeScript.Compiler](https://www.nuget.org/packages/Microsoft.TypeScript.Compiler/)
- [Microsoft.TypeScript.MSBuild](https://www.nuget.org/packages/Microsoft.TypeScript.MSBuild/)

Also, a nightly NuGet package to match the [nightly npm package](http://blogs.msdn.com/b/typescript/archive/2015/07/27/introducing-typescript-nightlies.aspx) is available on [myget](https://myget.org):

- [TypeScript-Preview](https://www.myget.org/gallery/typescript-preview)

## Prettier error messages from `tsc`

We understand that a ton of monochrome output can be a little difficult on the eyes.
Colors can help discern where a message starts and ends, and these visual clues are important when error output gets overwhelming.

By just passing the [`pretty`](/tsconfig#pretty) command line option, TypeScript gives a more colorful output with context about where things are going wrong.

![Showing off pretty error messages in ConEmu](https://raw.githubusercontent.com/wiki/Microsoft/TypeScript/images/new-in-typescript/pretty01.png)

## Colorization of JSX code in VS 2015

With TypeScript 1.8, JSX tags are now classified and colorized in Visual Studio 2015.

![jsx](https://cloud.githubusercontent.com/assets/8052307/12271404/b875c502-b90f-11e5-93d8-c6740be354d1.png)

The classification can be further customized by changing the font and color settings for the `VB XML` color and font settings through `Tools`->`Options`->`Environment`->`Fonts and Colors` page.

## The `--project` (`-p`) flag can now take any file path

The `--project` command line option originally could only take paths to a folder containing a `tsconfig.json`.
Given the different scenarios for build configurations, it made sense to allow `--project` to point to any other compatible JSON file.
For instance, a user might want to target ES2015 with CommonJS modules for Node 5, but ES5 with AMD modules for the browser.
With this new work, users can easily manage two separate build targets using `tsc` alone without having to perform hacky workarounds like placing `tsconfig.json` files in separate directories.

The old behavior still remains the same if given a directory - the compiler will try to find a file in the directory named `tsconfig.json`.

## Allow comments in tsconfig.json

It's always nice to be able to document your configuration!
`tsconfig.json` now accepts single and multi-line comments.

```json tsconfig
{
  "compilerOptions": {
    "target": "ES2015", // running on node v5, yaay!
    "sourceMap": true // makes debugging easier
  },
  /*
   * Excluded files
   */
  "exclude": ["file.d.ts"]
}
```

## Support output to IPC-driven files

TypeScript 1.8 allows users to use the [`outFile`](/tsconfig#outFile) argument with special file system entities like named pipes, devices, etc.

As an example, on many Unix-like systems, the standard output stream is accessible by the file `/dev/stdout`.

```shell
tsc foo.ts --outFile /dev/stdout
```

This can be used to pipe output between commands as well.

As an example, we can pipe our emitted JavaScript into a pretty printer like [pretty-js](https://www.npmjs.com/package/pretty-js):

```shell
tsc foo.ts --outFile /dev/stdout | pretty-js
```

## Improved support for `tsconfig.json` in Visual Studio 2015

TypeScript 1.8 allows `tsconfig.json` files in all project types.
This includes ASP.NET v4 projects, _Console Application_, and the _Html Application with TypeScript_ project types.
Further, you are no longer limited to a single `tsconfig.json` file but can add multiple, and each will be built as part of the project.
This allows you to separate the configuration for different parts of your application without having to use multiple different projects.

![Showing off tsconfig.json in Visual Studio](https://raw.githubusercontent.com/wiki/Microsoft/TypeScript/images/new-in-typescript/tsconfig-in-vs.png)

We also disable the project properties page when you add a `tsconfig.json` file.
This means that all configuration changes have to be made in the `tsconfig.json` file itself.

### A couple of limitations

- If you add a `tsconfig.json` file, TypeScript files that are not considered part of that context are not compiled.
- Apache Cordova Apps still have the existing limitation of a single `tsconfig.json` file, which must be in either the root or the `scripts` folder.
- There is no template for `tsconfig.json` in most project types.

---

## Source: `packages/documentation/copy/en/release-notes/TypeScript 2.2.md`

---
title: TypeScript 2.2
layout: docs
permalink: /docs/handbook/release-notes/typescript-2-2.html
oneline: TypeScript 2.2 Release Notes
---

## Support for Mix-in classes

TypeScript 2.2 adds support for the ECMAScript 2015 mixin class pattern (see [MDN Mixin description](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Classes#Mix-ins) and ["Real" Mixins with JavaScript Classes](http://justinfagnani.com/2015/12/21/real-mixins-with-javascript-classes/) for more details) as well as rules for combining mixin construct signatures with regular construct signatures in intersection types.

##### First some terminology

A **mixin constructor type** refers to a type that has a single construct signature with a single rest argument of type `any[]` and an object-like return type. For example, given an object-like type `X`, `new (...args: any[]) => X` is a mixin constructor type with an instance type `X`.

A **mixin class** is a class declaration or expression that `extends` an expression of a type parameter type. The following rules apply to mixin class declarations:

- The type parameter type of the `extends` expression must be constrained to a mixin constructor type.
- The constructor of a mixin class (if any) must have a single rest parameter of type `any[]` and must use the spread operator to pass those parameters as arguments in a `super(...args)` call.

Given an expression `Base` of a parametric type `T` with a constraint `X`, a mixin class `class C extends Base {...}` is processed as if `Base` had type `X` and the resulting type is the intersection `typeof C & T`.
In other words, a mixin class is represented as an intersection between the mixin class constructor type and the parametric base class constructor type.

When obtaining the construct signatures of an intersection type that contains mixin constructor types, the mixin construct signatures are discarded and their instance types are mixed into the return types of the other construct signatures in the intersection type.
For example, the intersection type `{ new(...args: any[]) => A } & { new(s: string) => B }` has a single construct signature `new(s: string) => A & B`.

##### Putting all of the above rules together in an example

```ts
class Point {
  constructor(public x: number, public y: number) {}
}

class Person {
  constructor(public name: string) {}
}

type Constructor<T> = new (...args: any[]) => T;

function Tagged<T extends Constructor<{}>>(Base: T) {
  return class extends Base {
    _tag: string;
    constructor(...args: any[]) {
      super(...args);
      this._tag = "";
    }
  };
}

const TaggedPoint = Tagged(Point);

let point = new TaggedPoint(10, 20);
point._tag = "hello";

class Customer extends Tagged(Person) {
  accountBalance: number;
}

let customer = new Customer("Joe");
customer._tag = "test";
customer.accountBalance = 0;
```

Mixin classes can constrain the types of classes they can mix into by specifying a construct signature return type in the constraint for the type parameter.
For example, the following `WithLocation` function implements a subclass factory that adds a `getLocation` method to any class that satisfies the `Point` interface (i.e. that has `x` and `y` properties of type `number`).

```ts
interface Point {
  x: number;
  y: number;
}

const WithLocation = <T extends Constructor<Point>>(Base: T) =>
  class extends Base {
    getLocation(): [number, number] {
      return [this.x, this.y];
    }
  };
```

## `object` type

TypeScript did not have a type that represents the non-primitive type, i.e. any thing that is not `number`, `string`, `boolean`, `symbol`, `null`, or `undefined`. Enter the new `object` type.

With `object` type, APIs like `Object.create` can be better represented. For example:

```ts
declare function create(o: object | null): void;

create({ prop: 0 }); // OK
create(null); // OK

create(42); // Error
create("string"); // Error
create(false); // Error
create(undefined); // Error
```

## Support for `new.target`

The `new.target` meta-property is new syntax introduced in ES2015.
When an instance of a constructor is created via `new`, the value of `new.target` is set to be a reference to the constructor function initially used to allocate the instance.
If a function is called rather than constructed via `new`, `new.target` is set to `undefined`.

`new.target` comes in handy when `Object.setPrototypeOf` or `__proto__` needs to be set in a class constructor. One such use case is inheriting from `Error` in NodeJS v4 and higher.

##### Example

```ts
class CustomError extends Error {
  constructor(message?: string) {
    super(message); // 'Error' breaks prototype chain here
    Object.setPrototypeOf(this, new.target.prototype); // restore prototype chain
  }
}
```

This results in the generated JS

```js
var CustomError = (function(_super) {
  __extends(CustomError, _super);
  function CustomError() {
    var _newTarget = this.constructor;
    var _this = _super.apply(this, arguments); // 'Error' breaks prototype chain here
    _this.__proto__ = _newTarget.prototype; // restore prototype chain
    return _this;
  }
  return CustomError;
})(Error);
```

`new.target` also comes in handy for writing constructable functions, for example:

```ts
function f() {
  if (new.target) {
    /* called via 'new' */
  }
}
```

Which translates to:

```js
function f() {
  var _newTarget = this && this instanceof f ? this.constructor : void 0;
  if (_newTarget) {
    /* called via 'new' */
  }
}
```

## Better checking for `null`/`undefined` in operands of expressions

TypeScript 2.2 improves checking of nullable operands in expressions. Specifically, these are now flagged as errors:

- If either operand of a `+` operator is nullable, and neither operand is of type `any` or `string`.
- If either operand of a `-`, `*`, `**`, `/`, `%`, `<<`, `>>`, `>>>`, `&`, `|`, or `^` operator is nullable.
- If either operand of a `<`, `>`, `<=`, `>=`, or `in` operator is nullable.
- If the right operand of an `instanceof` operator is nullable.
- If the operand of a `+`, `-`, `~`, `++`, or `--` unary operator is nullable.

An operand is considered nullable if the type of the operand is `null` or `undefined` or a union type that includes `null` or `undefined`.
Note that the union type case only occurs in [`strictNullChecks`](/tsconfig#strictNullChecks) mode because `null` and `undefined` disappear from unions in classic type checking mode.

## Dotted property for types with string index signatures

Types with a string index signature can be indexed using the `[]` notation, but were not allowed to use the `.`.
Starting with TypeScript 2.2 using either should be allowed.

```ts
interface StringMap<T> {
  [x: string]: T;
}

const map: StringMap<number>;

map["prop1"] = 1;
map.prop2 = 2;
```

This only applies to types with an _explicit_ string index signature.
It is still an error to access unknown properties on a type using `.` notation.

## Support for spread operator on JSX element children

TypeScript 2.2 adds support for using spread on JSX element children.
Please see [facebook/jsx#57](https://github.com/facebook/jsx/issues/57) for more details.

##### Example

```ts
function Todo(prop: { key: number; todo: string }) {
  return <div>{prop.key.toString() + prop.todo}</div>;
}

function TodoList({ todos }: TodoListProps) {
  return (
    <div>{...todos.map(todo => <Todo key={todo.id} todo={todo.todo} />)}</div>
  );
}

let x: TodoListProps;

<TodoList {...x} />;
```

## New `jsx: react-native`

React-native build pipeline expects all files to have a `.js` extension even if the file contains JSX syntax.
The new [`jsx`](/tsconfig#jsx) value `react-native` will preserve the JSX syntax in the output file, but give it a `.js` extension.

---

## Source: `packages/documentation/copy/en/release-notes/TypeScript 2.6.md`

---
title: TypeScript 2.6
layout: docs
permalink: /docs/handbook/release-notes/typescript-2-6.html
oneline: TypeScript 2.6 Release Notes
---

## Strict function types

TypeScript 2.6 introduces a new strict checking flag, [`strictFunctionTypes`](/tsconfig#strictFunctionTypes).
The [`strictFunctionTypes`](/tsconfig#strictFunctionTypes) switch is part of the [`strict`](/tsconfig#strict) family of switches, meaning that it defaults to on in [`strict`](/tsconfig#strict) mode.
You can opt-out by setting `--strictFunctionTypes false` on your command line or in your tsconfig.json.

Under [`strictFunctionTypes`](/tsconfig#strictFunctionTypes) function type parameter positions are checked _contravariantly_ instead of _bivariantly_.
For some background on what variance means for function types check out [What are covariance and contravariance?](https://web.archive.org/web/20220823104433/https://www.stephanboyer.com/post/132/what-are-covariance-and-contravariance).

The stricter checking applies to all function types, _except_ those originating in method or constructor declarations.
Methods are excluded specifically to ensure generic classes and interfaces (such as `Array<T>`) continue to mostly relate covariantly.

Consider the following example in which `Animal` is the supertype of `Dog` and `Cat`:

```ts
declare let f1: (x: Animal) => void;
declare let f2: (x: Dog) => void;
declare let f3: (x: Cat) => void;
f1 = f2; // Error with --strictFunctionTypes
f2 = f1; // Ok
f2 = f3; // Error
```

The first assignment is permitted in default type checking mode, but flagged as an error in strict function types mode.
Intuitively, the default mode permits the assignment because it is _possibly_ sound, whereas strict function types mode makes it an error because it isn't _provably_ sound.
In either mode the third assignment is an error because it is _never_ sound.

Another way to describe the example is that the type `(x: T) => void` is _bivariant_ (i.e. covariant _or_ contravariant) for `T` in default type checking mode, but _contravariant_ for `T` in strict function types mode.

##### Example

```ts
interface Comparer<T> {
  compare: (a: T, b: T) => number;
}

declare let animalComparer: Comparer<Animal>;
declare let dogComparer: Comparer<Dog>;

animalComparer = dogComparer; // Error
dogComparer = animalComparer; // Ok
```

The first assignment is now an error. Effectively, `T` is contravariant in `Comparer<T>` because it is used only in function type parameter positions.

By the way, note that whereas some languages (e.g. C# and Scala) require variance annotations (`out`/`in` or `+`/`-`), variance emerges naturally from the actual use of a type parameter within a generic type due to TypeScript's structural type system.

##### Note

Under [`strictFunctionTypes`](/tsconfig#strictFunctionTypes) the first assignment is still permitted if `compare` was declared as a method.
Effectively, `T` is bivariant in `Comparer<T>` because it is used only in method parameter positions.

```ts
interface Comparer<T> {
  compare(a: T, b: T): number;
}

declare let animalComparer: Comparer<Animal>;
declare let dogComparer: Comparer<Dog>;

animalComparer = dogComparer; // Ok because of bivariance
dogComparer = animalComparer; // Ok
```

TypeScript 2.6 also improves type inference involving contravariant positions:

```ts
function combine<T>(...funcs: ((x: T) => void)[]): (x: T) => void {
  return x => {
    for (const f of funcs) f(x);
  };
}

function animalFunc(x: Animal) {}
function dogFunc(x: Dog) {}

let combined = combine(animalFunc, dogFunc); // (x: Dog) => void
```

Above, all inferences for `T` originate in contravariant positions, and we therefore infer the _best common subtype_ for `T`.
This contrasts with inferences from covariant positions, where we infer the _best common supertype_.

## Cache tagged template objects in modules

TypeScript 2.6 fixes the tagged string template emit to align better with the ECMAScript spec.
As per the [ECMAScript spec](https://tc39.github.io/ecma262/#sec-gettemplateobject), every time a template tag is evaluated, the _same_ template strings object (the same `TemplateStringsArray`) should be passed as the first argument.
Before TypeScript 2.6, the generated output was a completely new template object each time.
Though the string contents are the same, this emit affects libraries that use the identity of the string for cache invalidation purposes, e.g. [lit-html](https://github.com/PolymerLabs/lit-html/issues/58).

##### Example

```ts
export function id(x: TemplateStringsArray) {
  return x;
}

export function templateObjectFactory() {
  return id`hello world`;
}

let result = templateObjectFactory() === templateObjectFactory(); // true in TS 2.6
```

Results in the following generated code:

```js
"use strict";
var __makeTemplateObject =
  (this && this.__makeTemplateObject) ||
  function(cooked, raw) {
    if (Object.defineProperty) {
      Object.defineProperty(cooked, "raw", { value: raw });
    } else {
      cooked.raw = raw;
    }
    return cooked;
  };

function id(x) {
  return x;
}

var _a;
function templateObjectFactory() {
  return id(
    _a || (_a = __makeTemplateObject(["hello world"], ["hello world"]))
  );
}

var result = templateObjectFactory() === templateObjectFactory();
```

> Note: This change brings a new emit helper, `__makeTemplateObject`;
> if you are using [`importHelpers`](/tsconfig#importHelpers) with [`tslib`](https://github.com/Microsoft/tslib), an updated to version 1.8 or later.

## Localized diagnostics on the command line

TypeScript 2.6 npm package ships with localized versions of diagnostic messages for 13 languages.
The localized messages are available when using the `--locale` flag on the command line.

##### Example

Error messages in Russian:

```sh
c:\ts>tsc --v
Version 2.6.0-dev.20171003

c:\ts>tsc --locale ru --pretty c:\test\a.ts

../test/a.ts(1,5): error TS2322: Тип ""string"" не может быть назначен для типа "number".

1 var x: number = "string";
      ~
```

And help in Japanese:

```sh
PS C:\ts> tsc --v
Version 2.6.0-dev.20171003

PS C:\ts> tsc --locale ja-jp
バージョン 2.6.0-dev.20171003
構文: tsc [オプション] [ファイル ...]

例:  tsc hello.ts
    tsc --outFile file.js file.ts
    tsc @args.txt

オプション:
 -h, --help                                 このメッセージを表示します。
 --all                                      コンパイラ オプションをすべて表示します。
 -v, --version                              コンパイラのバージョンを表示します。
 --init                                     TypeScript プロジェクトを初期化して、tsconfig.json ファイルを作成します。
 -p ファイルまたはディレクトリ, --project ファイルまたはディレクトリ  構成ファイルか、'tsconfig.json' を含むフォルダーにパスが指定されたプロジェクトをコ
ンパイルします。
 --pretty                                   色とコンテキストを使用してエラーとメッセージにスタイルを適用します (試験的)。
 -w, --watch                                入力ファイルを監視します。
 -t バージョン, --target バージョン                   ECMAScript のターゲット バージョンを指定します: 'ES3' (既定)、'ES5'、'ES2015'、'ES2016'、'ES2017'、'ES
NEXT'。
 -m 種類, --module 種類                         モジュール コード生成を指定します: 'none'、'commonjs'、'amd'、'system'、'umd'、'es2015'、'ESNext'。
 --lib                                      コンパイルに含めるライブラリ ファイルを指定します:
                                              'es5' 'es6' 'es2015' 'es7' 'es2016' 'es2017' 'esnext' 'dom' 'dom.iterable' 'webworker' 'scripthost' 'es201
5.core' 'es2015.collection' 'es2015.generator' 'es2015.iterable' 'es2015.promise' 'es2015.proxy' 'es2015.reflect' 'es2015.symbol' 'es2015.symbol.wellkno
wn' 'es2016.array.include' 'es2017.object' 'es2017.sharedmemory' 'es2017.string' 'es2017.intl' 'esnext.asynciterable'
 --allowJs                                  javascript ファイルのコンパイルを許可します。
 --jsx 種類                                   JSX コード生成を指定します: 'preserve'、'react-native'、'react'。
 -d, --declaration                          対応する '.d.ts' ファイルを生成します。
 --sourceMap                                対応する '.map' ファイルを生成します。
 --outFile ファイル                             出力を連結して 1 つのファイルを生成します。
 --outDir ディレクトリ                            ディレクトリへ出力構造をリダイレクトします。
 --removeComments                           コメントを出力しないでください。
 --noEmit                                   出力しないでください。
 --strict                                   strict 型チェックのオプションをすべて有効にします。
 --noImplicitAny                            暗黙的な 'any' 型を含む式と宣言に関するエラーを発生させます。
 --strictNullChecks                         厳格な null チェックを有効にします。
 --noImplicitThis                           暗黙的な 'any' 型を持つ 'this' 式でエラーが発生します。
 --alwaysStrict                             厳格モードで解析してソース ファイルごとに "use strict" を生成します。
 --noUnusedLocals                           使用されていないローカルに関するエラーを報告します。
 --noUnusedParameters                       使用されていないパラメーターに関するエラーを報告します。
 --noImplicitReturns                        関数の一部のコード パスが値を返さない場合にエラーを報告します。
 --noFallthroughCasesInSwitch               switch ステートメントに case のフォールスルーがある場合にエラーを報告します。
 --types                                    コンパイルに含む型宣言ファイル。
 @<ファイル>
```

## Suppress errors in .ts files using '// @ts-ignore' comments

TypeScript 2.6 supports suppressing errors in .ts files using `// @ts-ignore` comments placed above the offending lines.

##### Example

```ts
if (false) {
  // @ts-ignore: Unreachable code error
  console.log("hello");
}
```

A `// @ts-ignore` comment suppresses all errors that originate on the following line.
It is recommended practice to have the remainder of the comment following `@ts-ignore` explain which error is being suppressed.

Please note that this comment only suppresses the error reporting, and we recommend you use this comments _very sparingly_.

## Faster `tsc --watch`

TypeScript 2.6 brings a faster `--watch` implementation.
The new version optimizes code generation and checking for code bases using ES modules.
Changes detected in a module file will result in _only_ regenerating the changed module, and files that depend on it, instead of the whole project.
Projects with a large number of files should reap the most benefit from this change.

The new implementation also brings performance enhancements to watching in tsserver.
The watcher logic has been completely rewritten to respond faster to change events.

## Write-only references now flagged as unused

TypeScript 2.6 adds revised implementation the [`noUnusedLocals`](/tsconfig#noUnusedLocals) and [`noUnusedParameters`](/tsconfig#noUnusedParameters) [compiler options](/docs/handbook/compiler-options.html).
Declarations are only written to but never read from are now flagged as unused.

##### Example

Below both `n` and `m` will be marked as unused, because their values are never _read_. Previously TypeScript would only check whether their values were _referenced_.

```ts
function f(n: number) {
  n = 0;
}

class C {
  private m: number;
  constructor() {
    this.m = 0;
  }
}
```

Also functions that are only called within their own bodies are considered unused.

##### Example

```ts
function f() {
  f(); // Error: 'f' is declared but its value is never read
}
```

---

## Source: `packages/documentation/copy/en/release-notes/TypeScript 2.8.md`

---
title: TypeScript 2.8
layout: docs
permalink: /docs/handbook/release-notes/typescript-2-8.html
oneline: TypeScript 2.8 Release Notes
---

## Conditional Types

TypeScript 2.8 introduces _conditional types_ which add the ability to express non-uniform type mappings.
A conditional type selects one of two possible types based on a condition expressed as a type relationship test:

```ts
T extends U ? X : Y
```

The type above means when `T` is assignable to `U` the type is `X`, otherwise the type is `Y`.

A conditional type `T extends U ? X : Y` is either _resolved_ to `X` or `Y`, or _deferred_ because the condition depends on one or more type variables.
Whether to resolve or defer is determined as follows:

- First, given types `T'` and `U'` that are instantiations of `T` and `U` where all occurrences of type parameters are replaced with `any`, if `T'` is not assignable to `U'`, the conditional type is resolved to `Y`. Intuitively, if the most permissive instantiation of `T` is not assignable to the most permissive instantiation of `U`, we know that no instantiation will be and we can just resolve to `Y`.
- Next, for each type variable introduced by an `infer` (more later) declaration within `U` collect a set of candidate types by inferring from `T` to `U` (using the same inference algorithm as type inference for generic functions). For a given `infer` type variable `V`, if any candidates were inferred from co-variant positions, the type inferred for `V` is a union of those candidates. Otherwise, if any candidates were inferred from contra-variant positions, the type inferred for `V` is an intersection of those candidates. Otherwise, the type inferred for `V` is `never`.
- Then, given a type `T''` that is an instantiation of `T` where all `infer` type variables are replaced with the types inferred in the previous step, if `T''` is _definitely assignable_ to `U`, the conditional type is resolved to `X`. The definitely assignable relation is the same as the regular assignable relation, except that type variable constraints are not considered. Intuitively, when a type is definitely assignable to another type, we know that it will be assignable for _all instantiations_ of those types.
- Otherwise, the condition depends on one or more type variables and the conditional type is deferred.

##### Example

```ts
type TypeName<T> = T extends string
  ? "string"
  : T extends number
  ? "number"
  : T extends boolean
  ? "boolean"
  : T extends undefined
  ? "undefined"
  : T extends Function
  ? "function"
  : "object";

type T0 = TypeName<string>; // "string"
type T1 = TypeName<"a">; // "string"
type T2 = TypeName<true>; // "boolean"
type T3 = TypeName<() => void>; // "function"
type T4 = TypeName<string[]>; // "object"
```

## Distributive conditional types

Conditional types in which the checked type is a naked type parameter are called _distributive conditional types_.
Distributive conditional types are automatically distributed over union types during instantiation.
For example, an instantiation of `T extends U ? X : Y` with the type argument `A | B | C` for `T` is resolved as `(A extends U ? X : Y) | (B extends U ? X : Y) | (C extends U ? X : Y)`.

##### Example

```ts
type T10 = TypeName<string | (() => void)>; // "string" | "function"
type T12 = TypeName<string | string[] | undefined>; // "string" | "object" | "undefined"
type T11 = TypeName<string[] | number[]>; // "object"
```

In instantiations of a distributive conditional type `T extends U ? X : Y`, references to `T` within the conditional type are resolved to individual constituents of the union type (i.e. `T` refers to the individual constituents _after_ the conditional type is distributed over the union type).
Furthermore, references to `T` within `X` have an additional type parameter constraint `U` (i.e. `T` is considered assignable to `U` within `X`).

##### Example

```ts
type BoxedValue<T> = { value: T };
type BoxedArray<T> = { array: T[] };
type Boxed<T> = T extends any[] ? BoxedArray<T[number]> : BoxedValue<T>;

type T20 = Boxed<string>; // BoxedValue<string>;
type T21 = Boxed<number[]>; // BoxedArray<number>;
type T22 = Boxed<string | number[]>; // BoxedValue<string> | BoxedArray<number>;
```

Notice that `T` has the additional constraint `any[]` within the true branch of `Boxed<T>` and it is therefore possible to refer to the element type of the array as `T[number]`. Also, notice how the conditional type is distributed over the union type in the last example.

The distributive property of conditional types can conveniently be used to _filter_ union types:

```ts
type Diff<T, U> = T extends U ? never : T; // Remove types from T that are assignable to U
type Filter<T, U> = T extends U ? T : never; // Remove types from T that are not assignable to U

type T30 = Diff<"a" | "b" | "c" | "d", "a" | "c" | "f">; // "b" | "d"
type T31 = Filter<"a" | "b" | "c" | "d", "a" | "c" | "f">; // "a" | "c"
type T32 = Diff<string | number | (() => void), Function>; // string | number
type T33 = Filter<string | number | (() => void), Function>; // () => void

type NonNullable<T> = Diff<T, null | undefined>; // Remove null and undefined from T

type T34 = NonNullable<string | number | undefined>; // string | number
type T35 = NonNullable<string | string[] | null | undefined>; // string | string[]

function f1<T>(x: T, y: NonNullable<T>) {
  x = y; // Ok
  y = x; // Error
}

function f2<T extends string | undefined>(x: T, y: NonNullable<T>) {
  x = y; // Ok
  y = x; // Error
  let s1: string = x; // Error
  let s2: string = y; // Ok
}
```

Conditional types are particularly useful when combined with mapped types:

```ts
type FunctionPropertyNames<T> = {
  [K in keyof T]: T[K] extends Function ? K : never;
}[keyof T];
type FunctionProperties<T> = Pick<T, FunctionPropertyNames<T>>;

type NonFunctionPropertyNames<T> = {
  [K in keyof T]: T[K] extends Function ? never : K;
}[keyof T];
type NonFunctionProperties<T> = Pick<T, NonFunctionPropertyNames<T>>;

interface Part {
  id: number;
  name: string;
  subparts: Part[];
  updatePart(newName: string): void;
}

type T40 = FunctionPropertyNames<Part>; // "updatePart"
type T41 = NonFunctionPropertyNames<Part>; // "id" | "name" | "subparts"
type T42 = FunctionProperties<Part>; // { updatePart(newName: string): void }
type T43 = NonFunctionProperties<Part>; // { id: number, name: string, subparts: Part[] }
```

Similar to union and intersection types, conditional types are not permitted to reference themselves recursively.
For example the following is an error.

##### Example

```ts
type ElementType<T> = T extends any[] ? ElementType<T[number]> : T; // Error
```

## Type inference in conditional types

Within the `extends` clause of a conditional type, it is now possible to have `infer` declarations that introduce a type variable to be inferred.
Such inferred type variables may be referenced in the true branch of the conditional type.
It is possible to have multiple `infer` locations for the same type variable.

For example, the following extracts the return type of a function type:

```ts
type ReturnType<T> = T extends (...args: any[]) => infer R ? R : any;
```

Conditional types can be nested to form a sequence of pattern matches that are evaluated in order:

```ts
type Unpacked<T> = T extends (infer U)[]
  ? U
  : T extends (...args: any[]) => infer U
  ? U
  : T extends Promise<infer U>
  ? U
  : T;

type T0 = Unpacked<string>; // string
type T1 = Unpacked<string[]>; // string
type T2 = Unpacked<() => string>; // string
type T3 = Unpacked<Promise<string>>; // string
type T4 = Unpacked<Promise<string>[]>; // Promise<string>
type T5 = Unpacked<Unpacked<Promise<string>[]>>; // string
```

The following example demonstrates how multiple candidates for the same type variable in co-variant positions causes a union type to be inferred:

```ts
type Foo<T> = T extends { a: infer U; b: infer U } ? U : never;
type T10 = Foo<{ a: string; b: string }>; // string
type T11 = Foo<{ a: string; b: number }>; // string | number
```

Likewise, multiple candidates for the same type variable in contra-variant positions causes an intersection type to be inferred:

```ts
type Bar<T> = T extends { a: (x: infer U) => void; b: (x: infer U) => void }
  ? U
  : never;
type T20 = Bar<{ a: (x: string) => void; b: (x: string) => void }>; // string
type T21 = Bar<{ a: (x: string) => void; b: (x: number) => void }>; // string & number
```

When inferring from a type with multiple call signatures (such as the type of an overloaded function), inferences are made from the _last_ signature (which, presumably, is the most permissive catch-all case).
It is not possible to perform overload resolution based on a list of argument types.

```ts
declare function foo(x: string): number;
declare function foo(x: number): string;
declare function foo(x: string | number): string | number;
type T30 = ReturnType<typeof foo>; // string | number
```

It is not possible to use `infer` declarations in constraint clauses for regular type parameters:

```ts
type ReturnType<T extends (...args: any[]) => infer R> = R; // Error, not supported
```

However, much the same effect can be obtained by erasing the type variables in the constraint and instead specifying a conditional type:

```ts
type AnyFunction = (...args: any[]) => any;
type ReturnType<T extends AnyFunction> = T extends (...args: any[]) => infer R
  ? R
  : any;
```

## Predefined conditional types

TypeScript 2.8 adds several predefined conditional types to `lib.d.ts`:

- `Exclude<T, U>` -- Exclude from `T` those types that are assignable to `U`.
- `Extract<T, U>` -- Extract from `T` those types that are assignable to `U`.
- `NonNullable<T>` -- Exclude `null` and `undefined` from `T`.
- `ReturnType<T>` -- Obtain the return type of a function type.
- `InstanceType<T>` -- Obtain the instance type of a constructor function type.

##### Example

```ts
type T00 = Exclude<"a" | "b" | "c" | "d", "a" | "c" | "f">; // "b" | "d"
type T01 = Extract<"a" | "b" | "c" | "d", "a" | "c" | "f">; // "a" | "c"

type T02 = Exclude<string | number | (() => void), Function>; // string | number
type T03 = Extract<string | number | (() => void), Function>; // () => void

type T04 = NonNullable<string | number | undefined>; // string | number
type T05 = NonNullable<(() => string) | string[] | null | undefined>; // (() => string) | string[]

function f1(s: string) {
  return { a: 1, b: s };
}

class C {
  x = 0;
  y = 0;
}

type T10 = ReturnType<() => string>; // string
type T11 = ReturnType<(s: string) => void>; // void
type T12 = ReturnType<<T>() => T>; // {}
type T13 = ReturnType<<T extends U, U extends number[]>() => T>; // number[]
type T14 = ReturnType<typeof f1>; // { a: number, b: string }
type T15 = ReturnType<any>; // any
type T16 = ReturnType<never>; // any
type T17 = ReturnType<string>; // Error
type T18 = ReturnType<Function>; // Error

type T20 = InstanceType<typeof C>; // C
type T21 = InstanceType<any>; // any
type T22 = InstanceType<never>; // any
type T23 = InstanceType<string>; // Error
type T24 = InstanceType<Function>; // Error
```

> Note: The `Exclude` type is a proper implementation of the `Diff` type suggested [here](https://github.com/Microsoft/TypeScript/issues/12215#issuecomment-307871458). We've used the name `Exclude` to avoid breaking existing code that defines a `Diff`, plus we feel that name better conveys the semantics of the type. We did not include the `Omit<T, K>` type because it is trivially written as `Pick<T, Exclude<keyof T, K>>`.

## Improved control over mapped type modifiers

Mapped types support adding a `readonly` or `?` modifier to a mapped property, but they did not provide support for the ability to _remove_ modifiers.
This matters in [_homomorphic mapped types_](https://github.com/Microsoft/TypeScript/pull/12563) which by default preserve the modifiers of the underlying type.

TypeScript 2.8 adds the ability for a mapped type to either add or remove a particular modifier.
Specifically, a `readonly` or `?` property modifier in a mapped type can now be prefixed with either `+` or `-` to indicate that the modifier should be added or removed.

#### Example

```ts
type MutableRequired<T> = { -readonly [P in keyof T]-?: T[P] }; // Remove readonly and ?
type ReadonlyPartial<T> = { +readonly [P in keyof T]+?: T[P] }; // Add readonly and ?
```

A modifier with no `+` or `-` prefix is the same as a modifier with a `+` prefix. So, the `ReadonlyPartial<T>` type above corresponds to

```ts
type ReadonlyPartial<T> = { readonly [P in keyof T]?: T[P] }; // Add readonly and ?
```

Using this ability, `lib.d.ts` now has a new `Required<T>` type.
This type strips `?` modifiers from all properties of `T`, thus making all properties required.

##### Example

```ts
type Required<T> = { [P in keyof T]-?: T[P] };
```

Note that in [`strictNullChecks`](/tsconfig#strictNullChecks) mode, when a homomorphic mapped type removes a `?` modifier from a property in the underlying type it also removes `undefined` from the type of that property:

##### Example

```ts
type Foo = { a?: string }; // Same as { a?: string | undefined }
type Bar = Required<Foo>; // Same as { a: string }
```

## Improved `keyof` with intersection types

With TypeScript 2.8 `keyof` applied to an intersection type is transformed to a union of `keyof` applied to each intersection constituent.
In other words, types of the form `keyof (A & B)` are transformed to be `keyof A | keyof B`.
This change should address inconsistencies with inference from `keyof` expressions.

##### Example

```ts
type A = { a: string };
type B = { b: string };

type T1 = keyof (A & B); // "a" | "b"
type T2<T> = keyof (T & B); // keyof T | "b"
type T3<U> = keyof (A & U); // "a" | keyof U
type T4<T, U> = keyof (T & U); // keyof T | keyof U
type T5 = T2<A>; // "a" | "b"
type T6 = T3<B>; // "a" | "b"
type T7 = T4<A, B>; // "a" | "b"
```

## Better handling for namespace patterns in `.js` files

TypeScript 2.8 adds support for understanding more namespace patterns in `.js` files.
Empty object literals declarations on top level, just like functions and classes, are now recognized as namespace declarations in JavaScript.

```js
var ns = {}; // recognized as a declaration for a namespace `ns`
ns.constant = 1; // recognized as a declaration for var `constant`
```

Assignments at the top-level should behave the same way; in other words, a `var` or `const` declaration is not required.

```js
app = {}; // does NOT need to be `var app = {}`
app.C = class {};
app.f = function() {};
app.prop = 1;
```

## IIFEs as namespace declarations

An IIFE returning a function, class or empty object literal, is also recognized as a namespace:

```js
var C = (function() {
  function C(n) {
    this.p = n;
  }
  return C;
})();
C.staticProperty = 1;
```

## Defaulted declarations

"Defaulted declarations" allow initializers that reference the declared name in the left side of a logical or:

```js
my = window.my || {};
my.app = my.app || {};
```

## Prototype assignment

You can assign an object literal directly to the prototype property. Individual prototype assignments still work too:

```ts
var C = function(p) {
  this.p = p;
};
C.prototype = {
  m() {
    console.log(this.p);
  }
};
C.prototype.q = function(r) {
  return this.p === r;
};
```

## Nested and merged declarations

Nesting works to any level now, and merges correctly across files. Previously neither was the case.

```js
var app = window.app || {};
app.C = class {};
```

## Per-file JSX factories

TypeScript 2.8 adds support for a per-file configurable JSX factory name using `@jsx dom` pragma.
JSX factory can be configured for a compilation using [`jsxFactory`](/tsconfig#jsxFactory) (default is `React.createElement`). With TypeScript 2.8 you can override this on a per-file-basis by adding a comment to the beginning of the file.

##### Example

```ts
/** @jsx dom */
import { dom } from "./renderer";
<h></h>;
```

Generates:

```js
var renderer_1 = require("./renderer");
renderer_1.dom("h", null);
```

## Locally scoped JSX namespaces

JSX type checking is driven by definitions in a JSX namespace, for instance `JSX.Element` for the type of a JSX element, and `JSX.IntrinsicElements` for built-in elements.
Before TypeScript 2.8 the `JSX` namespace was expected to be in the global namespace, and thus only allowing one to be defined in a project.
Starting with TypeScript 2.8 the `JSX` namespace will be looked under the `jsxNamespace` (e.g. `React`) allowing for multiple jsx factories in one compilation.
For backward compatibility the global `JSX` namespace is used as a fallback if none was defined on the factory function.
Combined with the per-file `@jsx` pragma, each file can have a different JSX factory.

## New `--emitDeclarationOnly`

[`emitDeclarationOnly`](/tsconfig#emitDeclarationOnly) allows for _only_ generating declaration files; `.js`/`.jsx` output generation will be skipped with this flag. The flag is useful when the `.js` output generation is handled by a different transpiler like Babel.

---

## Source: `packages/documentation/copy/en/release-notes/TypeScript 2.9.md`

---
title: TypeScript 2.9
layout: docs
permalink: /docs/handbook/release-notes/typescript-2-9.html
oneline: TypeScript 2.9 Release Notes
---

## Support `number` and `symbol` named properties with `keyof` and mapped types

TypeScript 2.9 adds support for `number` and `symbol` named properties in index types and mapped types.
Previously, the `keyof` operator and mapped types only supported `string` named properties.

Changes include:

- An index type `keyof T` for some type `T` is a subtype of `string | number | symbol`.
- A mapped type `{ [P in K]: XXX }` permits any `K` assignable to `string | number | symbol`.
- In a `for...in` statement for an object of a generic type `T`, the inferred type of the iteration variable was previously `keyof T` but is now `Extract<keyof T, string>`. (In other words, the subset of `keyof T` that includes only string-like values.)

Given an object type `X`, `keyof X` is resolved as follows:

- If `X` contains a string index signature, `keyof X` is a union of `string`, `number`, and the literal types representing symbol-like properties, otherwise
- If `X` contains a numeric index signature, `keyof X` is a union of `number` and the literal types representing string-like and symbol-like properties, otherwise
- `keyof X` is a union of the literal types representing string-like, number-like, and symbol-like properties.

Where:

- String-like properties of an object type are those declared using an identifier, a string literal, or a computed property name of a string literal type.
- Number-like properties of an object type are those declared using a numeric literal or computed property name of a numeric literal type.
- Symbol-like properties of an object type are those declared using a computed property name of a unique symbol type.

In a mapped type `{ [P in K]: XXX }`, each string literal type in `K` introduces a property with a string name, each numeric literal type in `K` introduces a property with a numeric name, and each unique symbol type in `K` introduces a property with a unique symbol name.
Furthermore, if `K` includes type `string`, a string index signature is introduced, and if `K` includes type `number`, a numeric index signature is introduced.

##### Example

```ts
const c = "c";
const d = 10;
const e = Symbol();

const enum E1 {
  A,
  B,
  C,
}
const enum E2 {
  A = "A",
  B = "B",
  C = "C",
}

type Foo = {
  a: string; // String-like name
  5: string; // Number-like name
  [c]: string; // String-like name
  [d]: string; // Number-like name
  [e]: string; // Symbol-like name
  [E1.A]: string; // Number-like name
  [E2.A]: string; // String-like name
};

type K1 = keyof Foo; // "a" | 5 | "c" | 10 | typeof e | E1.A | E2.A
type K2 = Extract<keyof Foo, string>; // "a" | "c" | E2.A
type K3 = Extract<keyof Foo, number>; // 5 | 10 | E1.A
type K4 = Extract<keyof Foo, symbol>; // typeof e
```

Since `keyof` now reflects the presence of a numeric index signature by including type `number` in the key type, mapped types such as `Partial<T>` and `Readonly<T>` work correctly when applied to object types with numeric index signatures:

```ts
type Arrayish<T> = {
  length: number;
  [x: number]: T;
};

type ReadonlyArrayish<T> = Readonly<Arrayish<T>>;

declare const map: ReadonlyArrayish<string>;
let n = map.length;
let x = map[123]; // Previously of type any (or an error with --noImplicitAny)
```

Furthermore, with the `keyof` operator's support for `number` and `symbol` named keys, it is now possible to abstract over access to properties of objects that are indexed by numeric literals (such as numeric enum types) and unique symbols.

```ts
const enum Enum {
  A,
  B,
  C,
}

const enumToStringMap = {
  [Enum.A]: "Name A",
  [Enum.B]: "Name B",
  [Enum.C]: "Name C",
};

const sym1 = Symbol();
const sym2 = Symbol();
const sym3 = Symbol();

const symbolToNumberMap = {
  [sym1]: 1,
  [sym2]: 2,
  [sym3]: 3,
};

type KE = keyof typeof enumToStringMap; // Enum (i.e. Enum.A | Enum.B | Enum.C)
type KS = keyof typeof symbolToNumberMap; // typeof sym1 | typeof sym2 | typeof sym3

function getValue<T, K extends keyof T>(obj: T, key: K): T[K] {
  return obj[key];
}

let x1 = getValue(enumToStringMap, Enum.C); // Returns "Name C"
let x2 = getValue(symbolToNumberMap, sym3); // Returns 3
```

This is a breaking change; previously, the `keyof` operator and mapped types only supported `string` named properties.
Code that assumed values typed with `keyof T` were always `string`s, will now be flagged as error.

##### Example

```ts
function useKey<T, K extends keyof T>(o: T, k: K) {
  var name: string = k; // Error: keyof T is not assignable to string
}
```

#### Recommendations

- If your functions are only able to handle string named property keys, use `Extract<keyof T, string>` in the declaration:

  ```ts
  function useKey<T, K extends Extract<keyof T, string>>(o: T, k: K) {
    var name: string = k; // OK
  }
  ```

- If your functions are open to handling all property keys, then the changes should be done down-stream:

  ```ts
  function useKey<T, K extends keyof T>(o: T, k: K) {
    var name: string | number | symbol = k;
  }
  ```

- Otherwise use [`keyofStringsOnly`](/tsconfig#keyofStringsOnly) compiler option to disable the new behavior.

## Generic type arguments in JSX elements

JSX elements now allow passing type arguments to generic components.

##### Example

```ts
class GenericComponent<P> extends React.Component<P> {
  internalProp: P;
}

type Props = { a: number; b: string };

const x = <GenericComponent<Props> a={10} b="hi" />; // OK

const y = <GenericComponent<Props> a={10} b={20} />; // Error
```

## Generic type arguments in generic tagged templates

Tagged templates are a form of invocation introduced in ECMAScript 2015.
Like call expressions, generic functions may be used in a tagged template and TypeScript will infer the type arguments utilized.

TypeScript 2.9 allows passing generic type arguments to tagged template strings.

##### Example

```ts
declare function styledComponent<Props>(
  strs: TemplateStringsArray
): Component<Props>;

interface MyProps {
  name: string;
  age: number;
}

styledComponent<MyProps>`
  font-size: 1.5em;
  text-align: center;
  color: palevioletred;
`;

declare function tag<T>(strs: TemplateStringsArray, ...args: T[]): T;

// inference fails because 'number' and 'string' are both candidates that conflict
let a = tag<string | number>`${100} ${"hello"}`;
```

## `import` types

Modules can import types declared in other modules. But non-module global scripts cannot access types declared in modules. Enter `import` types.

Using `import("mod")` in a type annotation allows for reaching in a module and accessing its exported declaration without importing it.

##### Example

Given a declaration of a class `Pet` in a module file:

```ts
// module.d.ts

export declare class Pet {
  name: string;
}
```

Can be used in a non-module file `global-script.ts`:

```ts
// global-script.ts

function adopt(p: import("./module").Pet) {
  console.log(`Adopting ${p.name}...`);
}
```

This also works in JSDoc comments to refer to types from other modules in `.js`:

```js
// a.js

/**
 * @param p { import("./module").Pet }
 */
function walk(p) {
  console.log(`Walking ${p.name}...`);
}
```

## Relaxing declaration emit visibility rules

With `import` types available, many of the visibility errors reported during declaration file generation can be handled by the compiler without the need to change the input.

For instance:

```ts
import { createHash } from "crypto";

export const hash = createHash("sha256");
//           ^^^^
// Exported variable 'hash' has or is using name 'Hash' from external module "crypto" but cannot be named.
```

With TypeScript 2.9, no errors are reported, and now the generated file looks like:

```ts
export declare const hash: import("crypto").Hash;
```

## Support for `import.meta`

TypeScript 2.9 introduces support for `import.meta`, a new meta-property as described by the current [TC39 proposal](https://github.com/tc39/proposal-import-meta).

The type of `import.meta` is the global `ImportMeta` type which is defined in `lib.es5.d.ts`.
This interface is extremely limited.
Adding well-known properties for Node or browsers requires interface merging and possibly a global augmentation depending on the context.

##### Example

Assuming that `__dirname` is always available on `import.meta`, the declaration would be done through reopening `ImportMeta` interface:

```ts
// node.d.ts
interface ImportMeta {
  __dirname: string;
}
```

And usage would be:

```ts
import.meta.__dirname; // Has type 'string'
```

`import.meta` is only allowed when targeting `ESNext` modules and ECMAScript targets.

## New `--resolveJsonModule`

Often in Node.js applications a `.json` is needed. With TypeScript 2.9, [`resolveJsonModule`](/tsconfig#resolveJsonModule) allows for importing, extracting types from and generating `.json` files.

##### Example

```ts
// settings.json

{
    "repo": "TypeScript",
    "dry": false,
    "debug": false
}
```

```ts
// a.ts

import settings from "./settings.json";

settings.debug === true; // OK
settings.dry === 2; // Error: Operator '===' cannot be applied boolean and number
```

```json tsconfig
// tsconfig.json

{
  "compilerOptions": {
    "module": "commonjs",
    "resolveJsonModule": true,
    "esModuleInterop": true
  }
}
```

## `--pretty` output by default

Starting TypeScript 2.9 errors are displayed under [`pretty`](/tsconfig#pretty) by default if the output device is applicable for colorful text.
TypeScript will check if the output stream has [`isTty`](https://nodejs.org/api/tty.html) property set.

Use `--pretty false` on the command line or set `"pretty": false` in your `tsconfig.json` to disable [`pretty`](/tsconfig#pretty) output.

## New `--declarationMap`

Enabling [`declarationMap`](/tsconfig#declarationMap) alongside [`declaration`](/tsconfig#declaration) causes the compiler to emit `.d.ts.map` files alongside the output `.d.ts` files.
Language Services can also now understand these map files, and uses them to map declaration-file based definition locations to their original source, when available.

In other words, hitting go-to-definition on a declaration from a `.d.ts` file generated with [`declarationMap`](/tsconfig#declarationMap) will take you to the source file (`.ts`) location where that declaration was defined, and not to the `.d.ts`.

---

## Source: `packages/documentation/copy/en/release-notes/TypeScript 3.0.md`

---
title: TypeScript 3.0
layout: docs
permalink: /docs/handbook/release-notes/typescript-3-0.html
oneline: TypeScript 3.0 Release Notes
---

## Project References

TypeScript 3.0 introduces a new concept of project references. Project references allow TypeScript projects to depend on other TypeScript projects - specifically, allowing `tsconfig.json` files to reference other `tsconfig.json` files. Specifying these dependencies makes it easier to split your code into smaller projects, since it gives TypeScript (and tools around it) a way to understand build ordering and output structure.

TypeScript 3.0 also introduces a new mode for tsc, the `--build` flag, that works hand-in-hand with project references to enable faster TypeScript builds.

See [Project References handbook page](/docs/handbook/project-references.html) for more documentation.

## Tuples in rest parameters and spread expressions

TypeScript 3.0 adds support to multiple new capabilities to interact with function parameter lists as tuple types.
TypeScript 3.0 adds support for:

- [Expansion of rest parameters with tuple types into discrete parameters.](#rest-parameters-with-tuple-types)
- [Expansion of spread expressions with tuple types into discrete arguments.](#spread-expressions-with-tuple-types)
- [Generic rest parameters and corresponding inference of tuple types.](#generic-rest-parameters)
- [Optional elements in tuple types.](#optional-elements-in-tuple-types)
- [Rest elements in tuple types.](#rest-elements-in-tuple-types)

With these features it becomes possible to strongly type a number of higher-order functions that transform functions and their parameter lists.

## Rest parameters with tuple types

When a rest parameter has a tuple type, the tuple type is expanded into a sequence of discrete parameters.
For example the following two declarations are equivalent:

```ts
declare function foo(...args: [number, string, boolean]): void;
```

```ts
declare function foo(args_0: number, args_1: string, args_2: boolean): void;
```

## Spread expressions with tuple types

When a function call includes a spread expression of a tuple type as the last argument, the spread expression corresponds to a sequence of discrete arguments of the tuple element types.

Thus, the following calls are equivalent:

```ts
const args: [number, string, boolean] = [42, "hello", true];
foo(42, "hello", true);
foo(args[0], args[1], args[2]);
foo(...args);
```

## Generic rest parameters

A rest parameter is permitted to have a generic type that is constrained to an array type, and type inference can infer tuple types for such generic rest parameters. This enables higher-order capturing and spreading of partial parameter lists:

##### Example

```ts
declare function bind<T, U extends any[], V>(
  f: (x: T, ...args: U) => V,
  x: T
): (...args: U) => V;

declare function f3(x: number, y: string, z: boolean): void;

const f2 = bind(f3, 42); // (y: string, z: boolean) => void
const f1 = bind(f2, "hello"); // (z: boolean) => void
const f0 = bind(f1, true); // () => void

f3(42, "hello", true);
f2("hello", true);
f1(true);
f0();
```

In the declaration of `f2` above, type inference infers types `number`, `[string, boolean]` and `void` for `T`, `U` and `V` respectively.

Note that when a tuple type is inferred from a sequence of parameters and later expanded into a parameter list, as is the case for `U`, the original parameter names are used in the expansion (however, the names have no semantic meaning and are not otherwise observable).

## Optional elements in tuple types

Tuple types now permit a `?` postfix on element types to indicate that the element is optional:

##### Example

```ts
let t: [number, string?, boolean?];
t = [42, "hello", true];
t = [42, "hello"];
t = [42];
```

In [`strictNullChecks`](/tsconfig#strictNullChecks) mode, a `?` modifier automatically includes `undefined` in the element type, similar to optional parameters.

A tuple type permits an element to be omitted if it has a postfix `?` modifier on its type and all elements to the right of it also have `?` modifiers.

When tuple types are inferred for rest parameters, optional parameters in the source become optional tuple elements in the inferred type.

The `length` property of a tuple type with optional elements is a union of numeric literal types representing the possible lengths.
For example, the type of the `length` property in the tuple type `[number, string?, boolean?]` is `1 | 2 | 3`.

### Rest elements in tuple types

The last element of a tuple type can be a rest element of the form `...X`, where `X` is an array type.
A rest element indicates that the tuple type is open-ended and may have zero or more additional elements of the array element type.
For example, `[number, ...string[]]` means tuples with a `number` element followed by any number of `string` elements.

##### Example

```ts
function tuple<T extends any[]>(...args: T): T {
  return args;
}

const numbers: number[] = getArrayOfNumbers();
const t1 = tuple("foo", 1, true); // [string, number, boolean]
const t2 = tuple("bar", ...numbers); // [string, ...number[]]
```

The type of the `length` property of a tuple type with a rest element is `number`.

## New `unknown` top type

TypeScript 3.0 introduces a new top type `unknown`.
`unknown` is the type-safe counterpart of `any`.
Anything is assignable to `unknown`, but `unknown` isn't assignable to anything but itself and `any` without a type assertion or a control flow based narrowing.
Likewise, no operations are permitted on an `unknown` without first asserting or narrowing to a more specific type.

##### Example

```ts
// In an intersection everything absorbs unknown

type T00 = unknown & null; // null
type T01 = unknown & undefined; // undefined
type T02 = unknown & null & undefined; // null & undefined (which becomes never)
type T03 = unknown & string; // string
type T04 = unknown & string[]; // string[]
type T05 = unknown & unknown; // unknown
type T06 = unknown & any; // any

// In a union an unknown absorbs everything

type T10 = unknown | null; // unknown
type T11 = unknown | undefined; // unknown
type T12 = unknown | null | undefined; // unknown
type T13 = unknown | string; // unknown
type T14 = unknown | string[]; // unknown
type T15 = unknown | unknown; // unknown
type T16 = unknown | any; // any

// Type variable and unknown in union and intersection

type T20<T> = T & {}; // T & {}
type T21<T> = T | {}; // T | {}
type T22<T> = T & unknown; // T
type T23<T> = T | unknown; // unknown

// unknown in conditional types

type T30<T> = unknown extends T ? true : false; // Deferred
type T31<T> = T extends unknown ? true : false; // Deferred (so it distributes)
type T32<T> = never extends T ? true : false; // true
type T33<T> = T extends never ? true : false; // Deferred

// keyof unknown

type T40 = keyof any; // string | number | symbol
type T41 = keyof unknown; // never

// Only equality operators are allowed with unknown

function f10(x: unknown) {
  x == 5;
  x !== 10;
  x >= 0; // Error
  x + 1; // Error
  x * 2; // Error
  -x; // Error
  +x; // Error
}

// No property accesses, element accesses, or function calls

function f11(x: unknown) {
  x.foo; // Error
  x[5]; // Error
  x(); // Error
  new x(); // Error
}

// typeof, instanceof, and user defined type predicates

declare function isFunction(x: unknown): x is Function;

function f20(x: unknown) {
  if (typeof x === "string" || typeof x === "number") {
    x; // string | number
  }
  if (x instanceof Error) {
    x; // Error
  }
  if (isFunction(x)) {
    x; // Function
  }
}

// Homomorphic mapped type over unknown

type T50<T> = { [P in keyof T]: number };
type T51 = T50<any>; // { [x: string]: number }
type T52 = T50<unknown>; // {}

// Anything is assignable to unknown

function f21<T>(pAny: any, pNever: never, pT: T) {
  let x: unknown;
  x = 123;
  x = "hello";
  x = [1, 2, 3];
  x = new Error();
  x = x;
  x = pAny;
  x = pNever;
  x = pT;
}

// unknown assignable only to itself and any

function f22(x: unknown) {
  let v1: any = x;
  let v2: unknown = x;
  let v3: object = x; // Error
  let v4: string = x; // Error
  let v5: string[] = x; // Error
  let v6: {} = x; // Error
  let v7: {} | null | undefined = x; // Error
}

// Type parameter 'T extends unknown' not related to object

function f23<T extends unknown>(x: T) {
  let y: object = x; // Error
}

// Anything but primitive assignable to { [x: string]: unknown }

function f24(x: { [x: string]: unknown }) {
  x = {};
  x = { a: 5 };
  x = [1, 2, 3];
  x = 123; // Error
}

// Locals of type unknown always considered initialized

function f25() {
  let x: unknown;
  let y = x;
}

// Spread of unknown causes result to be unknown

function f26(x: {}, y: unknown, z: any) {
  let o1 = { a: 42, ...x }; // { a: number }
  let o2 = { a: 42, ...x, ...y }; // unknown
  let o3 = { a: 42, ...x, ...y, ...z }; // any
}

// Functions with unknown return type don't need return expressions

function f27(): unknown {}

// Rest type cannot be created from unknown

function f28(x: unknown) {
  let { ...a } = x; // Error
}

// Class properties of type unknown don't need definite assignment

class C1 {
  a: string; // Error
  b: unknown;
  c: any;
}
```

## Support for `defaultProps` in JSX

TypeScript 2.9 and earlier didn’t leverage [React `defaultProps`](https://reactjs.org/docs/typechecking-with-proptypes.html#default-prop-values) declarations inside JSX components.
Users would often have to declare properties optional and use non-null assertions inside of `render`, or they'd use type-assertions to fix up the type of the component before exporting it.

TypeScript 3.0 adds support for a new type alias in the `JSX` namespace called `LibraryManagedAttributes`.
This helper type defines a transformation on the component's `Props` type, before using to check a JSX expression targeting it; thus allowing customization like: how conflicts between provided props and inferred props are handled, how inferences are mapped, how optionality is handled, and how inferences from differing places should be combined.

In short using this general type, we can model React's specific behavior for things like `defaultProps` and, to some extent, `propTypes`.

```tsx
export interface Props {
  name: string;
}

export class Greet extends React.Component<Props> {
  render() {
    const { name } = this.props;
    return <div>Hello {name.toUpperCase()}!</div>;
  }
  static defaultProps = { name: "world" };
}

// Type-checks! No type assertions needed!
let el = <Greet />;
```

## Caveats

### Explicit types on `defaultProps`

The default-ed properties are inferred from the `defaultProps` property type. If an explicit type annotation is added, e.g. `static defaultProps: Partial<Props>;` the compiler will not be able to identify which properties have defaults (since the type of `defaultProps` include all properties of `Props`).

Use `static defaultProps: Pick<Props, "name">;` as an explicit type annotation instead, or do not add a type annotation as done in the example above.

For function components (formerly known as SFCs) use ES2015 default initializers:

```tsx
function Greet({ name = "world" }: Props) {
  return <div>Hello {name.toUpperCase()}!</div>;
}
```

#### Changes to `@types/React`

Corresponding changes to add `LibraryManagedAttributes` definition to the `JSX` namespace in `@types/React` are still needed.
Keep in mind that there are some limitations.

## `/// <reference lib="..." />` reference directives

TypeScript adds a new triple-slash-reference directive (`/// <reference lib="name" />`), allowing a file to explicitly include an existing built-in _lib_ file.

Built-in _lib_ files are referenced in the same fashion as the [`lib`](/tsconfig#lib) compiler option in _tsconfig.json_ (e.g. use `lib="es2015"` and not `lib="lib.es2015.d.ts"`, etc.).

For declaration file authors who rely on built-in types, e.g. DOM APIs or built-in JS run-time constructors like `Symbol` or `Iterable`, triple-slash-reference lib directives are recommended. Previously these .d.ts files had to add forward/duplicate declarations of such types.

##### Example

Using `/// <reference lib="es2017.string" />` to one of the files in a compilation is equivalent to compiling with `--lib es2017.string`.

```ts
/// <reference lib="es2017.string" />

"foo".padStart(4);
```

---

## Source: `packages/documentation/copy/en/release-notes/TypeScript 3.1.md`

---
title: TypeScript 3.1
layout: docs
permalink: /docs/handbook/release-notes/typescript-3-1.html
oneline: TypeScript 3.1 Release Notes
---

## Mapped types on tuples and arrays

In TypeScript 3.1, mapped object types<sup>[[1]](#ts-3-1-only-homomorphic)</sup> over tuples and arrays now produce new tuples/arrays, rather than creating a new type where members like `push()`, `pop()`, and `length` are converted.
For example:

```ts
type MapToPromise<T> = { [K in keyof T]: Promise<T[K]> };

type Coordinate = [number, number];

type PromiseCoordinate = MapToPromise<Coordinate>; // [Promise<number>, Promise<number>]
```

`MapToPromise` takes a type `T`, and when that type is a tuple like `Coordinate`, only the numeric properties are converted.
In `[number, number]`, there are two numerically named properties: `0` and `1`.
When given a tuple like that, `MapToPromise` will create a new tuple where the `0` and `1` properties are `Promise`s of the original type.
So the resulting type `PromiseCoordinate` ends up with the type `[Promise<number>, Promise<number>]`.

## Properties declarations on functions

TypeScript 3.1 brings the ability to define properties on function declarations and `const`-declared functions, simply by assigning to properties on these functions in the same scope.
This allows us to write canonical JavaScript code without resorting to `namespace` hacks.
For example:

```ts
function readImage(path: string, callback: (err: any, image: Image) => void) {
  // ...
}

readImage.sync = (path: string) => {
  const contents = fs.readFileSync(path);
  return decodeImageSync(contents);
};
```

Here, we have a function `readImage` which reads an image in a non-blocking asynchronous way.
In addition to `readImage`, we've provided a convenience function on `readImage` itself called `readImage.sync`.

While ECMAScript exports are often a better way of providing this functionality, this new support allows code written in this style to "just work" in TypeScript.
Additionally, this approach for property declarations allows us to express common patterns like `defaultProps` and `propTypes` on React function components (formerly known as SFCs).

```ts
export const FooComponent = ({ name }) => <div>Hello! I am {name}</div>;

FooComponent.defaultProps = {
  name: "(anonymous)",
};
```

<!--
fs.readFile(path, (err, data) => {
        if (err) callback(err, undefined);
        else decodeImage(data, (err, image) => {
            if (err) callback(err, undefined);
            else callback(undefined, image);
        });
    });
-->

---

<sup id="ts-3-1-only-homomorphic">[1]</sup> More specifically, homomorphic mapped types like in the above form.

## Version selection with `typesVersions`

Feedback from our community, as well as our own experience, has shown us that leveraging the newest TypeScript features while also accommodating users on the older versions are difficult.
TypeScript introduces a new feature called `typesVersions` to help accommodate these scenarios.

You can read [about it in the Publishing section of the declaration files section](https://www.typescriptlang.org/docs/handbook/declaration-files/publishing.html#version-selection-with-typesversions)

---

## Source: `packages/documentation/copy/en/release-notes/TypeScript 3.5.md`

---
title: TypeScript 3.5
layout: docs
permalink: /docs/handbook/release-notes/typescript-3-5.html
oneline: TypeScript 3.5 Release Notes
---

## Speed improvements

TypeScript 3.5 introduces several optimizations around type-checking and incremental builds.

### Type-checking speed-ups

TypeScript 3.5 contains certain optimizations over TypeScript 3.4 for type-checking more efficiently.
These improvements are significantly more pronounced in editor scenarios where type-checking drives operations like code completion lists.

### `--incremental` improvements

TypeScript 3.5 improves on 3.4's [`incremental`](/tsconfig#incremental) build mode, by saving information about how the state of the world was calculated - compiler settings, why files were looked up, where files were found, etc.
In scenarios involving hundreds of projects using TypeScript's project references in `--build` mode, [we've found that the amount of time rebuilding can be reduced by as much as 68% compared to TypeScript 3.4](https://github.com/Microsoft/TypeScript/pull/31101)!

For more details, you can see the pull requests to

- [cache module resolution](https://github.com/Microsoft/TypeScript/pull/31100)
- [cache settings calculated from `tsconfig.json`](https://github.com/Microsoft/TypeScript/pull/31101)

## The `Omit` helper type

TypeScript 3.5 introduces the new `Omit` helper type, which creates a new type with some properties dropped from the original.

```ts
type Person = {
  name: string;
  age: number;
  location: string;
};

type QuantumPerson = Omit<Person, "location">;

// equivalent to
type QuantumPerson = {
  name: string;
  age: number;
};
```

Here we were able to copy over all the properties of `Person` except for `location` using the `Omit` helper.

For more details, [see the pull request on GitHub to add `Omit`](https://github.com/Microsoft/TypeScript/pull/30552), as well as [the change to use `Omit` for object rest](https://github.com/microsoft/TypeScript/pull/31134).

### Improved excess property checks in union types

In TypeScript 3.4 and earlier, certain excess properties were allowed in situations where they really shouldn't have been.
For instance, TypeScript 3.4 permitted the incorrect `name` property in the object literal even though its types don't match between `Point` and `Label`.

```ts
type Point = {
  x: number;
  y: number;
};

type Label = {
  name: string;
};

const thing: Point | Label = {
  x: 0,
  y: 0,
  name: true // uh-oh!
};
```

Previously, a non-discriminated union wouldn't have _any_ excess property checking done on its members, and as a result, the incorrectly typed `name` property slipped by.

In TypeScript 3.5, the type-checker at least verifies that all the provided properties belong to _some_ union member and have the appropriate type, meaning that the sample above correctly issues an error.

Note that partial overlap is still permitted as long as the property types are valid.

```ts
const pl: Point | Label = {
  x: 0,
  y: 0,
  name: "origin" // okay
};
```

## The `--allowUmdGlobalAccess` flag

In TypeScript 3.5, you can now reference UMD global declarations like

```
export as namespace foo;
```

from anywhere - even modules - using the new [`allowUmdGlobalAccess`](/tsconfig#allowUmdGlobalAccess) flag.

This mode adds flexibility for mixing and matching the way 3rd party libraries, where globals that libraries declare can always be consumed, even from within modules.

For more details, [see the pull request on GitHub](https://github.com/Microsoft/TypeScript/pull/30776/files).

## Smarter union type checking

In TypeScript 3.4 and prior, the following example would fail:

```ts
type S = { done: boolean; value: number };
type T = { done: false; value: number } | { done: true; value: number };

declare let source: S;
declare let target: T;

target = source;
```

That's because `S` isn't assignable to `{ done: false, value: number }` nor `{ done: true, value: number }`.
Why?
Because the `done` property in `S` isn't specific enough - it's `boolean` whereas each constituent of `T` has a `done` property that's specifically `true` or `false`.
That's what we meant by each constituent type being checked in isolation: TypeScript doesn't just union each property together and see if `S` is assignable to that.
If it did, some bad code could get through like the following:

```ts
interface Foo {
  kind: "foo";
  value: string;
}

interface Bar {
  kind: "bar";
  value: number;
}

function doSomething(x: Foo | Bar) {
  if (x.kind === "foo") {
    x.value.toLowerCase();
  }
}

// uh-oh - luckily TypeScript errors here!
doSomething({
  kind: "foo",
  value: 123
});
```

However, this was a bit overly strict for the original example.
If you figure out the precise type of any possible value of `S`, you can actually see that it matches the types in `T` exactly.

In TypeScript 3.5, when assigning to types with discriminant properties like in `T`, the language actually _will_ go further and decompose types like `S` into a union of every possible inhabitant type.
In this case, since `boolean` is a union of `true` and `false`, `S` will be viewed as a union of `{ done: false, value: number }` and `{ done: true, value: number }`.

For more details, you can [see the original pull request on GitHub](https://github.com/microsoft/TypeScript/pull/30779).

## Higher order type inference from generic constructors

In TypeScript 3.4, we improved inference for when generic functions that return functions like so:

```ts
function compose<T, U, V>(f: (x: T) => U, g: (y: U) => V): (x: T) => V {
  return x => g(f(x));
}
```

took other generic functions as arguments, like so:

```ts
function arrayify<T>(x: T): T[] {
  return [x];
}

type Box<U> = { value: U };
function boxify<U>(y: U): Box<U> {
  return { value: y };
}

let newFn = compose(arrayify, boxify);
```

Instead of a relatively useless type like `(x: {}) => Box<{}[]>`, which older versions of the language would infer, TypeScript 3.4's inference allows `newFn` to be generic.
Its new type is `<T>(x: T) => Box<T[]>`.

TypeScript 3.5 generalizes this behavior to work on constructor functions as well.

```ts
class Box<T> {
  kind: "box";
  value: T;
  constructor(value: T) {
    this.value = value;
  }
}

class Bag<U> {
  kind: "bag";
  value: U;
  constructor(value: U) {
    this.value = value;
  }
}

function composeCtor<T, U, V>(
  F: new (x: T) => U,
  G: new (y: U) => V
): (x: T) => V {
  return x => new G(new F(x));
}

let f = composeCtor(Box, Bag); // has type '<T>(x: T) => Bag<Box<T>>'
let a = f(1024); // has type 'Bag<Box<number>>'
```

In addition to compositional patterns like the above, this new inference on generic constructors means that functions that operate on class components in certain UI libraries like React can more correctly operate on generic class components.

```ts
type ComponentClass<P> = new (props: P) => Component<P>;
declare class Component<P> {
  props: P;
  constructor(props: P);
}

declare function myHoc<P>(C: ComponentClass<P>): ComponentClass<P>;

type NestedProps<T> = { foo: number; stuff: T };

declare class GenericComponent<T> extends Component<NestedProps<T>> {}

// type is 'new <T>(props: NestedProps<T>) => Component<NestedProps<T>>'
const GenericComponent2 = myHoc(GenericComponent);
```

To learn more, [check out the original pull request on GitHub](https://github.com/microsoft/TypeScript/pull/31116).

---

## Source: `packages/documentation/copy/en/release-notes/TypeScript 3.8.md`

---
title: TypeScript 3.8
layout: docs
permalink: /docs/handbook/release-notes/typescript-3-8.html
oneline: TypeScript 3.8 Release Notes
---

## Type-Only Imports and Export

This feature is something most users may never have to think about; however, if you've hit issues under [`isolatedModules`](/tsconfig#isolatedModules), TypeScript's `transpileModule` API, or Babel, this feature might be relevant.

TypeScript 3.8 adds a new syntax for type-only imports and exports.

```ts
import type { SomeThing } from "./some-module.js";

export type { SomeThing };
```

`import type` only imports declarations to be used for type annotations and declarations.
It _always_ gets fully erased, so there's no remnant of it at runtime.
Similarly, `export type` only provides an export that can be used for type contexts, and is also erased from TypeScript's output.

It's important to note that classes have a value at runtime and a type at design-time, and the use is context-sensitive.
When using `import type` to import a class, you can't do things like extend from it.

```ts
import type { Component } from "react";

interface ButtonProps {
  // ...
}

class Button extends Component<ButtonProps> {
  //               ~~~~~~~~~
  // error! 'Component' only refers to a type, but is being used as a value here.
  // ...
}
```

If you've used Flow before, the syntax is fairly similar.
One difference is that we've added a few restrictions to avoid code that might appear ambiguous.

```ts
// Is only 'Foo' a type? Or every declaration in the import?
// We just give an error because it's not clear.

import type Foo, { Bar, Baz } from "some-module";
//     ~~~~~~~~~~~~~~~~~~~~~~
// error! A type-only import can specify a default import or named bindings, but not both.
```

In conjunction with `import type`, TypeScript 3.8 also adds a new compiler flag to control what happens with imports that won't be utilized at runtime: [`importsNotUsedAsValues`](/tsconfig#importsNotUsedAsValues).
This flag takes 3 different values:

- `remove`: this is today's behavior of dropping these imports. It's going to continue to be the default, and is a non-breaking change.
- `preserve`: this _preserves_ all imports whose values are never used. This can cause imports/side-effects to be preserved.
- `error`: this preserves all imports (the same as the `preserve` option), but will error when a value import is only used as a type. This might be useful if you want to ensure no values are being accidentally imported, but still make side-effect imports explicit.

For more information about the feature, you can [take a look at the pull request](https://github.com/microsoft/TypeScript/pull/35200), and [relevant changes](https://github.com/microsoft/TypeScript/pull/36092/) around broadening where imports from an `import type` declaration can be used.

## ECMAScript Private Fields

TypeScript 3.8 brings support for ECMAScript's private fields, part of the [stage-3 class fields proposal](https://github.com/tc39/proposal-class-fields/).

```ts
class Person {
  #name: string;

  constructor(name: string) {
    this.#name = name;
  }

  greet() {
    console.log(`Hello, my name is ${this.#name}!`);
  }
}

let jeremy = new Person("Jeremy Bearimy");

jeremy.#name;
//     ~~~~~
// Property '#name' is not accessible outside class 'Person'
// because it has a private identifier.
```

Unlike regular properties (even ones declared with the `private` modifier), private fields have a few rules to keep in mind.
Some of them are:

- Private fields start with a `#` character. Sometimes we call these _private names_.
- Every private field name is uniquely scoped to its containing class.
- TypeScript accessibility modifiers like `public` or `private` can't be used on private fields.
- Private fields can't be accessed or even detected outside of the containing class - even by JS users! Sometimes we call this _hard privacy_.

Apart from "hard" privacy, another benefit of private fields is that uniqueness we just mentioned.
For example, regular property declarations are prone to being overwritten in subclasses.

```ts
class C {
  foo = 10;

  cHelper() {
    return this.foo;
  }
}

class D extends C {
  foo = 20;

  dHelper() {
    return this.foo;
  }
}

let instance = new D();
// 'this.foo' refers to the same property on each instance.
console.log(instance.cHelper()); // prints '20'
console.log(instance.dHelper()); // prints '20'
```

With private fields, you'll never have to worry about this, since each field name is unique to the containing class.

```ts
class C {
  #foo = 10;

  cHelper() {
    return this.#foo;
  }
}

class D extends C {
  #foo = 20;

  dHelper() {
    return this.#foo;
  }
}

let instance = new D();
// 'this.#foo' refers to a different field within each class.
console.log(instance.cHelper()); // prints '10'
console.log(instance.dHelper()); // prints '20'
```

Another thing worth noting is that accessing a private field on any other type will result in a `TypeError`!

```ts
class Square {
  #sideLength: number;

  constructor(sideLength: number) {
    this.#sideLength = sideLength;
  }

  equals(other: any) {
    return this.#sideLength === other.#sideLength;
  }
}

const a = new Square(100);
const b = { sideLength: 100 };

// Boom!
// TypeError: attempted to get private field on non-instance
// This fails because 'b' is not an instance of 'Square'.
console.log(a.equals(b));
```

Finally, for any plain `.js` file users, private fields _always_ have to be declared before they're assigned to.

```js
class C {
  // No declaration for '#foo'
  // :(

  constructor(foo: number) {
    // SyntaxError!
    // '#foo' needs to be declared before writing to it.
    this.#foo = foo;
  }
}
```

JavaScript has always allowed users to access undeclared properties, whereas TypeScript has always required declarations for class properties.
With private fields, declarations are always needed regardless of whether we're working in `.js` or `.ts` files.

```js
class C {
  /** @type {number} */
  #foo;

  constructor(foo: number) {
    // This works.
    this.#foo = foo;
  }
}
```

For more information about the implementation, you can [check out the original pull request](https://github.com/Microsoft/TypeScript/pull/30829)

### Which should I use?

We've already received many questions on which type of privates you should use as a TypeScript user: most commonly, "should I use the `private` keyword, or ECMAScript's hash/pound (`#`) private fields?"
It depends!

When it comes to properties, TypeScript's `private` modifiers are fully erased - that means that at runtime, it acts entirely like a normal property and there's no way to tell that it was declared with a `private` modifier. When using the `private` keyword, privacy is only enforced at compile-time/design-time, and for JavaScript consumers it's entirely intent-based.

```ts
class C {
  private foo = 10;
}

// This is an error at compile time,
// but when TypeScript outputs .js files,
// it'll run fine and print '10'.
console.log(new C().foo); // prints '10'
//                  ~~~
// error! Property 'foo' is private and only accessible within class 'C'.

// TypeScript allows this at compile-time
// as a "work-around" to avoid the error.
console.log(new C()["foo"]); // prints '10'
```

The upside is that this sort of "soft privacy" can help your consumers temporarily work around not having access to some API, and also works in any runtime.

On the other hand, ECMAScript's `#` privates are completely inaccessible outside of the class.

```ts
class C {
  #foo = 10;
}

console.log(new C().#foo); // SyntaxError
//                  ~~~~
// TypeScript reports an error *and*
// this won't work at runtime!

console.log(new C()["#foo"]); // prints undefined
//          ~~~~~~~~~~~~~~~
// TypeScript reports an error under 'noImplicitAny',
// and this prints 'undefined'.
```

This hard privacy is really useful for strictly ensuring that nobody can take use of any of your internals.
If you're a library author, removing or renaming a private field should never cause a breaking change.

As we mentioned, another benefit is that subclassing can be easier with ECMAScript's `#` privates because they _really_ are private.
When using ECMAScript `#` private fields, no subclass ever has to worry about collisions in field naming.
When it comes to TypeScript's `private` property declarations, users still have to be careful not to trample over properties declared in superclasses.

One more thing to think about is where you intend for your code to run.
TypeScript currently can't support this feature unless targeting ECMAScript 2015 (ES6) targets or higher.
This is because our downleveled implementation uses `WeakMap`s to enforce privacy, and `WeakMap`s can't be polyfilled in a way that doesn't cause memory leaks.
In contrast, TypeScript's `private`-declared properties work with all targets - even ECMAScript 3!

A final consideration might be speed: `private` properties are no different from any other property, so accessing them is as fast as any other property access no matter which runtime you target.
In contrast, because `#` private fields are downleveled using `WeakMap`s, they may be slower to use.
While some runtimes might optimize their actual implementations of `#` private fields, and even have speedy `WeakMap` implementations, that might not be the case in all runtimes.

## `export * as ns` Syntax

It's often common to have a single entry-point that exposes all the members of another module as a single member.

```ts
import * as utilities from "./utilities.js";
export { utilities };
```

This is so common that ECMAScript 2020 recently added a new syntax to support this pattern!

```ts
export * as utilities from "./utilities.js";
```

This is a nice quality-of-life improvement to JavaScript, and TypeScript 3.8 implements this syntax.
When your module target is earlier than `es2020`, TypeScript will output something along the lines of the first code snippet.

## Top-Level `await`

TypeScript 3.8 provides support for a handy upcoming ECMAScript feature called "top-level `await`".

JavaScript users often introduce an `async` function in order to use `await`, and then immediately called the function after defining it.

```js
async function main() {
  const response = await fetch("...");
  const greeting = await response.text();
  console.log(greeting);
}

main().catch((e) => console.error(e));
```

This is because previously in JavaScript (along with most other languages with a similar feature), `await` was only allowed within the body of an `async` function.
However, with top-level `await`, we can use `await` at the top level of a module.

```ts
const response = await fetch("...");
const greeting = await response.text();
console.log(greeting);

// Make sure we're a module
export {};
```

Note there's a subtlety: top-level `await` only works at the top level of a _module_, and files are only considered modules when TypeScript finds an `import` or an `export`.
In some basic cases, you might need to write out `export {}` as some boilerplate to make sure of this.

Top level `await` may not work in all environments where you might expect at this point.
Currently, you can only use top level `await` when the [`target`](/tsconfig#target) compiler option is `es2017` or above, and `module` is `esnext` or `system`.
Support within several environments and bundlers may be limited or may require enabling experimental support.

For more information on our implementation, you can [check out the original pull request](https://github.com/microsoft/TypeScript/pull/35813).

## `es2020` for `target` and `module`

TypeScript 3.8 supports `es2020` as an option for `module` and [`target`](/tsconfig#target).
This will preserve newer ECMAScript 2020 features like optional chaining, nullish coalescing, `export * as ns`, and dynamic `import(...)` syntax.
It also means `bigint` literals now have a stable [`target`](/tsconfig#target) below `esnext`.

## JSDoc Property Modifiers

TypeScript 3.8 supports JavaScript files by turning on the [`allowJs`](/tsconfig#allowJs) flag, and also supports _type-checking_ those JavaScript files via the [`checkJs`](/tsconfig#checkJs) option or by adding a `// @ts-check` comment to the top of your `.js` files.

Because JavaScript files don't have dedicated syntax for type-checking, TypeScript leverages JSDoc.
TypeScript 3.8 understands a few new JSDoc tags for properties.

First are the accessibility modifiers: `@public`, `@private`, and `@protected`.
These tags work exactly like `public`, `private`, and `protected` respectively work in TypeScript.

```js
// @ts-check

class Foo {
  constructor() {
    /** @private */
    this.stuff = 100;
  }

  printStuff() {
    console.log(this.stuff);
  }
}

new Foo().stuff;
//        ~~~~~
// error! Property 'stuff' is private and only accessible within class 'Foo'.
```

- `@public` is always implied and can be left off, but means that a property can be reached from anywhere.
- `@private` means that a property can only be used within the containing class.
- `@protected` means that a property can only be used within the containing class, and all derived subclasses, but not on dissimilar instances of the containing class.

Next, we've also added the `@readonly` modifier to ensure that a property is only ever written to during initialization.

```js
// @ts-check

class Foo {
  constructor() {
    /** @readonly */
    this.stuff = 100;
  }

  writeToStuff() {
    this.stuff = 200;
    //   ~~~~~
    // Cannot assign to 'stuff' because it is a read-only property.
  }
}

new Foo().stuff++;
//        ~~~~~
// Cannot assign to 'stuff' because it is a read-only property.
```

## Better Directory Watching on Linux and `watchOptions`

TypeScript 3.8 ships a new strategy for watching directories, which is crucial for efficiently picking up changes to `node_modules`.

For some context, on operating systems like Linux, TypeScript installs directory watchers (as opposed to file watchers) on `node_modules` and many of its subdirectories to detect changes in dependencies.
This is because the number of available file watchers is often eclipsed by the number of files in `node_modules`, whereas there are way fewer directories to track.

Older versions of TypeScript would _immediately_ install directory watchers on folders, and at startup that would be fine; however, during an npm install, a lot of activity will take place within `node_modules` and that can overwhelm TypeScript, often slowing editor sessions to a crawl.
To prevent this, TypeScript 3.8 waits slightly before installing directory watchers to give these highly volatile directories some time to stabilize.

Because every project might work better under different strategies, and this new approach might not work well for your workflows, TypeScript 3.8 introduces a new `watchOptions` field in `tsconfig.json` and `jsconfig.json` which allows users to tell the compiler/language service which watching strategies should be used to keep track of files and directories.

```jsonc tsconfig
{
  // Some typical compiler options
  "compilerOptions": {
    "target": "es2020",
    "moduleResolution": "node"
    // ...
  },

  // NEW: Options for file/directory watching
  "watchOptions": {
    // Use native file system events for files and directories
    "watchFile": "useFsEvents",
    "watchDirectory": "useFsEvents",

    // Poll files for updates more frequently
    // when they're updated a lot.
    "fallbackPolling": "dynamicPriority"
  }
}
```

`watchOptions` contains 4 new options that can be configured:

- [`watchFile`](/tsconfig#watchFile): the strategy for how individual files are watched. This can be set to

  - `fixedPollingInterval`: Check every file for changes several times a second at a fixed interval.
  - `priorityPollingInterval`: Check every file for changes several times a second, but use heuristics to check certain types of files less frequently than others.
  - `dynamicPriorityPolling`: Use a dynamic queue where less-frequently modified files will be checked less often.
  - `useFsEvents` (the default): Attempt to use the operating system/file system's native events for file changes.
  - `useFsEventsOnParentDirectory`: Attempt to use the operating system/file system's native events to listen for changes on a file's containing directories. This can use fewer file watchers, but might be less accurate.

- [`watchDirectory`](/tsconfig#watchDirectory): the strategy for how entire directory trees are watched under systems that lack recursive file-watching functionality. This can be set to:

  - `fixedPollingInterval`: Check every directory for changes several times a second at a fixed interval.
  - `dynamicPriorityPolling`: Use a dynamic queue where less-frequently modified directories will be checked less often.
  - `useFsEvents` (the default): Attempt to use the operating system/file system's native events for directory changes.

- [`fallbackPolling`](/tsconfig#fallbackPolling): when using file system events, this option specifies the polling strategy that gets used when the system runs out of native file watchers and/or doesn't support native file watchers. This can be set to
  - `fixedPollingInterval`: _(See above.)_
  - `priorityPollingInterval`: _(See above.)_
  - `dynamicPriorityPolling`: _(See above.)_
  - `synchronousWatchDirectory`: Disable deferred watching on directories. Deferred watching is useful when lots of file changes might occur at once (e.g. a change in `node_modules` from running `npm install`), but you might want to disable it with this flag for some less-common setups.

For more information on these changes, [head over to GitHub to see the pull request](https://github.com/microsoft/TypeScript/pull/35615) to read more.

## "Fast and Loose" Incremental Checking

TypeScript 3.8 introduces a new compiler option called [`assumeChangesOnlyAffectDirectDependencies`](/tsconfig#assumeChangesOnlyAffectDirectDependencies).
When this option is enabled, TypeScript will avoid rechecking/rebuilding all truly possibly-affected files, and only recheck/rebuild files that have changed as well as files that directly import them.

For example, consider a file `fileD.ts` that imports `fileC.ts` that imports `fileB.ts` that imports `fileA.ts` as follows:

```
fileA.ts <- fileB.ts <- fileC.ts <- fileD.ts
```

In `--watch` mode, a change in `fileA.ts` would typically mean that TypeScript would need to at least re-check `fileB.ts`, `fileC.ts`, and `fileD.ts`.
Under [`assumeChangesOnlyAffectDirectDependencies`](/tsconfig#assumeChangesOnlyAffectDirectDependencies), a change in `fileA.ts` means that only `fileA.ts` and `fileB.ts` need to be re-checked.

In a codebase like Visual Studio Code, this reduced rebuild times for changes in certain files from about 14 seconds to about 1 second.
While we don't necessarily recommend this option for all codebases, you might be interested if you have an extremely large codebase and are willing to defer full project errors until later (e.g. a dedicated build via a `tsconfig.fullbuild.json` or in CI).

For more details, you can [see the original pull request](https://github.com/microsoft/TypeScript/pull/35711).

---

## Source: `packages/documentation/copy/en/release-notes/TypeScript 4.0.md`

---
title: TypeScript 4.0
layout: docs
permalink: /docs/handbook/release-notes/typescript-4-0.html
oneline: TypeScript 4.0 Release Notes
---

## Variadic Tuple Types

Consider a function in JavaScript called `concat` that takes two array or tuple types and concatenates them together to make a new array.

```js
function concat(arr1, arr2) {
  return [...arr1, ...arr2];
}
```

Also consider `tail`, that takes an array or tuple, and returns all elements but the first.

```js
function tail(arg) {
  const [_, ...result] = arg;
  return result;
}
```

How would we type either of these in TypeScript?

For `concat`, the only valid thing we could do in older versions of the language was to try and write some overloads.

```ts
function concat(arr1: [], arr2: []): [];
function concat<A>(arr1: [A], arr2: []): [A];
function concat<A, B>(arr1: [A, B], arr2: []): [A, B];
function concat<A, B, C>(arr1: [A, B, C], arr2: []): [A, B, C];
function concat<A, B, C, D>(arr1: [A, B, C, D], arr2: []): [A, B, C, D];
function concat<A, B, C, D, E>(arr1: [A, B, C, D, E], arr2: []): [A, B, C, D, E];
function concat<A, B, C, D, E, F>(arr1: [A, B, C, D, E, F], arr2: []): [A, B, C, D, E, F];
```

Uh...okay, that's...seven overloads for when the second array is always empty.
Let's add some for when `arr2` has one argument.

<!-- prettier-ignore -->
```ts
function concat<A2>(arr1: [], arr2: [A2]): [A2];
function concat<A1, A2>(arr1: [A1], arr2: [A2]): [A1, A2];
function concat<A1, B1, A2>(arr1: [A1, B1], arr2: [A2]): [A1, B1, A2];
function concat<A1, B1, C1, A2>(arr1: [A1, B1, C1], arr2: [A2]): [A1, B1, C1, A2];
function concat<A1, B1, C1, D1, A2>(arr1: [A1, B1, C1, D1], arr2: [A2]): [A1, B1, C1, D1, A2];
function concat<A1, B1, C1, D1, E1, A2>(arr1: [A1, B1, C1, D1, E1], arr2: [A2]): [A1, B1, C1, D1, E1, A2];
function concat<A1, B1, C1, D1, E1, F1, A2>(arr1: [A1, B1, C1, D1, E1, F1], arr2: [A2]): [A1, B1, C1, D1, E1, F1, A2];
```

We hope it's clear that this is getting unreasonable.
Unfortunately, you'd also end up with the same sorts of issues typing a function like `tail`.

This is another case of what we like to call "death by a thousand overloads", and it doesn't even solve the problem generally.
It only gives correct types for as many overloads as we care to write.
If we wanted to make a catch-all case, we'd need an overload like the following:

```ts
function concat<T, U>(arr1: T[], arr2: U[]): Array<T | U>;
```

But that signature doesn't encode anything about the lengths of the input, or the order of the elements, when using tuples.

TypeScript 4.0 brings two fundamental changes, along with inference improvements, to make typing these possible.

The first change is that spreads in tuple type syntax can now be generic.
This means that we can represent higher-order operations on tuples and arrays even when we don't know the actual types we're operating over.
When generic spreads are instantiated (or, replaced with a real type) in these tuple types, they can produce other sets of array and tuple types.

For example, that means we can type function like `tail`, without our "death by a thousand overloads" issue.

```ts twoslash
function tail<T extends any[]>(arr: readonly [any, ...T]) {
  const [_ignored, ...rest] = arr;
  return rest;
}

const myTuple = [1, 2, 3, 4] as const;
const myArray = ["hello", "world"];

const r1 = tail(myTuple);
//    ^?

const r2 = tail([...myTuple, ...myArray] as const);
//    ^?
```

The second change is that rest elements can occur anywhere in a tuple - not just at the end!

```ts
type Strings = [string, string];
type Numbers = [number, number];

type StrStrNumNumBool = [...Strings, ...Numbers, boolean];
```

Previously, TypeScript would issue an error like the following:

```
A rest element must be last in a tuple type.
```

But with TypeScript 4.0, this restriction is relaxed.

Note that in cases when we spread in a type without a known length, the resulting type becomes unbounded as well, and all the following elements factor into the resulting rest element type.

```ts
type Strings = [string, string];
type Numbers = number[];

type Unbounded = [...Strings, ...Numbers, boolean];
```

By combining both of these behaviors together, we can write a single well-typed signature for `concat`:

```ts twoslash
type Arr = readonly any[];

function concat<T extends Arr, U extends Arr>(arr1: T, arr2: U): [...T, ...U] {
  return [...arr1, ...arr2];
}
```

While that one signature is still a bit lengthy, it's just one signature that doesn't have to be repeated, and it gives predictable behavior on all arrays and tuples.

This functionality on its own is great, but it shines in more sophisticated scenarios too.
For example, consider a function to [partially apply arguments](https://en.wikipedia.org/wiki/Partial_application) called `partialCall`.
`partialCall` takes a function - let's call it `f` - along with the initial few arguments that `f` expects.
It then returns a new function that takes any other arguments that `f` still needs, and calls `f` when it receives them.

```js
function partialCall(f, ...headArgs) {
  return (...tailArgs) => f(...headArgs, ...tailArgs);
}
```

TypeScript 4.0 improves the inference process for rest parameters and rest tuple elements so that we can type this and have it "just work".

```ts twoslash
type Arr = readonly unknown[];

function partialCall<T extends Arr, U extends Arr, R>(
  f: (...args: [...T, ...U]) => R,
  ...headArgs: T
) {
  return (...tailArgs: U) => f(...headArgs, ...tailArgs);
}
```

In this case, `partialCall` understands which parameters it can and can't initially take, and returns functions that appropriately accept and reject anything left over.

```ts twoslash
// @errors: 2345 2554 2554 2345
type Arr = readonly unknown[];

function partialCall<T extends Arr, U extends Arr, R>(
  f: (...args: [...T, ...U]) => R,
  ...headArgs: T
) {
  return (...tailArgs: U) => f(...headArgs, ...tailArgs);
}
// ---cut---
const foo = (x: string, y: number, z: boolean) => {};

const f1 = partialCall(foo, 100);

const f2 = partialCall(foo, "hello", 100, true, "oops");

// This works!
const f3 = partialCall(foo, "hello");
//    ^?

// What can we do with f3 now?

// Works!
f3(123, true);

f3();

f3(123, "hello");
```

Variadic tuple types enable a lot of new exciting patterns, especially around function composition.
We expect we may be able to leverage it to do a better job type-checking JavaScript's built-in `bind` method.
A handful of other inference improvements and patterns also went into this, and if you're interested in learning more, you can take a look at [the pull request](https://github.com/microsoft/TypeScript/pull/39094) for variadic tuples.

## Labeled Tuple Elements

Improving the experience around tuple types and parameter lists is important because it allows us to get strongly typed validation around common JavaScript idioms - really just slicing and dicing argument lists and passing them to other functions.
The idea that we can use tuple types for rest parameters is one place where this is crucial.

For example, the following function that uses a tuple type as a rest parameter...

```ts
function foo(...args: [string, number]): void {
  // ...
}
```

...should appear no different from the following function...

```ts
function foo(arg0: string, arg1: number): void {
  // ...
}
```

...for any caller of `foo`.

```ts twoslash
// @errors: 2554
function foo(arg0: string, arg1: number): void {
  // ...
}
// ---cut---
foo("hello", 42);

foo("hello", 42, true);
foo("hello");
```

There is one place where the differences begin to become observable though: readability.
In the first example, we have no parameter names for the first and second elements.
While these have no impact on type-checking, the lack of labels on tuple positions can make them harder to use - harder to communicate our intent.

That's why in TypeScript 4.0, tuples types can now provide labels.

```ts
type Range = [start: number, end: number];
```

To deepen the connection between parameter lists and tuple types, the syntax for rest elements and optional elements mirrors the syntax for parameter lists.

```ts
type Foo = [first: number, second?: string, ...rest: any[]];
```

There are a few rules when using labeled tuples.
For one, when labeling a tuple element, all other elements in the tuple must also be labeled.

```ts twoslash
// @errors: 5084
type Bar = [first: string, number];
```

It's worth noting - labels don't require us to name our variables differently when destructuring.
They're purely there for documentation and tooling.

```ts twoslash
function foo(x: [first: string, second: number]) {
    // ...

    // note: we didn't need to name these 'first' and 'second'
    const [a, b] = x;
    a
//  ^?
    b
//  ^?
}
```

Overall, labeled tuples are handy when taking advantage of patterns around tuples and argument lists, along with implementing overloads in a type-safe way.
In fact, TypeScript's editor support will try to display them as overloads when possible.

![Signature help displaying a union of labeled tuples as in a parameter list as two signatures](https://devblogs.microsoft.com/typescript/wp-content/uploads/sites/11/2020/08/signatureHelpLabeledTuples.gif)

To learn more, check out [the pull request](https://github.com/microsoft/TypeScript/pull/38234) for labeled tuple elements.

## Class Property Inference from Constructors

TypeScript 4.0 can now use control flow analysis to determine the types of properties in classes when [`noImplicitAny`](/tsconfig#noImplicitAny) is enabled.

<!--prettier-ignore -->
```ts twoslash
class Square {
  // Previously both of these were any
  area;
// ^?
  sideLength;
// ^?
  constructor(sideLength: number) {
    this.sideLength = sideLength;
    this.area = sideLength ** 2;
  }
}
```

In cases where not all paths of a constructor assign to an instance member, the property is considered to potentially be `undefined`.

<!--prettier-ignore -->
```ts twoslash
// @errors: 2532 18048
class Square {
  sideLength;
// ^?

  constructor(sideLength: number) {
    if (Math.random()) {
      this.sideLength = sideLength;
    }
  }

  get area() {
    return this.sideLength ** 2;
  }
}
```

In cases where you know better (e.g. you have an `initialize` method of some sort), you'll still need an explicit type annotation along with a definite assignment assertion (`!`) if you're in [`strictPropertyInitialization`](/tsconfig#strictPropertyInitialization).

```ts twoslash
class Square {
  // definite assignment assertion
  //        v
  sideLength!: number;
  //         ^^^^^^^^
  // type annotation

  constructor(sideLength: number) {
    this.initialize(sideLength);
  }

  initialize(sideLength: number) {
    this.sideLength = sideLength;
  }

  get area() {
    return this.sideLength ** 2;
  }
}
```

For more details, [see the implementing pull request](https://github.com/microsoft/TypeScript/pull/37920).

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

## `unknown` on `catch` Clause Bindings

Since the beginning days of TypeScript, `catch` clause variables have always been typed as `any`.
This meant that TypeScript allowed you to do anything you wanted with them.

```ts twoslash
// @useUnknownInCatchVariables: false
try {
  // Do some work
} catch (x) {
  // x has type 'any' - have fun!
  console.log(x.message);
  console.log(x.toUpperCase());
  x++;
  x.yadda.yadda.yadda();
}
```

The above has some undesirable behavior if we're trying to prevent _more_ errors from happening in our error-handling code!
Because these variables have the type `any` by default, they lack any type-safety which could have errored on invalid operations.

That's why TypeScript 4.0 now lets you specify the type of `catch` clause variables as `unknown` instead.
`unknown` is safer than `any` because it reminds us that we need to perform some sorts of type-checks before operating on our values.

<!--prettier-ignore -->
```ts twoslash
// @errors: 2571 18046
try {
  // ...
} catch (e: unknown) {
  // Can't access values on unknowns
  console.log(e.toUpperCase());

  if (typeof e === "string") {
    // We've narrowed 'e' down to the type 'string'.
    console.log(e.toUpperCase());
  }
}
```

While the types of `catch` variables won't change by default, we might consider a new [`strict`](/tsconfig#strict) mode flag in the future so that users can opt in to this behavior.
In the meantime, it should be possible to write a lint rule to force `catch` variables to have an explicit annotation of either `: any` or `: unknown`.

For more details you can [peek at the changes for this feature](https://github.com/microsoft/TypeScript/pull/39015).

## Custom JSX Factories

When using JSX, a [_fragment_](https://reactjs.org/docs/fragments.html) is a type of JSX element that allows us to return multiple child elements.
When we first implemented fragments in TypeScript, we didn't have a great idea about how other libraries would utilize them.
Nowadays most other libraries that encourage using JSX and support fragments have a similar API shape.

In TypeScript 4.0, users can customize the fragment factory through the new [`jsxFragmentFactory`](/tsconfig#jsxFragmentFactory) option.

As an example, the following `tsconfig.json` file tells TypeScript to transform JSX in a way compatible with React, but switches each factory invocation to `h` instead of `React.createElement`, and uses `Fragment` instead of `React.Fragment`.

```jsonc tsconfig
{
  "compilerOptions": {
    "target": "esnext",
    "module": "commonjs",
    "jsx": "react",
    "jsxFactory": "h",
    "jsxFragmentFactory": "Fragment"
  }
}
```

In cases where you need to have a different JSX factory on a per-file basis<!-- (maybe you like to ship React, Preact, and Inferno to give a blazing fast experience) -->, you can take advantage of the new `/** @jsxFrag */` pragma comment.
For example, the following...

```tsx twoslash
// @noErrors
// Note: these pragma comments need to be written
// with a JSDoc-style multiline syntax to take effect.

/** @jsx h */
/** @jsxFrag Fragment */

import { h, Fragment } from "preact";

export const Header = (
  <>
    <h1>Welcome</h1>
  </>
);
```

...will get transformed to this output JavaScript...

```tsx twoslash
// @noErrors
// @showEmit
// Note: these pragma comments need to be written
// with a JSDoc-style multiline syntax to take effect.

/** @jsx h */
/** @jsxFrag Fragment */

import { h, Fragment } from "preact";

export const Header = (
  <>
    <h1>Welcome</h1>
  </>
);
```

We'd like to extend a big thanks to community member [Noj Vek](https://github.com/nojvek) for sending this pull request and patiently working with our team on it.

You can see that [the pull request](https://github.com/microsoft/TypeScript/pull/38720) for more details!

## Speed Improvements in `build` mode with `--noEmitOnError`

Previously, compiling a program after a previous compile with errors under [`incremental`](/tsconfig#incremental) would be extremely slow when using the [`noEmitOnError`](/tsconfig#noEmitOnError) flag.
This is because none of the information from the last compilation would be cached in a `.tsbuildinfo` file based on the [`noEmitOnError`](/tsconfig#noEmitOnError) flag.

TypeScript 4.0 changes this which gives a great speed boost in these scenarios, and in turn improves `--build` mode scenarios (which imply both [`incremental`](/tsconfig#incremental) and [`noEmitOnError`](/tsconfig#noEmitOnError)).

For details, [read up more on the pull request](https://github.com/microsoft/TypeScript/pull/38853).

## `--incremental` with `--noEmit`

TypeScript 4.0 allows us to use the [`noEmit`](/tsconfig#noEmit) flag while still leveraging [`incremental`](/tsconfig#incremental) compiles.
This was previously not allowed, as [`incremental`](/tsconfig#incremental) needs to emit a `.tsbuildinfo` files; however, the use-case to enable faster incremental builds is important enough to enable for all users.

For more details, you can [see the implementing pull request](https://github.com/microsoft/TypeScript/pull/39122).

## Editor Improvements

The TypeScript compiler doesn't only power the editing experience for TypeScript itself in most major editors - it also powers the JavaScript experience in the Visual Studio family of editors and more.
For that reason, much of our work focuses on improving editor scenarios - the place you spend most of your time as a developer.

Using new TypeScript/JavaScript functionality in your editor will differ depending on your editor, but

- Visual Studio Code supports [selecting different versions of TypeScript](https://code.visualstudio.com/docs/typescript/typescript-compiling#_using-the-workspace-version-of-typescript). Alternatively, there's the [JavaScript/TypeScript Nightly Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode.vscode-typescript-next) to stay on the bleeding edge (which is typically very stable).
- Visual Studio 2017/2019 have [the SDK installers above] and [MSBuild installs](https://www.nuget.org/packages/Microsoft.TypeScript.MSBuild).
- Sublime Text 3 supports [selecting different versions of TypeScript](https://github.com/microsoft/TypeScript-Sublime-Plugin#note-using-different-versions-of-typescript)

You can check out a partial [list of editors that have support for TypeScript](https://github.com/Microsoft/TypeScript/wiki/TypeScript-Editor-Support) to learn more about whether your favorite editor has support to use new versions.

### Convert to Optional Chaining

Optional chaining is a recent feature that's received a lot of love.
That's why TypeScript 4.0 brings a new refactoring to convert common patterns to take advantage of [optional chaining](https://devblogs.microsoft.com/typescript/announcing-typescript-3-7/#optional-chaining) and [nullish coalescing](https://devblogs.microsoft.com/typescript/announcing-typescript-3-7/#nullish-coalescing)!

![Converting `a && a.b.c && a.b.c.d.e.f()` to `a?.b.c?.d.e.f.()`](https://devblogs.microsoft.com/typescript/wp-content/uploads/sites/11/2020/08/convertToOptionalChain-4-0.gif)

Keep in mind that while this refactoring doesn't _perfectly_ capture the same behavior due to subtleties with truthiness/falsiness in JavaScript, we believe it should capture the intent for most use-cases, especially when TypeScript has more precise knowledge of your types.

For more details, [check out the pull request for this feature](https://github.com/microsoft/TypeScript/pull/39135).

### `/** @deprecated */` Support

TypeScript's editing support now recognizes when a declaration has been marked with a `/** @deprecated */` JSDoc comment.
That information is surfaced in completion lists and as a suggestion diagnostic that editors can handle specially.
In an editor like VS Code, deprecated values are typically displayed in a strike-though style ~~like this~~.

![Some examples of deprecated declarations with strikethrough text in the editor](https://devblogs.microsoft.com/typescript/wp-content/uploads/sites/11/2020/06/deprecated_4-0.png)

This new functionality is available thanks to [Wenlu Wang](https://github.com/Kingwl).
See [the pull request](https://github.com/microsoft/TypeScript/pull/38523) for more details.

### Partial Semantic Mode at Startup

We've heard a lot from users suffering from long startup times, especially on bigger projects.
The culprit is usually a process called _program construction_.
This is the process of starting with an initial set of root files, parsing them, finding their dependencies, parsing those dependencies, finding those dependencies' dependencies, and so on.
The bigger your project is, the longer you'll have to wait before you can get basic editor operations like go-to-definition or quick info.

That's why we've been working on a new mode for editors to provide a _partial_ experience until the full language service experience has loaded up.
The core idea is that editors can run a lightweight partial server that only looks at the current files that the editor has open.

It's hard to say precisely what sorts of improvements you'll see, but anecdotally, it used to take anywhere between _20 seconds to a minute_ before TypeScript would become fully responsive on the Visual Studio Code codebase.
In contrast, **our new partial semantic mode seems to bring that delay down to just a few seconds**.
As an example, in the following video, you can see two side-by-side editors with TypeScript 3.9 running on the left and TypeScript 4.0 running on the right.

<video loop autoplay muted style="width:100%;height:100%;" src="https://devblogs.microsoft.com/typescript/wp-content/uploads/sites/11/2020/08/partialModeFast.mp4">
</video>

When restarting both editors on a particularly large codebase, the one with TypeScript 3.9 can't provide completions or quick info at all.
On the other hand, the editor with TypeScript 4.0 can _immediately_ give us a rich experience in the current file we're editing, despite loading the full project in the background.

Currently the only editor that supports this mode is [Visual Studio Code](http://code.visualstudio.com/) which has some UX improvements coming up in [Visual Studio Code Insiders](http://code.visualstudio.com/insiders).
We recognize that this experience may still have room for polish in UX and functionality, and we have [a list of improvements](https://github.com/microsoft/TypeScript/issues/39035) in mind.
We're looking for more feedback on what you think might be useful.

For more information, you can [see the original proposal](https://github.com/microsoft/TypeScript/issues/37713), [the implementing pull request](https://github.com/microsoft/TypeScript/pull/38561), along with [the follow-up meta issue](https://github.com/microsoft/TypeScript/issues/39035).

### Smarter Auto-Imports

Auto-import is a fantastic feature that makes coding a lot easier; however, every time auto-import doesn't seem to work, it can throw users off a lot.
One specific issue that we heard from users was that auto-imports didn't work on dependencies that were written in TypeScript - that is, until they wrote at least one explicit import somewhere else in their project.

Why would auto-imports work for `@types` packages, but not for packages that ship their own types?
It turns out that auto-imports only work on packages your project _already_ includes.
Because TypeScript has some quirky defaults that automatically add packages in `node_modules/@types` to your project, _those_ packages would be auto-imported.
On the other hand, other packages were excluded because crawling through all your `node_modules` packages can be _really_ expensive.

All of this leads to a pretty lousy getting started experience for when you're trying to auto-import something that you've just installed but haven't used yet.

TypeScript 4.0 now does a little extra work in editor scenarios to include the packages you've listed in your `package.json`'s `dependencies` (and `peerDependencies`) fields.
The information from these packages is only used to improve auto-imports, and doesn't change anything else like type-checking.
This allows us to provide auto-imports for all of your dependencies that have types, without incurring the cost of a complete `node_modules` search.

In the rare cases when your `package.json` lists more than ten typed dependencies that haven't been imported yet, this feature automatically disables itself to prevent slow project loading.
To force the feature to work, or to disable it entirely, you should be able to configure your editor.
For Visual Studio Code, this is the "Include Package JSON Auto Imports" (or `typescript.preferences.includePackageJsonAutoImports`) setting.

![Configuring 'include package JSON auto imports'](https://devblogs.microsoft.com/typescript/wp-content/uploads/sites/11/2020/08/configurePackageJsonAutoImports4-0.png)
For more details, you can see the [proposal issue](https://github.com/microsoft/TypeScript/issues/37812) along with [the implementing pull request](https://github.com/microsoft/TypeScript/pull/38923).

## Our New Website!

[The TypeScript website](https://www.typescriptlang.org/) has recently been rewritten from the ground up and rolled out!

![A screenshot of the new TypeScript website](https://devblogs.microsoft.com/typescript/wp-content/uploads/sites/11/2020/08/ts-web.png)

[We already wrote a bit about our new site](https://devblogs.microsoft.com/typescript/announcing-the-new-typescript-website/), so you can read up more there; but it's worth mentioning that we're still looking to hear what you think!
If you have questions, comments, or suggestions, you can [file them over on the website's issue tracker](https://github.com/microsoft/TypeScript-Website).

## Breaking Changes

### `lib.d.ts` Changes

Our `lib.d.ts` declarations have changed - most specifically, types for the DOM have changed.
The most notable change may be the removal of [`document.origin`](https://developer.mozilla.org/en-US/docs/Web/API/Document/origin) which only worked in old versions of IE and Safari
MDN recommends moving to [`self.origin`](https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/origin).

### Properties Overriding Accessors (and vice versa) is an Error

Previously, it was only an error for properties to override accessors, or accessors to override properties, when using [`useDefineForClassFields`](/tsconfig#useDefineForClassFields); however, TypeScript now always issues an error when declaring a property in a derived class that would override a getter or setter in the base class.

```ts twoslash
// @errors: 1049 2610
class Base {
  get foo() {
    return 100;
  }
  set foo(value) {
    // ...
  }
}

class Derived extends Base {
  foo = 10;
}
```

```ts twoslash
// @errors: 2611
class Base {
  prop = 10;
}

class Derived extends Base {
  get prop() {
    return 100;
  }
}
```

See more details on [the implementing pull request](https://github.com/microsoft/TypeScript/pull/37894).

### Operands for `delete` must be optional.

When using the `delete` operator in [`strictNullChecks`](/tsconfig#strictNullChecks), the operand must now be `any`, `unknown`, `never`, or be optional (in that it contains `undefined` in the type).
Otherwise, use of the `delete` operator is an error.

```ts twoslash
// @errors: 2790
interface Thing {
  prop: string;
}

function f(x: Thing) {
  delete x.prop;
}
```

See more details on [the implementing pull request](https://github.com/microsoft/TypeScript/pull/37921).

### Usage of TypeScript's Node Factory is Deprecated

Today TypeScript provides a set of "factory" functions for producing AST Nodes; however, TypeScript 4.0 provides a new node factory API.
As a result, for TypeScript 4.0 we've made the decision to deprecate these older functions in favor of the new ones.

For more details, [read up on the relevant pull request for this change](https://github.com/microsoft/TypeScript/pull/35282).

---

## Source: `packages/documentation/copy/en/release-notes/TypeScript 4.1.md`

---
title: TypeScript 4.1
layout: docs
permalink: /docs/handbook/release-notes/typescript-4-1.html
oneline: TypeScript 4.1 Release Notes
---

## Template Literal Types

String literal types in TypeScript allow us to model functions and APIs that expect a set of specific strings.

```ts twoslash
// @errors: 2345
function setVerticalAlignment(location: "top" | "middle" | "bottom") {
  // ...
}

setVerticalAlignment("middel");
```

This is pretty nice because string literal types can basically spell-check our string values.

We also like that string literals can be used as property names in mapped types.
In this sense, they're also usable as building blocks:

```ts
type Options = {
  [K in "noImplicitAny" | "strictNullChecks" | "strictFunctionTypes"]?: boolean;
};
// same as
//   type Options = {
//       noImplicitAny?: boolean,
//       strictNullChecks?: boolean,
//       strictFunctionTypes?: boolean
//   };
```

But there's another place that string literal types could be used as building blocks: building other string literal types.

That's why TypeScript 4.1 brings the template literal string type.
It has the same syntax as [template literal strings in JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals), but is used in type positions.
When you use it with concrete literal types, it produces a new string literal type by concatenating the contents.

```ts twoslash
type World = "world";

type Greeting = `hello ${World}`;
//   ^?
```

What happens when you have unions in substitution positions?
It produces the set of every possible string literal that could be represented by each union member.

```ts twoslash
type Color = "red" | "blue";
type Quantity = "one" | "two";

type SeussFish = `${Quantity | Color} fish`;
//   ^?
```

This can be used beyond cute examples in release notes.
For example, several libraries for UI components have a way to specify both vertical and horizontal alignment in their APIs, often with both at once using a single string like `"bottom-right"`.
Between vertically aligning with `"top"`, `"middle"`, and `"bottom"`, and horizontally aligning with `"left"`, `"center"`, and `"right"`, there are 9 possible strings where each of the former strings is connected with each of the latter strings using a dash.

```ts twoslash
// @errors: 2345
type VerticalAlignment = "top" | "middle" | "bottom";
type HorizontalAlignment = "left" | "center" | "right";

// Takes
//   | "top-left"    | "top-center"    | "top-right"
//   | "middle-left" | "middle-center" | "middle-right"
//   | "bottom-left" | "bottom-center" | "bottom-right"

declare function setAlignment(value: `${VerticalAlignment}-${HorizontalAlignment}`): void;

setAlignment("top-left");   // works!
setAlignment("top-middel"); // error!
setAlignment("top-pot");    // error! but good doughnuts if you're ever in Seattle
```

While there are **lots** of examples of this sort of API in the wild, this is still a bit of a toy example since we could write these out manually.
In fact, for 9 strings, this is likely fine; but when you need a ton of strings, you should consider automatically generating them ahead of time to save work on every type-check (or just use `string`, which will be much simpler to comprehend).

Some of the real value comes from dynamically creating new string literals.
For example, imagine a `makeWatchedObject` API that takes an object and produces a mostly identical object, but with a new `on` method to detect for changes to the properties.

```ts
let person = makeWatchedObject({
  firstName: "Homer",
  age: 42, // give-or-take
  location: "Springfield",
});

person.on("firstNameChanged", () => {
  console.log(`firstName was changed!`);
});
```

Notice that `on` listens on the event `"firstNameChanged"`, not just `"firstName"`.
How would we type this?

```ts twslash
type PropEventSource<T> = {
    on(eventName: `${string & keyof T}Changed`, callback: () => void): void;
};

/// Create a "watched object" with an 'on' method
/// so that you can watch for changes to properties.
declare function makeWatchedObject<T>(obj: T): T & PropEventSource<T>;
```

With this, we can build something that errors when we give the wrong property!

```ts twoslash
// @errors: 2345
type PropEventSource<T> = {
    on(eventName: `${string & keyof T}Changed`, callback: () => void): void;
};
declare function makeWatchedObject<T>(obj: T): T & PropEventSource<T>;
let person = makeWatchedObject({
  firstName: "Homer",
  age: 42, // give-or-take
  location: "Springfield",
});

// ---cut---
// error!
person.on("firstName", () => {});

// error!
person.on("frstNameChanged", () => {});
```

We can also do something special in template literal types: we can _infer_ from substitution positions.
We can make our last example generic to infer from parts of the `eventName` string to figure out the associated property.

```ts twoslash
type PropEventSource<T> = {
    on<K extends string & keyof T>
        (eventName: `${K}Changed`, callback: (newValue: T[K]) => void ): void;
};

declare function makeWatchedObject<T>(obj: T): T & PropEventSource<T>;

let person = makeWatchedObject({
    firstName: "Homer",
    age: 42,
    location: "Springfield",
});

// works! 'newName' is typed as 'string'
person.on("firstNameChanged", newName => {
    // 'newName' has the type of 'firstName'
    console.log(`new name is ${newName.toUpperCase()}`);
});

// works! 'newAge' is typed as 'number'
person.on("ageChanged", newAge => {
    if (newAge < 0) {
        console.log("warning! negative age");
    }
})
```

Here we made `on` into a generic method.
When a user calls with the string `"firstNameChanged'`, TypeScript will try to infer the right type for `K`.
To do that, it will match `K` against the content prior to `"Changed"` and infer the string `"firstName"`.
Once TypeScript figures that out, the `on` method can fetch the type of `firstName` on the original object, which is `string` in this case.
Similarly, when we call with `"ageChanged"`, it finds the type for the property `age` which is `number`).

Inference can be combined in different ways, often to deconstruct strings, and reconstruct them in different ways.
In fact, to help with modifying these string literal types, we've added a few new utility type aliases for modifying casing in letters (i.e. converting to lowercase and uppercase characters).

```ts twoslash
type EnthusiasticGreeting<T extends string> = `${Uppercase<T>}`

type HELLO = EnthusiasticGreeting<"hello">;
//   ^?
```

The new type aliases are `Uppercase`, `Lowercase`, `Capitalize` and `Uncapitalize`.
The first two transform every character in a string, and the latter two transform only the first character in a string.

For more details, [see the original pull request](https://github.com/microsoft/TypeScript/pull/40336) and [the in-progress pull request to switch to type alias helpers](https://github.com/microsoft/TypeScript/pull/40580).

## Key Remapping in Mapped Types

Just as a refresher, a mapped type can create new object types based on arbitrary keys

```ts
type Options = {
  [K in "noImplicitAny" | "strictNullChecks" | "strictFunctionTypes"]?: boolean;
};
// same as
//   type Options = {
//       noImplicitAny?: boolean,
//       strictNullChecks?: boolean,
//       strictFunctionTypes?: boolean
//   };
```

or new object types based on other object types.

```ts
/// 'Partial<T>' is the same as 'T', but with each property marked optional.
type Partial<T> = {
  [K in keyof T]?: T[K];
};
```

Until now, mapped types could only produce new object types with keys that you provided them; however, lots of the time you want to be able to create new keys, or filter out keys, based on the inputs.

That's why TypeScript 4.1 allows you to re-map keys in mapped types with a new `as` clause.

```ts
type MappedTypeWithNewKeys<T> = {
    [K in keyof T as NewKeyType]: T[K]
    //            ^^^^^^^^^^^^^
    //            This is the new syntax!
}
```

With this new `as` clause, you can leverage features like template literal types to easily create property names based off of old ones.

```ts twoslash
type Getters<T> = {
    [K in keyof T as `get${Capitalize<string & K>}`]: () => T[K]
};

interface Person {
    name: string;
    age: number;
    location: string;
}

type LazyPerson = Getters<Person>;
//   ^?
```

and you can even filter out keys by producing `never`.
That means you don't have to use an extra `Omit` helper type in some cases.

```ts twoslash
// Remove the 'kind' property
type RemoveKindField<T> = {
    [K in keyof T as Exclude<K, "kind">]: T[K]
};

interface Circle {
    kind: "circle";
    radius: number;
}

type KindlessCircle = RemoveKindField<Circle>;
//   ^?
```

For more information, take a look at [the original pull request over on GitHub](https://github.com/microsoft/TypeScript/pull/40336).

## Recursive Conditional Types

In JavaScript it's fairly common to see functions that can flatten and build up container types at arbitrary levels.
For example, consider the `.then()` method on instances of `Promise`.
`.then(...)` unwraps each promise until it finds a value that's not "promise-like", and passes that value to a callback.
There's also a relatively new `flat` method on `Array`s that can take a depth of how deep to flatten.

Expressing this in TypeScript's type system was, for all practical intents and purposes, not possible.
While there were hacks to achieve this, the types ended up looking very unreasonable.

That's why TypeScript 4.1 eases some restrictions on conditional types - so that they can model these patterns.
In TypeScript 4.1, conditional types can now immediately reference themselves within their branches, making it easier to write recursive type aliases.

For example, if we wanted to write a type to get the element types of nested arrays, we could write the following `deepFlatten` type.

```ts
type ElementType<T> = T extends ReadonlyArray<infer U> ? ElementType<U> : T;

function deepFlatten<T extends readonly unknown[]>(x: T): ElementType<T>[] {
  throw "not implemented";
}

// All of these return the type 'number[]':
deepFlatten([1, 2, 3]);
deepFlatten([[1], [2, 3]]);
deepFlatten([[1], [[2]], [[[3]]]]);
```

Similarly, in TypeScript 4.1 we can write an `Awaited` type to deeply unwrap `Promise`s.

```ts
type Awaited<T> = T extends PromiseLike<infer U> ? Awaited<U> : T;

/// Like `promise.then(...)`, but more accurate in types.
declare function customThen<T, U>(
  p: Promise<T>,
  onFulfilled: (value: Awaited<T>) => U
): Promise<Awaited<U>>;
```

Keep in mind that while these recursive types are powerful, they should be used responsibly and sparingly.

First off, these types can do a lot of work which means that they can increase type-checking time.
Trying to model numbers in the Collatz conjecture or Fibonacci sequence might be fun, but don't ship that in `.d.ts` files on npm.

But apart from being computationally intensive, these types can hit an internal recursion depth limit on sufficiently-complex inputs.
When that recursion limit is hit, that results in a compile-time error.
In general, it's better not to use these types at all than to write something that fails on more realistic examples.

See more [at the implementation](https://github.com/microsoft/TypeScript/pull/40002).

## Checked Indexed Accesses (`--noUncheckedIndexedAccess`)

TypeScript has a feature called _index signatures_.
These signatures are a way to signal to the type system that users can access arbitrarily-named properties.

```ts twoslash
interface Options {
  path: string;
  permissions: number;

  // Extra properties are caught by this index signature.
  [propName: string]: string | number;
}

function checkOptions(opts: Options) {
  opts.path; // string
  opts.permissions; // number

  // These are all allowed too!
  // They have the type 'string | number'.
  opts.yadda.toString();
  opts["foo bar baz"].toString();
  opts[Math.random()].toString();
}
```

In the above example, `Options` has an index signature that says any accessed property that's not already listed should have the type `string | number`.
This is often convenient for optimistic code that assumes you know what you're doing, but the truth is that most values in JavaScript do not support every potential property name.
Most types will not, for example, have a value for a property key created by `Math.random()` like in the previous example.
For many users, this behavior was undesirable, and felt like it wasn't leveraging the full strict-checking of [`strictNullChecks`](/tsconfig#strictNullChecks).

That's why TypeScript 4.1 ships with a new flag called [`noUncheckedIndexedAccess`](/tsconfig#noUncheckedIndexedAccess).
Under this new mode, every property access (like `foo.bar`) or indexed access (like `foo["bar"]`) is considered potentially undefined.
That means that in our last example, `opts.yadda` will have the type `string | number | undefined` as opposed to just `string | number`.
If you need to access that property, you'll either have to check for its existence first or use a non-null assertion operator (the postfix `!` character).

```ts twoslash
// @errors: 2532 18048
// @noUncheckedIndexedAccess
interface Options {
  path: string;
  permissions: number;

  // Extra properties are caught by this index signature.
  [propName: string]: string | number;
}
// ---cut---
function checkOptions(opts: Options) {
  opts.path; // string
  opts.permissions; // number

  // These are not allowed with noUncheckedIndexedAccess
  opts.yadda.toString();
  opts["foo bar baz"].toString();
  opts[Math.random()].toString();

  // Checking if it's really there first.
  if (opts.yadda) {
    console.log(opts.yadda.toString());
  }

  // Basically saying "trust me I know what I'm doing"
  // with the '!' non-null assertion operator.
  opts.yadda!.toString();
}
```

One consequence of using [`noUncheckedIndexedAccess`](/tsconfig#noUncheckedIndexedAccess) is that indexing into an array is also more strictly checked, even in a bounds-checked loop.

```ts twoslash
// @errors: 2532 18048
// @noUncheckedIndexedAccess
function screamLines(strs: string[]) {
  // This will have issues
  for (let i = 0; i < strs.length; i++) {
    console.log(strs[i].toUpperCase());
  }
}
```

If you don't need the indexes, you can iterate over individual elements by using a `for`-`of` loop or a `forEach` call.

```ts twoslash
// @noUncheckedIndexedAccess
function screamLines(strs: string[]) {
  // This works fine
  for (const str of strs) {
    console.log(str.toUpperCase());
  }

  // This works fine
  strs.forEach((str) => {
    console.log(str.toUpperCase());
  });
}
```

This flag can be handy for catching out-of-bounds errors, but it might be noisy for a lot of code, so it is not automatically enabled by the [`strict`](/tsconfig#strict) flag; however, if this feature is interesting to you, you should feel free to try it and determine whether it makes sense for your team's codebase!

You can learn more [at the implementing pull request](https://github.com/microsoft/TypeScript/pull/39560).

## `paths` without `baseUrl`

Using path-mapping is fairly common - often it's to have nicer imports, often it's to simulate monorepo linking behavior.

Unfortunately, specifying [`paths`](/tsconfig#paths) to enable path-mapping required also specifying an option called [`baseUrl`](/tsconfig#baseUrl), which allows bare specifier paths to be reached relative to the [`baseUrl`](/tsconfig#baseUrl) too.
This also often caused poor paths to be used by auto-imports.

In TypeScript 4.1, the [`paths`](/tsconfig#paths) option can be used without [`baseUrl`](/tsconfig#baseUrl).
This helps avoid some of these issues.

## `checkJs` Implies `allowJs`

Previously if you were starting a checked JavaScript project, you had to set both [`allowJs`](/tsconfig#allowJs) and [`checkJs`](/tsconfig#checkJs).
This was a slightly annoying bit of friction in the experience, so [`checkJs`](/tsconfig#checkJs) now implies [`allowJs`](/tsconfig#allowJs) by default.

[See more details at the pull request](https://github.com/microsoft/TypeScript/pull/40275).

## React 17 JSX Factories

TypeScript 4.1 supports React 17's upcoming `jsx` and `jsxs` factory functions through two new options for the [`jsx`](/tsconfig#jsx) compiler option:

- `react-jsx`
- `react-jsxdev`

These options are intended for production and development compiles respectively.
Often, the options from one can extend from the other.
For example, a `tsconfig.json` for production builds might look like the following:

```json tsconfig
// ./src/tsconfig.json
{
  "compilerOptions": {
    "module": "esnext",
    "target": "es2015",
    "jsx": "react-jsx",
    "strict": true
  },
  "include": ["./**/*"]
}
```

and one for development builds might look like the following:

```json tsconfig
// ./src/tsconfig.dev.json
{
  "extends": "./tsconfig.json",
  "compilerOptions": {
    "jsx": "react-jsxdev"
  }
}
```

For more information, [check out the corresponding PR](https://github.com/microsoft/TypeScript/pull/39199).

## Editor Support for the JSDoc `@see` Tag

The JSDoc tag `@see` tag now has better support in editors for TypeScript and JavaScript.
This allows you to use functionality like go-to-definition in a dotted name following the tag.
For example, going to definition on `first` or `C` in the JSDoc comment just works in the following example:

```ts
// @filename: first.ts
export class C {}

// @filename: main.ts
import * as first from "./first";

/**
 * @see first.C
 */
function related() {}
```

Thanks to frequent contributor [Wenlu Wang](https://github.com/Kingwl) [for implementing this](https://github.com/microsoft/TypeScript/pull/39760)!

## Breaking Changes

### `lib.d.ts` Changes

`lib.d.ts` may have a set of changed APIs, potentially in part due to how the DOM types are automatically generated.
One specific change is that `Reflect.enumerate` has been removed, as it was removed from ES2016.

### `abstract` Members Can't Be Marked `async`

Members marked as `abstract` can no longer be marked as `async`.
The fix here is to remove the `async` keyword, since callers are only concerned with the return type.

### `any`/`unknown` Are Propagated in Falsy Positions

Previously, for an expression like `foo && somethingElse`, the type of `foo` was `any` or `unknown`, the type of the whole that expression would be the type of `somethingElse`.

For example, previously the type for `x` here was `{ someProp: string }`.

```ts
declare let foo: unknown;
declare let somethingElse: { someProp: string };

let x = foo && somethingElse;
```

However, in TypeScript 4.1, we are more careful about how we determine this type.
Since nothing is known about the type on the left side of the `&&`, we propagate `any` and `unknown` outward instead of the type on the right side.

The most common pattern we saw of this tended to be when checking compatibility with `boolean`s, especially in predicate functions.

```ts
function isThing(x: any): boolean {
  return x && typeof x === "object" && x.blah === "foo";
}
```

Often the appropriate fix is to switch from `foo && someExpression` to `!!foo && someExpression`.

### `resolve`'s Parameters Are No Longer Optional in `Promise`s

When writing code like the following

```ts
new Promise((resolve) => {
  doSomethingAsync(() => {
    doSomething();
    resolve();
  });
});
```

You may get an error like the following:

```
  resolve()
  ~~~~~~~~~
error TS2554: Expected 1 arguments, but got 0.
  An argument for 'value' was not provided.
```

This is because `resolve` no longer has an optional parameter, so by default, it must now be passed a value.
Often this catches legitimate bugs with using `Promise`s.
The typical fix is to pass it the correct argument, and sometimes to add an explicit type argument.

```ts
new Promise<number>((resolve) => {
  //     ^^^^^^^^
  doSomethingAsync((value) => {
    doSomething();
    resolve(value);
    //      ^^^^^
  });
});
```

However, sometimes `resolve()` really does need to be called without an argument.
In these cases, we can give `Promise` an explicit `void` generic type argument (i.e. write it out as `Promise<void>`).
This leverages new functionality in TypeScript 4.1 where a potentially-`void` trailing parameter can become optional.

```ts
new Promise<void>((resolve) => {
  //     ^^^^^^
  doSomethingAsync(() => {
    doSomething();
    resolve();
  });
});
```

TypeScript 4.1 ships with a quick fix to help fix this break.

### Conditional Spreads Create Optional Properties

In JavaScript, object spreads (like `{ ...foo }`) don't operate over falsy values.
So in code like `{ ...foo }`, `foo` will be skipped over if it's `null` or `undefined`.

Many users take advantage of this to spread properties "conditionally".

```ts
interface Person {
  name: string;
  age: number;
  location: string;
}

interface Animal {
  name: string;
  owner: Person;
}

function copyOwner(pet?: Animal) {
  return {
    ...(pet && pet.owner),
    otherStuff: 123,
  };
}

// We could also use optional chaining here:

function copyOwner(pet?: Animal) {
  return {
    ...pet?.owner,
    otherStuff: 123,
  };
}
```

Here, if `pet` is defined, the properties of `pet.owner` will be spread in - otherwise, no properties will be spread into the returned object.

The return type of `copyOwner` was previously a union type based on each spread:

```
{ x: number } | { x: number, name: string, age: number, location: string }
```

This modeled exactly how the operation would occur: if `pet` was defined, all the properties from `Person` would be present; otherwise, none of them would be defined on the result.
It was an all-or-nothing operation.

However, we've seen this pattern taken to the extreme, with hundreds of spreads in a single object, each spread potentially adding in hundreds or thousands of properties.
It turns out that for various reasons, this ends up being extremely expensive, and usually for not much benefit.

In TypeScript 4.1, the returned type sometimes uses all-optional properties.

```
{
    x: number;
    name?: string;
    age?: number;
    location?: string;
}
```

This ends up performing better and generally displaying better too.

For more details, [see the original change](https://github.com/microsoft/TypeScript/pull/40778).
While this behavior is not entirely consistent right now, we expect a future release will produce cleaner and more predictable results.

### Unmatched parameters are no longer related

TypeScript would previously relate parameters that didn't correspond to each other by relating them to the type `any`.
With [changes in TypeScript 4.1](https://github.com/microsoft/TypeScript/pull/41308), the language now skips this process entirely.
This means that some cases of assignability will now fail, but it also means that some cases of overload resolution can fail as well.
For example, overload resolution on `util.promisify` in Node.js may select a different overload in TypeScript 4.1, sometimes causing new or different errors downstream.

As a workaround, you may be best using a type assertion to squelch errors.

---

## Source: `packages/documentation/copy/en/release-notes/TypeScript 4.6.md`

---
title: TypeScript 4.6
layout: docs
permalink: /docs/handbook/release-notes/typescript-4-6.html
oneline: TypeScript 4.6 Release Notes
---

## Allowing Code in Constructors Before `super()`

In JavaScript classes it's mandatory to call `super()` before referring to `this`.
TypeScript enforces this as well, though it was a bit too strict in _how_ it ensured this.
In TypeScript, it was previously an error to contain _any_ code at the beginning of a constructor if its containing class had any property initializers.

```ts
class Base {
  // ...
}

class Derived extends Base {
  someProperty = true;

  constructor() {
    // error!
    // have to call 'super()' first because it needs to initialize 'someProperty'.
    doSomeStuff();
    super();
  }
}
```

This made it cheap to check that `super()` gets called before `this` is referenced, but it ended up rejecting a lot of valid code.
TypeScript 4.6 is now much more lenient in that check and permits other code to run before `super()`., all while still ensuring that `super()` occurs at the top-level before any references to `this`.

We'd like to extend our thanks to [Joshua Goldberg](https://github.com/JoshuaKGoldberg) for [patiently working with us to land this change](https://github.com/microsoft/TypeScript/pull/29374)!

## Control Flow Analysis for Destructured Discriminated Unions

TypeScript is able to narrow types based on what's called a discriminant property.
For example, in the following code snippet, TypeScript is able to narrow the type of `action` based on every time we check against the value of `kind`.

```ts
type Action =
  | { kind: "NumberContents"; payload: number }
  | { kind: "StringContents"; payload: string };

function processAction(action: Action) {
  if (action.kind === "NumberContents") {
    // `action.payload` is a number here.
    let num = action.payload * 2;
    // ...
  } else if (action.kind === "StringContents") {
    // `action.payload` is a string here.
    const str = action.payload.trim();
    // ...
  }
}
```

This lets us work with objects that can hold different data, but a common field tells us _which_ data those objects have.

This is very common in TypeScript; however, depending on your preferences, you might have wanted to destructure `kind` and `payload` in the example above.
Perhaps something like the following:

```ts
type Action =
  | { kind: "NumberContents"; payload: number }
  | { kind: "StringContents"; payload: string };

function processAction(action: Action) {
  const { kind, payload } = action;
  if (kind === "NumberContents") {
    let num = payload * 2;
    // ...
  } else if (kind === "StringContents") {
    const str = payload.trim();
    // ...
  }
}
```

Previously TypeScript would error on these - once `kind` and `payload` were extracted from the same object into variables, they were considered totally independent.

In TypeScript 4.6, this just works!

When destructuring individual properties into a `const` declaration, or when destructuring a parameter into variables that are never assigned to, TypeScript will check for if the destructured type is a discriminated union.
If it is, TypeScript can now narrow the types of variables depending on checks of other variables
So in our example, a check on `kind` narrows the type of `payload`.

For more information, [see the pull request that implemented this analysis](https://github.com/microsoft/TypeScript/pull/46266).

## Improved Recursion Depth Checks

TypeScript has some interesting challenges due to the fact that it's built on a structural type system that also provides generics.

In a structural type system, object types are compatible based on the members they have.

```ts
interface Source {
  prop: string;
}

interface Target {
  prop: number;
}

function check(source: Source, target: Target) {
  target = source;
  // error!
  // Type 'Source' is not assignable to type 'Target'.
  //   Types of property 'prop' are incompatible.
  //     Type 'string' is not assignable to type 'number'.
}
```

Notice that whether or not `Source` is compatible with `Target` has to do with whether their _properties_ are assignable.
In this case, that's just `prop`.

When you introduce generics into this, there are some harder questions to answer.
For instance, is a `Source<string>` assignable to a `Target<number>` in the following case?

```ts
interface Source<T> {
  prop: Source<Source<T>>;
}

interface Target<T> {
  prop: Target<Target<T>>;
}

function check(source: Source<string>, target: Target<number>) {
  target = source;
}
```

In order to answer that, TypeScript needs to check whether the types of `prop` are compatible.
That leads to the another question: is a `Source<Source<string>>` assignable to a `Target<Target<number>>`?
To answer that, TypeScript checks whether `prop` is compatible for _those_ types, and ends up checking whether `Source<Source<Source<string>>>` is assignable to `Target<Target<Target<number>>>`.
Keep going for a bit, and you might notice that the type infinitely expands the more you dig in.

TypeScript has a few heuristics here - if a type _appears_ to be infinitely expanding after encountering a certain depth check, then it considers that the types _could_ be compatible.
This is usually enough, but embarrassingly there were some false-negatives that this wouldn't catch.

```ts
interface Foo<T> {
  prop: T;
}

declare let x: Foo<Foo<Foo<Foo<Foo<Foo<string>>>>>>;
declare let y: Foo<Foo<Foo<Foo<Foo<string>>>>>;

x = y;
```

A human reader can see that `x` and `y` should be incompatible in the above example.
While the types are deeply nested, that's just a consequence of how they were declared.
The heuristic was meant to capture cases where deeply-nested types were generated through exploring the types, not from when a developer wrote that type out themselves.

TypeScript 4.6 is now able to distinguish these cases, and correctly errors on the last example.
Additionally, because the language is no longer concerned with false-positives from explicitly-written types, TypeScript can conclude that a type is infinitely expanding much earlier, and save a bunch of work in checking for type compatibility.
As a result, libraries on DefinitelyTyped like `redux-immutable`, `react-lazylog`, and `yup` saw a 50% reduction in check-time.

You may already have this change because it was cherry-picked into TypeScript 4.5.3, but it is a notable feature of TypeScript 4.6 which you can read up more about [here](https://github.com/microsoft/TypeScript/pull/46599).

## Indexed Access Inference Improvements

TypeScript now can correctly infer to indexed access types which immediately index into a mapped object type.

```ts
interface TypeMap {
  number: number;
  string: string;
  boolean: boolean;
}

type UnionRecord<P extends keyof TypeMap> = {
  [K in P]: {
    kind: K;
    v: TypeMap[K];
    f: (p: TypeMap[K]) => void;
  };
}[P];

function processRecord<K extends keyof TypeMap>(record: UnionRecord<K>) {
  record.f(record.v);
}

// This call used to have issues - now works!
processRecord({
  kind: "string",
  v: "hello!",

  // 'val' used to implicitly have the type 'string | number | boolean',
  // but now is correctly inferred to just 'string'.
  f: (val) => {
    console.log(val.toUpperCase());
  },
});
```

This pattern was already supported and allowed TypeScript to understand that the call to `record.f(record.v)` is valid, but previously the call to `processRecord` would give poor inference results for `val`

TypeScript 4.6 improves this so that no type assertions are necessary within the call to `processRecord`.

For more information, you can [read up on the pull request](https://github.com/microsoft/TypeScript/pull/47109).

## Control Flow Analysis for Dependent Parameters

A signature can be declared with a rest parameter whose type is a discriminated union of tuples.

```ts
function func(...args: ["str", string] | ["num", number]) {
  // ...
}
```

What this says is that the arguments to `func` depends entirely on the first argument.
When the first argument is the string `"str"`, then its second argument has to be a `string`.
When its first argument is the string `"num"`, its second argument has to be a `number`.

In cases where TypeScript infers the type of a function from a signature like this, TypeScript can now narrow parameters that depend on each other.

```ts
type Func = (...args: ["a", number] | ["b", string]) => void;

const f1: Func = (kind, payload) => {
  if (kind === "a") {
    payload.toFixed(); // 'payload' narrowed to 'number'
  }
  if (kind === "b") {
    payload.toUpperCase(); // 'payload' narrowed to 'string'
  }
};

f1("a", 42);
f1("b", "hello");
```

For more information, [see the change on GitHub](https://github.com/microsoft/TypeScript/pull/47190).

## `--target es2022`

TypeScript's `--target` option now supports `es2022`.
This means features like class fields now have a stable output target where they can be preserved.
It also means that new built-in functionality like the [`at()` method on `Array`s](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/at), [`Object.hasOwn`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/hasOwn), or [the `cause` option on `new Error`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/Error#rethrowing_an_error_with_a_cause) can be used either with this new `--target` setting, or with `--lib es2022`.

This functionality was [implemented](https://github.com/microsoft/TypeScript/pull/46291) by [Kagami Sascha Rosylight (saschanaz)](https://github.com/saschanaz) over several PRs, and we're grateful for that contribution!

## Removed Unnecessary Arguments in `react-jsx`

Previously, when compiling code like the following in `--jsx react-jsx`

```tsx
export const el = <div>foo</div>;
```

TypeScript would produce the following JavaScript code:

```jsx
import { jsx as _jsx } from "react/jsx-runtime";
export const el = _jsx("div", { children: "foo" }, void 0);
```

That last `void 0` argument is unnecessary in this emit mode, and removing it can improve bundle sizes.

```diff
- export const el = _jsx("div", { children: "foo" }, void 0);
+ export const el = _jsx("div", { children: "foo" });
```

Thanks to [a pull request](https://github.com/microsoft/TypeScript/pull/47467) from [Alexander Tarasyuk](https://github.com/a-tarasyuk), TypeScript 4.6 now drops the `void 0` argument.

## JSDoc Name Suggestions

In JSDoc, you can document parameters using an `@param` tag.

```js
/**
 * @param x The first operand
 * @param y The second operand
 */
function add(x, y) {
  return x + y;
}
```

But what happens when these comments fall out of date?
What if we rename `x` and `y` to `a` and `b`?

```js
/**
 * @param x {number} The first operand
 * @param y {number} The second operand
 */
function add(a, b) {
  return a + b;
}
```

Previously TypeScript would only tell you about this when performing type-checking on JavaScript files - when using either the `checkJs` option, or adding a `// @ts-check` comment to the top of your file.

You can now get similar information for TypeScript files in your editor!
TypeScript now provides suggestions for when parameter names don't match between your function and its JSDoc comment.

![Suggestion diagnostics being shown in the editor for parameter names in JSDoc comments that don't match an actual parameter name.](https://devblogs.microsoft.com/typescript/wp-content/uploads/sites/11/2022/02/jsdoc-comment-suggestions-4-6.png)

[This change](https://github.com/microsoft/TypeScript/pull/47257) was provided courtesy of [Alexander Tarasyuk](https://github.com/a-tarasyuk)!

## More Syntax and Binding Errors in JavaScript

TypeScript has expanded its set of syntax and binding errors in JavaScript files.
You'll see these new errors if you open JavaScript files in an editor like Visual Studio or Visual Studio Code, or if you run JavaScript code through the TypeScript compiler - even if you don't turn on `checkJs` or add a `// @ts-check` comment to the top of your files.

As one example, if you have two declarations of a `const` in the same scope of a JavaScript file, TypeScript will now issue an error on those declarations.

```ts
const foo = 1234;
//    ~~~
// error: Cannot redeclare block-scoped variable 'foo'.

// ...

const foo = 5678;
//    ~~~
// error: Cannot redeclare block-scoped variable 'foo'.
```

As another example, TypeScript will let you know if a modifier is being incorrectly used.

```ts
function container() {
    export function foo() {
//  ~~~~~~
// error: Modifiers cannot appear here.
    }
}
```

These errors can be disabled by adding a `// @ts-nocheck` at the top of your file, but we're interested in hearing some early feedback about how it works for your JavaScript workflow.
You can easily try it out for Visual Studio Code by installing the [TypeScript and JavaScript Nightly Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode.vscode-typescript-next), and read up more on the [first](https://github.com/microsoft/TypeScript/pull/47067) and [second](https://github.com/microsoft/TypeScript/pull/47075) pull requests.

## TypeScript Trace Analyzer

Occasionally, teams may encounter types that are computationally expensive to create and compare against other types.
[TypeScript has a `--generateTrace` flag](https://github.com/microsoft/TypeScript/wiki/Performance#performance-tracing) to help identify some of those expensive types, or sometimes help diagnose issues in the TypeScript compiler.
While the information generated by `--generateTrace` can be useful (especially with some information added in TypeScript 4.6), it can often be hard to read in existing trace visualizers.

We recently published a tool called [@typescript/analyze-trace](https://www.npmjs.com/package/@typescript/analyze-trace) to get a more digestible view of this information.
While we don't expect everyone to need `analyze-trace`, we think it can come in handy for any team that is running into [build performance issues with TypeScript](https://github.com/microsoft/TypeScript/wiki/Performance).

For more information, [see the `analyze-trace` tool's repo](https://github.com/microsoft/typescript-analyze-trace).

## Breaking Changes

### Object Rests Drop Unspreadable Members from Generic Objects

Object rest expressions now drop members that appear to be unspreadable on generic objects.
In the following example...

```ts
class Thing {
  someProperty = 42;

  someMethod() {
    // ...
  }
}

function foo<T extends Thing>(x: T) {
  let { someProperty, ...rest } = x;

  // Used to work, is now an error!
  // Property 'someMethod' does not exist on type 'Omit<T, "someProperty" | "someMethod">'.
  rest.someMethod();
}
```

the variable `rest` used to have the type `Omit<T, "someProperty">` because TypeScript would strictly analyze which other properties were destructured.
This doesn't model how `...rest` would work in a destructuring from a non-generic type because `someMethod` would typically be dropped as well.
In TypeScript 4.6, the type of `rest` is `Omit<T, "someProperty" | "someMethod">`.

This can also come up in cases when destructuring from `this`.
When destructuring `this` using a `...rest` element, unspreadable and non-public members are now dropped, which is consistent with destructuring instances of a class in other places.

```ts
class Thing {
  someProperty = 42;

  someMethod() {
    // ...
  }

  someOtherMethod() {
    let { someProperty, ...rest } = this;

    // Used to work, is now an error!
    // Property 'someMethod' does not exist on type 'Omit<T, "someProperty" | "someMethod">'.
    rest.someMethod();
  }
}
```

For more details, [see the corresponding change here](https://github.com/microsoft/TypeScript/pull/47078).

### JavaScript Files Always Receive Grammar and Binding Errors

Previously, TypeScript would ignore most grammar errors in JavaScript apart from accidentally using TypeScript syntax in a JavaScript file.
TypeScript now shows JavaScript syntax and binding errors in your file, such as using incorrect modifiers, duplicate declarations, and more.
These will typically be most apparent in Visual Studio Code or Visual Studio, but can also occur when running JavaScript code through the TypeScript compiler.

You can explicitly turn these errors off by inserting a `// @ts-nocheck` comment at the top of your file.

For more information, see the [first](https://github.com/microsoft/TypeScript/pull/47067) and [second](https://github.com/microsoft/TypeScript/pull/47075) implementing pull requests for these features.

---

## Source: `packages/documentation/copy/en/release-notes/TypeScript 4.7.md`

---
title: TypeScript 4.7
layout: docs
permalink: /docs/handbook/release-notes/typescript-4-7.html
oneline: TypeScript 4.7 Release Notes
---

## ECMAScript Module Support in Node.js

For the last few years, Node.js has been working to support ECMAScript modules (ESM).
This has been a very difficult feature, since the Node.js ecosystem is built on a different module system called CommonJS (CJS).
Interoperating between the two brings large challenges, with many new features to juggle;
however, support for ESM in Node.js was largely implemented in Node.js 12 and later.
Around TypeScript 4.5 we rolled out nightly-only support for ESM in Node.js to get some feedback from users and let library authors ready themselves for broader support.

TypeScript 4.7 adds this functionality with two new `module` settings: `node16` and `nodenext`.

```jsonc
{
    "compilerOptions": {
        "module": "node16",
    }
}
```

These new modes bring a few high-level features which we'll explore here.

### `type` in `package.json` and New Extensions

Node.js supports [a new setting in `package.json`](https://nodejs.org/api/packages.html#packages_package_json_and_file_extensions) called `type`.
`"type"` can be set to either `"module"` or `"commonjs"`.

```jsonc
{
    "name": "my-package",
    "type": "module",

    "//": "...",
    "dependencies": {
    }
}
```

This setting controls whether `.js` and `.d.ts` files are interpreted as ES modules or CommonJS modules, and defaults to CommonJS when not set.
When a file is considered an ES module, a few different rules come into play compared to CommonJS:

* `import`/`export` statements can be used.
* Top-level `await` can be used
* Relative import paths need full extensions (we have to write `import "./foo.js"` instead of `import "./foo"`).
* Imports might resolve differently from dependencies in `node_modules`.
* Certain global-like values like `require` and `module` cannot be used directly.
* CommonJS modules get imported under certain special rules.

We'll come back to some of these.

To overlay the way TypeScript works in this system, `.ts` and `.tsx` files now work the same way.
When TypeScript finds a `.ts`, `.tsx`, `.js`, or `.jsx` file, it will walk up looking for a `package.json` to see whether that file is an ES module, and use that to determine:

* how to find other modules which that file imports
* and how to transform that file if producing outputs

When a `.ts` file is compiled as an ES module, ECMAScript `import`/`export` statements are left alone in the `.js` output;
when it's compiled as a CommonJS module, it will produce the same output you get today under `--module commonjs`.

This also means paths resolve differently between `.ts` files that are ES modules and ones that are CJS modules.
For example, let's say you have the following code today:

```ts
// ./foo.ts
export function helper() {
    // ...
}

// ./bar.ts
import { helper } from "./foo"; // only works in CJS

helper();
```

This code works in CommonJS modules, but will fail in ES modules because relative import paths need to use extensions.
As a result, it will have to be rewritten to use the extension of the *output* of `foo.ts` - so `bar.ts` will instead have to import from `./foo.js`.

```ts
// ./bar.ts
import { helper } from "./foo.js"; // works in ESM & CJS

helper();
```

This might feel a bit cumbersome at first, but TypeScript tooling like auto-imports and path completion will typically just do this for you.

One other thing to mention is the fact that this applies to `.d.ts` files too.
When TypeScript finds a `.d.ts` file in a package, it is interpreted based on the containing package.

### New File Extensions

The `type` field in `package.json` is nice because it allows us to continue using the `.ts` and `.js` file extensions which can be convenient;
however, you will occasionally need to write a file that differs from what `type` specifies.
You might also just prefer to always be explicit.

Node.js supports two extensions to help with this: `.mjs` and `.cjs`.
`.mjs` files are always ES modules, and `.cjs` files are always CommonJS modules, and there's no way to override these.

In turn, TypeScript supports two new source file extensions: `.mts` and `.cts`.
When TypeScript emits these to JavaScript files, it will emit them to `.mjs` and `.cjs` respectively.

Furthermore, TypeScript also supports two new declaration file extensions: `.d.mts` and `.d.cts`.
When TypeScript generates declaration files for `.mts` and `.cts`, their corresponding extensions will be `.d.mts` and `.d.cts`.

Using these extensions is entirely optional, but will often be useful even if you choose not to use them as part of your primary workflow.

### CommonJS Interoperability

Node.js allows ES modules to import CommonJS modules as if they were ES modules with a default export.

```ts
// ./foo.cts
export function helper() {
    console.log("hello world!");
}

// ./bar.mts
import foo from "./foo.cjs";

// prints "hello world!"
foo.helper();
```

In some cases, Node.js also synthesizes named exports from CommonJS modules, which can be more convenient.
In these cases, ES modules can use a "namespace-style" import (i.e. `import * as foo from "..."`), or named imports (i.e. `import { helper } from "..."`).

```ts
// ./foo.cts
export function helper() {
    console.log("hello world!");
}

// ./bar.mts
import { helper } from "./foo.cjs";

// prints "hello world!"
helper();
```

There isn't always a way for TypeScript to know whether these named imports will be synthesized, but TypeScript will err on being permissive and use some heuristics when importing from a file that is definitely a CommonJS module.

One TypeScript-specific note about interop is the following syntax:

```ts
import foo = require("foo");
```

In a CommonJS module, this just boils down to a `require()` call, and in an ES module, this imports [`createRequire`](https://nodejs.org/api/module.html#module_module_createrequire_filename) to achieve the same thing.
This will make code less portable on runtimes like the browser (which don't support `require()`), but will often be useful for interoperability.
In turn, you can write the above example using this syntax as follows:

```ts
// ./foo.cts
export function helper() {
    console.log("hello world!");
}

// ./bar.mts
import foo = require("./foo.cjs");

foo.helper()
```

Finally, it's worth noting that the only way to import ESM files from a CJS module is using dynamic `import()` calls.
This can present challenges, but is the behavior in Node.js today.

You can [read more about ESM/CommonJS interop in Node.js here](https://nodejs.org/api/esm.html#esm_interoperability_with_commonjs).

### `package.json` Exports, Imports, and Self-Referencing

Node.js supports [a new field for defining entry points in `package.json` called `"exports"`](https://nodejs.org/api/packages.html#packages_exports).
This field is a more powerful alternative to defining `"main"` in `package.json`, and can control what parts of your package are exposed to consumers.

Here's a `package.json` that supports separate entry-points for CommonJS and ESM:

```jsonc
// package.json
{
    "name": "my-package",
    "type": "module",
    "exports": {
        ".": {
            // Entry-point for `import "my-package"` in ESM
            "import": "./esm/index.js",

            // Entry-point for `require("my-package") in CJS
            "require": "./commonjs/index.cjs",
        },
    },

    // CJS fall-back for older versions of Node.js
    "main": "./commonjs/index.cjs",
}
```

There's a lot to this feature, [which you can read more about on the Node.js documentation](https://nodejs.org/api/packages.html).
Here we'll try to focus on how TypeScript supports it.

With TypeScript's original Node support, it would look for a `"main"` field, and then look for declaration files that corresponded to that entry.
For example, if `"main"` pointed to `./lib/index.js`, TypeScript would look for a file called `./lib/index.d.ts`.
A package author could override this by specifying a separate field called `"types"` (e.g. `"types": "./types/index.d.ts"`).

The new support works similarly with [import conditions](https://nodejs.org/api/packages.html).
By default, TypeScript overlays the same rules with import conditions - if you write an `import` from an ES module, it will look up the `import` field, and from a CommonJS module, it will look at the `require` field.
If it finds them, it will look for a corresponding declaration file.
If you need to point to a different location for your type declarations, you can add a `"types"` import condition.

```jsonc
// package.json
{
    "name": "my-package",
    "type": "module",
    "exports": {
        ".": {
            // Entry-point for `import "my-package"` in ESM
            "import": {
                // Where TypeScript will look.
                "types": "./types/esm/index.d.ts",

                // Where Node.js will look.
                "default": "./esm/index.js"
            },
            // Entry-point for `require("my-package") in CJS
            "require": {
                // Where TypeScript will look.
                "types": "./types/commonjs/index.d.cts",

                // Where Node.js will look.
                "default": "./commonjs/index.cjs"
            },
        }
    },

    // Fall-back for older versions of TypeScript
    "types": "./types/index.d.ts",

    // CJS fall-back for older versions of Node.js
    "main": "./commonjs/index.cjs"
}
```

> The `"types"` condition should always come first in `"exports"`.

It's important to note that the CommonJS entrypoint and the ES module entrypoint each needs its own declaration file, even if the contents are the same between them.
Every declaration file is interpreted either as a CommonJS module or as an ES module, based on its file extension and the `"type"` field of the `package.json`, and this detected module kind must match the module kind that Node will detect for the corresponding JavaScript file for type checking to be correct.
Attempting to use a single `.d.ts` file to type both an ES module entrypoint and a CommonJS entrypoint will cause TypeScript to think only one of those entrypoints exists, causing compiler errors for users of the package.

TypeScript also supports [the `"imports"` field of `package.json`](https://nodejs.org/api/packages.html#packages_imports) in a similar manner by looking for declaration files alongside corresponding files, and supports [packages self-referencing themselves](https://nodejs.org/api/packages.html#packages_self_referencing_a_package_using_its_name).
These features are generally not as involved to set up, but are supported.

### Your Feedback Wanted!

As we continue working on TypeScript 4.7, we expect to see more documentation and polish go into this functionality.
Supporting these new features has been an ambitious under-taking, and that's why we're looking for early feedback on it!
Please try it out and let us know how it works for you.

For more information, [you can see the implementing PR here](https://github.com/microsoft/TypeScript/pull/44501).

## Control over Module Detection

One issue with the introduction of modules to JavaScript was the ambiguity between existing "script" code and the new module code.
JavaScript code in a module runs slightly differently, and has different scoping rules, so tools have to make decisions as to how each file runs.
For example, Node.js requires module entry-points to be written in a `.mjs`, or have a nearby `package.json` with `"type": "module"`.
TypeScript treats a file as a module whenever it finds any `import` or `export` statement in a file, but otherwise, will assume a `.ts` or `.js` file is a script file acting on the global scope.

This doesn't quite match up with the behavior of Node.js where the `package.json` can change the format of a file, or the `--jsx` setting `react-jsx`, where any JSX file contains an implicit import to a JSX factory.
It also doesn't match modern expectations where most new TypeScript code is written with modules in mind.

That's why TypeScript 4.7 introduces a new option called `moduleDetection`.
`moduleDetection` can take on 3 values: `"auto"` (the default), `"legacy"` (the same behavior as 4.6 and prior), and `"force"`.

Under the mode `"auto"`, TypeScript will not only look for `import` and `export` statements, but it will also check whether

* the `"type"` field in `package.json` is set to `"module"` when running under `--module nodenext`/`--module node16`, and
* check whether the current file is a JSX file when running under `--jsx react-jsx`

In cases where you want every file to be treated as a module, the `"force"` setting ensures that every non-declaration file is treated as a module.
This will be true regardless of how `module`, `moduleResolution`, and `jsx` are configured.

Meanwhile, the `"legacy"` option simply goes back to the old behavior of only seeking out `import` and `export` statements to determine whether a file is a module.

You can [read up more about this change on the pull request](https://github.com/microsoft/TypeScript/pull/47495).

## Control-Flow Analysis for Bracketed Element Access

TypeScript 4.7 now narrows the types of element accesses when the indexed keys are literal types and unique symbols.
For example, take the following code:

```ts
const key = Symbol();

const numberOrString = Math.random() < 0.5 ? 42 : "hello";

const obj = {
    [key]: numberOrString,
};

if (typeof obj[key] === "string") {
    let str = obj[key].toUpperCase();
}
```

Previously, TypeScript would not consider any type guards on `obj[key]`, and would have no idea that `obj[key]` was really a `string`.
Instead, it would think that `obj[key]` was still a `string | number` and accessing `toUpperCase()` would trigger an error.

TypeScript 4.7 now knows that `obj[key]` is a string.

This also means that under `--strictPropertyInitialization`, TypeScript can correctly check that computed properties are initialized by the end of a constructor body.

```ts
// 'key' has type 'unique symbol'
const key = Symbol();

class C {
    [key]: string;

    constructor(str: string) {
        // oops, forgot to set 'this[key]'
    }

    screamString() {
        return this[key].toUpperCase();
    }
}
```

Under TypeScript 4.7, `--strictPropertyInitialization` reports an error telling us that the `[key]` property wasn't definitely assigned by the end of the constructor.

We'd like to extend our gratitude to [Oleksandr Tarasiuk](https://github.com/a-tarasyuk) who provided [this change](https://github.com/microsoft/TypeScript/pull/45974)!

## Improved Function Inference in Objects and Methods

TypeScript 4.7 can now perform more granular inferences from functions within objects and arrays.
This allows the types of these functions to consistently flow in a left-to-right manner just like for plain arguments.

```ts
declare function f<T>(arg: {
    produce: (n: string) => T,
    consume: (x: T) => void }
): void;

// Works
f({
    produce: () => "hello",
    consume: x => x.toLowerCase()
});

// Works
f({
    produce: (n: string) => n,
    consume: x => x.toLowerCase(),
});

// Was an error, now works.
f({
    produce: n => n,
    consume: x => x.toLowerCase(),
});

// Was an error, now works.
f({
    produce: function () { return "hello"; },
    consume: x => x.toLowerCase(),
});

// Was an error, now works.
f({
    produce() { return "hello" },
    consume: x => x.toLowerCase(),
});
```

Inference failed in some of these examples because knowing the type of their `produce` functions would indirectly request the type of `arg` before finding a good type for `T`.
TypeScript now gathers functions that could contribute to the inferred type of `T` and infers from them lazily.

For more information, you can [take a look at the specific modifications to our inference process](https://github.com/microsoft/TypeScript/pull/48538).

## Instantiation Expressions

Occasionally functions can be a bit more general than we want.
For example, let's say we had a `makeBox` function.

```ts
interface Box<T> {
    value: T;
}

function makeBox<T>(value: T) {
    return { value };
}
```

Maybe we want to create a more specialized set of functions for making `Box`es of `Wrench`es and `Hammer`s.
To do that today, we'd have to wrap `makeBox` in other functions, or use an explicit type for an alias of `makeBox`.

```ts
function makeHammerBox(hammer: Hammer) {
    return makeBox(hammer);
}

// or...

const makeWrenchBox: (wrench: Wrench) => Box<Wrench> = makeBox;
```

These work, but wrapping a call to `makeBox` is a bit wasteful, and writing the full signature of `makeWrenchBox` could get unwieldy.
Ideally, we would be able to say that we just want to alias `makeBox` while replacing all of the generics in its signature.

TypeScript 4.7 allows exactly that!
We can now take functions and constructors and feed them type arguments directly.

```ts
const makeHammerBox = makeBox<Hammer>;
const makeWrenchBox = makeBox<Wrench>;
```

So with this, we can specialize `makeBox` to accept more specific types and reject anything else.

```ts
const makeStringBox = makeBox<string>;

// TypeScript correctly rejects this.
makeStringBox(42);
```

This logic also works for constructor functions such as `Array`, `Map`, and `Set`.

```ts
// Has type `new () => Map<string, Error>`
const ErrorMap = Map<string, Error>;

// Has type `// Map<string, Error>`
const errorMap = new ErrorMap();
```

When a function or constructor is given type arguments, it will produce a new type that keeps all signatures with compatible type parameter lists, and replaces the corresponding type parameters with the given type arguments.
Any other signatures are dropped, as TypeScript will assume that they aren't meant to be used.

For more information on this feature, [check out the pull request](https://github.com/microsoft/TypeScript/pull/47607).

## `extends` Constraints on `infer` Type Variables

Conditional types are a bit of a power-user feature.
They allow us to match and infer against the shape of types, and make decisions based on them.
For example, we can write a conditional type that returns the first element of a tuple type if it's a `string`-like type.

```ts
type FirstIfString<T> =
    T extends [infer S, ...unknown[]]
        ? S extends string ? S : never
        : never;

 // string
type A = FirstIfString<[string, number, number]>;

// "hello"
type B = FirstIfString<["hello", number, number]>;

// "hello" | "world"
type C = FirstIfString<["hello" | "world", boolean]>;

// never
type D = FirstIfString<[boolean, number, string]>;
```

`FirstIfString` matches against any tuple with at least one element and grabs the type of the first element as `S`.
Then it checks if `S` is compatible with `string` and returns that type if it is.

Note that we had to use two conditional types to write this.
We could have written `FirstIfString` as follows:

```ts
type FirstIfString<T> =
    T extends [string, ...unknown[]]
        // Grab the first type out of `T`
        ? T[0]
        : never;
```

This works, but it's slightly more "manual" and less declarative.
Instead of just pattern-matching on the type and giving the first element a name, we have to fetch out the `0`th element of `T` with `T[0]`.
If we were dealing with types more complex than tuples, this could get a lot trickier, so `infer` can simplify things.

Using nested conditionals to infer a type and then match against that inferred type is pretty common.
To avoid that second level of nesting, TypeScript 4.7 now allows you to place a constraint on any `infer` type.

```ts
type FirstIfString<T> =
    T extends [infer S extends string, ...unknown[]]
        ? S
        : never;
```

This way, when TypeScript matches against `S`, it also ensures that `S` has to be a `string`.
If `S` isn't a `string`, it takes the false path, which in these cases is `never`.

For more details, you can [read up on the change on GitHub](https://github.com/microsoft/TypeScript/pull/48112).

## Optional Variance Annotations for Type Parameters

Let's take the following types.

```ts
interface Animal {
    animalStuff: any;
}

interface Dog extends Animal {
    dogStuff: any;
}

// ...

type Getter<T> = () => T;

type Setter<T> = (value: T) => void;
```

Imagine we had two different instances of `Getter`s.
Figuring out whether any two different `Getter`s are substitutable for one another depends entirely on `T`.
In the case of whether an assignment of `Getter<Dog>`&nbsp;&rarr;&nbsp;`Getter<Animal>` is valid, we have to check whether `Dog`&nbsp;&rarr;&nbsp;`Animal` is valid.
Because each type for `T` just gets related in the same "direction", we say that the `Getter` type is *covariant* on `T`.
On the other hand, checking whether `Setter<Dog>`&nbsp;&rarr;&nbsp;`Setter<Animal>` is valid involves checking whether `Animal`&nbsp;&rarr;&nbsp;`Dog` is valid.
That "flip" in direction is kind of like how in math, checking whether &minus;*x*&nbsp;&lt;&nbsp;*&minus;y* is the same as checking whether *y*&nbsp;&lt;&nbsp;*x*.
When we have to flip directions like this to compare `T`, we say that `Setter` is *contravariant* on `T`.

With TypeScript 4.7, we're now able to *explicitly* specify variance on type parameters.

So now, if we want to make it explicit that `Getter` is covariant on `T`, we can now give it an `out` modifier.

```ts
type Getter<out T> = () => T;
```

And similarly, if we also want to make it explicit that `Setter` is contravariant on `T`, we can give it an `in` modifier.

```ts
type Setter<in T> = (value: T) => void;
```

`out` and `in` are used here because a type parameter's variance depends on whether it's used in an *output* or an *input*.
Instead of thinking about variance, you can just think about if `T` is used in output and input positions.

There are also cases for using both `in` and `out`.

```ts
interface State<in out T> {
    get: () => T;
    set: (value: T) => void;
}
```

When a `T` is used in both an output and input position, it becomes *invariant*.
Two different `State<T>`s can't be interchanged unless their `T`s are the same.
In other words, `State<Dog>` and `State<Animal>` aren't substitutable for the other.

Now technically speaking, in a purely structural type system, type parameters and their variance don't really matter - you can just plug in types in place of each type parameter and check whether each matching member is structurally compatible.
So if TypeScript uses a structural type system, why are we interested in the variance of type parameters?
And why might we ever want to annotate them?

One reason is that it can be useful for a reader to explicitly see how a type parameter is used at a glance.
For much more complex types, it can be difficult to tell whether a type is meant to be read, written, or both.
TypeScript will also help us out if we forget to mention how that type parameter is used.
As an example, if we forgot to specify both `in` and `out` on `State`, we'd get an error.

```ts
interface State<out T> {
    //          ~~~~~
    // error!
    // Type 'State<sub-T>' is not assignable to type 'State<super-T>' as implied by variance annotation.
    //   Types of property 'set' are incompatible.
    //     Type '(value: sub-T) => void' is not assignable to type '(value: super-T) => void'.
    //       Types of parameters 'value' and 'value' are incompatible.
    //         Type 'super-T' is not assignable to type 'sub-T'.
    get: () => T;
    set: (value: T) => void;
}
```

Another reason is precision and speed!
TypeScript already tries to infer the variance of type parameters as an optimization.
By doing this, it can type-check larger structural types in a reasonable amount of time.
Calculating variance ahead of time allows the type-checker to skip deeper comparisons and just compare type arguments which can be *much* faster than comparing the full structure of a type over and over again.
But often there are cases where this calculation is still fairly expensive, and the calculation may find circularities that can't be accurately resolved, meaning there's no clear answer for the variance of a type.

```ts
type Foo<T> = {
    x: T;
    f: Bar<T>;
}

type Bar<U> = (x: Baz<U[]>) => void;

type Baz<V> = {
    value: Foo<V[]>;
}

declare let foo1: Foo<unknown>;
declare let foo2: Foo<string>;

foo1 = foo2;  // Should be an error but isn't ❌
foo2 = foo1;  // Error - correct ✅
```

Providing an explicit annotation can speed up type-checking at these circularities and provide better accuracy.
For instance, marking `T` as invariant in the above example can help stop the problematic assignment.

```diff
- type Foo<T> = {
+ type Foo<in out T> = {
      x: T;
      f: Bar<T>;
  }
```

We don't necessarily recommend annotating every type parameter with its variance;
For example, it's possible (but not recommended) to make variance a little stricter than is necessary, so TypeScript won't stop you from marking something as invariant if it's really just covariant, contravariant, or even independent.
So if you do choose to add explicit variance markers, we would encourage thoughtful and precise use of them.

But if you're working with deeply recursive types, especially if you're a library author, you may be interested in using these annotations to the benefit of your users.
Those annotations can provide wins in both accuracy and type-checking speed, which can even affect their code editing experience.
Determining when variance calculation is a bottleneck on type-checking time can be done experimentally, and determined using tooling like our [analyze-trace](https://github.com/microsoft/typescript-analyze-trace) utility.


For more details on this feature, you can [read up on the pull request](https://github.com/microsoft/TypeScript/pull/48240).

## Resolution Customization with `moduleSuffixes`

TypeScript 4.7 now supports a `moduleSuffixes` option to customize how module specifiers are looked up.

```jsonc
{
    "compilerOptions": {
        "moduleSuffixes": [".ios", ".native", ""]
    }
}
```

Given the above configuration, an import like the following...

```ts
import * as foo from "./foo";
```

will try to look at the relative files `./foo.ios.ts`, `./foo.native.ts`, and finally `./foo.ts`.

<aside>

Note that the empty string `""` in `moduleSuffixes` is necessary for TypeScript to also look-up `./foo.ts`.
In a sense, the default value for `moduleSuffixes` is `[""]`.

</aside>

This feature can be useful for React Native projects where each target platform can use a separate `tsconfig.json` with differing `moduleSuffixes`.

[The `moduleSuffixes` option](https://github.com/microsoft/TypeScript/pull/48189) was contributed thanks to [Adam Foxman](https://github.com/afoxman)!

## resolution-mode

With Node's ECMAScript resolution, the mode of the containing file and the syntax you use determines how imports are resolved;
however it would be useful to reference the types of a CommonJS module from an ECMAScript module, or vice-versa.

TypeScript now allows `/// <reference types="..." />` directives.

```ts
/// <reference types="pkg" resolution-mode="require" />

// or

/// <reference types="pkg" resolution-mode="import" />
```

Additionally, in nightly versions of TypeScript, `import type` can specify an import assertion to achieve something similar.

```ts
// Resolve `pkg` as if we were importing with a `require()`
import type { TypeFromRequire } from "pkg" assert {
    "resolution-mode": "require"
};

// Resolve `pkg` as if we were importing with an `import`
import type { TypeFromImport } from "pkg" assert {
    "resolution-mode": "import"
};

export interface MergedType extends TypeFromRequire, TypeFromImport {}
```

These import assertions can also be used on `import()` types.

```ts
export type TypeFromRequire =
    import("pkg", { assert: { "resolution-mode": "require" } }).TypeFromRequire;

export type TypeFromImport =
    import("pkg", { assert: { "resolution-mode": "import" } }).TypeFromImport;

export interface MergedType extends TypeFromRequire, TypeFromImport {}
```

The `import type` and `import()` syntaxes only support `resolution-mode` in [nightly builds of TypeScript](https://www.typescriptlang.org/docs/handbook/nightly-builds.html).
You'll likely get an error like

```
Resolution mode assertions are unstable. Use nightly TypeScript to silence this error. Try updating with 'npm install -D typescript@next'.
```

If you do find yourself using this feature in nightly versions of TypeScript, [consider providing feedback on this issue](https://github.com/microsoft/TypeScript/issues/49055).

You can see the respective changes [for reference directives](https://github.com/microsoft/TypeScript/pull/47732) and [for type import assertions](https://github.com/microsoft/TypeScript/pull/47807).

## Go to Source Definition

TypeScript 4.7 contains support for a new experimental editor command called *Go To Source Definition*.
It's similar to *Go To Definition*, but it never returns results inside declaration files.
Instead, it tries to find corresponding *implementation* files (like `.js` or `.ts` files), and find definitions there &mdash; even if those files are normally shadowed by `.d.ts` files.

This comes in handy most often when you need to peek at the implementation of a function you're importing from a library instead of its type declaration in a `.d.ts` file.

![The "Go to Source Definition" command on a use of the yargs package jumps the editor to an index.cjs file in yargs.](https://devblogs.microsoft.com/typescript/wp-content/uploads/sites/11/2022/05/go-to-source-definition-4-7-v1.gif)

You can try this new command in the latest versions of Visual Studio Code.
Note, though, that this functionality is still in preview, and there are some known limitations.
In some cases TypeScript uses heuristics to guess which `.js` file corresponds to the given result of a definition, so these results might be inaccurate.
Visual Studio Code also doesn't yet indicate whether a result was a guess, but it's something we're collaborating on.

You can leave feedback about the feature, read about known limitations, or learn more at [our dedicated feedback issue](https://github.com/microsoft/TypeScript/issues/49003).

## Group-Aware Organize Imports

TypeScript has an *Organize Imports* editor feature for both JavaScript and TypeScript.
Unfortunately, it could be a bit of a blunt instrument, and would often naively sort your import statements.

For instance, if you ran Organize Imports on the following file...

```ts
// local code
import * as bbb from "./bbb";
import * as ccc from "./ccc";
import * as aaa from "./aaa";

// built-ins
import * as path from "path";
import * as child_process from "child_process"
import * as fs from "fs";

// some code...
```

You would get something like the following

```ts
// local code
import * as child_process from "child_process";
import * as fs from "fs";
// built-ins
import * as path from "path";
import * as aaa from "./aaa";
import * as bbb from "./bbb";
import * as ccc from "./ccc";


// some code...
```

This is... not ideal.
Sure, our imports are sorted by their paths, and our comments and newlines are preserved, but not in a way we expected.
Much of the time, if we have our imports grouped in a specific way, then we want to keep them that way.

TypeScript 4.7 performs Organize Imports in a group-aware manner.
Running it on the above code looks a little bit more like what you'd expect:

```ts
// local code
import * as aaa from "./aaa";
import * as bbb from "./bbb";
import * as ccc from "./ccc";

// built-ins
import * as child_process from "child_process";
import * as fs from "fs";
import * as path from "path";

// some code...
```

We'd like to extend our thanks to [Minh Quy](https://github.com/MQuy) who provided [this feature](https://github.com/microsoft/TypeScript/pull/48330).

## Object Method Snippet Completions

TypeScript now provides snippet completions for object literal methods.
When completing members in an object, TypeScript will provide a typical completion entry for just the name of a method, along with a separate completion entry for the full method definition!

![Completion a full method signature from an object](https://devblogs.microsoft.com/typescript/wp-content/uploads/sites/11/2022/05/object-method-completions-4-7-v2.gif)

For more details, [see the implementing pull request](https://github.com/microsoft/TypeScript/pull/48168).

## Breaking Changes

### `lib.d.ts` Updates

While TypeScript strives to avoid major breaks, even small changes in the built-in libraries can cause issues.
We don't expect major breaks as a result of DOM and `lib.d.ts` updates, but there may be some small ones.

### Stricter Spread Checks in JSX

When writing a `...spread` in JSX, TypeScript now enforces stricter checks that the given type is actually an object.
As a result, values with the types `unknown` and `never` (and more rarely, just bare `null` and `undefined`) can no longer be spread into JSX elements.

So for the following example:

```tsx
import * as React from "react";

interface Props {
    stuff?: string;
}

function MyComponent(props: unknown) {
    return <div {...props} />;
}
```

you'll now receive an error like the following:

```
Spread types may only be created from object types.
```

This makes this behavior more consistent with spreads in object literals.

For more details, [see the change on GitHub](https://github.com/microsoft/TypeScript/pull/48570).

### Stricter Checks with Template String Expressions

When a `symbol` value is used in a template string, it will trigger a runtime error in JavaScript.

```js
let str = `hello ${Symbol()}`;
// TypeError: Cannot convert a Symbol value to a string
```

As a result, TypeScript will issue an error as well;
however, TypeScript now also checks if a generic value that is constrained to a symbol in some way is used in a template string.

```ts
function logKey<S extends string | symbol>(key: S): S {
    // Now an error.
    console.log(`${key} is the key`);
    return key;
}

function get<T, K extends keyof T>(obj: T, key: K) {
    // Now an error.
    console.log(`Grabbing property '${key}'.`);
    return obj[key];
}
```

TypeScript will now issue the following error:

```
Implicit conversion of a 'symbol' to a 'string' will fail at runtime. Consider wrapping this expression in 'String(...)'.
```

In some cases, you can get around this by wrapping the expression in a call to `String`, just like the error message suggests.

```ts
function logKey<S extends string | symbol>(key: S): S {
    // No longer an error.
    console.log(`${String(key)} is the key`);
    return key;
}
```

In others, this error is too pedantic, and you might not ever care to even allow `symbol` keys when using `keyof`.
In such cases, you can switch to `string & keyof ...`:

```ts
function get<T, K extends string & keyof T>(obj: T, key: K) {
    // No longer an error.
    console.log(`Grabbing property '${key}'.`);
    return obj[key];
}
```

For more information, you can [see the implementing pull request](https://github.com/microsoft/TypeScript/pull/44578).

### `readFile` Method is No Longer Optional on `LanguageServiceHost`

If you're creating `LanguageService` instances, then provided `LanguageServiceHost`s will need to provide a `readFile` method.
This change was necessary to support the new `moduleDetection` compiler option.

You can [read more on the change here](https://github.com/microsoft/TypeScript/pull/47495).

### `readonly` Tuples Have a `readonly` `length` Property

A `readonly` tuple will now treat its `length` property as `readonly`.
This was almost never witnessable for fixed-length tuples, but was an oversight which could be observed for tuples with trailing optional and rest element types.

As a result, the following code will now fail:

```ts
function overwriteLength(tuple: readonly [string, string, string]) {
    // Now errors.
    tuple.length = 7;
}
```

You can [read more on this change here](https://github.com/microsoft/TypeScript/pull/47717).

---

## Source: `packages/documentation/copy/en/release-notes/TypeScript 5.1.md`

---
title: TypeScript 5.1
layout: docs
permalink: /docs/handbook/release-notes/typescript-5-1.html
oneline: TypeScript 5.1 Release Notes
---

## Easier Implicit Returns for `undefined`-Returning Functions

In JavaScript, if a function finishes running without hitting a `return`, it returns the value `undefined`.

```ts
function foo() {
    // no return
}
// x = undefined
let x = foo();
```

However, in previous versions of TypeScript, the *only* functions that could have absolutely no return statements were `void`- and `any`-returning functions.
That meant that even if you explicitly said "this function returns `undefined`" you were forced to have at least one return statement.

```ts
// ✅ fine - we inferred that 'f1' returns 'void'
function f1() {
    // no returns
}
// ✅ fine - 'void' doesn't need a return statement
function f2(): void {
    // no returns
}
// ✅ fine - 'any' doesn't need a return statement
function f3(): any {
    // no returns
}
// ❌ error!
// A function whose declared type is neither 'void' nor 'any' must return a value.
function f4(): undefined {
    // no returns
}
```

This could be a pain if some API expected a function returning `undefined` - you would need to have either at least one explicit return of `undefined` or a `return` statement *and* an explicit annotation.

```ts
declare function takesFunction(f: () => undefined): undefined;
// ❌ error!
// Argument of type '() => void' is not assignable to parameter of type '() => undefined'.
takesFunction(() => {
    // no returns
});
// ❌ error!
// A function whose declared type is neither 'void' nor 'any' must return a value.
takesFunction((): undefined => {
    // no returns
});
// ❌ error!
// Argument of type '() => void' is not assignable to parameter of type '() => undefined'.
takesFunction(() => {
    return;
});
// ✅ works
takesFunction(() => {
    return undefined;
});
// ✅ works
takesFunction((): undefined => {
    return;
});
```

This behavior was frustrating and confusing, especially when calling functions outside of one's control.
Understanding the interplay between inferring `void` over `undefined`, whether an `undefined`-returning function needs a `return` statement, etc. seems like a distraction.

First, TypeScript 5.1 now allows `undefined`-returning functions to have no return statement.

```ts
// ✅ Works in TypeScript 5.1!
function f4(): undefined {
    // no returns
}
// ✅ Works in TypeScript 5.1!
takesFunction((): undefined => {
    // no returns
});
```

Second, if a function has no return expressions and is being passed to something expecting a function that returns `undefined`, TypeScript infers `undefined` for that function's return type.

```ts
// ✅ Works in TypeScript 5.1!
takesFunction(function f() {
    //                 ^ return type is undefined
    // no returns
});
// ✅ Works in TypeScript 5.1!
takesFunction(function f() {
    //                 ^ return type is undefined
    return;
});
```

To address another similar pain-point, under TypeScript's `--noImplicitReturns` option, functions returning *only* `undefined` now have a similar exception to `void`, in that not every single code path must end in an explicit `return`.

```ts
// ✅ Works in TypeScript 5.1 under '--noImplicitReturns'!
function f(): undefined {
    if (Math.random()) {
        // do some stuff...
        return;
    }
}
```

For more information, you can read up on [the original issue](https://github.com/microsoft/TypeScript/issues/36288) and [the implementing pull request](https://github.com/microsoft/TypeScript/pull/53607).

## Unrelated Types for Getters and Setters

TypeScript 4.3 made it possible to say that a `get` and `set` accessor pair might specify two different types.

```ts
interface Serializer {
    set value(v: string | number | boolean);
    get value(): string;
}
declare let box: Serializer;
// Allows writing a 'boolean'
box.value = true;
// Comes out as a 'string'
console.log(box.value.toUpperCase());
```

Initially we required that the `get` type had to be a subtype of the `set` type.
This meant that writing

```ts
box.value = box.value;
```

would always be valid.

However, there are plenty of existing and proposed APIs that have completely unrelated types between their getters and setters.
For example, consider one of the most common examples - the `style` property in the DOM and [`CSSStyleRule`](https://developer.mozilla.org/en-US/docs/Web/API/CSSStyleRule) API.
Every style rule has [a `style` property](https://developer.mozilla.org/en-US/docs/Web/API/CSSStyleRule/style) that is a [`CSSStyleDeclaration`](https://developer.mozilla.org/en-US/docs/Web/API/CSSStyleDeclaration);
however, if you try to write to that property, it will only work correctly with a string!

TypeScript 5.1 now allows completely unrelated types for `get` and `set` accessor properties, provided that they have explicit type annotations.
And while this version of TypeScript does not yet change the types for these built-in interfaces, `CSSStyleRule` can now be defined in the following way:

```ts
interface CSSStyleRule {
    // ...
    /** Always reads as a `CSSStyleDeclaration` */
    get style(): CSSStyleDeclaration;
    /** Can only write a `string` here. */
    set style(newValue: string);
    // ...
}
```

This also allows other patterns like requiring `set` accessors to accept only "valid" data, but specifying that `get` accessors may return `undefined` if some underlying state hasn't been initialized yet.

```ts
class SafeBox {
    #value: string | undefined;
    // Only accepts strings!
    set value(newValue: string) {
    }
    // Must check for 'undefined'!
    get value(): string | undefined {
        return this.#value;
    }
}
```

In fact, this is similar to how optional properties are checked under `--exactOptionalProperties`.

You can read up more on [the implementing pull request](https://github.com/microsoft/TypeScript/pull/53417).

## Decoupled Type-Checking Between JSX Elements and JSX Tag Types

One pain point TypeScript had with JSX was its requirements on the type of every JSX element's tag.

For context, a JSX element is either of the following:

```tsx
// A self-closing JSX tag
<Foo />
// A regular element with an opening/closing tag
<Bar></Bar>
```

When type-checking `<Foo />` or `<Bar></Bar>`, TypeScript always looks up a namespace called `JSX` and fetches a type out of it called `Element` - or more directly, it looks up `JSX.Element`.

But to check whether `Foo` or `Bar` themselves were valid to use as tag names, TypeScript would roughly just grab the types returned or constructed by `Foo` or `Bar` and check for compatibility with `JSX.Element` (or another type called `JSX.ElementClass` if the type is constructable).

The limitations here meant that components could not be used if they returned or "rendered" a more broad type than just `JSX.Element`.
For example, a JSX library might be fine with a component returning `string`s or `Promise`s.

As a more concrete example, [React is considering adding limited support for components that return `Promise`s](https://github.com/acdlite/rfcs/blob/first-class-promises/text/0000-first-class-support-for-promises.md), but existing versions of TypeScript cannot express that without someone drastically loosening the type of `JSX.Element`.

```tsx
import * as React from "react";
async function Foo() {
    return <div></div>;
}
let element = <Foo />;
//             ~~~
// 'Foo' cannot be used as a JSX component.
//   Its return type 'Promise<Element>' is not a valid JSX element.
```

To provide libraries with a way to express this, TypeScript 5.1 now looks up a type called `JSX.ElementType`.
`ElementType` specifies precisely what is valid to use as a tag in a JSX element.
So it might be typed today as something like

```tsx
namespace JSX {
    export type ElementType =
        // All the valid lowercase tags
        keyof IntrinsicAttributes
        // Function components
        (props: any) => Element
        // Class components
        new (props: any) => ElementClass;
    export interface IntrinsicAttributes extends /*...*/ {}
    export type Element = /*...*/;
    export type ElementClass = /*...*/;
}
```

We'd like to extend our thanks to [Sebastian Silbermann](https://github.com/eps1lon) who contributed [this change](https://github.com/microsoft/TypeScript/pull/51328)!

## Namespaced JSX Attributes

TypeScript now supports namespaced attribute names when using JSX.

```tsx
import * as React from "react";
// Both of these are equivalent:
const x = <Foo a:b="hello" />;
const y = <Foo a : b="hello" />;
interface FooProps {
    "a:b": string;
}
function Foo(props: FooProps) {
    return <div>{props["a:b"]}</div>;
}
```

Namespaced tag names are looked up in a similar way on `JSX.IntrinsicAttributes` when the first segment of the name is a lowercase name.

```tsx
// In some library's code or in an augmentation of that library:
namespace JSX {
    interface IntrinsicElements {
        ["a:b"]: { prop: string };
    }
}
// In our code:
let x = <a:b prop="hello!" />;
```

[This contribution](https://github.com/microsoft/TypeScript/pull/53799) was provided thanks to [Oleksandr Tarasiuk](https://github.com/a-tarasyuk).

## `typeRoots` Are Consulted In Module Resolution

When TypeScript's specified module lookup strategy is unable to resolve a path, it will now resolve packages relative to the specified `typeRoots`.

See [this pull request](https://github.com/microsoft/TypeScript/pull/51715) for more details.

## Move Declarations to Existing Files

In addition to moving declarations to new files, TypeScript now ships a preview feature for moving declarations to existing files as well.
You can try this functionality out in a recent version of Visual Studio Code.

![Moving a function 'getThanks' to an existing file in the workspace.](https://devblogs.microsoft.com/typescript/wp-content/uploads/sites/11/2023/05/moveToFile-5.1-preview.gif)

Keep in mind that this feature is currently in preview, and we are seeking further feedback on it.

https://github.com/microsoft/TypeScript/pull/53542

## Linked Cursors for JSX Tags

TypeScript now supports *linked editing* for JSX tag names.
Linked editing (occasionally called "mirrored cursors") allows an editor to edit multiple locations at the same time automatically.

![An example of JSX tags with linked editing modifying a JSX fragment and a div element.](https://devblogs.microsoft.com/typescript/wp-content/uploads/sites/11/2023/04/linkedEditingJsx-5.1-1.gif)

This new feature should work in both TypeScript and JavaScript files, and can be enabled in Visual Studio Code Insiders.
In Visual Studio Code, you can either edit the `Editor: Linked Editing` option in the Settings UI:

![Visual Studio Code's Editor: Linked Editing` option](https://devblogs.microsoft.com/typescript/wp-content/uploads/sites/11/2023/04/linkedEditing-5.1-vscode-ui-1.png)

or configure `editor.linkedEditing` in your JSON settings file:

```jsonc
{
    // ...
    "editor.linkedEditing": true,
}
```

This feature will also be supported by Visual Studio 17.7 Preview 1.

You can take a look at [our implementation of linked editing](https://github.com/microsoft/TypeScript/pull/53284) here!

## Snippet Completions for `@param` JSDoc Tags

TypeScript now provides snippet completions when typing out a `@param` tag in both TypeScript and JavaScript files.
This can help cut down on some typing and jumping around text as you document your code or add JSDoc types in JavaScript.

![An example of completing JSDoc `param` comments on an 'add' function.](https://devblogs.microsoft.com/typescript/wp-content/uploads/sites/11/2023/04/paramTagSnippets-5-1-1.gif)

You can [check out how this new feature was implemented on GitHub](https://github.com/microsoft/TypeScript/pull/53260).

## Optimizations

### Avoiding Unnecessary Type Instantiation

TypeScript 5.1 now avoids performing type instantiation within object types that are known not to contain references to outer type parameters.
This has the potential to cut down on many unnecessary computations, and reduced the type-checking time of [material-ui's docs directory](https://github.com/mui/material-ui/tree/b0351248fb396001a30330daac86d0e0794a0c1d/docs) by over 50%.

You can [see the changes involved for this change on GitHub](https://github.com/microsoft/TypeScript/pull/53246).

### Negative Case Checks for Union Literals

When checking if a source type is part of a union type, TypeScript will first do a fast look-up using an internal type identifier for that source.
If that look-up fails, then TypeScript checks for compatibility against every type within the union.

When relating a literal type to a union of purely literal types, TypeScript can now avoid that full walk against every other type in the union.
This assumption is safe because TypeScript always interns/caches literal types - though there are some edge cases to handle relating to "fresh" literal types.

[This optimization](https://github.com/microsoft/TypeScript/pull/53192) was able to reduce the type-checking time of [the code in this issue](https://github.com/microsoft/TypeScript/issues/53191) from about 45 seconds to about 0.4 seconds.

### Reduced Calls into Scanner for JSDoc Parsing

When older versions of TypeScript parsed out a JSDoc comment, they would use the scanner/tokenizer to break the comment into fine-grained tokens and piece the contents back together.
This could be helpful for normalizing comment text, so that multiple spaces would just collapse into one;
but it was extremely "chatty" and meant the parser and scanner would jump back and forth very often, adding overhead to JSDoc parsing.

TypeScript 5.1 has moved more logic around breaking down JSDoc comments into the scanner/tokenizer.
The scanner now returns larger chunks of content directly to the parser to do as it needs.

[These changes](https://github.com/microsoft/TypeScript/pull/53081) have brought down the parse time of several 10Mb mostly-prose-comment JavaScript files by about half.
For a more realistic example, our performance suite's snapshot of [xstate](https://github.com/statelyai/xstate) dropped about 300ms of parse time, making it faster to load and analyze.

## Breaking Changes

### ES2020 and Node.js 14.17 as Minimum Runtime Requirements

TypeScript 5.1 now ships JavaScript functionality that was introduced in ECMAScript 2020.
As a result, at minimum TypeScript must be run in a reasonably modern runtime.
For most users, this means TypeScript now only runs on Node.js 14.17 and later.

If you try running TypeScript 5.1 under an older version of Node.js such as Node 10 or 12, you may see an error like the following from running either `tsc.js` or `tsserver.js`:

```
node_modules/typescript/lib/tsserver.js:2406
  for (let i = startIndex ?? 0; i < array.length; i++) {
                           ^
 
SyntaxError: Unexpected token '?'
    at wrapSafe (internal/modules/cjs/loader.js:915:16)
    at Module._compile (internal/modules/cjs/loader.js:963:27)
    at Object.Module._extensions..js (internal/modules/cjs/loader.js:1027:10)
    at Module.load (internal/modules/cjs/loader.js:863:32)
    at Function.Module._load (internal/modules/cjs/loader.js:708:14)
    at Function.executeUserEntryPoint [as runMain] (internal/modules/run_main.js:60:12)
    at internal/main/run_main_module.js:17:47
```

Additionally, if you try installing TypeScript you'll get something like the following error messages from npm:

```
npm WARN EBADENGINE Unsupported engine {
npm WARN EBADENGINE   package: 'typescript@5.1.1-rc',
npm WARN EBADENGINE   required: { node: '>=14.17' },
npm WARN EBADENGINE   current: { node: 'v12.22.12', npm: '8.19.2' }
npm WARN EBADENGINE }
```

from Yarn:

```
error typescript@5.1.1-rc: The engine "node" is incompatible with this module. Expected version ">=14.17". Got "12.22.12"
error Found incompatible module.
```

<!-- or from pnpm -->

[See more information around this change here](https://github.com/microsoft/TypeScript/pull/53291).

### Explicit `typeRoots` Disables Upward Walks for `node_modules/@types`

Previously, when the `typeRoots` option was specified in a `tsconfig.json` but resolution to any `typeRoots` directories had failed, TypeScript would still continue walking up parent directories, trying to resolve packages within each parent's `node_modules/@types` folder.

This behavior could prompt excessive look-ups and has been disabled in TypeScript 5.1.
As a result, you may begin to see errors like the following based on entries in your `tsconfig.json`'s `types` option or `/// <reference >` directives

```
error TS2688: Cannot find type definition file for 'node'.
error TS2688: Cannot find type definition file for 'mocha'.
error TS2688: Cannot find type definition file for 'jasmine'.
error TS2688: Cannot find type definition file for 'chai-http'.
error TS2688: Cannot find type definition file for 'webpack-env"'.
```

The solution is typically to add specific entries for `node_modules/@types` to your `typeRoots`:

```jsonc
{
    "compilerOptions": {
        "types": [
            "node",
            "mocha"
        ],
        "typeRoots": [
            // Keep whatever you had around before.
            "./some-custom-types/",
            // You might need your local 'node_modules/@types'.
            "./node_modules/@types",
            // You might also need to specify a shared 'node_modules/@types'
            // if you're using a "monorepo" layout.
            "../../node_modules/@types",
        ]
    }
}
```

More information is available [on the original change on our issue tracker](https://github.com/microsoft/TypeScript/pull/51715).

---

## Source: `packages/documentation/copy/en/release-notes/TypeScript 5.5.md`

---
title: TypeScript 5.5
layout: docs
permalink: /docs/handbook/release-notes/typescript-5-5.html
oneline: TypeScript 5.5 Release Notes
---

## Inferred Type Predicates

*This section was written by [Dan Vanderkam](https://github.com/danvk), who [implemented this feature in TypeScript 5.5](https://github.com/microsoft/TypeScript/pull/57465). Thanks Dan!*

TypeScript's control flow analysis does a great job of tracking how the type of a variable changes as it moves through your code:

```tsx
interface Bird {
    commonName: string;
    scientificName: string;
    sing(): void;
}

// Maps country names -> national bird.
// Not all nations have official birds (looking at you, Canada!)
declare const nationalBirds: Map<string, Bird>;

function makeNationalBirdCall(country: string) {
  const bird = nationalBirds.get(country);  // bird has a declared type of Bird | undefined
  if (bird) {
    bird.sing();  // bird has type Bird inside the if statement
  } else {
    // bird has type undefined here.
  }
}
```

By making you handle the `undefined` case, TypeScript pushes you to write more robust code.

In the past, this sort of type refinement was more difficult to apply to arrays. This would have been an error in all previous versions of TypeScript:

```tsx
function makeBirdCalls(countries: string[]) {
  // birds: (Bird | undefined)[]
  const birds = countries
    .map(country => nationalBirds.get(country))
    .filter(bird => bird !== undefined);

  for (const bird of birds) {
    bird.sing();  // error: 'bird' is possibly 'undefined'.
  }
}
```

This code is perfectly fine: we've filtered all the `undefined` values out of the list.
But TypeScript hasn't been able to follow along.

With TypeScript 5.5, the type checker is fine with this code:

```tsx
function makeBirdCalls(countries: string[]) {
  // birds: Bird[]
  const birds = countries
    .map(country => nationalBirds.get(country))
    .filter(bird => bird !== undefined);

  for (const bird of birds) {
    bird.sing();  // ok!
  }
}
```

Note the more precise type for `birds`.

This works because TypeScript now infers a [type predicate](https://www.typescriptlang.org/docs/handbook/2/narrowing.html#using-type-predicates) for the `filter` function.
You can see what's going on more clearly by pulling it out into a standalone function:

```tsx
// function isBirdReal(bird: Bird | undefined): bird is Bird
function isBirdReal(bird: Bird | undefined) {
  return bird !== undefined;
}
```

`bird is Bird` is the type predicate.
It means that, if the function returns `true`, then it's a `Bird` (if the function returns `false` then it's `undefined`).
The type declarations for `Array.prototype.filter` know about type predicates, so the net result is that you get a more precise type and the code passes the type checker.

TypeScript will infer that a function returns a type predicate if these conditions hold:

1. The function does not have an explicit return type or type predicate annotation.
2. The function has a single `return` statement and no implicit returns.
3. The function does not mutate its parameter.
4. The function returns a `boolean` expression that's tied to a refinement on the parameter.

Generally this works how you'd expect.
Here's a few more examples of inferred type predicates:

```tsx
// const isNumber: (x: unknown) => x is number
const isNumber = (x: unknown) => typeof x === 'number';

// const isNonNullish: <T>(x: T) => x is NonNullable<T>
const isNonNullish = <T,>(x: T) => x != null;
```

Previously, TypeScript would have just inferred that these functions return `boolean`.
It now infers signatures with type predicates like `x is number` or `x is NonNullable<T>`.

Type predicates have "if and only if" semantics.
If a function returns `x is T`, then it means that:

1. If the function returns `true` then `x` has the type `T`.
2. If the function returns `false` then `x` does *not* have type `T`.

If you're expecting a type predicate to be inferred but it's not, then you may be running afoul of the second rule. This often comes up with "truthiness" checks:

```tsx
function getClassroomAverage(students: string[], allScores: Map<string, number>) {
  const studentScores = students
    .map(student => allScores.get(student))
    .filter(score => !!score);

  return studentScores.reduce((a, b) => a + b) / studentScores.length;
  //     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  // error: Object is possibly 'undefined'.
}
```

TypeScript did not infer a type predicate for `score => !!score`, and rightly so: if this returns `true` then `score` is a `number`.
But if it returns `false`, then `score` could be either `undefined` or a `number` (specifically, `0`).
This is a real bug: if any student got a zero on the test, then filtering out their score will skew the average upwards.
Fewer will be above average and more will be sad!

As with the first example, it's better to explicitly filter out `undefined` values:

```tsx
function getClassroomAverage(students: string[], allScores: Map<string, number>) {
  const studentScores = students
    .map(student => allScores.get(student))
    .filter(score => score !== undefined);

  return studentScores.reduce((a, b) => a + b) / studentScores.length;  // ok!
}
```

A truthiness check *will* infer a type predicate for object types, where there's no ambiguity.
Remember that functions must return a `boolean` to be a candidate for an inferred type predicate: `x => !!x` might infer a type predicate, but `x => x` definitely won't.

Explicit type predicates continue to work exactly as before.
TypeScript will not check whether it would infer the same type predicate.
Explicit type predicates ("is") are no safer than a type assertion ("as").

It's possible that this feature will break existing code if TypeScript now infers a more precise type than you want. For example:

```tsx
// Previously, nums: (number | null)[]
// Now, nums: number[]
const nums = [1, 2, 3, null, 5].filter(x => x !== null);

nums.push(null);  // ok in TS 5.4, error in TS 5.5
```

The fix is to tell TypeScript the type that you want using an explicit type annotation:

```tsx
const nums: (number | null)[] = [1, 2, 3, null, 5].filter(x => x !== null);
nums.push(null);  // ok in all versions
```

For more information, check out the [implementing pull request](https://github.com/microsoft/TypeScript/pull/57465) and [Dan's blog post about implementing this feature](https://effectivetypescript.com/2024/04/16/inferring-a-type-predicate/).

## Control Flow Narrowing for Constant Indexed Accesses

TypeScript is now able to narrow expressions of the form `obj[key]` when both `obj` and `key` are effectively constant.

```ts
function f1(obj: Record<string, unknown>, key: string) {
    if (typeof obj[key] === "string") {
        // Now okay, previously was error
        obj[key].toUpperCase();
    }
}
```

In the above, neither `obj` nor `key` are ever mutated, so TypeScript can narrow the type of `obj[key]` to `string` after the `typeof` check.
For more information, [see the implementing pull request here](https://github.com/microsoft/TypeScript/pull/57847).

## The JSDoc `@import` Tag

Today, if you want to import something only for type-checking in a JavaScript file, it is cumbersome.
JavaScript developers can't simply import a type named `SomeType` if it's not there at runtime.

```js
// ./some-module.d.ts
export interface SomeType {
    // ...
}

// ./index.js
import { SomeType } from "./some-module"; // ❌ runtime error!

/**
 * @param {SomeType} myValue
 */
function doSomething(myValue) {
    // ...
}
```

`SomeType` won't exist at runtime, so the import will fail.
Developers can instead use a namespace import instead.

```js
import * as someModule from "./some-module";

/**
 * @param {someModule.SomeType} myValue
 */
function doSomething(myValue) {
    // ...
}
```

But `./some-module` is still imported at runtime - which might also not be desirable.

To avoid this, developers typically had to use `import(...)` types in JSDoc comments.

```js
/**
 * @param {import("./some-module").SomeType} myValue
 */
function doSomething(myValue) {
    // ...
}
```

If you wanted to reuse the same type in multiple places, you could use a `typedef` to avoid repeating the import.

```js
/**
 * @typedef {import("./some-module").SomeType} SomeType
 */

/**
 * @param {SomeType} myValue
 */
function doSomething(myValue) {
    // ...
}
```

This helps with local uses of `SomeType`, but it gets repetitive for many imports and can be a bit verbose.

That's why TypeScript now supports a new `@import` comment tag that has the same syntax as ECMAScript imports.

```js
/** @import { SomeType } from "some-module" */

/**
 * @param {SomeType} myValue
 */
function doSomething(myValue) {
    // ...
}
```

Here, we used named imports.
We could also have written our import as a namespace import.

```js
/** @import * as someModule from "some-module" */

/**
 * @param {someModule.SomeType} myValue
 */
function doSomething(myValue) {
    // ...
}
```

Because these are just JSDoc comments, they don't affect runtime behavior at all.

We would like to extend a big thanks to [Oleksandr Tarasiuk](https://github.com/a-tarasyuk) who contributed [this change](https://github.com/microsoft/TypeScript/pull/57207)!

## Regular Expression Syntax Checking

Until now, TypeScript has typically skipped over most regular expressions in code.
This is because regular expressions technically have an extensible grammar and TypeScript never made any effort to compile regular expressions to earlier versions of JavaScript.
Still, this meant that lots of common problems would go undiscovered in regular expressions, and they would either turn into errors at runtime, or silently fail.

But TypeScript now does basic syntax checking on regular expressions!

```ts
let myRegex = /@robot(\s+(please|immediately)))? do some task/;
//                                            ~
// error!
// Unexpected ')'. Did you mean to escape it with backslash?
```

This is a simple example, but this checking can catch a lot of common mistakes.
In fact, TypeScript's checking goes slightly beyond syntactic checks.
For instance, TypeScript can now catch issues around backreferences that don't exist.

```ts
let myRegex = /@typedef \{import\((.+)\)\.([a-zA-Z_]+)\} \3/u;
//                                                        ~
// error!
// This backreference refers to a group that does not exist.
// There are only 2 capturing groups in this regular expression.
```

The same applies to named capturing groups.

```ts
let myRegex = /@typedef \{import\((?<importPath>.+)\)\.(?<importedEntity>[a-zA-Z_]+)\} \k<namedImport>/;
//                                                                                        ~~~~~~~~~~~
// error!
// There is no capturing group named 'namedImport' in this regular expression.
```

TypeScript's checking is now also aware of when certain RegExp features are used when newer than your target version of ECMAScript.
For example, if we use named capturing groups like the above in an ES5 target, we'll get an error.

```ts
let myRegex = /@typedef \{import\((?<importPath>.+)\)\.(?<importedEntity>[a-zA-Z_]+)\} \k<importedEntity>/;
//                                  ~~~~~~~~~~~~         ~~~~~~~~~~~~~~~~
// error!
// Named capturing groups are only available when targeting 'ES2018' or later.
```

The same is true for certain regular expression flags as well.

Note that TypeScript's regular expression support is limited to regular expression *literals*.
If you try calling `new RegExp` with a string literal, TypeScript will not check the provided string.

We would like to thank [GitHub user graphemecluster](https://github.com/graphemecluster/) who iterated a ton with us [to get this feature into TypeScript](https://github.com/microsoft/TypeScript/pull/55600).

## Support for New ECMAScript `Set` Methods

TypeScript 5.5 declares [new proposed methods for the ECMAScript `Set` type](https://github.com/tc39/proposal-set-methods).

Some of these methods, like `union`, `intersection`, `difference`, and `symmetricDifference`, take another `Set` and return a new `Set` as the result.
The other methods, `isSubsetOf`, `isSupersetOf`, and `isDisjointFrom`, take another `Set` and return a `boolean`.
None of these methods mutate the original `Set`s.

Here's a quick example of how you might use these methods and how they behave:

```ts
let fruits = new Set(["apples", "bananas", "pears", "oranges"]);
let applesAndBananas = new Set(["apples", "bananas"]);
let applesAndOranges = new Set(["apples", "oranges"]);
let oranges = new Set(["oranges"]);
let emptySet = new Set();

////
// union
////

// Set(4) {'apples', 'bananas', 'pears', 'oranges'}
console.log(fruits.union(oranges));

// Set(3) {'apples', 'bananas', 'oranges'}
console.log(applesAndBananas.union(oranges));

////
// intersection
////

// Set(2) {'apples', 'bananas'}
console.log(fruits.intersection(applesAndBananas));

// Set(0) {}
console.log(applesAndBananas.intersection(oranges));

// Set(1) {'apples'}
console.log(applesAndBananas.intersection(applesAndOranges));

////
// difference
////

// Set(3) {'apples', 'bananas', 'pears'}
console.log(fruits.difference(oranges));

// Set(2) {'pears', 'oranges'}
console.log(fruits.difference(applesAndBananas));

// Set(1) {'bananas'}
console.log(applesAndBananas.difference(applesAndOranges));

////
// symmetricDifference
////

// Set(2) {'bananas', 'oranges'}
console.log(applesAndBananas.symmetricDifference(applesAndOranges)); // no apples

////
// isDisjointFrom
////

// true
console.log(applesAndBananas.isDisjointFrom(oranges));

// false
console.log(applesAndBananas.isDisjointFrom(applesAndOranges));

// true
console.log(fruits.isDisjointFrom(emptySet));

// true
console.log(emptySet.isDisjointFrom(emptySet));

////
// isSubsetOf
////

// true
console.log(applesAndBananas.isSubsetOf(fruits));

// false
console.log(fruits.isSubsetOf(applesAndBananas));

// false
console.log(applesAndBananas.isSubsetOf(oranges));

// true
console.log(fruits.isSubsetOf(fruits));

// true
console.log(emptySet.isSubsetOf(fruits));

////
// isSupersetOf
////

// true
console.log(fruits.isSupersetOf(applesAndBananas));

// false
console.log(applesAndBananas.isSupersetOf(fruits));

// false
console.log(applesAndBananas.isSupersetOf(oranges));

// true
console.log(fruits.isSupersetOf(fruits));

// false
console.log(emptySet.isSupersetOf(fruits));
```

We'd like to thank [Kevin Gibbons](https://github.com/bakkot) who not only co-championed the feature in ECMAScript, but [also provided the declarations for `Set`, `ReadonlySet`, and `ReadonlySetLike` in TypeScript](https://github.com/microsoft/TypeScript/pull/57230)!

## Isolated Declarations

*This section was co-authored by [Rob Palmer](https://github.com/robpalme) who supported the design of isolated declarations.*

Declaration files (a.k.a. `.d.ts` files) describe the shape of existing libraries and modules to TypeScript.
This lightweight description includes the library's type signatures and excludes implementation details such as the function bodies.
They are published so that TypeScript can efficiently check your usage of a library without needing to analyse the library itself.
Whilst it is possible to handwrite declaration files, if you are authoring typed code, it's much safer and simpler to let TypeScript generate them automatically from source files using `--declaration`.

The TypeScript compiler and its APIs have always had the job of generating declaration files;
however, there are some use-cases where you might want to use other tools, or where the traditional build process doesn't scale.

### Use-case: Faster Declaration Emit Tools

Imagine if you wanted to create a faster tool to generate declaration files, perhaps as part of a publishing service or a new bundler.
Whilst there is a thriving ecosystem of blazing fast tools that can turn TypeScript into JavaScript, the same is not true for turning TypeScript into declaration files.
The reason is that TypeScript's inference allows us to write code without explicitly declaring types, meaning declaration emit can be complex.

Let's consider a simple example of a function that adds two imported variables.

```ts
// util.ts
export let one = "1";
export let two = "2";

// add.ts
import { one, two } from "./util";
export function add() { return one + two; }
```

Even if the only thing we want to do is generate `add.d.ts`, TypeScript needs to crawl into another imported file (`util.ts`), infer that the type of `one` and `two` are strings, and then calculate that the `+` operator on two strings will lead to a `string` return type.

```ts
// add.d.ts
export declare function add(): string;
```

While this inference is important for the developer experience, it means that tools that want to generate declaration files would need to replicate parts of the type-checker including inference and the ability to resolve module specifiers to follow the imports.

### Use-case: Parallel Declaration Emit and Parallel Checking

Imagine if you had a monorepo containing many projects and a multi-core CPU that just wished it could help you check your code faster.
Wouldn't it be great if we could check all those projects at the same time by running each project on a different core?

Unfortunately we don't have the freedom to do all the work in parallel.
The reason is that we have to build those projects in dependency order, because each project is checking against the declaration files of their dependencies.
So we must build the dependency first to generate the declaration files.
TypeScript's project references feature works the same way, building the set of projects in "topological" dependency order.

As an example, if we have two projects called `backend` and `frontend`, and they both depend on a project called `core`, TypeScript can't start type-checking either `frontend` or `backend` until `core` has been built and its declaration files have been generated.

![frontend and backend point to core, other stuff might point to each of those](https://devblogs.microsoft.com/typescript/wp-content/uploads/sites/11/2024/04/5-5-beta-isolated-declarations-deps.png)

In the above graph, you can see that we have a bottleneck.
Whilst we can build `frontend` and `backend` in parallel, we need to first wait for `core` to finish building before either can start.

How could we improve upon this?
Well, if a fast tool could generate all those declaration files for `core` *in parallel*, TypeScript then could immediately follow that by type-checking `core`, `frontend`, and `backend` also *in parallel*.

### Solution: Explicit Types!

The common requirement in both use-cases is that we need a cross-file type-checker to generate declaration files.
Which is a lot to ask from the tooling community.

As a more complex example, if we want a declaration file for the following code...

```ts
import { add } from "./add";

const x = add();

export function foo() {
    return x;
}
```

...we would need to generate a signature for `foo`.
Well that requires looking at the implementation of `foo`.
`foo` just returns `x`, so getting the type of `x`  requires looking at the implementation of `add`.
But that might require looking at the implementation of `add`'s dependencies, and so on.
What we're seeing here is that generating declaration files requires a whole lot of logic to figure out the types of different places that might not even be local to the current file.

Still, for developers looking for fast iteration time and fully parallel builds, there is another way of thinking about this problem.
A declaration file only requires the types of the public API of a module - in other words, the types of the things that are exported.
If, controversially, developers are willing to explicitly write out the types of the things they export, tools could generate declaration files without needing to look at the implementation of the module - and without reimplementing a full type-checker.

This is where the new `--isolatedDeclarations` option comes in.
`--isolatedDeclarations` reports errors when a module can't be reliably transformed without a type-checker.
More plainly, it makes TypeScript report errors if you have a file that isn't sufficiently annotated on its exports.

That means in the above example, we would see an error like the following:

```ts
export function foo() {
//              ~~~
// error! Function must have an explicit
// return type annotation with --isolatedDeclarations.
    return x;
}
```

### Why are errors desirable?

Because it means that TypeScript can

1. Tell us up-front whether other tools will have issues with generating declaration files
2. Provide a quick fix to help add these missing annotations.

This mode doesn't require annotations *everywhere* though.
For locals, these can be ignored, since they don't affect the public API.
For example, the following code would **not** produce an error:

```ts
import { add } from "./add";

const x = add("1", "2"); // no error on 'x', it's not exported.

export function foo(): string {
    return x;
}
```

There are also certain expressions where the type is "trivial" to calculate.

```ts
// No error on 'x'.
// It's trivial to calculate the type is 'number'
export let x = 10;

// No error on 'y'.
// We can get the type from the return expression.
export function y() {
    return 20;
}

// No error on 'z'.
// The type assertion makes it clear what the type is.
export function z() {
    return Math.max(x, y()) as number;
}
```

### Using `isolatedDeclarations`

`isolatedDeclarations` requires that either the `declaration` or `composite` flags are also set.

Note that `isolatedDeclarations` does not change how TypeScript performs emit - just how it reports errors.
Importantly, and similar to `isolatedModules`, enabling the feature in TypeScript won't immediately bring about the potential benefits discussed here.
So please be patient and look forward to future developments in this space.
Keeping tool authors in mind, we should also recognize that today, not all of TypeScript's declaration emit can be easily replicated by other tools wanting to use it as a guide.
That's something we're actively working on improving.

On top of this, isolated declarations are still a new feature, and we're actively working on improving the experience.
Some scenarios, like using computed property declarations in classes and object literals, are not *yet* supported under `isolatedDeclarations`.
Keep an eye on this space, and feel free to provide us with feedback.

We also feel it is worth calling out that `isolatedDeclarations` should be adopted on a case-by-case basis.
There are some developer ergonomics that are lost when using `isolatedDeclarations`, and thus it may not be the right choice if your setup is not leveraging the two scenarios mentioned earlier.
For others, the work on `isolatedDeclarations` has already uncovered many optimizations and opportunities to unlock different parallel build strategies.
In the meantime, if you're willing to make the trade-offs, we believe `isolatedDeclarations` can be a powerful tool to speed up your build process as external tooling becomes more widely available.

For more information, read up on the [Isolated Declarations: State of the Feature](https://github.com/microsoft/TypeScript/issues/58944) discussion on the TypeScript issue tracker.

### Credit

Work on `isolatedDeclarations` has been a long-time collaborative effort between the TypeScript team and the infrastructure and tooling teams within Bloomberg and Google.
Individuals like Hana Joo from Google who implemented [the quick fix for isolated declaration errors](https://github.com/microsoft/TypeScript/pull/58260) (more on that soon), as well as Ashley Claymore, Jan Kühle, Lisa Velden, Rob Palmer, and Thomas Chetwin have been involved in discussion, specification, and implementation for many months.
But we feel it is specifically worth calling out the tremendous amount of work provided by [Titian Cernicova-Dragomir](https://github.com/dragomirtitian) from Bloomberg.
Titian has been instrumental in driving the implementation of `isolatedDeclarations` and has been a contributor to the TypeScript project for years prior.

While the feature involved many changes, you can see [the core work for Isolated Declarations here](https://github.com/microsoft/TypeScript/pull/58201).

## The `${configDir}` Template Variable for Configuration Files

It's common in many codebases to reuse a shared `tsconfig.json` file that acts as a "base" for other configuration files.
This is done by using the `extends` field in a `tsconfig.json` file.

```json
{
    "extends": "../../tsconfig.base.json",
    "compilerOptions": {
        "outDir": "./dist"
    }
}
```

One of the issues with this is that all paths in the `tsconfig.json` file are relative to the location of the file itself.
This means that if you have a shared `tsconfig.base.json` file that is used by multiple projects, relative paths often won't be useful in the derived projects.
For example, imagine the following `tsconfig.base.json`:

```json5
{
    "compilerOptions": {
        "typeRoots": [
            "./node_modules/@types",
            "./custom-types"
        ],
        "outDir": "dist"
    }
}
```

If author's intent was that every `tsconfig.json` that extends this file should

1. output to a `dist` directory relative to the derived `tsconfig.json` , and
1. have a `custom-types` directory relative to the derived `tsconfig.json`,

then this would not work.
The `typeRoots` paths would be relative to the location of the shared `tsconfig.base.json` file, not the project that extends it.
Each project that extends this shared file would need to declare its own `outDir` and `typeRoots` with identical contents.
This could be frustrating and hard to keep in sync between projects, and while the example above is using `typeRoots`, this is a common problem for `paths` and other options.

To solve this, TypeScript 5.5 introduces a new template variable `${configDir}`.
When `${configDir}` is written in certain path fields of a `tsconfig.json` or `jsconfig.json` files, this variable is substituted with the containing directory of the configuration file in a given compilation.
This means that the above `tsconfig.base.json` could be rewritten as:

```json5
{
    "compilerOptions": {
        "typeRoots": [
            "${configDir}/node_modules/@types",
            "${configDir}/custom-types"
        ],
        "outDir": "${configDir}/dist"
    }
}
```

Now, when a project extends this file, the paths will be relative to the derived `tsconfig.json`, not the shared `tsconfig.base.json` file.
This makes it easier to share configuration files across projects and ensures that the configuration files are more portable.

If you intend to make a `tsconfig.json` file extendable, consider if a `./` should instead be written with `${configDir}`.

For more information, see [the proposal issue](https://github.com/microsoft/TypeScript/issues/57485) and [the implementing pull request](https://github.com/microsoft/TypeScript/pull/58042).

## Consulting `package.json` Dependencies for Declaration File Generation

Previously, TypeScript would often issue an error message like

```
The inferred type of "X" cannot be named without a reference to "Y". This is likely not portable. A type annotation is necessary.
```

This was often due to TypeScript's declaration file generation finding itself in the contents of files that were never explicitly imported in a program.
Generating an import to such a file could be risky if the path ended up being relative.
Still, for codebases with explicit dependencies in the `dependencies` (or `peerDependencies` and `optionalDependencies`) of a `package.json`, generating such an import should be safe under certain resolution modes.
So in TypeScript 5.5, we're more lenient when that's the case, and many occurrences of this error should disappear.

[See this pull request](https://github.com/microsoft/TypeScript/issues/42873) for more details on the change.

## Editor and Watch-Mode Reliability Improvements

TypeScript has either added some new functionality or fixed existing logic that makes `--watch` mode and TypeScript's editor integration feel more reliable.
That should hopefully translate to fewer TSServer/editor restarts.

### Correctly Refresh Editor Errors in Configuration Files

TypeScript can generate errors for `tsconfig.json` files;
however, those errors are actually generated from loading a project, and editors typically don't directly request those errors for `tsconfig.json` files.
While this sounds like a technical detail, it means that when all errors issued in a `tsconfig.json` are fixed, TypeScript doesn't issue a new fresh empty set of errors, and users are left with stale errors unless they reload their editor.

TypeScript 5.5 now intentionally issues an event to clear these out.
[See more here](https://github.com/microsoft/TypeScript/pull/58120).

### Better Handling for Deletes Followed by Immediate Writes

Instead of overwriting files, some tools will opt to delete them and then create new files from scratch.
This is the case when running `npm ci`, for instance.

While this can be efficient for those tools, it can be problematic for TypeScript's editor scenarios where deleting a watched might dispose of it and all of its transitive dependencies.
Deleting and creating a file in quick succession could lead to TypeScript tearing down an entire project and then rebuilding it from scratch.

TypeScript 5.5 now has a more nuanced approach by keeping parts of a deleted project around until it picks up on a new creation event.
This should make operations like `npm ci` work a lot better with TypeScript.
See [more information on the approach here](https://github.com/microsoft/TypeScript/pull/57492).

### Symlinks are Tracked in Failed Resolutions

When TypeScript fails to resolve a module, it will still need to watch for any failed lookup paths in case the module is added later.
Previously this was not done for symlinked directories, which could cause reliability issues in monorepo-like scenarios when a build occurred in one project but was not witnessed in the other.
This should be fixed in TypeScript 5.5, and means you won't need to restart your editor as often.

[See more information here](https://github.com/microsoft/TypeScript/pull/58139).

### Project References Contribute to Auto-Imports

Auto-imports no longer requires at least one explicit import to dependent projects in a project reference setup.
Instead, auto-import completions should just work across anything you've listed in the `references` field of your `tsconfig.json`.

[See more on the implementing pull request](https://github.com/microsoft/TypeScript/pull/55955).

## Performance and Size Optimizations

### Monomorphized Objects in Language Service and Public API

In TypeScript 5.0, we ensured that our [`Node`](https://github.com/microsoft/TypeScript/pull/51682) and [`Symbol`](https://github.com/microsoft/TypeScript/pull/51880) objects had a consistent set of properties with a consistent initialization order.
Doing so helps reduce polymorphism in different operations, which allows runtimes to fetch properties more quickly.

By making this change, we witnessed impressive speed wins in the compiler;
however, most of these changes were performed on internal allocators for our data structures.
The language service, along with TypeScript's public API, uses a different set of allocators for certain objects.
This allowed the TypeScript compiler to be a bit leaner, as data used only for the language service would never be used in the compiler.

In TypeScript 5.5, the same monomorphization work has been done for the language service and public API.
What this means is that your editor experience, and any build tools that use the TypeScript API, will get a decent amount faster.
In fact, in our benchmarks, we've seen a **5-8% speedup in build times** when using the public TypeScript API's allocators, and **language service operations getting 10-20% faster**.
While this does imply an increase in memory, we believe that tradeoff is worth it and hope to find ways to reduce that memory overhead.
Things should feel a lot snappier now.

For more information, [see the change here](https://github.com/microsoft/TypeScript/pull/58045).

### Monomorphized Control Flow Nodes

In TypeScript 5.5, nodes of the control flow graph have been monomorphized so that they always hold a consistent shape.
By doing so, check times will often be reduced by about 1%.

[See this change here](https://github.com/microsoft/TypeScript/pull/57977).

### Optimizations on our Control Flow Graph

In many cases, control flow analysis will traverse nodes that don't provide any new information.
We observed that in the absence of any early termination or effects in the antecedents (or "dominators") of certain nodes meant that those nodes could always be skipped over.
As such, TypeScript now constructs its control flow graphs to take advantage of this by linking to an earlier node that *does* provide interesting information for control flow analysis.
This yields a flatter control flow graph, which can be more efficient to traverse.
This optimization has yielded modest gains, but with up to 2% reductions in build time on certain codebases.

You can [read more here](https://github.com/microsoft/TypeScript/pull/58013).

### Skipped Checking in `transpileModule` and `transpileDeclaration`

TypeScript's `transpileModule` API can be used for compiling a single TypeScript file's contents into JavaScript.
Similarly, the `transpileDeclaration` API (see below) can be used to generate a declaration file for a single TypeScript file.
One of the issues with these APIs is that TypeScript internally would perform a full type-checking pass over the entire contents of the file before emitting the output.
This was necessary to collect certain information which would later be used for the emit phase.

In TypeScript 5.5, we've found a way to avoid performing a full check, only lazily collecting this information as necessary, and `transpileModule` and `transpileDeclaration` both enable this functionality by default.
As a result, tools that integrate with these APIs, like [ts-loader](https://www.npmjs.com/package/ts-loader) with `transpileOnly` and [ts-jest](https://www.npmjs.com/package/ts-jest), should see a noticeable speedup.
In our testing, [we generally witness around a 2x speed-up in build time using `transpileModule`](https://github.com/microsoft/TypeScript/pull/58364#issuecomment-2138580690).

### TypeScript Package Size Reduction

Further leveraging [our transition to modules in 5.0](https://devblogs.microsoft.com/typescript/typescripts-migration-to-modules/), we've significantly reduced TypeScript's overall package size [by making `tsserver.js` and `typingsInstaller.js` import from a common API library instead of having each of them produce standalone bundles](https://github.com/microsoft/TypeScript/pull/55326).

This reduces TypeScript's size on disk from 30.2 MB to 20.4 MB, and reduces its packed size from 5.5 MB to 3.7 MB!

### Node Reuse in Declaration Emit

As part of the work to enable `isolatedDeclarations`, we've substantially improved how often TypeScript can directly copy your input source code when producing declaration files.

For example, let's say you wrote

```ts
export const strBool: string | boolean = "hello";
export const boolStr: boolean | string = "world";
```

Note that the union types are equivalent, but the order of the union is different.
When emitting the declaration file, TypeScript has two equivalent output possibilities.

The first is to use a consistent canonical representation for each type:

```ts
export const strBool: string | boolean;
export const boolStr: string | boolean;
```

The second is to re-use the type annotations exactly as written:

```ts
export const strBool: string | boolean;
export const boolStr: boolean | string;
```

The second approach is generally preferable for a few reasons:

* Many equivalent representations still encode some level of intent that is better to preserve in the declaration file
* Producing a fresh representation of a type can be somewhat expensive, so avoiding is better
* User-written types are usually shorter than generated type representations

In 5.5, we've greatly improved the number of places where TypeScript can correctly identify places where it's safe and correct to print back types exactly as they were written in the input file.
Many of these cases are invisible performance improvements - TypeScript would generate fresh sets of syntax nodes and serialize them into a string.
Instead, TypeScript can now operate over the original syntax nodes directly, which is much cheaper and faster.

### Caching Contextual Types from Discriminated Unions

When TypeScript asks for the contextual type of an expression like an object literal, it will often encounter a union type.
In those cases, TypeScript tries to filter out members of the union based on known properties with well known values (i.e. discriminant properties).
This work can be fairly expensive, especially if you end up with an object consisting of many many properties.
In TypeScript 5.5, [much of the computation is cached once so that TypeScript doesn't need to recompute it for every property in the object literal](https://github.com/microsoft/TypeScript/pull/58372).
Performing this optimization shaved 250ms off of compiling the TypeScript compiler itself.

## Easier API Consumption from ECMAScript Modules

Previously, if you were writing an ECMAScript module in Node.js, named imports were not available from the `typescript` package.

```ts
import { createSourceFile } from "typescript"; // ❌ error

import * as ts from "typescript";
ts.createSourceFile // ❌ undefined???

ts.default.createSourceFile // ✅ works - but ugh!
```

This is because [cjs-module-lexer](https://github.com/nodejs/cjs-module-lexer) did not recognize the pattern of TypeScript's generated CommonJS code.
This has been fixed, and users can now use named imports from the TypeScript npm package with ECMAScript modules in Node.js.

```ts
import { createSourceFile } from "typescript"; // ✅ works now!

import * as ts from "typescript";
ts.createSourceFile // ✅ works now!
```

For more information, [see the change here](https://github.com/microsoft/TypeScript/pull/57133).

## The `transpileDeclaration` API

TypeScript's API exposes a function called `transpileModule`.
It's intended to make it easy to compile a single file of TypeScript code.
Because it doesn't have access to an entire *program*, the caveat is that it may not produce the right output if the code violates any errors under the `isolatedModules` option.

In TypeScript 5.5, we've added a new similar API called `transpileDeclaration`.
This API is similar to `transpileModule`, but it's specifically designed to generate a single *declaration file* based on some input source text.
Just like `transpileModule`, it doesn't have access to a full program, and a similar caveat applies: it only generates an accurate declaration file if the input code is free of errors under the new `isolatedDeclarations` option.

If desired, this function can be used to parallelize declaration emit across all files under `isolatedDeclarations` mode.

For more information, [see the implementation here](https://github.com/microsoft/TypeScript/pull/58261).

## Notable Behavioral Changes

This section highlights a set of noteworthy changes that should be acknowledged and understood as part of any upgrade.
Sometimes it will highlight deprecations, removals, and new restrictions.
It can also contain bug fixes that are functionally improvements, but which can also affect an existing build by introducing new errors.

### Disabling Features Deprecated in TypeScript 5.0

TypeScript 5.0 deprecated the following options and behaviors:

* `charset`
* `target: ES3`
* `importsNotUsedAsValues`
* `noImplicitUseStrict`
* `noStrictGenericChecks`
* `keyofStringsOnly`
* `suppressExcessPropertyErrors`
* `suppressImplicitAnyIndexErrors`
* `out`
* `preserveValueImports`
* `prepend` in project references
* implicitly OS-specific `newLine`

To continue using the deprecated options above, developers using TypeScript 5.0 and other more recent versions have had to specify a new option called `ignoreDeprecations` with the value `"5.0"`.

In TypeScript 5.5, these options no longer have any effect.
To help with a smooth upgrade path, you may still specify them in your tsconfig, but these will be an error to specify in TypeScript 6.0.
See also the [Flag Deprecation Plan](https://github.com/microsoft/TypeScript/issues/51000) which outlines our deprecation strategy.

[More information around these deprecation plans is available on GitHub](https://github.com/microsoft/TypeScript/issues/51909), which contains suggestions in how to best adapt your codebase.

### `lib.d.ts` Changes

Types generated for the DOM may have an impact on type-checking your codebase.
For more information, [see the DOM updates for TypeScript 5.5](https://github.com/microsoft/TypeScript/pull/58211).

### Stricter Parsing for Decorators

Since TypeScript originally introduced support for decorators, the specified grammar for the proposal has been tightened up.
TypeScript is now stricter about what forms it allows.
While rare, existing decorators may need to be parenthesized to avoid errors.

```ts
class DecoratorProvider {
    decorate(...args: any[]) { }
}

class D extends DecoratorProvider {
    m() {
        class C {
            @super.decorate // ❌ error
            method1() { }

            @(super.decorate) // ✅ okay
            method2() { }
        }
    }
}
```

See [more information on the change here](https://github.com/microsoft/TypeScript/pull/57749).

### `undefined` is No Longer a Definable Type Name

TypeScript has always disallowed type alias names that conflict with built-in types:

```ts
// Illegal
type null = any;
// Illegal
type number = any;
// Illegal
type object = any;
// Illegal
type any = any;
```

Due to a bug, this logic didn't also apply to the built-in type `undefined`.
In 5.5, this is now correctly identified as an error:

```ts
// Now also illegal
type undefined = any;
```

Bare references to type aliases named `undefined` never actually worked in the first place.
You could define them, but you couldn't use them as an unqualified type name.

```ts
export type undefined = string;
export const m: undefined = "";
//           ^
// Errors in 5.4 and earlier - the local definition of 'undefined' was not even consulted.
```

For more information, [see the change here](https://github.com/microsoft/TypeScript/pull/57575).

### Simplified Reference Directive Declaration Emit

When producing a declaration file, TypeScript would synthesize a reference directive when it believed one was required.
For example, all Node.js modules are declared ambiently, so cannot be loaded by module resolution alone.
A file like:

```tsx
import path from "path";
export const myPath = path.parse(__filename);
```

Would emit a declaration file like:

```tsx
/// <reference types="node" />
import path from "path";
export declare const myPath: path.ParsedPath;
```

Even though the reference directive never appeared in the original source.

Similarly, TypeScript also *removed* reference directives that it did not believe needed to be a part of the output.
For example, let's imagine we had a reference directive to `jest`;
however, imagine the reference directive isn't necessary to generate the declaration file.
TypeScript would simply drop it.
So in the following example:

```tsx
/// <reference types="jest" />
import path from "path";
export const myPath = path.parse(__filename);
```

TypeScript would still emit:

```tsx
/// <reference types="node" />
import path from "path";
export declare const myPath: path.ParsedPath;
```

In the course of working on `isolatedDeclarations`, we realized that this logic was untenable for anyone attempting to implement a declaration emitter without type checking or using more than a single file's context.
This behavior is also hard to understand from a user's perspective; whether or not a reference directive appeared in the emitted file seems inconsistent and difficult to predict unless you understand exactly what's going on during typechecking.
To prevent declaration emit from being different when `isolatedDeclarations` was enabled, we knew that our emit needed to change.

Through [experimentation](https://github.com/microsoft/TypeScript/pull/57569), we found that nearly all cases where TypeScript synthesized reference directives were just to pull in `node` or `react`.
These are cases where the expectation is that a downstream user already references those types through tsconfig.json `"types"` or library imports, so no longer synthesizing these reference directives would be unlikely to break anyone.
It's worth noting that this is already how it works for `lib.d.ts`; TypeScript doesn't synthesize a reference to `lib="es2015"` when a module exports a `WeakMap`, instead assuming that a downstream user will have included that as part of their environment.

For reference directives that had been written by library authors (not synthesized), [further experimentation](https://github.com/microsoft/TypeScript/pull/57656) showed that nearly all were removed, never showing up in the output.
Most reference directives that were preserved were broken and likely not intended to be preserved.

Given those results, we decided to greatly simplfy reference directives in declaration emit in TypeScript 5.5.
A more consistent strategy will help library authors and consumers have better control of their declaration files.

Reference directives are no longer synthesized.
User-written reference directives are no longer preserved, unless annotated with a new `preserve="true"` attribute.
Concretely, an input file like:

```tsx
/// <reference types="some-lib" preserve="true" />
/// <reference types="jest" />
import path from "path";
export const myPath = path.parse(__filename);
```

will emit:

```tsx
/// <reference types="some-lib" preserve="true" />
import path from "path";
export declare const myPath: path.ParsedPath;
```

Adding `preserve="true"` is backwards compatible with older versions of TypeScript as unknown attributes are ignored.

This change also improved performance; in our benchmarks, the emit stage saw a 1-4% improvement in projects with declaration emit enabled.

---

## Source: `packages/documentation/copy/en/release-notes/TypeScript 5.9.md`

---
title: TypeScript 5.9
layout: docs
permalink: /docs/handbook/release-notes/typescript-5-9.html
oneline: TypeScript 5.9 Release Notes
---


## Minimal and Updated `tsc --init`

For a while, the TypeScript compiler has supported an `--init` flag that can create a `tsconfig.json` within the current directory.
In the last few years, running `tsc --init` created a very "full" `tsconfig.json`, filled with commented-out settings and their descriptions.
We designed this with the intent of making options discoverable and easy to toggle.

However, given external feedback (and our own experience), we found it's common to immediately delete most of the contents of these new `tsconfig.json` files.
When users want to discover new options, we find they rely on auto-complete from their editor, or navigate to [the tsconfig reference on our website](https://www.typescriptlang.org/tsconfig/) (which the generated `tsconfig.json` links to!).
What each setting does is also documented on that same page, and can be seen via editor hovers/tooltips/quick info.
While surfacing some commented-out settings might be helpful, the generated `tsconfig.json` was often considered overkill.

We also felt that it was time that `tsc --init` initialized with a few more prescriptive settings than we already enable.
We looked at some common pain points and papercuts users have when they create a new TypeScript project.
For example, most users write in modules (not global scripts), and `--moduleDetection` can force TypeScript to treat every implementation file as a module.
Developers also often want to use the latest ECMAScript features directly in their runtime, so `--target` can typically be set to `esnext`.
JSX users often find that going back to set `--jsx` is needless friction, and its options are slightly confusing.
And often, projects end up loading more declaration files from `node_modules/@types` than TypeScript actually needs; but specifying an empty `types` array can help limit this.

In TypeScript 5.9, a plain `tsc --init` with no other flags will generate the following `tsconfig.json`:

```json5
{
  // Visit https://aka.ms/tsconfig to read more about this file
  "compilerOptions": {
    // File Layout
    // "rootDir": "./src",
    // "outDir": "./dist",

    // Environment Settings
    // See also https://aka.ms/tsconfig_modules
    "module": "nodenext",
    "target": "esnext",
    "types": [],
    // For nodejs:
    // "lib": ["esnext"],
    // "types": ["node"],
    // and npm install -D @types/node

    // Other Outputs
    "sourceMap": true,
    "declaration": true,
    "declarationMap": true,

    // Stricter Typechecking Options
    "noUncheckedIndexedAccess": true,
    "exactOptionalPropertyTypes": true,

    // Style Options
    // "noImplicitReturns": true,
    // "noImplicitOverride": true,
    // "noUnusedLocals": true,
    // "noUnusedParameters": true,
    // "noFallthroughCasesInSwitch": true,
    // "noPropertyAccessFromIndexSignature": true,

    // Recommended Options
    "strict": true,
    "jsx": "react-jsx",
    "verbatimModuleSyntax": true,
    "isolatedModules": true,
    "noUncheckedSideEffectImports": true,
    "moduleDetection": "force",
    "skipLibCheck": true,
  }
}
```

For more details, see the [implementing pull request](https://github.com/microsoft/TypeScript/pull/61813) and [discussion issue](https://github.com/microsoft/TypeScript/issues/58420).

## Support for `import defer`

TypeScript 5.9 introduces support for [ECMAScript's deferred module evaluation proposal](https://github.com/tc39/proposal-defer-import-eval/) using the new `import defer` syntax.
This feature allows you to import a module without immediately executing the module and its dependencies, providing better control over when work and side-effects occur.

The syntax only permits namespace imports:

```ts
import defer * as feature from "./some-feature.js";
```

The key benefit of `import defer` is that the module is only evaluated when one of its exports is first accessed.
Consider this example:

```ts
// ./some-feature.ts
initializationWithSideEffects();

function initializationWithSideEffects() {
  // ...
  specialConstant = 42;

  console.log("Side effects have occurred!");
}

export let specialConstant: number;
```

When using `import defer`, the `initializationWithSideEffects()` function will not be called until you actually access a property of the imported namespace:

```ts
import defer * as feature from "./some-feature.js";

// No side effects have occurred yet

// ...

// As soon as `specialConstant` is accessed, the contents of the `feature`
// module are run and side effects have taken place.
console.log(feature.specialConstant); // 42
```

Because evaluation of the module is deferred until you access a member off of the module, you cannot use named imports or default imports with `import defer`:

```ts
// ❌ Not allowed
import defer { doSomething } from "some-module";

// ❌ Not allowed  
import defer defaultExport from "some-module";

// ✅ Only this syntax is supported
import defer * as feature from "some-module";
```

Note that when you write `import defer`, the module and its dependencies are fully loaded and ready for execution.
That means that the module will need to exist, and will be loaded from the file system or a network resource.
The key difference between a regular `import` and `import defer` is that *the execution of statements and declarations* is deferred until you access a property of the imported namespace.

This feature is particularly useful for conditionally loading modules with expensive or platform-specific initialization. It can also improve startup performance by deferring module evaluation for app features until they are actually needed.

Note that `import defer` is not transformed or "downleveled" at all by TypeScript.
It is intended to be used in runtimes that support the feature natively, or by tools such as bundlers that can apply the appropriate transformation.
That means that `import defer` will only work under the `--module` modes `preserve` and `esnext`.

We'd like to extend our thanks to [Nicolò Ribaudo](https://github.com/nicolo-ribaudo) who championed the proposal in TC39 and also provided [the implementation for this feature](https://github.com/microsoft/TypeScript/pull/60757).

## Support for `--module node20`

TypeScript provides several `node*` options for the `--module` and `--moduleResolution` settings.
Most recently, `--module nodenext` has supported the ability to `require()` ECMAScript modules from CommonJS modules, and correctly rejects import assertions (in favor of the standards-bound [import attributes](https://github.com/tc39/proposal-import-attributes)).

TypeScript 5.9 brings a stable option for these settings called `node20`, intended to model the behavior of Node.js v20.
This option is unlikely to have new behaviors in the future, unlike `--module nodenext` or `--moduleResolution nodenext`.
Also unlike `nodenext`, specifying `--module node20` will imply `--target es2023` unless otherwise configured.
`--module nodenext`, on the other hand, implies the floating `--target esnext`.

For more information, [take a look at the implementation here](https://github.com/microsoft/TypeScript/pull/61805).

## Summary Descriptions in DOM APIs

Previously, many of the DOM APIs in TypeScript only linked to the MDN documentation for the API.
These links were useful, but they didn't provide a quick summary of what the API does.
Thanks to a few changes from [Adam Naji](https://github.com/Bashamega), TypeScript now includes summary descriptions for many DOM APIs based on the MDN documentation.
You can see more of these changes [here](https://github.com/microsoft/TypeScript-DOM-lib-generator/pull/1993) and [here](https://github.com/microsoft/TypeScript-DOM-lib-generator/pull/1940).

## Expandable Hovers (Preview)

*Quick Info* (also called "editor tooltips" and "hovers") can be very useful for peeking at variables to see their types, or at type aliases to see what they actually refer to.
Still, it's common for people to want to *go deeper* and get details from whatever's displayed within the quick info tooltip.
For example, if we hover our mouse over the parameter `options` in the following example:

```ts
export function drawButton(options: Options): void
```

We're left with `(parameter) options: Options`.

![Tooltip for a parameter declared as `options` which just shows `options: Options`.](https://devblogs.microsoft.com/typescript/wp-content/uploads/sites/11/2025/06/bare-hover-5.8-01.png)

Do we really need to jump to the definition of the type `Options` just to see what members this value has?

Previously, that was actually the case.
To help here, TypeScript 5.9 is now previewing a feature called *expandable hovers*, or "quick info verbosity".
If you use an editor like VS Code, you'll now see a `+` and `-` button on the left of these hover tooltips.
Clicking on the `+` button will expand out types more deeply, while clicking on the `-` button will collapse to the last view.

<video autoplay loop style="width: 100%;" src="https://devblogs.microsoft.com/typescript/wp-content/uploads/sites/11/2025/06/expandable-quick-info-1.mp4" aria-label="Expanding quick info to see more about the type of `Options`."></video>

This feature is currently in preview, and we are seeking feedback for both TypeScript and our partners on Visual Studio Code.
For more details, see [the PR for this feature here](https://github.com/microsoft/TypeScript/pull/59940).

## Configurable Maximum Hover Length

Occasionally, quick info tooltips can become so long that TypeScript will truncate them to make them more readable.
The downside here is that often the most important information will be omitted from the hover tooltip, which can be frustrating.
To help with this, TypeScript 5.9's language server supports a configurable hover length, which can be configured in VS Code via the `js/ts.hover.maximumLength` setting.

Additionally, the new default hover length is substantially larger than the previous default.
This means that in TypeScript 5.9, you should see more information in your hover tooltips by default.
For more details, see [the PR for this feature here](https://github.com/microsoft/TypeScript/pull/61662) and [the corresponding change to Visual Studio Code here](https://github.com/microsoft/vscode/pull/248181).

## Optimizations

### Cache Instantiations on Mappers

When TypeScript replaces type parameters with specific type arguments, it can end up instantiating many of the same intermediate types over and over again.
In complex libraries like Zod and tRPC, this could lead to both performance issues and errors reported around excessive type instantiation depth.
Thanks to [a change](https://github.com/microsoft/TypeScript/pull/61505) from [Mateusz Burzyński](https://github.com/Andarist), TypeScript 5.9 is able to cache many intermediate instantiations when work has already begun on a specific type instantiation.
This in turn avoids lots of unnecessary work and allocations.

### Avoiding Closure Creation in `fileOrDirectoryExistsUsingSource`

In JavaScript, a function expression will typically allocate a new function object, even if the wrapper function is just passing through arguments to another function with no captured variables.
In code paths around file existence checks, [Vincent Bailly](https://github.com/VincentBailly) found examples of these pass-through function calls, even though the underlying functions only took single arguments.
Given the number of existence checks that could take place in larger projects, he cited a speed-up of around 11%.
[See more on this change here](https://github.com/microsoft/TypeScript/pull/61822/).

## Notable Behavioral Changes

### `lib.d.ts` Changes

Types generated for the DOM may have an impact on type-checking your codebase.

Additionally, one notable change is that `ArrayBuffer` has been changed in such a way that it is no longer a supertype of several different `TypedArray` types.
This also includes subtypes of `UInt8Array`, such as `Buffer` from Node.js.
As a result, you'll see new error messages such as:

```
error TS2345: Argument of type 'ArrayBufferLike' is not assignable to parameter of type 'BufferSource'.
error TS2322: Type 'ArrayBufferLike' is not assignable to type 'ArrayBuffer'.
error TS2322: Type 'Buffer' is not assignable to type 'Uint8Array<ArrayBufferLike>'.
error TS2322: Type 'Buffer' is not assignable to type 'ArrayBuffer'.
error TS2345: Argument of type 'Buffer' is not assignable to parameter of type 'string | Uint8Array<ArrayBufferLike>'.
```

If you encounter issues with `Buffer`, you may first want to check that you are using the latest version of the `@types/node` package.
This might include running

```
npm update @types/node --save-dev
```

Much of the time, the solution is to specify a more specific underlying buffer type instead of using the default `ArrayBufferLike` (i.e. explicitly writing out `Uint8Array<ArrayBuffer>` rather than a plain `Uint8Array`).
In instances where some `TypedArray` (like `Uint8Array`) is passed to a function expecting an `ArrayBuffer` or `SharedArrayBuffer`, you can also try accessing the `buffer` property of that `TypedArray` like in the following example:

```diff
  let data = new Uint8Array([0, 1, 2, 3, 4]);
- someFunc(data)
+ someFunc(data.buffer)
```

## Type Argument Inference Changes

In an effort to fix "leaks" of type variables during inference, TypeScript 5.9 may introduce changes in types and possibly new errors in some codebases.
These are hard to predict, but can often be fixed by adding type arguments to generic functions calls.
[See more details here](https://github.com/microsoft/TypeScript/pull/61668).

---

## Source: `packages/documentation/copy/en/tutorials/DOM Manipulation.md`

---
title: DOM Manipulation
layout: docs
permalink: /docs/handbook/dom-manipulation.html
oneline: Using the DOM with TypeScript
translatable: true
---

## DOM Manipulation

### _An exploration into the `HTMLElement` type_

In the 20+ years since its standardization, JavaScript has come a very long way. While in 2020, JavaScript can be used on servers, in data science, and even on IoT devices, it is important to remember its most popular use case: web browsers.

Websites are made up of HTML and/or XML documents. These documents are static, they do not change. The *Document Object Model (DOM)* is a programming interface implemented by browsers to make static websites functional. The DOM API can be used to change the document structure, style, and content. The API is so powerful that countless frontend frameworks (jQuery, React, Angular, etc.) have been developed around it to make dynamic websites even easier to develop.

TypeScript is a typed superset of JavaScript, and it ships type definitions for the DOM API. These definitions are readily available in any default TypeScript project. Of the 20,000+ lines of definitions in _lib.dom.d.ts_, one stands out among the rest: `HTMLElement`. This type is the backbone for DOM manipulation with TypeScript.

> You can explore the source code for the [DOM type definitions](https://github.com/microsoft/TypeScript/blob/main/src/lib/dom.generated.d.ts)

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

## The `Document` Interface

The first line of the TypeScript code uses a global variable `document`. Inspecting the variable shows it is defined by the `Document` interface from the _lib.dom.d.ts_ file. The code snippet contains calls to two methods, `getElementById` and `createElement`.

### `Document.getElementById`

The definition for this method is as follows:

```ts
getElementById(elementId: string): HTMLElement | null;
```

Pass it an element id string and it will return either `HTMLElement` or `null`. This method introduces one of the most important types, `HTMLElement`. It serves as the base interface for every other element interface. For example, the `p` variable in the code example is of type `HTMLParagraphElement`. Also, take note that this method can return `null`. This is because the method can't be certain pre-runtime if it will be able to actually find the specified element or not. In the last line of the code snippet, the new _optional chaining_ operator is used to call `appendChild`.

### `Document.createElement`

The definition for this method is (I have omitted the _deprecated_ definition):

```ts
createElement<K extends keyof HTMLElementTagNameMap>(tagName: K, options?: ElementCreationOptions): HTMLElementTagNameMap[K];
createElement(tagName: string, options?: ElementCreationOptions): HTMLElement;
```

This is an overloaded function definition. The second overload is simplest and works a lot like the `getElementById` method does. Pass it any `string` and it will return a standard HTMLElement. This definition is what enables developers to create unique HTML element tags.

For example `document.createElement('xyz')` returns a `<xyz></xyz>` element, clearly not an element that is specified by the HTML specification.

> For those interested, you can interact with custom tag elements using the `document.getElementsByTagName`

For the first definition of `createElement`, it is using some advanced generic patterns. It is best understood broken down into chunks, starting with the generic expression: `<K extends keyof HTMLElementTagNameMap>`. This expression defines a generic parameter `K` that is _constrained_ to the keys of the interface `HTMLElementTagNameMap`. The map interface contains every specified HTML tag name and its corresponding type interface. For example here are the first 5 mapped values:

```ts
interface HTMLElementTagNameMap {
    "a": HTMLAnchorElement;
    "abbr": HTMLElement;
    "address": HTMLElement;
    "applet": HTMLAppletElement;
    "area": HTMLAreaElement;
        ...
}
```

Some elements do not exhibit unique properties and so they just return `HTMLElement`, but other types do have unique properties and methods so they return their specific interface (which will extend from or implement `HTMLElement`).

Now, for the remainder of the `createElement` definition: `(tagName: K, options?: ElementCreationOptions): HTMLElementTagNameMap[K]`. The first argument `tagName` is defined as the generic parameter `K`. The TypeScript interpreter is smart enough to _infer_ the generic parameter from this argument. This means that the developer does not have to specify the generic parameter when using the method; whatever value is passed to the `tagName` argument will be inferred as `K` and thus can be used throughout the remainder of the definition. This is exactly what happens; the return value `HTMLElementTagNameMap[K]` takes the `tagName` argument and uses it to return the corresponding type. This definition is how the `p` variable from the code snippet gets a type of `HTMLParagraphElement`. And if the code was `document.createElement('a')`, then it would be an element of type `HTMLAnchorElement`.

## The `Node` interface

The `document.getElementById` function returns an `HTMLElement`. `HTMLElement` interface extends the `Element` interface which extends the `Node` interface. This prototypal extension allows for all `HTMLElements` to utilize a subset of standard methods. In the code snippet, we use a property defined on the `Node` interface to append the new `p` element to the website.

### `Node.appendChild`

The last line of the code snippet is `app?.appendChild(p)`. The previous, `document.getElementById`, section detailed that the _optional chaining_ operator is used here because `app` can potentially be null at runtime. The `appendChild` method is defined by:

```ts
appendChild<T extends Node>(newChild: T): T;
```

This method works similarly to the `createElement` method as the generic parameter `T` is inferred from the `newChild` argument. `T` is _constrained_ to another base interface `Node`.

## Difference between `children` and `childNodes`

Previously, this document details the `HTMLElement` interface extends from `Element` which extends from `Node`. In the DOM API there is a concept of _children_ elements. For example in the following HTML, the `p` tags are children of the `div` element

```tsx
<div>
  <p>Hello, World</p>
  <p>TypeScript!</p>
</div>;

const div = document.getElementsByTagName("div")[0];

div.children;
// HTMLCollection(2) [p, p]

div.childNodes;
// NodeList(2) [p, p]
```

After capturing the `div` element, the `children` prop will return an `HTMLCollection` list containing the `HTMLParagraphElements`. The `childNodes` property will return a similar `NodeList` list of nodes. Each `p` tag will still be of type `HTMLParagraphElements`, but the `NodeList` can contain additional _HTML nodes_ that the `HTMLCollection` list cannot.

Modify the HTML by removing one of the `p` tags, but keep the text.

```tsx
<div>
  <p>Hello, World</p>
  TypeScript!
</div>;

const div = document.getElementsByTagName("div")[0];

div.children;
// HTMLCollection(1) [p]

div.childNodes;
// NodeList(2) [p, text]
```

See how both lists change. `children` now only contains the `<p>Hello, World</p>` element, and the `childNodes` contains a `text` node rather than two `p` nodes. The `text` part of the `NodeList` is the literal `Node` containing the text `TypeScript!`. The `children` list does not contain this `Node` because it is not considered an `HTMLElement`.

## The `querySelector` and `querySelectorAll` methods

Both of these methods are great tools for getting lists of dom elements that fit a more unique set of constraints. They are defined in _lib.dom.d.ts_ as:

```ts
/**
 * Returns the first element that is a descendant of node that matches selectors.
 */
querySelector<K extends keyof HTMLElementTagNameMap>(selectors: K): HTMLElementTagNameMap[K] | null;
querySelector<K extends keyof SVGElementTagNameMap>(selectors: K): SVGElementTagNameMap[K] | null;
querySelector<E extends Element = Element>(selectors: string): E | null;

/**
 * Returns all element descendants of node that match selectors.
 */
querySelectorAll<K extends keyof HTMLElementTagNameMap>(selectors: K): NodeListOf<HTMLElementTagNameMap[K]>;
querySelectorAll<K extends keyof SVGElementTagNameMap>(selectors: K): NodeListOf<SVGElementTagNameMap[K]>;
querySelectorAll<E extends Element = Element>(selectors: string): NodeListOf<E>;
```

The `querySelectorAll` definition is similar to `getElementsByTagName`, except it returns a new type: `NodeListOf`. This return type is essentially a custom implementation of the standard JavaScript list element. Arguably, replacing `NodeListOf<E>` with `E[]` would result in a very similar user experience. `NodeListOf` only implements the following properties and methods: `length`, `item(index)`, `forEach((value, key, parent) => void)`, and numeric indexing. Additionally, this method returns a list of _elements_, not _nodes_, which is what `NodeList` was returning from the `.childNodes` method. While this may appear as a discrepancy, take note that interface `Element` extends from `Node`.

To see these methods in action modify the existing code to:

```tsx
<ul>
  <li>First :)</li>
  <li>Second!</li>
  <li>Third times a charm.</li>
</ul>;

const first = document.querySelector("li"); // returns the first li element
const all = document.querySelectorAll("li"); // returns the list of all li elements
```

## Interested in learning more?

The best part about the _lib.dom.d.ts_ type definitions is that they are reflective of the types annotated in the Mozilla Developer Network (MDN) documentation site. For example, the `HTMLElement` interface is documented by this [HTMLElement page](https://developer.mozilla.org/docs/Web/API/HTMLElement) on MDN. These pages list all available properties, methods, and sometimes even examples. Another great aspect of the pages is that they provide links to the corresponding standard documents. Here is the link to the [W3C Recommendation for HTMLElement](https://www.w3.org/TR/html52/dom.html#htmlelement).

Sources:

- [ECMA-262 Standard](http://www.ecma-international.org/ecma-262/10.0/index.html)
- [Introduction to the DOM](https://developer.mozilla.org/docs/Web/API/Document_Object_Model/Introduction)

---

## Source: `packages/documentation/copy/en/tutorials/Migrating from JavaScript.md`

---
title: Migrating from JavaScript
layout: docs
permalink: /docs/handbook/migrating-from-javascript.html
oneline: How to migrate from JavaScript to TypeScript
---

TypeScript doesn't exist in a vacuum.
It was built with the JavaScript ecosystem in mind, and a lot of JavaScript exists today.
Converting a JavaScript codebase over to TypeScript is, while somewhat tedious, usually not challenging.
In this tutorial, we're going to look at how you might start out.
We assume you've read enough of the handbook to write new TypeScript code.

If you're looking to convert a React project, we recommend looking at the [React Conversion Guide](https://github.com/Microsoft/TypeScript-React-Conversion-Guide#typescript-react-conversion-guide) first.

## Setting up your Directories

If you're writing in plain JavaScript, it's likely that you're running your JavaScript directly,
where your `.js` files are in a `src`, `lib`, or `dist` directory, and then run as desired.

If that's the case, the files that you've written are going to be used as inputs to TypeScript, and you'll run the outputs it produces.
During our JS to TS migration, we'll need to separate our input files to prevent TypeScript from overwriting them.
If your output files need to reside in a specific directory, then that will be your output directory.

You might also be running some intermediate steps on your JavaScript, such as bundling or using another transpiler like Babel.
In this case, you might already have a folder structure like this set up.

From this point on, we're going to assume that your directory is set up something like this:

```
projectRoot
├── src
│   ├── file1.js
│   └── file2.js
├── built
└── tsconfig.json
```

If you have a `tests` folder outside of your `src` directory, you might have one `tsconfig.json` in `src`, and one in `tests` as well.

## Writing a Configuration File

TypeScript uses a file called `tsconfig.json` for managing your project's options, such as which files you want to include, and what sorts of checking you want to perform.
Let's create a bare-bones one for our project:

```json
{
  "compilerOptions": {
    "outDir": "./built",
    "allowJs": true,
    "target": "es5"
  },
  "include": ["./src/**/*"]
}
```

Here we're specifying a few things to TypeScript:

1. Read in any files it understands in the `src` directory (with [`include`](/tsconfig#include)).
2. Accept JavaScript files as inputs (with [`allowJs`](/tsconfig#allowJs)).
3. Emit all of the output files in `built` (with [`outDir`](/tsconfig#outDir)).
4. Translate newer JavaScript constructs down to an older version like ECMAScript 5 (using [`target`](/tsconfig#target)).

At this point, if you try running `tsc` at the root of your project, you should see output files in the `built` directory.
The layout of files in `built` should look identical to the layout of `src`.
You should now have TypeScript working with your project.

## Early Benefits

Even at this point you can get some great benefits from TypeScript understanding your project.
If you open up an editor like [VS Code](https://code.visualstudio.com) or [Visual Studio](https://visualstudio.com), you'll see that you can often get some tooling support like completion.
You can also catch certain bugs with options like:

- [`noImplicitReturns`](/tsconfig#noImplicitReturns) which prevents you from forgetting to return at the end of a function.
- [`noFallthroughCasesInSwitch`](/tsconfig#noFallthroughCasesInSwitch) which is helpful if you never want to forget a `break` statement between `case`s in a `switch` block.

TypeScript will also warn about unreachable code and labels, which you can disable with [`allowUnreachableCode`](/tsconfig#allowUnreachableCode) and [`allowUnusedLabels`](/tsconfig#allowUnusedLabels) respectively.

## Integrating with Build Tools

You might have some more build steps in your pipeline.
Perhaps you concatenate something to each of your files.
Each build tool is different, but we'll do our best to cover the gist of things.

### Gulp

If you're using Gulp in some fashion, we have a tutorial on [using Gulp](/docs/handbook/gulp.html) with TypeScript, and integrating with common build tools like Browserify, Babelify, and Uglify.
You can read more there.

### Webpack

Webpack integration is pretty simple.
You can use `ts-loader`, a TypeScript loader, combined with `source-map-loader` for easier debugging.
Simply run

```shell
npm install ts-loader source-map-loader
```

and merge in options from the following into your `webpack.config.js` file:

```js
module.exports = {
  entry: "./src/index.ts",
  output: {
    filename: "./dist/bundle.js",
  },

  // Enable sourcemaps for debugging webpack's output.
  devtool: "source-map",

  resolve: {
    // Add '.ts' and '.tsx' as resolvable extensions.
    extensions: ["", ".webpack.js", ".web.js", ".ts", ".tsx", ".js"],
  },

  module: {
    rules: [
      // All files with a '.ts' or '.tsx' extension will be handled by 'ts-loader'.
      { test: /\.tsx?$/, loader: "ts-loader" },

      // All output '.js' files will have any sourcemaps re-processed by 'source-map-loader'.
      { test: /\.js$/, loader: "source-map-loader" },
    ],
  },

  // Other options...
};
```

It's important to note that ts-loader will need to run before any other loader that deals with `.js` files.

You can see an example of using Webpack in our [tutorial on React and Webpack](/docs/handbook/react-&-webpack.html).

## Moving to TypeScript Files

At this point, you're probably ready to start using TypeScript files.
The first step is to rename one of your `.js` files to `.ts`.
If your file uses JSX, you'll need to rename it to `.tsx`.

Finished with that step?
Great!
You've successfully migrated a file from JavaScript to TypeScript!

Of course, that might not feel right.
If you open that file in an editor with TypeScript support (or if you run `tsc --pretty`), you might see red squiggles on certain lines.
You should think of these the same way you'd think of red squiggles in an editor like Microsoft Word.
TypeScript will still translate your code, just like Word will still let you print your documents.

If that sounds too lax for you, you can tighten that behavior up.
If, for instance, you _don't_ want TypeScript to compile to JavaScript in the face of errors, you can use the [`noEmitOnError`](/tsconfig#noEmitOnError) option.
In that sense, TypeScript has a dial on its strictness, and you can turn that knob up as high as you want.

If you plan on using the stricter settings that are available, it's best to turn them on now (see [Getting Stricter Checks](#getting-stricter-checks) below).
For instance, if you never want TypeScript to silently infer `any` for a type without you explicitly saying so, you can use [`noImplicitAny`](/tsconfig#noImplicitAny) before you start modifying your files.
While it might feel somewhat overwhelming, the long-term gains become apparent much more quickly.

### Weeding out Errors

Like we mentioned, it's not unexpected to get error messages after conversion.
The important thing is to actually go one by one through these and decide how to deal with the errors.
Often these will be legitimate bugs, but sometimes you'll have to explain what you're trying to do a little better to TypeScript.

#### Importing from Modules

You might start out getting a bunch of errors like `Cannot find name 'require'.`, and `Cannot find name 'define'.`.
In these cases, it's likely that you're using modules.
While you can just convince TypeScript that these exist by writing out

```ts
// For Node/CommonJS
declare function require(path: string): any;
```

or

```ts
// For RequireJS/AMD
declare function define(...args: any[]): any;
```

it's better to get rid of those calls and use TypeScript syntax for imports.

First, you'll need to enable some module system by setting TypeScript's [`module`](/tsconfig#module) option.
Valid options are `commonjs`, `amd`, `system`, and `umd`.

If you had the following Node/CommonJS code:

```js
var foo = require("foo");

foo.doStuff();
```

or the following RequireJS/AMD code:

```js
define(["foo"], function (foo) {
  foo.doStuff();
});
```

then you would write the following TypeScript code:

```ts
import foo = require("foo");

foo.doStuff();
```

#### Getting Declaration Files

If you started converting over to TypeScript imports, you'll probably run into errors like `Cannot find module 'foo'.`.
The issue here is that you likely don't have _declaration files_ to describe your library.
Luckily this is pretty easy.
If TypeScript complains about a package like `lodash`, you can just write

```shell
npm install -S @types/lodash
```

If you're using a module option other than `commonjs`, you'll need to set your [`moduleResolution`](/tsconfig#moduleResolution) option to `node`.

After that, you'll be able to import lodash with no issues, and get accurate completions.

#### Exporting from Modules

Typically, exporting from a module involves adding properties to a value like `exports` or `module.exports`.
TypeScript allows you to use top-level export statements.
For instance, if you exported a function like so:

```js
module.exports.feedPets = function (pets) {
  // ...
};
```

you could write that out as the following:

```ts
export function feedPets(pets) {
  // ...
}
```

Sometimes you'll entirely overwrite the exports object.
This is a common pattern people use to make their modules immediately callable like in this snippet:

```js
var express = require("express");
var app = express();
```

You might have previously written that like so:

```js
function foo() {
  // ...
}
module.exports = foo;
```

In TypeScript, you can model this with the `export =` construct.

```ts
function foo() {
  // ...
}
export = foo;
```

#### Too many/too few arguments

You'll sometimes find yourself calling a function with too many/few arguments.
Typically, this is a bug, but in some cases, you might have declared a function that uses the `arguments` object instead of writing out any parameters:

```js
function myCoolFunction() {
  if (arguments.length == 2 && !Array.isArray(arguments[1])) {
    var f = arguments[0];
    var arr = arguments[1];
    // ...
  }
  // ...
}

myCoolFunction(
  function (x) {
    console.log(x);
  },
  [1, 2, 3, 4]
);
myCoolFunction(
  function (x) {
    console.log(x);
  },
  1,
  2,
  3,
  4
);
```

In this case, we need to use TypeScript to tell any of our callers about the ways `myCoolFunction` can be called using function overloads.

```ts
function myCoolFunction(f: (x: number) => void, nums: number[]): void;
function myCoolFunction(f: (x: number) => void, ...nums: number[]): void;
function myCoolFunction() {
  if (arguments.length == 2 && !Array.isArray(arguments[1])) {
    var f = arguments[0];
    var arr = arguments[1];
    // ...
  }
  // ...
}
```

We added two overload signatures to `myCoolFunction`.
The first checks states that `myCoolFunction` takes a function (which takes a `number`), and then a list of `number`s.
The second one says that it will take a function as well, and then uses a rest parameter (`...nums`) to state that any number of arguments after that need to be `number`s.

#### Sequentially Added Properties

Some people find it more aesthetically pleasing to create an object and add properties immediately after like so:

```js
var options = {};
options.color = "red";
options.volume = 11;
```

TypeScript will say that you can't assign to `color` and `volume` because it first figured out the type of `options` as `{}` which doesn't have any properties.
If you instead moved the declarations into the object literal themselves, you'd get no errors:

```ts
let options = {
  color: "red",
  volume: 11,
};
```

You could also define the type of `options` and add a type assertion on the object literal.

```ts
interface Options {
  color: string;
  volume: number;
}

let options = {} as Options;
options.color = "red";
options.volume = 11;
```

Alternatively, you can just say `options` has the type `any` which is the easiest thing to do, but which will benefit you the least.

#### `any`, `Object`, and `{}`

You might be tempted to use `Object` or `{}` to say that a value can have any property on it because `Object` is, for most purposes, the most general type.
However **`any` is actually the type you want to use** in those situations, since it's the most _flexible_ type.

For instance, if you have something that's typed as `Object` you won't be able to call methods like `toLowerCase()` on it.
Being more general usually means you can do less with a type, but `any` is special in that it is the most general type while still allowing you to do anything with it.
That means you can call it, construct it, access properties on it, etc.
Keep in mind though, whenever you use `any`, you lose out on most of the error checking and editor support that TypeScript gives you.

If a decision ever comes down to `Object` and `{}`, you should prefer `{}`.
While they are mostly the same, technically `{}` is a more general type than `Object` in certain esoteric cases.

### Getting Stricter Checks

TypeScript comes with certain checks to give you more safety and analysis of your program.
Once you've converted your codebase to TypeScript, you can start enabling these checks for greater safety.

#### No Implicit `any`

There are certain cases where TypeScript can't figure out what certain types should be.
To be as lenient as possible, it will decide to use the type `any` in its place.
While this is great for migration, using `any` means that you're not getting any type safety, and you won't get the same tooling support you'd get elsewhere.
You can tell TypeScript to flag these locations down and give an error with the [`noImplicitAny`](/tsconfig#noImplicitAny) option.

#### Strict `null` & `undefined` Checks

By default, TypeScript assumes that `null` and `undefined` are in the domain of every type.
That means anything declared with the type `number` could be `null` or `undefined`.
Since `null` and `undefined` are such a frequent source of bugs in JavaScript and TypeScript, TypeScript has the [`strictNullChecks`](/tsconfig#strictNullChecks) option to spare you the stress of worrying about these issues.

When [`strictNullChecks`](/tsconfig#strictNullChecks) is enabled, `null` and `undefined` get their own types called `null` and `undefined` respectively.
Whenever anything is _possibly_ `null`, you can use a union type with the original type.
So for instance, if something could be a `number` or `null`, you'd write the type out as `number | null`.

If you ever have a value that TypeScript thinks is possibly `null`/`undefined`, but you know better, you can use the postfix `!` operator to tell it otherwise.

```ts
declare var foo: string[] | null;

foo.length; // error - 'foo' is possibly 'null'

foo!.length; // okay - 'foo!' just has type 'string[]'
```

As a heads up, when using [`strictNullChecks`](/tsconfig#strictNullChecks), your dependencies may need to be updated to use [`strictNullChecks`](/tsconfig#strictNullChecks) as well.

#### No Implicit `any` for `this`

When you use the `this` keyword outside of classes, it has the type `any` by default.
For instance, imagine a `Point` class, and imagine a function that we wish to add as a method:

```ts
class Point {
  constructor(public x, public y) {}
  getDistance(p: Point) {
    let dx = p.x - this.x;
    let dy = p.y - this.y;
    return Math.sqrt(dx ** 2 + dy ** 2);
  }
}
// ...

// Reopen the interface.
interface Point {
  distanceFromOrigin(): number;
}
Point.prototype.distanceFromOrigin = function () {
  return this.getDistance({ x: 0, y: 0 });
};
```

This has the same problems we mentioned above - we could easily have misspelled `getDistance` and not gotten an error.
For this reason, TypeScript has the [`noImplicitThis`](/tsconfig#noImplicitThis) option.
When that option is set, TypeScript will issue an error when `this` is used without an explicit (or inferred) type.
The fix is to use a `this`-parameter to give an explicit type in the interface or in the function itself:

```ts
Point.prototype.distanceFromOrigin = function (this: Point) {
  return this.getDistance({ x: 0, y: 0 });
};
```

---

## Source: `packages/documentation/copy/en/tutorials/React.md`

---
title: React
layout: docs
permalink: /docs/handbook/react.html
oneline: Links to learn about TypeScript and React
translatable: true
experimental: false
---

TypeScript supports [JSX](/docs/handbook/jsx.html) and can correctly model the patterns used in React codebases like `useState`.

### Getting Set Up With a React Project

Today there are many frameworks which support TypeScript out of the box:

- [Create React App](https://create-react-app.dev) - [TS docs](https://create-react-app.dev/docs/adding-typescript/)
- [Next.js](https://nextjs.org) - [TS docs](https://nextjs.org/learn/excel/typescript)
- [Gatsby](https://www.gatsbyjs.org) - [TS Docs](https://www.gatsbyjs.org/docs/typescript/)

All of these are great starting points. We [use Gatsby](https://www.gatsbyjs.org/blog/2020-01-23-why-typescript-chose-gatsby/#reach-skip-nav) with TypeScript for [this website](https://github.com/microsoft/TypeScript-Website/), so that can also be a useful reference implementation.

### Documentation

Here are some of the best places to find up-to-date information on React and TypeScript:

- [React TypeScript Cheatsheets](https://react-typescript-cheatsheet.netlify.app)
- [React & Redux in TypeScript](https://github.com/piotrwitek/react-redux-typescript-guide#react--redux-in-typescript---complete-guide)

---

## Source: `packages/playground-handbook/copy/en/Compiler Settings.md`

## Compiler Settings

There isn't a `tsconfig.json` file in a Playground, but you need to be able to set the compiler flags in order to accurately re-create a particular environment. Even for the simplest code, the difference in how TypeScript acts between `strict: true` and `strict: false` is pretty drastic and not being able to set that to match would suck.

Above this prose there are two toolbars, one is the site navigation in bright blue - under that is the Playground's toolbar. This toolbar has a button "TS Config", clicking that will show you the main interface for setting compiler options in the Playground. You can do it now by the way, then click "Close" to get back to this text.

### TS Config Panel

The TS Config panel contains a focused list of the TypeScript compiler options available inside a `tsconfig.json`. It starts off with some dropdowns for some of the most important compiler options and then it moves down to categories with boolean check boxes. This list has grown organically over time and generally represents the settings which people use most. If you need to set a value which isn't in that list, there is a way to set any option via [twoslash annotations](/play?#handbook-12) which we'll get to later in the handbook.

Changing a compiler flag will update the URL in your browser (unless you have that disabled in the settings.) The URL structure works by comparing the current compiler options versus the default settings (covered below) and only showing compiler options which differ from the defaults. For example, the default for a Playground is to have `esModuleInterop: true` enabled, thus turning `esModuleInterop` to `false` would append `?esModuleInterop=false` to the URL:

```diff
# Before
- https://www.typescriptlang.org/play

# After turning esModuleInterop off
+ https://www.typescriptlang.org/play?esModuleInterop=false
```

This helps keep Playground URLs on the short side, or at least doesn't add to their size needlessly. You might notice that sometimes the compiler flags aren't the exact same in the URL as the user interface, for example `?target=6` is `target: ES2019` this is us saving characters by using the enum's numerical value rather than the string representation.

<details>
<summary>The defaults for the compiler in a Playground</summary>

_In rough_, the Playground has settings which can be summed up as this:

```json
{
  "compilerOptions": {
    "strict": true,
    "module": "esnext",
    "moduleResolution": "node",
    "target": "es2017",
    "jsx": "react",

    "experimentalDecorators": true,
    "emitDecoratorMetadata": true
  }
}
```

The reality is (of course) a tad more complex, we detect if a compiler setting is in the following list as a cue for showing the compiler setting in the TS Config panel user interface and only add a setting to the URL if it differs from this list.

So, the full specification for the default compiler settings (as of TypeScript 4.5) looks like this:

```ts
export function getDefaultSandboxCompilerOptions(config: SandboxConfig, monaco: Monaco) {
  const useJavaScript = config.filetype === "js"
  const settings: CompilerOptions = {
    strict: true,

    noImplicitAny: true,
    strictNullChecks: !useJavaScript,
    strictFunctionTypes: true,
    strictPropertyInitialization: true,
    strictBindCallApply: true,
    noImplicitThis: true,
    noImplicitReturns: true,
    noUncheckedIndexedAccess: false,

    useDefineForClassFields: false,

    alwaysStrict: true,
    allowUnreachableCode: false,
    allowUnusedLabels: false,

    downlevelIteration: false,
    noEmitHelpers: false,
    noLib: false,
    noStrictGenericChecks: false,
    noUnusedLocals: false,
    noUnusedParameters: false,

    esModuleInterop: true,
    preserveConstEnums: false,
    removeComments: false,
    skipLibCheck: false,

    checkJs: useJavaScript,
    allowJs: useJavaScript,
    declaration: true,

    importHelpers: false,

    experimentalDecorators: true,
    emitDecoratorMetadata: true,
    moduleResolution: monaco.languages.typescript.ModuleResolutionKind.NodeJs,

    target: monaco.languages.typescript.ScriptTarget.ES2017,
    jsx: monaco.languages.typescript.JsxEmit.React,
    module: monaco.languages.typescript.ModuleKind.ESNext,
  }

  return { ...settings, ...config.compilerOptions }
}
```

This includes a lot of values which are set to their default value too. Which actually can make setting up a _perfect_ environment tricky because 'no value set' can differ from 'false' for some settings, but breaking this system would break backwards compatibility (URLs would change) and make URLs longer, thus it stays the way it is.

</details>

That's that for the compiler settings. Next up, [Examples](/play#handbook-2).

---

## Source: `packages/playground-handbook/copy/en/Type Acquisition.md`

## Type Acquisition

No Playground is an island. Well, not strictly, no playground _needs_ to be an island. One of the first problem we hit when adding support for `.tsx`/`.jsx` to the Playground was that to **_really_** use JSX to write React components - you need the types for React.

This left us with the dilemma of needing to either bundle React's evolving types into the Playground, or to replicate the feature found in JavaScript projects utilizing TypeScript: Automatic Type Acquisition. The idea behind Automatic Type Acquisition (ATA) is that behind the scenes the Playground will look at any `import` / `require` / [`/// <reference types"`](/docs/handbook/triple-slash-directives.html) and understand what npm modules have been referenced.

For these referenced modules, TypeScript will search through the npm package contents, and potentially in the `@types` equivalent for `.d.ts` files to describe how the library works. This means to get the types for React, you would create a playground like:

```ts
import React from "react"

const myComponent = () => <h1>Hello, world</h1>
```

Type Acquisition will:

- look in the package `react` on npm, see there are no `.d.ts` files in its contents
- look to see if `@types/react` exists, downloads all of the `.d.ts` files
- read the `.d.ts` files in `@types/react`, and discover they import from `csstype` and `prop-types`
  - look in the package `csstype` for `.d.ts` files and downloads them
  - look in the package `prop-types` for `.d.ts` files and finds none
  - look to see if `@types/prop-types` exists and download the `.d.ts` files from that

That one import line has downloaded the `.d.ts` files from `@types/react`, `@types/prop-types` and `csstype`. These are added to the Playground's TypeScript project's `node_modules` folder and TypeScript picks them up.

This is all built on the [jsdelivr CDN](https://www.jsdelivr.com/) which has kept the complexity down, and the type acquisition system is available for other projects to use via npm on [`@typescript/ata`](https://www.npmjs.com/package/@typescript/ata).

If you need more control over the version of the types which are imported into the Playground, you can append `// types: npm_tag_or_version`

```
import { xy } from "xyz" // types: beta
```

The type acquisition as-is is quite eager and may start pulling your types before you've set the npm tag or version. In that case, you can reload your browser once it's written to get the right version.

---

## Source: `packages/tsconfig-reference/copy/en/options/allowSyntheticDefaultImports.md`

---
display: "Allow Synthetic Default Imports"
oneline: "Allow 'import x from y' when a module doesn't have a default export."
---

When set to true, `allowSyntheticDefaultImports` allows you to write an import like:

```ts
import React from "react";
```

instead of:

```ts
import * as React from "react";
```

When the module **does not** explicitly specify a default export.

For example, without `allowSyntheticDefaultImports` as true:

```ts twoslash
// @errors: 1259 1192
// @checkJs
// @allowJs
// @esModuleInterop: false
// @filename: utilFunctions.js
// @noImplicitAny: false
const getStringLength = (str) => str.length;

module.exports = {
  getStringLength,
};

// @filename: index.ts
import utils from "./utilFunctions";

const count = utils.getStringLength("Check JS");
```

This code raises an error because there isn't a `default` object which you can import. Even though it feels like it should.
For convenience, transpilers like Babel will automatically create a default if one isn't created. Making the module look a bit more like:

```js
// @filename: utilFunctions.js
const getStringLength = (str) => str.length;
const allFunctions = {
  getStringLength,
};

module.exports = allFunctions;
module.exports.default = allFunctions;
```

This flag does not affect the JavaScript emitted by TypeScript, it's only for the type checking.
This option brings the behavior of TypeScript in-line with Babel, where extra code is emitted to make using a default export of a module more ergonomic.

---

## Source: `packages/tsconfig-reference/copy/en/options/jsx.md`

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

### For example

This sample code:

```tsx
export const HelloWorld = () => <h1>Hello world</h1>;
```

React: `"react-jsx"`<sup>[[1]](https://reactjs.org/blog/2020/09/22/introducing-the-new-jsx-transform.html)</sup>

```tsx twoslash
declare module JSX {
  interface Element {}
  interface IntrinsicElements {
    [s: string]: any;
  }
}
// @showEmit
// @noErrors
// @jsx: react-jsx
export const HelloWorld = () => <h1>Hello world</h1>;
```

React dev transform: `"react-jsxdev"`<sup>[[1]](https://reactjs.org/blog/2020/09/22/introducing-the-new-jsx-transform.html)</sup>

```tsx twoslash
declare module JSX {
  interface Element {}
  interface IntrinsicElements {
    [s: string]: any;
  }
}
// @showEmit
// @noErrors
// @jsx: react-jsxdev
export const HelloWorld = () => <h1>Hello world</h1>;
```

Preserve: `"preserve"`

```tsx twoslash
declare module JSX {
  interface Element {}
  interface IntrinsicElements {
    [s: string]: any;
  }
}
// @showEmit
// @noErrors
// @jsx: preserve
export const HelloWorld = () => <h1>Hello world</h1>;
```

React Native: `"react-native"`

```tsx twoslash
declare module JSX {
  interface Element {}
  interface IntrinsicElements {
    [s: string]: any;
  }
}
// @showEmit
// @noErrors
// @jsx: react-native
export const HelloWorld = () => <h1>Hello world</h1>;
```


Legacy React runtime: `"react"`

```tsx twoslash
declare module JSX {
  interface Element {}
  interface IntrinsicElements {
    [s: string]: any;
  }
}
// @showEmit
// @noErrors
export const HelloWorld = () => <h1>Hello world</h1>;
```

This option can be used on a per-file basis too using an `@jsxRuntime` comment.

Always use the classic runtime (`"react"`) for this file:

```tsx
/* @jsxRuntime classic */
export const HelloWorld = () => <h1>Hello world</h1>;
```

Always use the automatic runtime (`"react-jsx"`) for this file:

```tsx
/* @jsxRuntime automatic */
export const HelloWorld = () => <h1>Hello world</h1>;
```

---

## Source: `packages/tsconfig-reference/copy/en/options/jsxFactory.md`

---
display: "JSX Factory"
oneline: "Specify the JSX factory function used when targeting React JSX emit, e.g. 'React.createElement' or 'h'."
---

Changes the function called in `.js` files when compiling JSX Elements using the classic JSX runtime.
The most common change is to use `"h"` or `"preact.h"` instead of the default `"React.createElement"` if using `preact`.

For example, this TSX file:

```tsx
import { h } from "preact";

const HelloWorld = () => <div>Hello</div>;
```

With `jsxFactory: "h"` looks like:

```tsx twoslash
// @showEmit
// @showEmittedFile: index.js
// @jsxFactory: h
// @noErrors
// @target: esnext
// @module: commonjs

import { h, Fragment } from "preact";

const HelloWorld = () => <div>Hello</div>;
```

This option can be used on a per-file basis too similar to [Babel's `/** @jsx h */` directive](https://babeljs.io/docs/en/babel-plugin-transform-react-jsx#custom).

```tsx twoslash
/** @jsx h */
import { h } from "preact";

const HelloWorld = () => <div>Hello</div>;
```

The factory chosen will also affect where the `JSX` namespace is looked up (for type checking information) before falling back to the global one.

If the factory is defined as `React.createElement` (the default), the compiler will check for `React.JSX` before checking for a global `JSX`. If the factory is defined as `h`, it will check for `h.JSX` before a global `JSX`.

---

## Source: `packages/tsconfig-reference/copy/en/options/jsxFragmentFactory.md`

---
display: "JSX Fragment Factory"
oneline: "Specify the JSX Fragment reference used for fragments when targeting React JSX emit e.g. 'React.Fragment' or 'Fragment'."
---

Specify the JSX fragment factory function to use when targeting react JSX emit with [`jsxFactory`](#jsxFactory) compiler option is specified, e.g. `Fragment`.

For example with this TSConfig:

```json tsconfig
{
  "compilerOptions": {
    "target": "esnext",
    "module": "commonjs",
    "jsx": "react",
    "jsxFactory": "h",
    "jsxFragmentFactory": "Fragment"
  }
}
```

This TSX file:

```tsx
import { h, Fragment } from "preact";

const HelloWorld = () => (
  <>
    <div>Hello</div>
  </>
);
```

Would look like:

```tsx twoslash
// @showEmit
// @showEmittedFile: index.js
// @jsxFactory: h
// @jsxFragmentFactory: Fragment
// @noErrors
// @target: esnext
// @module: commonjs

import { h, Fragment } from "preact";

const HelloWorld = () => (
  <>
    <div>Hello</div>
  </>
);
```

This option can be used on a per-file basis too similar to [Babel's `/* @jsxFrag h */` directive](https://babeljs.io/docs/en/babel-plugin-transform-react-jsx#fragments).

For example:

```tsx twoslash
/** @jsx h */
/** @jsxFrag Fragment */

import { h, Fragment } from "preact";

const HelloWorld = () => (
  <>
    <div>Hello</div>
  </>
);
```

---

## Source: `packages/tsconfig-reference/copy/en/options/jsxImportSource.md`

---
display: "JSX Import Source"
oneline: "Specify module specifier used to import the JSX factory functions when using `jsx: react-jsx*`."
---

Declares the module specifier to be used for importing the `jsx` and `jsxs` factory functions when using [`jsx`](#jsx) as `"react-jsx"` or `"react-jsxdev"` which were introduced in TypeScript 4.1.

With [React 17](https://reactjs.org/blog/2020/09/22/introducing-the-new-jsx-transform.html) the library supports a new form of JSX transformation via a separate import.

For example with this code:

```tsx
import React from "react";

function App() {
  return <h1>Hello World</h1>;
}
```

Using this TSConfig:

```json tsconfig
{
  "compilerOptions": {
    "target": "esnext",
    "module": "commonjs",
    "jsx": "react-jsx"
  }
}
```

The emitted JavaScript from TypeScript is:

```tsx twoslash
// @showEmit
// @noErrors
// @jsx: react-jsx
// @module: commonjs
// @target: esnext
declare module JSX {
  interface Element {}
  interface IntrinsicElements {
    [s: string]: any;
  }
}
import React from "react";

function App() {
  return <h1>Hello World</h1>;
}
```

For example if you wanted to use `"jsxImportSource": "preact"`, you need a tsconfig like:

```json tsconfig
{
  "compilerOptions": {
    "target": "esnext",
    "module": "commonjs",
    "jsx": "react-jsx",
    "jsxImportSource": "preact",
    "types": ["preact"]
  }
}
```

Which generates code like:

```tsx twoslash
// @showEmit
// @jsxImportSource: preact
// @types: preact
// @jsx: react-jsx
// @target: esnext
// @module: commonjs
// @noErrors

export function App() {
  return <h1>Hello World</h1>;
}
```

Alternatively, you can use a per-file pragma to set this option, for example:

```tsx
/** @jsxImportSource preact */

export function App() {
  return <h1>Hello World</h1>;
}
```

Would add `preact/jsx-runtime` as an import for the `_jsx` factory.

_Note:_ In order for this to work like you would expect, your `tsx` file must include an `export` or `import` so that it is considered a module.

---

## Source: `packages/tsconfig-reference/copy/en/options/moduleDetection.md`

---
display: "Module Detection"
oneline: "Specify what method is used to detect whether a file is a script or a module."
---

This setting controls how TypeScript determines whether a file is a
[script or a module](/docs/handbook/modules/theory.html#scripts-and-modules-in-javascript).

There are three choices:

- `"auto"` (default) - TypeScript will not only look for import and export statements, but it will also check whether the `"type"` field in a `package.json` is set to `"module"` when running with [`module`](#module): `nodenext` or `node16`, and check whether the current file is a JSX file when running under [`jsx`](#jsx):  `react-jsx`.

- `"legacy"` - The same behavior as 4.6 and prior, usings import and export statements to determine whether a file is a module.

- `"force"` - Ensures that every non-declaration file is treated as a module.

---

## Source: `packages/tsconfig-reference/copy/en/options/moduleSuffixes.md`

---
display: "Module Suffixes"
oneline: "List of file name suffixes to search when resolving a module."
---

Provides a way to override the default list of file name suffixes to search when resolving a module.

```json tsconfig
{
    "compilerOptions": {
        "moduleSuffixes": [".ios", ".native", ""]
    }
}
```

Given the above configuration, an import like the following:

```ts
import * as foo from "./foo";
```

TypeScript will look for the relative files `./foo.ios.ts`, `./foo.native.ts`, and finally `./foo.ts`.

Note the empty string `""` in [`moduleSuffixes`](#moduleSuffixes) which is necessary for TypeScript to also look-up `./foo.ts`.

This feature can be useful for React Native projects where each target platform can use a separate tsconfig.json with differing `moduleSuffixes`.

---

## Source: `packages/tsconfig-reference/copy/en/options/reactNamespace.md`

---
display: "React Namespace"
oneline: "Specify the object invoked for `createElement`. This only applies when targeting `react` JSX emit."
---

Use [`jsxFactory`](#jsxFactory) instead. Specify the object invoked for `createElement` when targeting `react` for TSX files.

