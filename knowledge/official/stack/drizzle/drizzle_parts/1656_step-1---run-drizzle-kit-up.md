#### Step 1 - Run `drizzle-kit up`

> Linked discussion: https://github.com/drizzle-team/drizzle-orm/discussions/2832

We've updated the migrations folder structure by:
- removing `journal.json`
- grouping SQL files and snapshots into separate migration folders
- removing the `drizzle-kit drop` command

These changes eliminate potential Git conflicts with the journal file and simplify the process of dropping or fixing conflicted migrations

In upcoming `beta` releases, we'll introduce commutativity checks to help guide you through team migration conflicts, detect possible collisions, and suggest ways to resolve them
> Commutativity discussion: https://github.com/drizzle-team/drizzle-orm/discussions/5005

To migrate previous folders to a new format you would need to run

<Npx>
drizzle-kit up
</Npx>

