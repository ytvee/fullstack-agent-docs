# Drizzle migrations fundamentals

SQL databases require you to specify a **strict schema** of entities you're going to store upfront 
and if (when) you need to change the shape of those entities - you will need to do it via **schema migrations**.

There're multiple production grade ways of managing database migrations. 
Drizzle is designed to perfectly suits all of them, regardless of you going **database first** or **codebase first**.

**Database first** is when your database schema is a source of truth. You manage your database schema either directly on the database or 
via database migration tools and then you pull your database schema to your codebase application level entities.  
 
**Codebase first** is when database schema in your codebase is a source of truth and is under version control. You declare and manage your database schema in JavaScript/TypeScript
and then you apply that schema to the database itself either with Drizzle, directly or via external migration tools. 

