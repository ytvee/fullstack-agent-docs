# Get by contact email
contact_topics = Resend::Contacts::Topics.list(id: "steve.wozniak@gmail.com")
```
```go
package main

import (
	"context"
	"fmt"

	"github.com/resend/resend-go/v3"
)

func main() {
	ctx := context.TODO()
	client := resend.NewClient("re_xxxxxxxxx")

	// Get by contact id
	topics, err := client.Contacts.Topics.ListWithContext(ctx, &resend.ListContactTopicsRequest{
		ContactId: "e169aa45-1ecf-4183-9955-b1499d5701d3",
	})
	if err != nil {
		panic(err)
	}
	fmt.Println(topics)

	// Get by contact email
	topics, err = client.Contacts.Topics.ListWithContext(ctx, &resend.ListContactTopicsRequest{
		Email: "steve.wozniak@gmail.com",
	})
	if err != nil {
		panic(err)
	}
	fmt.Println(topics)
}
```
```rust
use resend_rs::{list_opts::ListOptions, Resend, Result};

#[tokio::main]
async fn main() -> Result<()> {
  let resend = Resend::new("re_xxxxxxxxx");

  let _topics = resend
    .contacts
    .get_contact_topics(
      "e169aa45-1ecf-4183-9955-b1499d5701d3",
      ListOptions::default(),
    )
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
    resend.contacts().topics().list("e169aa45-1ecf-4183-9955-b1499d5701d3");

    // Get by contact email
    resend.contacts().topics().list("steve.wozniak@gmail.com");
  }
}
```
```csharp
using Resend;

IResend resend = ResendClient.Create( "re_xxxxxxxxx" ); // Or from DI

var resp = await resend.ContactListTopicsAsync( new Guid( "e169aa45-1ecf-4183-9955-b1499d5701d3" ));
Console.WriteLine( "Nr Topics={0}", resp.Content.Data.Count );
```
```bash
// Get by contact id
curl -X GET 'https://api.resend.com/contacts/e169aa45-1ecf-4183-9955-b1499d5701d3/topics' \
     -H 'Authorization: Bearer re_xxxxxxxxx'

// Get by contact email
curl -X GET 'https://api.resend.com/contacts/steve.wozniak@gmail.com/topics' \
     -H 'Authorization: Bearer re_xxxxxxxxx'
```
</RequestExample>

<ResponseExample>
  ```json Response theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "object": "list",
    "has_more": false,
    "data": [
      {
        "id": "b6d24b8e-af0b-4c3c-be0c-359bbd97381e",
        "name": "Product Updates",
        "description": "New features, and latest announcements.",
        "subscription": "opt_in"
      }
    ]
  }
  ```
</ResponseExample>

