# Delete by contact email
Resend::Contacts.remove(
  email: "acme@example.com"
)
```
```go
package main

import "github.com/resend/resend-go/v3"

func main() {
	client := resend.NewClient("re_xxxxxxxxx")

	// Delete by contact id
	client.Contacts.Remove("520784e2-887d-4c25-b53c-4ad46ad38100")

	// Delete by contact email
	client.Contacts.Remove("acme@example.com")
}
```
```rust
use resend_rs::{Resend, Result};

#[tokio::main]
async fn main() -> Result<()> {
  let resend = Resend::new("re_xxxxxxxxx");

  // Delete by contact id
  let _deleted = resend
    .contacts
    .delete("520784e2-887d-4c25-b53c-4ad46ad38100")
    .await?;

  // Delete by contact email
  let _deleted = resend
    .contacts
    .delete("acme@example.com")
    .await?;

  Ok(())
}
```
```java
import com.resend.*;

public class Main {
    public static void main(String[] args) {
        Resend resend = new Resend("re_xxxxxxxxx");

        // Delete by contact id
        resend.contacts().remove(ContactRequestOptions.builder()
                        .id("520784e2-887d-4c25-b53c-4ad46ad38100")
                        .build());

        // Delete by contact email
        resend.contacts().remove(ContactRequestOptions.builder()
                        .email("acme@example.com")
                        .build());
    }
}
```
```csharp
using Resend;

IResend resend = ResendClient.Create( "re_xxxxxxxxx" ); // Or from DI

// By Id
await resend.ContactDeleteAsync(
    contactId: new Guid( "520784e2-887d-4c25-b53c-4ad46ad38100" )
);

// By Email
await resend.ContactDeleteByEmailAsync(
    "acme@example.com"
);
```
```bash
