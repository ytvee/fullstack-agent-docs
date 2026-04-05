# Delete Webhook

Source: https://resend.com/docs/api-reference/webhooks/delete-webhook

DELETE /webhooks/:webhook_id
Remove an existing webhook.

## Path Parameters

<ResendParamField type="string">
  The Webhook ID.
</ResendParamField>

<RequestExample>
  ```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { Resend } from 'resend';

const resend = new Resend('re_xxxxxxxxx');

const { data, error } = await resend.webhooks.remove(
'4dd369bc-aa82-4ff3-97de-514ae3000ee0',
);

```

```php PHP theme={"theme":{"light":"github-light","dark":"vesper"}}
$resend = Resend::client('re_xxxxxxxxx');

$resend->webhooks->remove('4dd369bc-aa82-4ff3-97de-514ae3000ee0');
```
```python
import resend

resend.api_key = 're_xxxxxxxxx'

webhook = resend.Webhooks.remove(webhook_id='4dd369bc-aa82-4ff3-97de-514ae3000ee0')
```
```ruby
require 'resend'

Resend.api_key = 're_xxxxxxxxx'

webhook = Resend::Webhooks.remove('4dd369bc-aa82-4ff3-97de-514ae3000ee0')
```
```go
package main

import "github.com/resend/resend-go/v3"

func main() {
	client := resend.NewClient("re_xxxxxxxxx")

	client.Webhooks.Remove("4dd369bc-aa82-4ff3-97de-514ae3000ee0")
}
```
```rust
use resend_rs::{Resend, Result};

#[tokio::main]
async fn main() -> Result<()> {
  let resend = Resend::new("re_xxxxxxxxx");

  let _deleted = resend
    .webhooks
    .delete("4dd369bc-aa82-4ff3-97de-514ae3000ee0")
    .await?;

  Ok(())
}
```
```java
import com.resend.*;

public class Main {
    public static void main(String[] args) {
        Resend resend = new Resend("re_xxxxxxxxx");

        RemoveWebhookResponseSuccess response = resend.webhooks().remove("4dd369bc-aa82-4ff3-97de-514ae3000ee0");
    }
}
```
```csharp
using Resend;

IResend resend = ResendClient.Create( "re_xxxxxxxxx" ); // Or from DI

await resend.WebhookDeleteAsync( new Guid( "d91cd9bd-1176-453e-8fc1-35364d380206" ) );
```
```bash
curl -X DELETE 'https://api.resend.com/webhooks/4dd369bc-aa82-4ff3-97de-514ae3000ee0' \
     -H 'Authorization: Bearer re_xxxxxxxxx'
```
</RequestExample>

<ResponseExample>
  ```json Response theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "object": "webhook",
    "id": "4dd369bc-aa82-4ff3-97de-514ae3000ee0",
    "deleted": true
  }
  ```
</ResponseExample>

