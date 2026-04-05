# List API keys

Source: https://resend.com/docs/api-reference/api-keys/list-api-keys

GET /api-keys
Retrieve a list of API keys for the authenticated user.

<QueryParams type="API keys" />

<RequestExample>
  ```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { Resend } from 'resend';

const resend = new Resend('re_xxxxxxxxx');

const { data, error } = await resend.apiKeys.list();

```

```php PHP theme={"theme":{"light":"github-light","dark":"vesper"}}
$resend = Resend::client('re_xxxxxxxxx');

$resend->apiKeys->list();
```

```python
import resend

resend.api_key = "re_xxxxxxxxx"
resend.ApiKeys.list()
```

```ruby
require "resend"

Resend.api_key = "re_xxxxxxxxx"

Resend::ApiKeys.list
```

```go
package main

import "github.com/resend/resend-go/v3"

func main() {
	client := resend.NewClient("re_xxxxxxxxx")
	client.ApiKeys.List()
}
```

```rust
use resend_rs::{Resend, Result, list_opts::ListOptions};

#[tokio::main]
async fn main() -> Result<()> {
  let resend = Resend::new("re_xxxxxxxxx");

  let _api_keys = resend.api_keys.list(ListOptions::default()).await?;

  Ok(())
}
```

```java
import com.resend.*;

public class Main {
    public static void main(String[] args) {
        Resend resend = new Resend("re_xxxxxxxxx");

        resend.apiKeys().list();
    }
}
```

```csharp
using Resend;

IResend resend = ResendClient.Create( "re_xxxxxxxxx" ); // Or from DI

var resp = await resend.ApiKeyListAsync();
Console.WriteLine( "Nr keys={0}", resp.Content.Count );
```

```bash
curl -X GET 'https://api.resend.com/api-keys' \
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
        "id": "91f3200a-df72-4654-b0cd-f202395f5354",
        "name": "Production",
        "created_at": "2023-04-08T00:11:13.110779+00:00",
        "last_used_at": "2024-11-01T17:09:51.813959+00:00"
      }
    ]
  }
  ```
</ResponseExample>

