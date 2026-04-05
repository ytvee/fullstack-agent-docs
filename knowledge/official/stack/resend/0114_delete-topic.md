# Delete Topic

Source: https://resend.com/docs/api-reference/topics/delete-topic

DELETE /topics/:topic_id
Remove an existing topic.

## Path Parameters

<ResendParamField type="string">
  The topic ID.
</ResendParamField>

<RequestExample>
  ```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { Resend } from 'resend';

const resend = new Resend('re_xxxxxxxxx');

const { data, error } = await resend.topics.remove(
'b6d24b8e-af0b-4c3c-be0c-359bbd97381e',
);

```

```php PHP theme={"theme":{"light":"github-light","dark":"vesper"}}
$resend = Resend::client('re_xxxxxxxxx');

$resend->topics->remove('b6d24b8e-af0b-4c3c-be0c-359bbd97381e');
```
```python
import resend

resend.api_key = "re_xxxxxxxxx"

resend.Topics.remove(id="b6d24b8e-af0b-4c3c-be0c-359bbd97381e")
```
```ruby
require "resend"

Resend.api_key = "re_xxxxxxxxx"

Resend::Topics.remove("b6d24b8e-af0b-4c3c-be0c-359bbd97381e")
```
```go
import (
	"context"

	"github.com/resend/resend-go/v3"
)

func main() {
	client := resend.NewClient("re_xxxxxxxxx")

	client.Topics.RemoveWithContext(
		context.TODO(),
		"b6d24b8e-af0b-4c3c-be0c-359bbd97381e",
	)
}
```
```rust
use resend_rs::{Resend, Result};

#[tokio::main]
async fn main() -> Result<()> {
  let resend = Resend::new("re_xxxxxxxxx");

  let _deleted = resend.topics.delete("delete").await?;

  Ok(())
}
```
```java
import com.resend.*;

public class Main {
  public static void main(String[] args) {
    Resend resend = new Resend("re_xxxxxxxxx");

    RemoveTopicResponseSuccess response = resend.topics().remove("b6d24b8e-af0b-4c3c-be0c-359bbd97381e");
  }
}
```
```csharp
using Resend;

IResend resend = ResendClient.Create( "re_xxxxxxxxx" ); // Or from DI

var resp = await resend.TopicDeleteAsync( new Guid( "b6d24b8e-af0b-4c3c-be0c-359bbd97381e" ) );
```
```bash
curl -X DELETE 'https://api.resend.com/topics/b6d24b8e-af0b-4c3c-be0c-359bbd97381e' \
     -H 'Authorization: Bearer re_xxxxxxxxx'
```
</RequestExample>

<ResponseExample>
  ```json Response theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "object": "topic",
    "id": "b6d24b8e-af0b-4c3c-be0c-359bbd97381e",
    "deleted": true
  }
  ```
</ResponseExample>

