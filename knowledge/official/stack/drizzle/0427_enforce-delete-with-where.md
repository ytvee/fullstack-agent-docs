### **enforce-delete-with-where**

Enforce using `delete` with the`.where()` clause in the `.delete()` statement. Most of the time, 
you don't need to delete all rows in the table and require some kind of `WHERE` statements.

Optionally, you can define a `drizzleObjectName` in the plugin options that accept a `string` or
`string[]`. This is useful when you have objects or classes with a delete method that's not from
Drizzle. Such a `delete` method will trigger the ESLint rule. To avoid that, you can define the 
name of the Drizzle object that you use in your codebase (like db) so that the rule would only 
trigger if the delete method comes from this object:

Example, config 1:
```yml
rules:
  'drizzle/enforce-delete-with-where': "error"
```

```ts
class MyClass {
  public delete() {
    return {}
  }
}

const myClassObj = new MyClass();

// ---> Will be triggered by ESLint Rule
myClassObj.delete()

const db = drizzle(...)
// ---> Will be triggered by ESLint Rule
db.delete()
```

Example, config 2:
```yml
rules:
  'drizzle/enforce-delete-with-where':
    - "error"
    - "drizzleObjectName": 
      - "db"
```
```ts
class MyClass {
  public delete() {
    return {}
  }
}

const myClassObj = new MyClass();

// ---> Will NOT be triggered by ESLint Rule
myClassObj.delete()

const db = drizzle(...)
// ---> Will be triggered by ESLint Rule
db.delete()
```

