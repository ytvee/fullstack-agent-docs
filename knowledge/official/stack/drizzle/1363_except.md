### Except
For two query blocks A and B, return all results from A which are not also present in B, omitting any duplicates.

Suppose you have two tables that store information about employees' project assignments. 
You want to find the projects that are unique to one department 
and not shared with another department, excluding duplicates.

In this scenario, you want to identify the projects that are exclusive to one department and
not shared with the other department. You don't want to count the same project 
multiple times, even if multiple employees from the same department are assigned to it.

<Tabs items={["PostgreSQL", "MySQL", "SQLite", "SingleStore", "MSSQL", "CockroachDB"]}>
  <Tab>
  <CodeTabs items={["import-pattern", "builder-pattern", "schema.ts"]}>
	<CodeTab>
	```typescript copy
    import { except } from 'drizzle-orm/pg-core'
    import { depA, depB } from './schema'

    const departmentACourses = db.select({ courseName: depA.projectsName }).from(depA);
    const departmentBCourses = db.select({ courseName: depB.projectsName }).from(depB);

    const result = await except(departmentACourses, departmentBCourses);
    ```
    ```sql
    select "projects_name" from "department_a_projects"
    except
    select "projects_name" from "department_b_projects"
    ```
	</CodeTab>
    <CodeTab>
    ```ts copy
    import { depA, depB } from './schema'

    const result = await db
        .select({ courseName: depA.projectsName })
        .from(depA)
        .except(db.select({ courseName: depB.projectsName }).from(depB));
    ```
    ```sql
    select "projects_name" from "department_a_projects"
    except
    select "projects_name" from "department_b_projects"
    ```
    </CodeTab>
    <CodeTab>
	```typescript copy
    import { integer, pgTable, varchar } from "drizzle-orm/pg-core";

    const depA = pgTable('department_a_projects', {
        employeeId: integer('employee_id'),
        projectsName: varchar('projects_name').notNull(),
    });
    
    const depB = pgTable('department_b_projects', {
        employeeId: integer('employee_id'),
        projectsName: varchar('projects_name').notNull(),
    });
    ```
    </CodeTab>
  </CodeTabs>
  </Tab> 
  <Tab>
  <CodeTabs items={["import-pattern", "builder-pattern", "schema.ts"]}>
	<CodeTab>
	```typescript copy
    import { except } from 'drizzle-orm/mysql-core'
    import { depA, depB } from './schema'

    const departmentACourses = db.select({ courseName: depA.projectsName }).from(depA);
    const departmentBCourses = db.select({ courseName: depB.projectsName }).from(depB);

    const result = await except(departmentACourses, departmentBCourses);
    ```
    ```sql
    select `projects_name` from `department_a_projects`
    except
    select `projects_name` from `department_b_projects`
    ```
	</CodeTab>
    <CodeTab>
    ```ts copy
    import { depA, depB } from './schema'

    const result = await db
        .select({ courseName: depA.projectsName })
        .from(depA)
        .except(db.select({ courseName: depB.projectsName }).from(depB));
    ```
    ```sql
    select `projects_name` from `department_a_projects`
    except
    select `projects_name` from `department_b_projects`
    ```
    </CodeTab>
    <CodeTab>
	```typescript 
    import { int, mysqlTable, varchar } from "drizzle-orm/mysql-core";

    const depA = mysqlTable('department_a_projects', {
        employeeId: int('employee_id'),
        projectsName: varchar('projects_name', { length: 256 }).notNull(),
    });
    
    const depB = mysqlTable('department_b_projects', {
        employeeId: int('employee_id'),
        projectsName: varchar('projects_name', { length: 256 }).notNull(),
    });
    ```
    </CodeTab>
  </CodeTabs>
  </Tab> 
  <Tab>
  <CodeTabs items={["import-pattern", "builder-pattern", "schema.ts"]}>
	<CodeTab>
	```typescript copy
    import { except } from 'drizzle-orm/sqlite-core'
    import { depA, depB } from './schema'

    const departmentACourses = db.select({ courseName: depA.projectsName }).from(depA);
    const departmentBCourses = db.select({ courseName: depB.projectsName }).from(depB);

    const result = await except(departmentACourses, departmentBCourses);
    ```
    ```sql
    select "projects_name" from "department_a_projects" 
    except 
    select "projects_name" from "department_b_projects"
    ```
	</CodeTab>
    <CodeTab>
    ```ts copy
    import { depA, depB } from './schema'

    const result = await db
        .select({ courseName: depA.projectsName })
        .from(depA)
        .except(db.select({ courseName: depB.projectsName }).from(depB));
    ```
    ```sql
    select "projects_name" from "department_a_projects" 
    except 
    select "projects_name" from "department_b_projects"
    ```
    </CodeTab>
    <CodeTab>
	```typescript copy
    import { int, sqliteTable, text } from "drizzle-orm/sqlite-core";

    const depA = sqliteTable('department_a_projects', {
        employeeId: int('employee_id'),
        projectsName: text('projects_name').notNull(),
    });
    
    const depB = sqliteTable('department_b_projects', {
        employeeId: int('employee_id'),
        projectsName: text('projects_name').notNull(),
    });
    ```
    </CodeTab>
  </CodeTabs>
  </Tab> 
  <Tab>
  <CodeTabs items={["import-pattern", "builder-pattern", "schema.ts"]}>
	<CodeTab>
	```typescript copy
    import { except } from 'drizzle-orm/singlestore-core'
    import { depA, depB } from './schema'

    const departmentACourses = db.select({ courseName: depA.projectsName }).from(depA);
    const departmentBCourses = db.select({ courseName: depB.projectsName }).from(depB);

    const result = await except(departmentACourses, departmentBCourses);
    ```
    ```sql
    select `projects_name` from `department_a_projects`
    except
    select `projects_name` from `department_b_projects`
    ```
	</CodeTab>
    <CodeTab>
    ```ts copy
    import { depA, depB } from './schema'

    const result = await db
        .select({ courseName: depA.projectsName })
        .from(depA)
        .except(db.select({ courseName: depB.projectsName }).from(depB));
    ```
    ```sql
    select `projects_name` from `department_a_projects`
    except
    select `projects_name` from `department_b_projects`
    ```
    </CodeTab>
    <CodeTab>
	```typescript 
    import { int, singlestoreTable, varchar } from "drizzle-orm/singlestore-core";

    const depA = singlestoreTable('department_a_projects', {
        employeeId: int('employee_id'),
        projectsName: varchar('projects_name', { length: 256 }).notNull(),
    });
    
    const depB = singlestoreTable('department_b_projects', {
        employeeId: int('employee_id'),
        projectsName: varchar('projects_name', { length: 256 }).notNull(),
    });
    ```
    </CodeTab>
  </CodeTabs>
  </Tab> 
  <Tab>
  <CodeTabs items={["import-pattern", "builder-pattern", "schema.ts"]}>
	<CodeTab>
	```typescript copy
    import { except } from 'drizzle-orm/mssql-core'
    import { depA, depB } from './schema'

    const departmentACourses = db.select({ courseName: depA.projectsName }).from(depA);
    const departmentBCourses = db.select({ courseName: depB.projectsName }).from(depB);

    const result = await except(departmentACourses, departmentBCourses);
    ```
    ```sql
    (select `projects_name` from `department_a_projects`)
    except
    (select `projects_name` from `department_b_projects`)
    ```
	</CodeTab>
    <CodeTab>
    ```ts copy
    import { depA, depB } from './schema'

    const result = await db
        .select({ courseName: depA.projectsName })
        .from(depA)
        .except(db.select({ courseName: depB.projectsName }).from(depB));
    ```
    ```sql
    (select `projects_name` from `department_a_projects`)
    except
    (select `projects_name` from `department_b_projects`)
    ```
    </CodeTab>
    <CodeTab>
	```typescript 
    import { int, mssqlTable, nvarchar } from "drizzle-orm/mssql-core";

    const depA = mssqlTable('department_a_projects', {
        employeeId: int('employee_id'),
        projectsName: nvarchar('projects_name', { length: 256 }).notNull(),
    });
    
    const depB = mssqlTable('department_b_projects', {
        employeeId: int('employee_id'),
        projectsName: nvarchar('projects_name', { length: 256 }).notNull(),
    });
    ```
    </CodeTab>
  </CodeTabs>
  </Tab> 
  <Tab>
  <CodeTabs items={["import-pattern", "builder-pattern", "schema.ts"]}>
	<CodeTab>
	```typescript copy
    import { except } from 'drizzle-orm/cockroach-core'
    import { depA, depB } from './schema'

    const departmentACourses = db.select({ courseName: depA.projectsName }).from(depA);
    const departmentBCourses = db.select({ courseName: depB.projectsName }).from(depB);

    const result = await except(departmentACourses, departmentBCourses);
    ```
    ```sql
    select "projects_name" from "department_a_projects"
    except
    select "projects_name" from "department_b_projects"
    ```
	</CodeTab>
    <CodeTab>
    ```ts copy
    import { depA, depB } from './schema'

    const result = await db
        .select({ courseName: depA.projectsName })
        .from(depA)
        .except(db.select({ courseName: depB.projectsName }).from(depB));
    ```
    ```sql
    select "projects_name" from "department_a_projects"
    except
    select "projects_name" from "department_b_projects"
    ```
    </CodeTab>
    <CodeTab>
	```typescript copy
    import { int4, cockroachTable, varchar } from "drizzle-orm/cockroach-core";

    const depA = cockroachTable('department_a_projects', {
        employeeId: int4('employee_id'),
        projectsName: varchar('projects_name').notNull(),
    });
    
    const depB = cockroachTable('department_b_projects', {
        employeeId: int4('employee_id'),
        projectsName: varchar('projects_name').notNull(),
    });
    ```
    </CodeTab>
  </CodeTabs>
  </Tab> 
</Tabs>

