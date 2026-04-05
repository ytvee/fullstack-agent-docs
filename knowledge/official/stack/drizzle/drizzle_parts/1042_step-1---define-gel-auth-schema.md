#### Step 1 - Define Gel auth schema

In `dbschema/default.esdl` file add a Gel schema with an auth extension

```esdl
using extension auth;

module default {
  global current_user := (
    assert_single((
      select User { id, username, email }
      filter .identity = global ext::auth::ClientTokenIdentity
    ))
  );

  type User {
    required identity: ext::auth::Identity;
    required username: str;
    required email: str;
  }
}
```

