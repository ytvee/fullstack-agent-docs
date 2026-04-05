# Update Domain

Source: https://resend.com/docs/api-reference/domains/update-domain

PATCH /domains/:domain_id
Update an existing domain.

## Path Parameters

<ResendParamField type="string">
  The Domain ID.
</ResendParamField>

## Body Parameters

<ResendParamField type="boolean">
  Track clicks within the body of each HTML email. Use [custom tracking
  domains](/api-reference/domains/create-tracking-domain) to serve click
  tracking from your own domain (e.g. `track.example.com`).
</ResendParamField>

<ResendParamField type="boolean">
  Track the open rate of each email. Use [custom tracking
  domains](/api-reference/domains/create-tracking-domain) to serve open tracking
  from your own domain (e.g. `track.example.com`).
</ResendParamField>

<ParamField type="string">
  <ul>
    <li>
      `opportunistic`: Opportunistic TLS means that it always attempts to make a
      secure connection to the receiving mail server. If it can't establish a
      secure connection, it sends the message unencrypted.
    </li>

<li>
  `enforced`: Enforced TLS on the other hand, requires that the email
  communication must use TLS no matter what. If the receiving server does
  not support TLS, the email will not be sent.
</li>
</ul>
</ParamField>

<ParamField type="object">
  Update the domain capabilities for sending and receiving emails. You can specify one or both fields. Omitted fields will keep their current value. At least one capability must remain enabled.

<Expandable title="properties">
    <ParamField type="string">
      Enable or disable sending emails from this domain. Possible values: `'enabled' | 'disabled'`
    </ParamField>

<ParamField type="string">
  Enable or disable receiving emails to this domain. Possible values: `'enabled' | 'disabled'`
</ParamField>
</Expandable>
</ParamField>

<RequestExample>
  ```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { Resend } from 'resend';

const resend = new Resend('re_xxxxxxxxx');

const { data, error } = await resend.domains.update({
id: 'b8617ad3-b712-41d9-81a0-f7c3d879314e',
openTracking: false,
clickTracking: true,
tls: 'enforced',
});

```

```php PHP theme={"theme":{"light":"github-light","dark":"vesper"}}
$resend = Resend::client('re_xxxxxxxxx');

$resend->domains->update(
  'b8617ad3-b712-41d9-81a0-f7c3d879314e',
  [
    'open_tracking' => false,
    'click_tracking' => true,
    'tls' => 'enforced',
  ]
);
```
```python
import resend

resend.api_key = "re_xxxxxxxxx"

params: resend.Domains.UpdateParams = {
  "id": "b8617ad3-b712-41d9-81a0-f7c3d879314e",
  "open_tracking": False,
  "click_tracking": True,
  "tls": "enforced",
}

resend.Domains.update(params)
```
```ruby
Resend.api_key = "re_xxxxxxxxx"

Resend::Domains.update({
  id: "b8617ad3-b712-41d9-81a0-f7c3d879314e",
  open_tracking: false,
  click_tracking: true,
  tls: "enforced",
})
```
```go
package main

import "github.com/resend/resend-go/v3"

func main() {
	client := resend.NewClient("re_xxxxxxxxx")

	updateDomainParams := &resend.UpdateDomainRequest{
		OpenTracking:  false,
		ClickTracking: true,
		Tls:           resend.Enforced,
	}

	client.Domains.Update("b8617ad3-b712-41d9-81a0-f7c3d879314e", updateDomainParams)
}
```
```rust
use resend_rs::{types::{DomainChanges, Tls}, Resend, Result};

#[tokio::main]
async fn main() -> Result<()> {
  let resend = Resend::new("re_xxxxxxxxx");

  let changes = DomainChanges::new()
    .with_open_tracking(false)
    .with_click_tracking(true)
    .with_tls(Tls::Enforced);

  let _domain = resend
    .domains
    .update("b8617ad3-b712-41d9-81a0-f7c3d879314e", changes)
    .await?;

  Ok(())
}
```
```java
Resend resend = new Resend("re_xxxxxxxxx");

UpdateDomainOptions params = UpdateDomainOptions.builder()
                .id("b8617ad3-b712-41d9-81a0-f7c3d879314e")
                .openTracking(false)
                .clickTracking(true)
                .tls(Tls.ENFORCED)
                .build();

resend.domains().update(params);
```
```csharp
using Resend;

IResend resend = ResendClient.Create( "re_xxxxxxxxx" ); // Or from DI

await resend.DomainUpdateAsync(
    new Guid( "b8617ad3-b712-41d9-81a0-f7c3d879314e" ),
    new DomainUpdateData()
    {
        TrackOpen = false,
        TrackClicks = true,
        TlsMode = TlsMode.Enforced,
    }
);
```
```bash
curl -X PATCH 'https://api.resend.com/domains/b8617ad3-b712-41d9-81a0-f7c3d879314e' \
     -H 'Authorization: Bearer re_xxxxxxxxx' \
     -H 'Content-Type: application/json' \
     -d $'{
  "open_tracking": false,
  "click_tracking": true,
  "tls": "enforced"
}'
```
</RequestExample>

<ResponseExample>
  ```json Response theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "object": "domain",
    "id": "b8617ad3-b712-41d9-81a0-f7c3d879314e"
  }
  ```
</ResponseExample>

