#### One-to-Many

In a one-to-many relationship, one record in `table A` can be related to many records in `table B`, but each 
record in `table B` is related to at most one record in `table A`. Think of it as a "parent-child" relationship.

<Callout collapsed="Use Cases & Examples">
1. **Customers and Orders**: One customer can place many orders, but each order belongs to only one customer.
2. **Authors and Books**: One author can write many books, but (let's simplify for now and say) each book is written by one primary author.
3. **Departments and Employees**: One department can have many employees, but each employee belongs to only one department.

```
Table A (One Side)      Table B (Many Side)
+---------+             +---------+
| PK (A)  | ----------> | FK (A)  | (Foreign Key referencing Table A)
| ...     |             | ...     |
+---------+             +---------+
     (One)                  (Many)
```
</Callout>

