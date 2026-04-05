### Intersect
Combine only those rows which the results of two query blocks have in common, omitting any duplicates.

Suppose you have two tables that store information about students' course enrollments. 
You want to find the courses that are common between two different departments,
but you want distinct course names, and you're not interested in counting multiple 
enrollments of the same course by the same student.

In this scenario, you want to find courses that are common between the two departments but don't want 
to count the same course multiple times even if multiple students from the same department are enrolled in it.

<Tabs items={["PostgreSQL", "MySQL", "SQLite", "SingleStore", "MSSQL", "CockroachDB"]}>
  <Tab>
  <CodeTabs items={["import-pattern", "builder-pattern", "schema.ts"]}>
	<CodeTab>
	```typescript copy
    import { intersect } from 'drizzle-orm/pg-core'
    import { depA, depB } from './schema'

    const departmentACourses = db.select({ courseName: depA.courseName }).from(depA);
    const departmentBCourses = db.select({ courseName: depB.courseName }).from(depB);

    const result = await intersect(departmentACourses, departmentBCourses);
    ```
    ```sql
    select "course_name" from "department_a_courses"
    intersect
    select "course_name" from "department_b_courses"
    ```
	</CodeTab>
    <CodeTab>
    ```typescript copy
    import { depA, depB } from './schema'

    const result = await db
      .select({ courseName: depA.courseName })
      .from(depA)
      .intersect(db.select({ courseName: depB.courseName }).from(depB));
    ```
    ```sql
    select "course_name" from "department_a_courses"
    intersect
    select "course_name" from "department_b_courses"
    ```
    </CodeTab>
    <CodeTab>
	```typescript copy
    import { integer, pgTable, varchar } from "drizzle-orm/pg-core";

    const depA = pgTable('department_a_courses', {
        studentId: integer('student_id'),
        courseName: varchar('course_name').notNull(),
    });
    
    const depB = pgTable('department_b_courses', {
        studentId: integer('student_id'),
        courseName: varchar('course_name').notNull(),
    });
    ```
    </CodeTab>
  </CodeTabs>
  </Tab> 
  <Tab>
    <CodeTabs items={["import-pattern", "builder-pattern", "schema.ts"]}>
	<CodeTab>
	```typescript copy
    import { intersect } from 'drizzle-orm/mysql-core'
    import { depA, depB } from './schema'

    const departmentACourses = db.select({ courseName: depA.courseName }).from(depA);
    const departmentBCourses = db.select({ courseName: depB.courseName }).from(depB);

    const result = await intersect(departmentACourses, departmentBCourses);
    ```
    ```sql
    select `projects_name` from `department_a_projects`
    intersect
    select `projects_name` from `department_b_projects`
    ```
	</CodeTab>
    <CodeTab>
    ```typescript copy
    import { depA, depB } from './schema'

    const result = await db
      .select({ courseName: depA.courseName })
      .from(depA)
      .intersect(db.select({ courseName: depB.courseName }).from(depB));
    ```
    ```sql
    select `projects_name` from `department_a_projects`
    intersect
    select `projects_name` from `department_b_projects`
    ```
    </CodeTab>
    <CodeTab>
	```typescript copy
    import { int, mysqlTable, varchar } from "drizzle-orm/mysql-core";

    const depA = mysqlTable('department_a_courses', {
        studentId: int('student_id'),
        courseName: varchar('course_name', { length: 256 }).notNull(),
    });
    
    const depB = mysqlTable('department_b_courses', {
        studentId: int('student_id'),
        courseName: varchar('course_name', { length: 256 }).notNull(),
    });
    ```
    </CodeTab>
  </CodeTabs>
  </Tab> 
  <Tab>
      <CodeTabs items={["import-pattern", "builder-pattern", "schema.ts"]}>
	<CodeTab>
	```typescript copy
    import { intersect } from 'drizzle-orm/sqlite-core'
    import { depA, depB } from './schema'

    const departmentACourses = db.select({ courseName: depA.courseName }).from(depA);
    const departmentBCourses = db.select({ courseName: depB.courseName }).from(depB);

    const result = await intersect(departmentACourses, departmentBCourses);
    ```
    ```sql
    select "course_name" from "department_a_courses"
    intersect
    select "course_name" from "department_b_courses"
    ```
	</CodeTab>
    <CodeTab>
    ```typescript copy
    import { depA, depB } from './schema'

    const result = await db
      .select({ courseName: depA.courseName })
      .from(depA)
      .intersect(db.select({ courseName: depB.courseName }).from(depB));
    ```
    ```sql
    select "course_name" from "department_a_courses" 
    intersect 
    select "course_name" from "department_b_courses"
    ```
    </CodeTab>
    <CodeTab>
	```typescript copy
    import { int, sqliteTable, text } from "drizzle-orm/sqlite-core";

    const depA = sqliteTable('department_a_courses', {
        studentId: int('student_id'),
        courseName: text('course_name').notNull(),
    });
    
    const depB = sqliteTable('department_b_courses', {
        studentId: int('student_id'),
        courseName: text('course_name').notNull(),
    });
    ```
    </CodeTab>
  </CodeTabs>
  </Tab> 
  <Tab>
    <CodeTabs items={["import-pattern", "builder-pattern", "schema.ts"]}>
	<CodeTab>
	```typescript copy
    import { intersect } from 'drizzle-orm/singlestore-core'
    import { depA, depB } from './schema'

    const departmentACourses = db.select({ courseName: depA.courseName }).from(depA);
    const departmentBCourses = db.select({ courseName: depB.courseName }).from(depB);

    const result = await intersect(departmentACourses, departmentBCourses);
    ```
    ```sql
    select `projects_name` from `department_a_projects`
    intersect
    select `projects_name` from `department_b_projects`
    ```
	</CodeTab>
    <CodeTab>
    ```typescript copy
    import { depA, depB } from './schema'

    const result = await db
      .select({ courseName: depA.courseName })
      .from(depA)
      .intersect(db.select({ courseName: depB.courseName }).from(depB));
    ```
    ```sql
    select `projects_name` from `department_a_projects`
    intersect
    select `projects_name` from `department_b_projects`
    ```
    </CodeTab>
    <CodeTab>
	```typescript copy
    import { int, singlestoreTable, varchar } from "drizzle-orm/singlestore-core";

    const depA = singlestoreTable('department_a_courses', {
        studentId: int('student_id'),
        courseName: varchar('course_name', { length: 256 }).notNull(),
    });
    
    const depB = singlestoreTable('department_b_courses', {
        studentId: int('student_id'),
        courseName: varchar('course_name', { length: 256 }).notNull(),
    });
    ```
    </CodeTab>
  </CodeTabs>
  </Tab> 
  <Tab>
  <CodeTabs items={["import-pattern", "builder-pattern", "schema.ts"]}>
	<CodeTab>
	```typescript copy
    import { intersect } from 'drizzle-orm/mssql-core'
    import { depA, depB } from './schema'

    const departmentACourses = db.select({ courseName: depA.courseName }).from(depA);
    const departmentBCourses = db.select({ courseName: depB.courseName }).from(depB);

    const result = await intersect(departmentACourses, departmentBCourses);
    ```
    ```sql
    (select `projects_name` from `department_a_projects`)
    intersect
    (select `projects_name` from `department_b_projects`)
    ```
	</CodeTab>
    <CodeTab>
    ```typescript copy
    import { depA, depB } from './schema'

    const result = await db
      .select({ courseName: depA.courseName })
      .from(depA)
      .intersect(db.select({ courseName: depB.courseName }).from(depB));
    ```
    ```sql
    (select `projects_name` from `department_a_projects`)
    intersect
    (select `projects_name` from `department_b_projects`)
    ```
    </CodeTab>
    <CodeTab>
	```typescript copy
    import { int, mssqlTable, varchar } from "drizzle-orm/mssqlTable-core";

    const depA = mssqlTable('department_a_courses', {
        studentId: int('student_id'),
        courseName: varchar('course_name', { length: 256 }).notNull(),
    });
    
    const depB = mssqlTable('department_b_courses', {
        studentId: int('student_id'),
        courseName: varchar('course_name', { length: 256 }).notNull(),
    });
    ```
    </CodeTab>
  </CodeTabs>
  </Tab>
  <Tab>
  <CodeTabs items={["import-pattern", "builder-pattern", "schema.ts"]}>
	<CodeTab>
	```typescript copy
    import { intersect } from 'drizzle-orm/cockroach-core'
    import { depA, depB } from './schema'

    const departmentACourses = db.select({ courseName: depA.courseName }).from(depA);
    const departmentBCourses = db.select({ courseName: depB.courseName }).from(depB);

    const result = await intersect(departmentACourses, departmentBCourses);
    ```
    ```sql
    select "course_name" from "department_a_courses"
    intersect
    select "course_name" from "department_b_courses"
    ```
	</CodeTab>
    <CodeTab>
    ```typescript copy
    import { depA, depB } from './schema'

    const result = await db
      .select({ courseName: depA.courseName })
      .from(depA)
      .intersect(db.select({ courseName: depB.courseName }).from(depB));
    ```
    ```sql
    select "course_name" from "department_a_courses"
    intersect
    select "course_name" from "department_b_courses"
    ```
    </CodeTab>
    <CodeTab>
	```typescript copy
    import { int4, cockroachTable, varchar } from "drizzle-orm/cockroach-core";

    const depA = cockroachTable('department_a_courses', {
        studentId: int4('student_id'),
        courseName: varchar('course_name').notNull(),
    });
    
    const depB = cockroachTable('department_b_courses', {
        studentId: int4('student_id'),
        courseName: varchar('course_name').notNull(),
    });
    ```
    </CodeTab>
  </CodeTabs>
  </Tab> 
</Tabs>

