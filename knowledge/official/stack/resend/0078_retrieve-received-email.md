# Retrieve Received Email

Source: https://resend.com/docs/api-reference/emails/retrieve-received-email

GET /emails/receiving/:email_id
Retrieve a single received email.

## Path Parameters

<ParamField type="string">
  The ID for the received email.
</ParamField>

## Response Parameters

<ParamField type="object | null">
Raw email content download information. Contains a signed URL to download the original email file including all attachments.

<Expandable title="properties">
    <ParamField type="string">
      Signed CloudFront URL to download the raw email file.
    </ParamField>

<ParamField type="string">
  ISO 8601 timestamp indicating when the download URL expires.
</ParamField>
</Expandable>
</ParamField>

<RequestExample>
  ```js Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { Resend } from 'resend';

const resend = new Resend('re_xxxxxxxxx');

const { data, error } = await resend.emails.receiving.get(
'37e4414c-5e25-4dbc-a071-43552a4bd53b',
);

```

```php PHP theme={"theme":{"light":"github-light","dark":"vesper"}}
$resend = Resend::client('re_xxxxxxxxx');

$resend->emails->receiving->get('37e4414c-5e25-4dbc-a071-43552a4bd53b');
```
```python
import resend

resend.api_key = "re_xxxxxxxxx"

resend.Emails.Receiving.get(email_id="37e4414c-5e25-4dbc-a071-43552a4bd53b")
```
```ruby
require "resend"

Resend.api_key = "re_xxxxxxxxx"

Resend::Emails::Receiving.get("37e4414c-5e25-4dbc-a071-43552a4bd53b")
```
```go
import (
	"context"

	"github.com/resend/resend-go/v3"
)

func main() {
	client := resend.NewClient("re_xxxxxxxxx")

	client.Emails.Receiving.GetWithContext(
		context.TODO(),
		"37e4414c-5e25-4dbc-a071-43552a4bd53b",
	)
}
```
```rust
use resend_rs::{Resend, Result};

#[tokio::main]
async fn main() -> Result<()> {
  let resend = Resend::new("re_xxxxxxxxx");

  let _email = resend
    .receiving
    .get("37e4414c-5e25-4dbc-a071-43552a4bd53b")
    .await?;

  Ok(())
}
```
```java
import com.resend.*;

public class Main {
  public static void main(String[] args) {
    Resend resend = new Resend("re_xxxxxxxxx");

    ReceivedEmail email = resend.receiving().get("37e4414c-5e25-4dbc-a071-43552a4bd53b");
  }
}
```
```csharp
using Resend;

IResend resend = ResendClient.Create( "re_xxxxxxxxx" ); // Or from DI

var resp = await resend.ReceivedEmailRetrieveAsync( new Guid( "4ef9a417-02e9-4d39-ad75-9611e0fcc33c" ) );
Console.WriteLine( "Subject={0}", resp.Content.Subject );
```
```bash
curl -X GET 'https://api.resend.com/emails/receiving/4ef9a417-02e9-4d39-ad75-9611e0fcc33c' \
     -H 'Authorization: Bearer re_xxxxxxxxx'
```
</RequestExample>

<ResponseExample>
  ```json Response theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "object": "email",
    "id": "4ef9a417-02e9-4d39-ad75-9611e0fcc33c",
    "to": ["delivered@resend.dev"],
    "from": "Acme <onboarding@resend.dev>",
    "created_at": "2023-04-03T22:13:42.674981+00:00",
    "subject": "Hello World",
    "html": "Congrats on sending your <strong>first email</strong>!",
    "text": null,
    "headers": {
      "return-path": "lucas.costa@resend.com",
      "mime-version": "1.0"
    },
    "bcc": [],
    "cc": [],
    "reply_to": [],
    "message_id": "<example+123>",
    "raw": {
      "download_url": "https://example.resend.com/receiving/raw/054da427-439a-4e91-b785-e4fb1966285f?Signature=...",
      "expires_at": "2023-04-03T23:13:42.674981+00:00"
    },
    "attachments": [
      {
        "id": "2a0c9ce0-3112-4728-976e-47ddcd16a318",
        "filename": "avatar.png",
        "content_type": "image/png",
        "content_disposition": "inline",
        "content_id": "img001"
      },
      {
        "id": "3b1d0df1-4223-5839-087f-54eedd27b419",
        "filename": "document.pdf",
        "content_type": "application/pdf",
        "content_disposition": null,
        "content_id": null
      }
    ]
  }
  ```
</ResponseExample>

