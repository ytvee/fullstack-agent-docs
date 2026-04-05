#### Limitations

Currently, the SingleStore dialect has a set of limitations and features that do not work on the SingleStore database side:

- SingleStore's serial column type only ensures the uniqueness of column values.
- `ORDER BY` and `LIMIT` cannot be chained together.
- Foreign keys are not supported (check).
- `INTERSECT ALL` and `EXCEPT ALL` operations are not supported by SingleStore.
- Nested transactions are not supported by [SingleStore](https://docs.singlestore.com/cloud/reference/sql-reference/procedural-sql-reference/transactions-in-stored-procedures/).
- SingleStore [only supports](https://docs.singlestore.com/cloud/getting-started-with-singlestore-helios/about-singlestore-helios/singlestore-helios-faqs/durability/) one `isolationLevel`.
- The FSP option in `DATE`, `TIMESTAMP`, and `DATETIME` is not supported.
- The relational API is not supported and will be implemented once the SingleStore team develops all the necessary APIs for it.
- There may be more limitations because SingleStore is not 100% compatible with MySQL.

