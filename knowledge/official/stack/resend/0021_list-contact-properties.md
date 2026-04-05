# List Contact Properties

Source: https://resend.com/docs/api-reference/contact-properties/list-contact-properties

GET /contact-properties
Retrieve a list of contact properties.

<QueryParams type="contact-properties" />

<RequestExample>
  ```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { Resend } from 'resend';

const resend = new Resend('re_xxxxxxxxx');

const { data, error } = await resend.contactProperties.list();

```

```php PHP theme={"theme":{"light":"github-light","dark":"vesper"}}
$resend = Resend::client('re_xxxxxxxxx');

$resend->contactProperties->list();
```

```python
import resend

resend.api_key = 're_xxxxxxxxx'

contact_properties = resend.ContactProperties.list()
```

```ruby
require "resend"

Resend.api_key = "re_xxxxxxxxx"

properties = Resend::ContactProperties.list
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

	properties, err := client.ContactProperties.ListWithContext(ctx)
	if err != nil {
		panic(err)
	}
	fmt.Println(properties)
}
```

```rust
use resend_rs::{list_opts::ListOptions, Resend, Result};

#[tokio::main]
async fn main() -> Result<()> {
  let resend = Resend::new("re_xxxxxxxxx");

  let _contact_properties = resend
    .contacts
    .list_properties(ListOptions::default())
    .await?;

  Ok(())
}
```

```java
import com.resend.*;

public class Main {
  public static void main(String[] args) {
    Resend resend = new Resend("re_xxxxxxxxx");

    resend.contactProperties().list();
  }
}
```

```csharp
using Resend;

IResend resend = ResendClient.Create( "re_xxxxxxxxx" ); // Or from DI

var resp = await resend.ContactPropListAsync();
Console.WriteLine( "Nr Props={0}", resp.Content.Data.Count );
```

```bash
curl -X GET 'https://api.resend.com/contact-properties' \
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
        "id": "b6d24b8e-af0b-4c3c-be0c-359bbd97381e",
        "key": "company_name",
        "type": "string",
        "fallback_value": "Acme Corp",
        "created_at": "2023-04-08T00:11:13.110779+00:00"
      }
    ]
  }
  ```
</ResponseExample>

