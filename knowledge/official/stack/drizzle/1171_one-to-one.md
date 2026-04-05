#### One-to-One

In a one-to-one relationship, each record in `table A` is related to at most one record in `table B`, and each record in `table B` is
related to at most one record in `table A`. It's a very direct, exclusive pairing.

<Callout collapsed="Use Cases & Examples">
1. **User Profiles and User Account Details**: Think of a website. Each user account (in a Users table) might have exactly one user profile (in a UserProfiles table) containing more detailed information.
2. **Employees and Parking Spaces**: An Employees table and a ParkingSpaces table. Each employee might be assigned at most one parking space, and each parking space is assigned to at most one employee.
3. **Splitting Tables for Organization**: Sometimes, you might split a very wide table into two for better organization or security reasons, maintaining a 1-1 relationship between them.

```
Table A (One Side)      Table B (One Side)
+---------+             +---------+
| PK (A)  | <---------> | FK (A)  | (Foreign Key referencing Table A)
| ...     |             | ...     |
+---------+             +---------+
```
</Callout>


