# Update by contact email
params = {
  "email": "acme@example.com",
  "unsubscribed": true,
}

Resend::Contacts.update(params)
```
```go
import "github.com/resend/resend-go/v3"

client := resend.NewClient("re_xxxxxxxxx")

// Update by contact id
params := &resend.UpdateContactRequest{
  Id:           "e169aa45-1ecf-4183-9955-b1499d5701d3",
  Unsubscribed: true,
}
params.SetUnsubscribed(true)

contact, err := client.Contacts.Update(params)

// Update by contact email
params = &resend.UpdateContactRequest{
  Email:        "acme@example.com",
  Unsubscribed: true,
}
params.SetUnsubscribed(true)

contact, err := client.Contacts.Update(params)
```
```rust
use resend_rs::{types::ContactChanges, Resend, Result};

#[tokio::main]
async fn main() -> Result<()> {
  let resend = Resend::new("re_xxxxxxxxx");

  let changes = ContactChanges::new().with_unsubscribed(true);

  // Update by contact id
  let _contact = resend
    .contacts
    .update("e169aa45-1ecf-4183-9955-b1499d5701d3", changes.clone())
    .await?;

  // Update by contact email
  let _contact = resend
    .contacts
    .update("acme@example.com", changes)
    .await?;

  Ok(())
}
```
```java
import com.resend.*;

public class Main {
    public static void main(String[] args) {
        Resend resend = new Resend("re_xxxxxxxxx");

        // Update by contact id
        UpdateContactOptions params = UpdateContactOptions.builder()
                .id("e169aa45-1ecf-4183-9955-b1499d5701d3")
                .unsubscribed(true)
                .build();

        // Update by contact email
        UpdateContactOptions params = UpdateContactOptions.builder()
                .email("acme@example.com")
                .unsubscribed(true)
                .build();

        UpdateContactResponseSuccess data = resend.contacts().update(params);
    }
}
```
```csharp
using Resend;

IResend resend = ResendClient.Create( "re_xxxxxxxxx" ); // Or from DI

// By Id
await resend.ContactUpdateAsync(
    contactId: new Guid( "e169aa45-1ecf-4183-9955-b1499d5701d3" ),
    new ContactData()
    {
        FirstName = "Stevie",
        LastName = "Wozniaks",
        IsUnsubscribed = true,
    }
);

// By Email
await resend.ContactUpdateByEmailAsync(
    "acme@example.com",
    new ContactData()
    {
        FirstName = "Stevie",
        LastName = "Wozniaks",
        IsUnsubscribed = true,
    }
);
```
```bash
