# Verify Domain

Source: https://resend.com/docs/api-reference/domains/verify-domain

POST /domains/:domain_id/verify
Verify an existing domain.

<Note>
  Calling this API endpoint triggers an **asynchronous domain verification
  process**. The domain will be temporarily marked as `pending` regardless of
  its current status while the verification is in progress. Since this request
  initiates the complete domain verification cycle, it will trigger
  `domain.updated` webhook events as the domain status changes during the
  verification process.
</Note>

## Path Parameters

<ResendParamField type="string">
  The Domain ID.
</ResendParamField>

<RequestExample>
  ```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { Resend } from 'resend';

const resend = new Resend('re_xxxxxxxxx');

const { data, error } = await resend.domains.verify(
'd91cd9bd-1176-453e-8fc1-35364d380206',
);

```

```php PHP theme={"theme":{"light":"github-light","dark":"vesper"}}
$resend = Resend::client('re_xxxxxxxxx');

$resend->domains->verify('d91cd9bd-1176-453e-8fc1-35364d380206');
```
```python
import resend

resend.api_key = "re_xxxxxxxxx"
resend.Domains.verify(domain_id="d91cd9bd-1176-453e-8fc1-35364d380206")
```
```ruby
Resend.api_key = ENV["RESEND_API_KEY"]
Resend::Domains.verify("d91cd9bd-1176-453e-8fc1-35364d380206")
```
```go
package main

import "github.com/resend/resend-go/v3"

func main() {
	client := resend.NewClient("re_xxxxxxxxx")

	client.Domains.Verify("d91cd9bd-1176-453e-8fc1-35364d380206")
}
```
```rust
use resend_rs::{Resend, Result};

#[tokio::main]
async fn main() -> Result<()> {
  let resend = Resend::new("re_xxxxxxxxx");

  resend
    .domains
    .verify("d91cd9bd-1176-453e-8fc1-35364d380206")
    .await?;

  Ok(())
}
```
```java
import com.resend.*;

public class Main {
    public static void main(String[] args) {
        Resend resend = new Resend("re_xxxxxxxxx");

        VerifyDomainResponse verified = resend.domains().verify("d91cd9bd-1176-453e-8fc1-35364d380206");
    }
}
```
```csharp
using Resend;

IResend resend = ResendClient.Create( "re_xxxxxxxxx" ); // Or from DI

var resp = await resend.DomainVerifyAsync( new Guid( "d91cd9bd-1176-453e-8fc1-35364d380206" ) );
```
```bash
curl -X POST 'https://api.resend.com/domains/d91cd9bd-1176-453e-8fc1-35364d380206/verify' \
     -H 'Authorization: Bearer re_xxxxxxxxx' \
     -H 'Content-Type: application/json'
```
</RequestExample>

<ResponseExample>
  ```json Response theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "object": "domain",
    "id": "d91cd9bd-1176-453e-8fc1-35364d380206"
  }
  ```
</ResponseExample>

