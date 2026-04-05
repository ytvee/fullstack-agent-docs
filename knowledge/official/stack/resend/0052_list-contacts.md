# List Contacts

Source: https://resend.com/docs/api-reference/contacts/list-contacts

GET /contacts
Show all contacts.

## Path Parameters

<ResendParamField type="string">
  The Segment ID to filter contacts by. If provided, only contacts in this Segment will be returned.
</ResendParamField>

<QueryParams type="contacts" />

<RequestExample>
  ```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { Resend } from 'resend';

const resend = new Resend('re_xxxxxxxxx');

const { data, error } = await resend.contacts.list();

```

```php PHP theme={"theme":{"light":"github-light","dark":"vesper"}}
$resend = Resend::client('re_xxxxxxxxx');

$resend->contacts->list();
```
```python
import resend

resend.api_key = "re_xxxxxxxxx"

resend.Contacts.list()
```
```ruby
require "resend"

Resend.api_key = "re_xxxxxxxxx"

Resend::Contacts.list()
```
```go
package main

import "github.com/resend/resend-go/v3"

func main() {
	client := resend.NewClient("re_xxxxxxxxx")

	client.Contacts.List()
}
```
```rust
use resend_rs::{Resend, Result, list_opts::ListOptions};

#[tokio::main]
async fn main() -> Result<()> {
  let resend = Resend::new("re_xxxxxxxxx");

  let _contacts = resend
    .contacts
    .list(
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

        ListContactsResponseSuccess data = resend.contacts().list();
    }
}
```
```csharp
using Resend;

IResend resend = ResendClient.Create( "re_xxxxxxxxx" ); // Or from DI

var resp = await resend.ContactListAsync();
Console.WriteLine( "Nr Contacts={0}", resp.Content.Data.Count );
```
```bash
curl -X GET 'https://api.resend.com/contacts' \
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
        "id": "e169aa45-1ecf-4183-9955-b1499d5701d3",
        "email": "steve.wozniak@gmail.com",
        "first_name": "Steve",
        "last_name": "Wozniak",
        "created_at": "2023-10-06T23:47:56.678Z",
        "unsubscribed": false
      }
    ]
  }
  ```
</ResponseExample>

