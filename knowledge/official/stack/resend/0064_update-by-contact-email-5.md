# Update by contact email
update_params = {
  email: "steve.wozniak@gmail.com",
  topics: [
    { id: "07d84122-7224-4881-9c31-1c048e204602", subscription: "opt_out" },
    { id: "07d84122-7224-4881-9c31-1c048e204602", subscription: "opt_in" }
  ]
}
updated_topics = Resend::Contacts::Topics.update(update_params)
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

	// Update by contact id
	params := &resend.UpdateContactTopicsRequest{
		ContactId: "e169aa45-1ecf-4183-9955-b1499d5701d3",
		Topics: []resend.TopicSubscriptionUpdate{
			{
				Id:           "b6d24b8e-af0b-4c3c-be0c-359bbd97381e",
				Subscription: "opt_out",
			},
			{
				Id:           "07d84122-7224-4881-9c31-1c048e204602",
				Subscription: "opt_in",
			},
		},
	}

	updatedTopics, err := client.Contacts.Topics.UpdateWithContext(ctx, params)
	if err != nil {
		panic(err)
	}
	fmt.Println(updatedTopics)

	// Update by contact email
	params = &resend.UpdateContactTopicsRequest{
		Email: "steve.wozniak@gmail.com",
		Topics: []resend.TopicSubscriptionUpdate{
			{
				Id:           "07d84122-7224-4881-9c31-1c048e204602",
				Subscription: "opt_out",
			},
			{
				Id:           "b6d24b8e-af0b-4c3c-be0c-359bbd97381e",
				Subscription: "opt_in",
			},
		},
	}

	updatedTopics, err = client.Contacts.Topics.UpdateWithContext(ctx, params)
	if err != nil {
		panic(err)
	}
	fmt.Println(updatedTopics)
}
```
```rust
use resend_rs::{
  types::{SubscriptionType, UpdateContactTopicOptions},
  Resend, Result,
};

#[tokio::main]
async fn main() -> Result<()> {
  let resend = Resend::new("re_xxxxxxxxx");

  let topics = [
    UpdateContactTopicOptions::new(
      "b6d24b8e-af0b-4c3c-be0c-359bbd97381e",
      SubscriptionType::OptOut,
    ),
    UpdateContactTopicOptions::new(
      "07d84122-7224-4881-9c31-1c048e204602",
      SubscriptionType::OptIn,
    ),
  ];

  let _contact = resend
    .contacts
    .update_contact_topics("e169aa45-1ecf-4183-9955-b1499d5701d3", topics)
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
    UpdateContactTopicsOptions optionsById = UpdateContactTopicsOptions.builder()
                .id("e169aa45-1ecf-4183-9955-b1499d5701d3")
                .topics(ContactTopicOptions.builder()
                            .id("b6d24b8e-af0b-4c3c-be0c-359bbd97381e")
                            .subscription("opt_out")
                            .build(),
                        ContactTopicOptions.builder()
                            .id("07d84122-7224-4881-9c31-1c048e204602")
                            .subscription("opt_in")
                            .build())
                .build();

    resend.contacts().topics().update(optionsById);

    // Update by contact email
    UpdateContactTopicsOptions optionsByEmail = UpdateContactTopicsOptions.builder()
                .email("steve.wozniak@gmail.com")
                .topics(ContactTopicOptions.builder()
                            .id("07d84122-7224-4881-9c31-1c048e204602")
                            .subscription("opt_in")
                            .build(),
                        ContactTopicOptions.builder()
                            .id("b6d24b8e-af0b-4c3c-be0c-359bbd97381e")
                            .subscription("opt_out")
                            .build())
                .build();

    resend.contacts().topics().update(optionsById);
  }
}
```
```csharp
using Resend;

IResend resend = ResendClient.Create( "re_xxxxxxxxx" ); // Or from DI

var topics = new List<TopicSubscription>();

topics.Add( new TopicSubscription() {
  Id = new Guid( "07d84122-7224-4881-9c31-1c048e204602" ),
  Subscription = SubscriptionType.OptIn,
});

topics.Add( new TopicSubscription() {
  Id = new Guid( "b6d24b8e-af0b-4c3c-be0c-359bbd97381e" ),
  Subscription = SubscriptionType.OptOut,
});

await resend.ContactUpdateTopicsAsync(
    new Guid( "e169aa45-1ecf-4183-9955-b1499d5701d3" ),
    topics );
```
```bash
// Update by contact id
curl -X PATCH 'https://api.resend.com/contacts/e169aa45-1ecf-4183-9955-b1499d5701d3/topics' \
     -H 'Authorization: Bearer re_xxxxxxxxx' \
     -H 'Content-Type: application/json' \
     -d $'[
      {
        "id": "b6d24b8e-af0b-4c3c-be0c-359bbd97381e",
        "subscription": "opt_out"
      }
     ]'

// Update by contact email
curl -X PATCH 'https://api.resend.com/contacts/steve.wozniak@gmail.com/topics' \
     -H 'Authorization: Bearer re_xxxxxxxxx' \
     -H 'Content-Type: application/json' \
     -d $'[
      {
        "id": "b6d24b8e-af0b-4c3c-be0c-359bbd97381e",
        "subscription": "opt_out"
      }
     ]'
```
</RequestExample>

<ResponseExample>
  ```json Response theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "id": "b6d24b8e-af0b-4c3c-be0c-359bbd97381e"
  }
  ```
</ResponseExample>

