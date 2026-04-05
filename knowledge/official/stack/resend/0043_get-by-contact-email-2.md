# Get by contact email
params = {
  "email": "steve.wozniak@gmail.com",
}

Resend::Contacts.get(params)
```
```go
package main

import "github.com/resend/resend-go/v3"

func main() {
	client := resend.NewClient("re_xxxxxxxxx")

	// Get by contact id
	client.Contacts.Get("e169aa45-1ecf-4183-9955-b1499d5701d3")

	// Get by contact email
	client.Contacts.Get("steve.wozniak@gmail.com")
}
```
```rust
use resend_rs::{Resend, Result};

#[tokio::main]
async fn main() -> Result<()> {
  let resend = Resend::new("re_xxxxxxxxx");

  // Get by contact id
  let _contact = resend
    .contacts
    .get("e169aa45-1ecf-4183-9955-b1499d5701d3")
    .await?;

  // Get by contact email
  let _contact = resend
    .contacts
    .get("steve.wozniak@gmail.com")
    .await?;

  Ok(())
}
```
```java
import com.resend.*;

public class Main {
    public static void main(String[] args) {
        Resend resend = new Resend("re_xxxxxxxxx");

        // Get by contact id
        GetContactOptions params = GetContactOptions.builder()
                .id("e169aa45-1ecf-4183-9955-b1499d5701d3")
                .build();

        // Get by contact email
        GetContactOptions params = GetContactOptions.builder()
                .email("steve.wozniak@gmail.com")
                .build();

        GetContactResponseSuccess data = resend.contacts().get(params);
    }
}
```
```csharp
using Resend;

IResend resend = ResendClient.Create( "re_xxxxxxxxx" ); // Or from DI

// Get by contact id
var resp1 = await resend.ContactRetrieveAsync(
    contactId: new Guid( "e169aa45-1ecf-4183-9955-b1499d5701d3" )
);

// Get by contact email
var resp2 = await resend.ContactRetrieveByEmailAsync(
    email: "steve.wozniak@gmail.com"
);

Console.WriteLine( "Contact Email={0}", resp2.Content.Email );
```
```bash
