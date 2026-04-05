### Why NOT Foreign Keys?

While highly beneficial, there are some scenarios where you might reconsider or use Foreign Keys with caution. 
These are typically edge cases and often involve trade-offs.

<Callout collapsed="1. Performance Overhead in Very High-Write Environments">
- **Scenario**: Extremely high-volume transactional systems (e.g., real-time logging, very high-frequency trading
platforms, massive IoT data ingestion).
- **Explanation**: Every time you insert or update data in a table with a foreign key, the database system 
needs to perform checks to ensure referential integrity. In extremely high-write scenarios, these 
checks can introduce a small but potentially noticeable performance overhead.
</Callout>

<Callout collapsed="2. Distributed Database Systems and Cross-Node Foreign Keys:">
- **Scenario**: Systems where data is distributed across multiple database nodes or clusters (common in sharded databases, cloud environments, and microservices).
- **Explanation**:  Cross-node foreign keys can introduce significant complexity and performance overhead. Validating referential integrity requires communication between nodes, leading to increased latency. Distributed transactions needed to maintain consistency are also more complex and can be less performant than local transactions. In such architectures, application-level data integrity checks or eventual consistency models might be considered alternatives.
</Callout>

<Callout collapsed="3. Legacy Systems and Data Integration with Non-Relational Data:">
- **Scenario**: Integrating a relational database with older legacy systems or non-relational data stores (e.g., NoSQL, flat files, external APIs).
- **Explanation**:  Legacy systems or non-relational data might not consistently adhere to the referential integrity rules enforced by foreign keys.  Imposing foreign keys in such scenarios can lead to data import issues, data inconsistencies, and might necessitate complex data transformation or application-level integrity management instead. You might need to carefully evaluate the data quality and consistency of the external sources and potentially rely on application logic or ETL processes to ensure data integrity instead of strictly enforcing foreign keys at the database level.
</Callout>

You can also check out some great explanations from the PlanetScale team in their [article](https://planetscale.com/docs/learn/operating-without-foreign-key-constraints#why-does-planetscale-not-recommend-constraints)

