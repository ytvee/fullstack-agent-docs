#### 1NF (First Normal Form): `Atomic Values`

**Goal**: Each column should hold a single, indivisible value. No repeating groups of data within a single cell

**Example**: Instead of having a single `address` column that stores `123 Main St, City, USA`, you'd 
break it down into separate columns: `street_address`, `city`, `state`, `zip_code`.

```sql
-- Unnormalized (violates 1NF)
CREATE TABLE Customers_Unnormalized (
    customer_id INT PRIMARY KEY,
    name VARCHAR(255),
    address VARCHAR(255) -- Problem: Multiple pieces of info in one column
);

-- Normalized to 1NF
CREATE TABLE Customers_1NF (
    customer_id INT PRIMARY KEY,
    name VARCHAR(255),
    street_address VARCHAR(255),
    city VARCHAR(255),
    state VARCHAR(255),
    zip_code VARCHAR(10)
);
```

