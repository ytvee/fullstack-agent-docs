#### Many-to-Many

In a many-to-many relationship, one record in `table A` can be related to many records in `table B`, and one 
record in `table B` can be related to many records in `table A`. It's a more complex, bidirectional relationship.

<Callout collapsed="Use Cases & Examples">
1. **Students and Courses**: One student can enroll in many courses, and one course can have many students enrolled.
2. **Products and Categories**: One product can belong to multiple categories (e.g., a "T-shirt" can be
in "Clothing" and "Summer Wear" categories), and one category can contain many products.
3. **Authors and Books**: A book can be written by multiple authors, and an author can write multiple books.

```
Table A (Many Side)    Junction Table      Table B (Many Side)
+---------+          +-------------+     +---------+
| PK (A)  | -------->| FK (A)      | <----| FK (B)  |
| ...     |          | FK (B)      |     | ...     |
+---------+          +-------------+     +---------+
     (Many)             (Junction)          (Many)
```
</Callout>

Many-to-many relationships are not directly implemented with foreign keys between the two main tables. 
Instead, you need a `junction` table (also called an associative table or bridging table). 
This table acts as an intermediary to link records from both tables.

```sql
-- Table for Students (Many side)
CREATE TABLE students (
    iid INT PRIMARY KEY,
    name VARCHAR(255)
);

-- Table for Courses (Many side)
CREATE TABLE courses (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    credits INT
);

-- Junction Table: Enrollments (Connects Students and Courses - M-M relationship)
CREATE TABLE enrollments (
    id INT PRIMARY KEY AUTO_INCREMENT, -- Optional, but good practice for junction tables
    student_id INT,
    course_id INT,
    enrollment_date DATE,
    -- Composite Foreign Keys (often part of a composite primary key or unique constraint)
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (course_id) REFERENCES courses(id),
    UNIQUE KEY (student_id, course_id) -- Prevent duplicate enrollments for the same student and course
);
```

