#### Add routes

Lastly, we need to add some routes for creating and listing tenants and todos. Note how we are using `tenantDB` wrapper to connect to the tenant's virtual database.
Also note how in `app.get("/api/tenants/:tenantId/todos"` we did not need to specify `where tenant_id=...` in the query. 
This is exactly because we are routed to that tenant's database and the query cannot return data for any other tenant.

```typescript copy filename="src/app.ts" {6,20,39,58,62,75,83}
// create new tenant
app.post("/api/tenants", async (req, res) => {
  try {
    const name = req.body.name;
    var tenants: any = null;
    tenants = await tenantDB(async (tx) => {
        return await tx.insert(tenantSchema).values({ name }).returning();
    });
    res.json(tenants);
  } catch (error: any) {
    console.log("error creating tenant: " + error.message);
    res.status(500).json({message: "Internal Server Error",});
  }
});

// return list of tenants
app.get("/api/tenants", async (req, res) => {
  let tenants: any = [];
  try {
      tenants = await tenantDB(async (tx) => {
        return await tx.select().from(tenantSchema);
      });
    res.json(tenants);
  } catch (error: any) {
    console.log("error listing tenants: " + error.message);
    res.status(500).json({message: "Internal Server Error",});
  }
});

// add new task for tenant
app.post("/api/tenants/:tenantId/todos", async (req, res) => {
  try {
    const { title, complete } = req.body;
    if (!title) {
      res.status(400).json({message: "No task title provided",});
    }
    const tenantId = req.params.tenantId;

    const newTodo = await tenantDB(async (tx) => {
      return await tx
        .insert(todoSchema)
        .values({ tenantId, title, complete })
        .returning();
    });
    // return without the embedding vector, since it is huge and useless
    res.json(newTodo);
  } catch (error: any) {
    console.log("error adding task: " + error.message);
    res.status(500).json({message: "Internal Server Error",});
  }
});

// update tasks for tenant
// No need for where clause because we have the tenant in the context
app.put("/api/tenants/:tenantId/todos", async (req, res) => {
  try {
    const { id, complete } = req.body;
    await tenantDB(async (tx) => {
      return await tx
        .update(todoSchema)
        .set({ complete })
        .where(eq(todoSchema.id, id));
    });
    res.sendStatus(200);
  } catch (error: any) {
    console.log("error updating tasks: " + error.message);
    res.status(500).json({message: "Internal Server Error",});
  }
});

// get all tasks for tenant
app.get("/api/tenants/:tenantId/todos", async (req, res) => {
  try {
    // No need for a "where" clause here because we are setting the tenant ID in the context
    const todos = await tenantDB(async (tx) => {
      return await tx
        .select({
          id: todoSchema.id,
          tenant_id: todoSchema.tenantId,
          title: todoSchema.title,
          estimate: todoSchema.estimate,
        })
        .from(todoSchema);
    });
    res.json(todos);
  } catch (error: any) {
    console.log("error listing tasks: " + error.message);
    res.status(500).json({message: error.message,});
  }
});
```

