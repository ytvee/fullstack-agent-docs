#### 3NF (Third Normal Form): `Eliminate Redundant Data Dependent on Non-Key Attributes`

**Goal**: Remove data that is dependent on other non-key attributes. This is about eliminating transitive dependencies.

**Problem**: Let's say we have a `suppliers` table. We store supplier information, including their `zip_code`, `city`, and `state`. `supplier_id` is the primary key.

<Callout collapsed="">
```sql
CREATE TABLE suppliers (
    supplier_id VARCHAR(10) PRIMARY KEY,
    supplier_name VARCHAR(255),
    zip_code VARCHAR(10),
    city VARCHAR(100),
    state VARCHAR(50)
);

INSERT INTO suppliers (supplier_id, supplier_name, zip_code, city, state) VALUES
('S1', 'Acme Corp', '12345', 'Anytown', 'NY'),
('S2', 'Beta Inc', '67890', 'Otherville', 'CA'),
('S3', 'Gamma Ltd', '12345', 'Anytown', 'NY');
```
```
+---------------------------------------------------------------+
| suppliers                                                     |
+---------------------------------------------------------------+
| PK supplier_id | supplier_name | zip_code | city      | state |
+---------------------------------------------------------------+
| S1             | Acme Corp     | 12345    | Anytown    | NY   |
| S2             | Beta Inc      | 67890    | Otherville | CA   |
| S3             | Gamma Ltd     | 12345    | Anytown    | NY   |
+---------------------------------------------------------------+
```
</Callout>

**Solution**: To achieve 3NF, we remove the attributes dependent on the non-key attribute (`city`, `state` dependent on `zip_code`) and put 
them into a separate table keyed by the non-key attribute itself (`zip_code`).

<Callout collapsed="Normalization to 3NF: Visual explanation">
```
+-------------------+     1:M     +--------------------+
| zip_codes         | <---------- | suppliers          |
+-------------------+             +--------------------+
| PK zip_code       |             | PK supplier_id     |
| city              |             | supplier_name      |
| state             |             | FK zip_code        |
+-------------------+             +--------------------+
```
```sql
CREATE TABLE zip_codes (
    zip_code VARCHAR(10) PRIMARY KEY,
    city VARCHAR(100),
    state VARCHAR(50)
);

CREATE TABLE suppliers (
    supplier_id VARCHAR(10) PRIMARY KEY,
    supplier_name VARCHAR(255),
    zip_code VARCHAR(10), -- Foreign Key to zip_codes
    FOREIGN KEY (zip_code) REFERENCES zip_codes(zip_code)
);

-- Insert data into zip_codes
INSERT INTO zip_codes (zip_code, city, state) VALUES
('12345', 'Anytown', 'NY'),
('67890', 'Otherville', 'CA');

-- Insert data into suppliers (referencing zip_codes)
INSERT INTO suppliers (supplier_id, supplier_name, zip_code) VALUES
('S1', 'Acme Corp', '12345'),
('S2', 'Beta Inc', '67890'),
('S3', 'Gamma Ltd', '12345');
```
</Callout>

<Callout title="Good to know">
There are additional normal forms, such as `4NF`, `5NF`, `6NF`, `EKNF`, `ETNF`, and `DKNF`. We won't cover these here, but we will create a 
dedicated set of tutorials for them in our guides and tutorials section.
</Callout>

