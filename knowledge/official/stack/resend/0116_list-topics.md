# List Topics

Source: https://resend.com/docs/api-reference/topics/list-topics

GET /topics
Retrieve a list of topics for the authenticated user.

<QueryParams type="topics" />

<RequestExample>
  ```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { Resend } from 'resend';

const resend = new Resend('re_xxxxxxxxx');

const { data, error } = await resend.topics.list();

```

```php PHP theme={"theme":{"light":"github-light","dark":"vesper"}}
$resend = Resend::client('re_xxxxxxxxx');

$resend->topics->list();
```
```python
import resend

resend.api_key = "re_xxxxxxxxx"

resend.Topics.list()
```
```ruby
require "resend"

Resend.api_key = "re_xxxxxxxxx"

Resend::Topics.list()
```
```go
import (
	"context"

	"github.com/resend/resend-go/v3"
)

func main() {
	client := resend.NewClient("re_xxxxxxxxx")

	client.Topics.ListWithContext(context.TODO(), nil)
}
```
```rust
use resend_rs::{list_opts::ListOptions, Resend, Result};

#[tokio::main]
async fn main() -> Result<()> {
  let resend = Resend::new("re_xxxxxxxxx");

  let _list = resend.topics.list(ListOptions::default()).await?;

  Ok(())
}
```
```java
import com.resend.*;

public class Main {
  public static void main(String[] args) {
    Resend resend = new Resend("re_xxxxxxxxx");

    ListTopicsResponseSuccess response = resend.topics().list();
  }
}
```
```csharp
using Resend;

IResend resend = ResendClient.Create( "re_xxxxxxxxx" ); // Or from DI

var resp = await resend.TopicListAsync();
Console.WriteLine( "Nr Topics={0}", resp.Content.Data.Count );
```
```bash
curl -X GET 'https://api.resend.com/topics' \
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
        "name": "Weekly Newsletter",
        "description": "Weekly newsletter for our subscribers",
        "default_subscription": "opt_in",
        "visibility": "public",
        "created_at": "2023-04-08T00:11:13.110779+00:00"
      }
    ]
  }
  ```
</ResponseExample>

