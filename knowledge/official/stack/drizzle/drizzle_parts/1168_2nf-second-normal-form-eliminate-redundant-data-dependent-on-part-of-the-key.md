#### 2NF (Second Normal Form): `Eliminate Redundant Data Dependent on Part of the Key`

**Goal**: Applies when you have a table with a composite primary key (a primary key made up of two or more columns). 
2NF ensures that all non-key attributes are fully dependent on the entire composite primary key, not just part of it.

Imagine we have a table called `order_items`. This table tracks items within orders, and we use a composite primary key (`order_id`, `product_id`) 
because a single order can have multiple of the same product (though in this simplified example, let's assume each product appears only 
once per order for clarity, but the composite key logic still applies).

<Callout collapsed="Expand for visual example">
```sql
CREATE TABLE OrderItems_Unnormalized (
    order_id INT,
    product_id VARCHAR(10),
    product_name VARCHAR(100),
    product_price DECIMAL(10, 2),
    quantity INT,
    order_date DATE,
    PRIMARY KEY (order_id, product_id) -- Composite Primary Key
);

INSERT INTO OrderItems_Unnormalized (order_id, product_id, product_name, product_price, quantity, order_date) VALUES
(101, 'A123', 'Laptop', 1200.00, 1, '2023-10-27'),
(101, 'B456', 'Mouse', 25.00, 2, '2023-10-27'),
(102, 'A123', 'Laptop', 1200.00, 1, '2023-10-28'),
(103, 'C789', 'Keyboard', 75.00, 1, '2023-10-29');
```
```
+------------------------------------------------------------------------------------+
| OrderItems_Unnormalized                                                            |
+------------------------------------------------------------------------------------+
| PK (order_id, product_id) | product_name | product_price | quantity | order_date   |
+------------------------------------------------------------------------------------+
| 101, A123               | Laptop       | 1200.00       | 1        | 2023-10-27     |
| 101, B456               | Mouse        | 25.00         | 2        | 2023-10-27     |
| 102, A123               | Laptop       | 1200.00       | 1        | 2023-10-28     |
| 103, C789               | Keyboard     | 75.00         | 1        | 2023-10-29     |
+------------------------------------------------------------------------------------+
```
</Callout>

**Problem**: Notice that `product_name` and `product_price` are repeated whenever the same `product_id` appears in different orders. 
These attributes are only dependent on `product_id`, which is part of the composite primary key (`order_id`, `product_id`), but not the entire key. 
This is a partial dependency.

To achieve 2NF, we need to remove the partially dependent attributes (`product_name`, `product_price`) and place them in a separate table where they are 
fully dependent on the primary key of that new table.

<Callout collapsed="Normalization to 2NF: Visual explanation">
```
+-------------------+     1:M     +---------------------------+
| Products          | <---------- | OrderItems_2NF            |
+-------------------+             +---------------------------+
| PK product_id     |             | PK (order_id, product_id) |
| product_name      |             | quantity                  |
| product_price     |             | order_date                |
+-------------------+             | FK product_id             |
                                  +---------------------------+
```
```sql
CREATE TABLE Products (
    product_id VARCHAR(10) PRIMARY KEY,
    product_name VARCHAR(100),
    product_price DECIMAL(10, 2)
);

CREATE TABLE OrderItems_2NF (
    order_id INT,
    product_id VARCHAR(10),
    quantity INT,
    order_date DATE,
    PRIMARY KEY (order_id, product_id), -- Composite Primary Key remains
    FOREIGN KEY (product_id) REFERENCES Products(product_id) -- Foreign Key to Products
);

-- Insert data into Products
INSERT INTO Products (product_id, product_name, product_price) VALUES
('A123', 'Laptop', 1200.00),
('B456', 'Mouse', 25.00),
('C789', 'Keyboard', 75.00);

-- Insert data into OrderItems_2NF (referencing Products)
INSERT INTO OrderItems_2NF (order_id, product_id, quantity, order_date) VALUES
(101, 'A123', 1, '2023-10-27'),
(101, 'B456', 2, '2023-10-27'),
(102, 'A123', 1, '2023-10-28'),
(103, 'C789', 1, '2023-10-29');
```
</Callout>

