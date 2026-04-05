#### Step 2 - Define basic Gel schema

In `dbschema/default.esdl` file add a basic Gel schema

```esdl
module default {
    type user {
        name: str;
        required email: str;
        age: int16;
    }
}
```

