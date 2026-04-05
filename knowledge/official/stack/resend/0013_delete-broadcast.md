# Delete Broadcast

Source: https://resend.com/docs/api-reference/broadcasts/delete-broadcast

DELETE /broadcasts/:broadcast_id
Remove an existing broadcast.

You can only delete broadcasts that are in the `draft` status. In addition, if you delete a broadcast that has already been scheduled to be sent, we will automatically cancel the scheduled delivery and it won't be sent.

## Path Parameters

<ResendParamField type="string">
  The broadcast ID.
</ResendParamField>

<RequestExample>
  ```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { Resend } from 'resend';

const resend = new Resend('re_xxxxxxxxx');

const { data, error } = await resend.broadcasts.remove(
'559ac32e-9ef5-46fb-82a1-b76b840c0f7b',
);

```

```php PHP theme={"theme":{"light":"github-light","dark":"vesper"}}
$resend = Resend::client('re_xxxxxxxxx');

$resend->broadcasts->remove('559ac32e-9ef5-46fb-82a1-b76b840c0f7b');
```

```py
import resend

resend.api_key = "re_xxxxxxxxx"

resend.Broadcasts.remove(id="559ac32e-9ef5-46fb-82a1-b76b840c0f7b")
```

```ruby
require "resend"

Resend.api_key = "re_xxxxxxxxx"

Resend::Broadcasts.remove("559ac32e-9ef5-46fb-82a1-b76b840c0f7b")
```

```go
package main

import "github.com/resend/resend-go/v3"

func main() {
	client := resend.NewClient("re_xxxxxxxxx")

	client.Broadcasts.Remove("559ac32e-9ef5-46fb-82a1-b76b840c0f7b")
}
```

```rust
use resend_rs::{Resend, Result};

#[tokio::main]
async fn main() -> Result<()> {
  let resend = Resend::new("re_xxxxxxxxx");

  let _deleted = resend
    .broadcasts
    .delete("559ac32e-9ef5-46fb-82a1-b76b840c0f7b")
    .await?;

  Ok(())
}
```

```java
Resend resend = new Resend("re_xxxxxxxxx");

RemoveBroadcastResponseSuccess data = resend.broadcasts().remove("559ac32e-9ef5-46fb-82a1-b76b840c0f7b");
```

```csharp
using Resend;

IResend resend = ResendClient.Create( "re_xxxxxxxxx" ); // Or from DI

await resend.BroadcastDeleteAsync( new Guid( "559ac32e-9ef5-46fb-82a1-b76b840c0f7b" ) );
```

```bash
curl -X DELETE 'https://api.resend.com/broadcasts/559ac32e-9ef5-46fb-82a1-b76b840c0f7b' \
     -H 'Authorization: Bearer re_xxxxxxxxx'
```

</RequestExample>

<ResponseExample>
  ```json Response theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "object": "broadcast",
    "id": "559ac32e-9ef5-46fb-82a1-b76b840c0f7b",
    "deleted": true
  }
  ```
</ResponseExample>

