# Delete API key

Source: https://resend.com/docs/api-reference/api-keys/delete-api-key

DELETE /api-keys/:api_key_id
Remove an existing API key.

## Path Parameters

<ResendParamField type="string">
  The API key ID.
</ResendParamField>

<RequestExample>
  ```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { Resend } from 'resend';

const resend = new Resend('re_xxxxxxxxx');

const { data, error } = await resend.apiKeys.remove(
'b6d24b8e-af0b-4c3c-be0c-359bbd97381e',
);

```

```php PHP theme={"theme":{"light":"github-light","dark":"vesper"}}
$resend = Resend::client('re_xxxxxxxxx');

$resend->apiKeys->remove('b6d24b8e-af0b-4c3c-be0c-359bbd97381e');
```

```python
import resend

resend.api_key = "re_xxxxxxxxx"
resend.ApiKeys.remove(api_key_id="b6d24b8e-af0b-4c3c-be0c-359bbd97381e")
```

```ruby
require "resend"

Resend.api_key = "re_xxxxxxxxx"

Resend::ApiKeys.remove "b6d24b8e-af0b-4c3c-be0c-359bbd97381e"
```

```go
package main

import "github.com/resend/resend-go/v3"

func main() {
	client := resend.NewClient("re_xxxxxxxxx")
	client.ApiKeys.Remove("b6d24b8e-af0b-4c3c-be0c-359bbd97381e")
}
```

```rust
use resend_rs::{Resend, Result};

#[tokio::main]
async fn main() -> Result<()> {
  let resend = Resend::new("re_xxxxxxxxx");

  resend
    .api_keys
    .delete("b6d24b8e-af0b-4c3c-be0c-359bbd97381e")
    .await?;

  Ok(())
}
```

```java
import com.resend.*;

public class Main {
    public static void main(String[] args) {
        Resend resend = new Resend("re_xxxxxxxxx");

        resend.apiKeys().remove("b6d24b8e-af0b-4c3c-be0c-359bbd97381e");
    }
}
```

```csharp
using Resend;

IResend resend = ResendClient.Create( "re_xxxxxxxxx" ); // Or from DI

await resend.ApiKeyDeleteAsync( new Guid( "b6d24b8e-af0b-4c3c-be0c-359bbd97381e" ) );
```

```bash
curl -X DELETE 'https://api.resend.com/api-keys/b6d24b8e-af0b-4c3c-be0c-359bbd97381e' \
     -H 'Authorization: Bearer re_xxxxxxxxx'
```

</RequestExample>

<ResponseExample>
  ```text Response theme={"theme":{"light":"github-light","dark":"vesper"}}
  HTTP 200 OK
  ```
</ResponseExample>

