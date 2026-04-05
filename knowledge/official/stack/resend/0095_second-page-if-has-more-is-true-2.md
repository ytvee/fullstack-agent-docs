# Second page (if has_more is true)
if first_page['has_more']
  last_id = first_page['data'].last['id']
  second_page = Resend::Contacts.list(limit: 50, after: last_id)
end
```
```go
package main

import "github.com/resend/resend-go/v3"

func main() {
	client := resend.NewClient("re_xxxxxxxxx")

	// First page
	firstPage, err := client.Contacts.List(&resend.ListContactsRequest{
		Limit: 50,
	})

	// Second page (if has_more is true)
	if firstPage.HasMore {
		lastId := firstPage.Data[len(firstPage.Data)-1].ID
		client.Contacts.List(&resend.ListContactsRequest{
			Limit: 50,
			After: lastId,
		})
	}
}
```
```rust
use resend_rs::{Resend, Result, types::ListContactOptions};

#[tokio::main]
async fn main() -> Result<()> {
    let resend = Resend::new("re_xxxxxxxxx");

    // First page
    let list_opts = ListContactOptions::default().with_limit(50);
    let first_page = resend.emails.list(list_opts).await?;

    // Second page (if has_more is true)
    if first_page.has_more {
        let last_id = &first_page.data.last().unwrap().id;
        let list_opts = ListContactOptions::default()
            .with_limit(10)
            .list_after(last_id);
        let second_page = resend.contacts.list(list_opts).await?;
    }

    Ok(())
}
```
```java
import com.resend.*;

public class Main {
    public static void main(String[] args) {
        Resend resend = new Resend("re_xxxxxxxxx");

        // First page
        ListEmailsResponse firstPage = resend.emails().list(10);

        // Second page (if has_more is true)
        if (firstPage.getHasMore()) {
            String lastId = firstPage.getData().get(firstPage.getData().size() - 1).getId();
            ListContactsResponse secondPage = resend.contacts().list(50, lastId, null);
        }
    }
}
```
```csharp
using Resend;
using System.Linq;

IResend resend = ResendClient.Create("re_xxxxxxxxx");

// First page
var firstPage = await resend.EmailListAsync( new PaginatedQuery() {
  Limit = 50,
});

// Second page (if has_more is true)
if (firstPage.Content.HasMore)
{
    var lastId = firstPage.Content.Data.Last().Id;
    var secondPage = await resend.EmailListAsync( new PaginatedQuery() {
      Limit = 50,
      After = lastId.ToString(),
    });
}
```
```bash
