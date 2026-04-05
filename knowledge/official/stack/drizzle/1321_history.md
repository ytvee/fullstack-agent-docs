## History
<TableWrapper>
|          api version  |   npm version    |     Changed generators                             |
|  :-------------- | :-------------- | :-------------                         |
|       `v1`            | `0.1.1`          |                                         |
|       `v2 (LTS) `       | `0.2.1`          |`string()`, `interval({ isUnique: true })` |
</TableWrapper>

<Callout collapsed="How it works under the hood?">
> This is not an actual API change; it is just an example of how we will proceed with `drizzle-seed` versioning.

For example, `lastName` generator was changed, and new version, `V2`, of this generator became available.

Later, `firstName` generator was changed, making `V3` version of this generator available.

|                  |       `V1`       |      `V2`       |   `V3(latest)`   |
| :--------------: | :--------------: | :-------------: | :--------------: |
| **LastNameGen**  | `LastNameGenV1`  | `LastNameGenV2` |                  |
| **FirstNameGen** | `FirstNameGenV1` |                 | `FirstNameGenV3` |


