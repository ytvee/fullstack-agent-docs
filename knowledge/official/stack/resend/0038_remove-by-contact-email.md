# Remove by contact email
removed = Resend::Contacts::Segments.remove(
  email: 'steve.wozniak@gmail.com',
  segment_id: '78261eea-8f8b-4381-83c6-79fa7120f1cf'
)
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

	// Remove by contact id
	removeParams := &resend.RemoveContactSegmentRequest{
		ContactId: "e169aa45-1ecf-4183-9955-b1499d5701d3",
		SegmentId: "78261eea-8f8b-4381-83c6-79fa7120f1cf",
	}

	response, err := client.Contacts.Segments.RemoveWithContext(ctx, removeParams)
	if err != nil {
		panic(err)
	}
	fmt.Println(response)

	// Remove by contact email
	removeByEmailParams := &resend.RemoveContactSegmentRequest{
		Email:     "steve.wozniak@gmail.com",
		SegmentId: "78261eea-8f8b-4381-83c6-79fa7120f1cf",
	}

	response, err = client.Contacts.Segments.RemoveWithContext(ctx, removeByEmailParams)
	if err != nil {
		panic(err)
	}
	fmt.Println(response)
}
```
```rust
use resend_rs::{Resend, Result};

#[tokio::main]
async fn main() -> Result<()> {
  let resend = Resend::new("re_xxxxxxxxx");

  // Update by contact id
  let _contact = resend
    .contacts
    .delete_contact_segment(
      "e169aa45-1ecf-4183-9955-b1499d5701d3",
      "78261eea-8f8b-4381-83c6-79fa7120f1cf",
    )
    .await?;

  // // Update by contact email
  let _contact = resend
    .contacts
    .delete_contact_segment(
      "steve.wozniak@gmail.com",
      "78261eea-8f8b-4381-83c6-79fa7120f1cf",
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

    // Remove by contact id
    RemoveContactFromSegmentOptions optionsById = RemoveContactFromSegmentOptions.builder()
      .id("e169aa45-1ecf-4183-9955-b1499d5701d3")
      .segmentId("78261eea-8f8b-4381-83c6-79fa7120f1cf")
      .build();

    resend.contacts().segments().remove(optionsById);

    // Remove by contact email
    RemoveContactFromSegmentOptions optionsByEmail = RemoveContactFromSegmentOptions.builder()
      .email("steve.wozniak@gmail.com")
      .segmentId("78261eea-8f8b-4381-83c6-79fa7120f1cf")
      .build();

    resend.contacts().segments().remove(optionsByEmail);
  }
}
```
```csharp
using Resend;

IResend resend = ResendClient.Create( "re_xxxxxxxxx" ); // Or from DI

await resend.ContactRemoveFromSegmentAsync(
    contactId: new Guid( "e169aa45-1ecf-4183-9955-b1499d5701d3" ),
    segmentId: new Guid( "78261eea-8f8b-4381-83c6-79fa7120f1cf" )
);
```
```bash
// Update by contact id
curl -X DELETE 'https://api.resend.com/contacts/e169aa45-1ecf-4183-9955-b1499d5701d3/segments/78261eea-8f8b-4381-83c6-79fa7120f1cf' \
     -H 'Authorization: Bearer re_xxxxxxxxx'

// Update by contact email
curl -X DELETE 'https://api.resend.com/contacts/steve.wozniak@gmail.com/segments/78261eea-8f8b-4381-83c6-79fa7120f1cf' \
     -H 'Authorization: Bearer re_xxxxxxxxx' \
     -H 'Content-Type: application/json'
```
</RequestExample>

<ResponseExample>
  ```json Response theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "id": "78261eea-8f8b-4381-83c6-79fa7120f1cf",
    "deleted": true
  }
  ```
</ResponseExample>

