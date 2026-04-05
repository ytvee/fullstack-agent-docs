### Normalization
Normalization is the process of organizing data in your database to reduce redundancy (duplication) and improve data integrity 
(accuracy and consistency). Think of it like tidying up a messy filing cabinet. Instead of having all sorts of papers 
crammed into one folder, you organize them into logical folders and categories to make everything easier to find and manage.

<Callout collapsed="Why is Normalization Important?">
- **Reduces Data Redundancy**: Imagine storing a customer's address every time they place an order. If the address changes, you'd have to update it in multiple places! Normalization helps you store information in one place and refer to it from other places, minimizing repetition.
- **Improves Data Integrity**: Less redundancy means less chance of inconsistencies. If you update an address in one place, it's updated everywhere it's needed.
- **Prevents Anomalies**: Normalization helps prevent issues like:
  1. **Insertion Anomalies**: Difficulty adding new data because you're missing related information.
  2. **Update Anomalies**: Having to update the same information in multiple rows.
  3. **Deletion Anomalies**: Accidentally losing valuable information when you delete something seemingly unrelated.
- **Easier to Understand and Maintain**: A normalized database is generally more logically structured and easier to understand, query, and modify.
</Callout>

Normalization is often described in terms of "normal forms" (1NF, 2NF, 3NF, and beyond). While the details can get quite technical, the core ideas are straightforward:

