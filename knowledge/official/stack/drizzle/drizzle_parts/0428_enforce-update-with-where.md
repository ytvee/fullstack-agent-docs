### **enforce-update-with-where**: 

Enforce using `update` with the`.where()` clause in the `.update()` statement. 
Most of the time, you don't need to update all rows in the table and require 
some kind of `WHERE` statements.

Optionally, you can define a `drizzleObjectName` in the plugin options that accept 
a `string` or `string[]`. This is useful when you have objects or classes with a delete 
method that's not from Drizzle. Such as `update` method will trigger the ESLint rule. To 
avoid that, you can define the name of the Drizzle object that you use in your codebase (like db) 
so that the rule would only trigger if the delete method comes from this object:

Example, config 1:
```yml
rules:
  'drizzle/enforce-update-with-where': "error"
```

```ts
class MyClass {
  public update() {
    return {}
  }
}

const myClassObj = new MyClass();

// ---> Will be triggered by ESLint Rule
myClassObj.update()

const db = drizzle(...)
// ---> Will be triggered by ESLint Rule
db.update()
```

Example, config 2:
```yml
rules:
  'drizzle/enforce-update-with-where':
    - "error"
    - "drizzleObjectName": 
      - "db"
```
```ts
class MyClass {
  public update() {
    return {}
  }
}

const myClassObj = new MyClass();

// ---> Will NOT be triggered by ESLint Rule
myClassObj.update()

const db = drizzle(...)
// ---> Will be triggered by ESLint Rule
db.update()
```

Source: https://orm.drizzle.team/docs/extensions/mysql


import Callout from '@mdx/Callout.astro';

<Callout>
Currently, there are no MySQL extensions natively supported by Drizzle. Once those are added, we will have them here!
</Callout>

Source: https://orm.drizzle.team/docs/extensions/pg


import Callout from '@mdx/Callout.astro';
import Section from '@mdx/Section.astro';

