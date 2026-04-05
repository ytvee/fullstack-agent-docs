# List Segments

Source: https://resend.com/docs/api-reference/segments/list-segments

GET /segments
Retrieve a list of segments.

<QueryParams type="segments" />

<RequestExample>
  ```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { Resend } from 'resend';

const resend = new Resend('re_xxxxxxxxx');

const { data, error } = await resend.segments.list();

```

```php PHP theme={"theme":{"light":"github-light","dark":"vesper"}}
$resend = Resend::client('re_xxxxxxxxx');

$resend->segments->list();
```
```python
import resend

resend.api_key = 're_xxxxxxxxx'

segments = resend.Segments.list()
```
```ruby
require "resend"

Resend.api_key = "re_xxxxxxxxx"

segments = Resend::Segments.list
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

	segments, err := client.Segments.ListWithContext(ctx)
	if err != nil {
		panic(err)
	}
	fmt.Println(segments)
}
```
```rust
use resend_rs::{list_opts::ListOptions, Resend, Result};

#[tokio::main]
async fn main() -> Result<()> {
  let resend = Resend::new("re_xxxxxxxxx");

  let _segments = resend.segments.list(ListOptions::default()).await?;

  Ok(())
}
```
```java
import com.resend.*;

public class Main {
    public static void main(String[] args) {
        Resend resend = new Resend("re_xxxxxxxxx");

        ListSegmentsResponseSuccess response = resend.segments().list();
    }
}
```
```csharp
using Resend;

IResend resend = ResendClient.Create( "re_xxxxxxxxx" ); // Or from DI

var resp = await resend.SegmentListAsync();
Console.WriteLine( "Nr Segments={0}", resp.Content.Data.Count );
```
```bash
curl -X GET 'https://api.resend.com/segments' \
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
        "id": "78261eea-8f8b-4381-83c6-79fa7120f1cf",
        "name": "Registered Users",
        "created_at": "2023-10-06T22:59:55.977Z"
      }
    ]
  }
  ```
</ResponseExample>

