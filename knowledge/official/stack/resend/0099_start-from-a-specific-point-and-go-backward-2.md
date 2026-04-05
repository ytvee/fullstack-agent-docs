# Start from a specific point and go backward
page = Resend::Contacts.list(limit: 50, before: 'some-contact-id')

if page['has_more']
  first_id = page['data'].first['id']
  previous_page = Resend::Contacts.list(limit: 50, before: first_id)
end
```
```go
package main

import "github.com/resend/resend-go/v3"

func main() {
	client := resend.NewClient("re_xxxxxxxxx")

	// Start from a specific point and go backward
	page, err := client.Contacts.List(&resend.ListContactsRequest{
		Limit:  resend.Int(50),
		Before: resend.String("some-contact-id"),
	})

	if page.HasMore {
		firstId := page.Data[0].ID
		client.Contacts.List(&resend.ListContactsRequest{
			Limit:  resend.Int(50),
			Before: resend.String(firstId),
		})
	}
}
```
```rust
use resend_rs::{Resend, Result, types::ListContactOptions};

#[tokio::main]
async fn main() -> Result<()> {
    let resend = Resend::new("re_xxxxxxxxx");

    // Start from a specific point and go backward
    let list_opts = ListContactOptions::default()
        .with_limit(50)
        .list_before("some-email-id");
    let page = resend.contacts.list(list_opts).await?;

    if page.has_more {
        let first_id = &page.data.first().unwrap().id;
        let list_opts = ListContactOptions::default()
            .with_limit(10)
            .list_before(first_id);
        let previous_page = resend.contacts.list(list_opts).await?;
    }

    Ok(())
}
```
```java
import com.resend.*;

public class Main {
    public static void main(String[] args) {
        Resend resend = new Resend("re_xxxxxxxxx");

        // Start from a specific point and go backward
        ListContactsResponse page = resend.contacts().list(50, null, "some-contact-id");

        if (page.getHasMore()) {
            String firstId = page.getData().get(0).getId();
            ListContactsResponse previousPage = resend.contacts().list(50, null, firstId);
        }
    }
}
```
```csharp
using Resend;
using System.Linq;

IResend resend = ResendClient.Create("re_xxxxxxxxx");

// Start from a specific point and go backward
var page = await resend.EmailListAsync( new PaginatedQuery() {
  Limit = 50,
  Before = "some-email-id",
});

if (page.Content.HasMore)
{
    var firstId = page.Content.Data.First().Id;
    var prevPage = await resend.EmailListAsync( new PaginatedQuery() {
      Limit = 50,
      Before = firstId.ToString(),
    });
}
```
```bash
curl -X GET 'https://api.resend.com/contacts?limit=50&before=some-contact-id' \
     -H 'Authorization: Bearer re_xxxxxxxxx'
```
</CodeGroup>

## Best Practices

<AccordionGroup>
  <Accordion title="Use appropriate page sizes">
    Choose a `limit` that balances performance and usability. Smaller pages are good for real-time applications, while larger pages
    (hundreds of items) work better for bulk processing.
  </Accordion>

<Accordion title="Handle pagination gracefully">
Always check the `has_more` field before attempting to fetch additional pages.
This prevents unnecessary API calls when you've reached the end of the
dataset.
</Accordion>

<Accordion title="Consider rate limits">
Be mindful of API rate limits when paginating through large datasets.
Implement appropriate delays or batching strategies if processing many
pages.
</Accordion>
</AccordionGroup>

## Error Handling

Pagination requests may return the following validation errors:


| Error              | Description                                         |
| ------------------ | --------------------------------------------------- |
| `validation_error` | Invalid cursor format or limit out of range (1-100) |
| `validation_error` | Both`before` and `after` parameters provided        |

Example error response:

```json
{
  "name": "validation_error",
  "statusCode": 422,
  "message": "The pagination limit must be a number between 1 and 100. See https://resend.com/docs/pagination for more information."
}
```
