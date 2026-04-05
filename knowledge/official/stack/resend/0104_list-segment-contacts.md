# List Segment Contacts

Source: https://resend.com/docs/api-reference/segments/list-segment-contacts

GET /segments/:segment_id/contacts
Retrieve a list of contacts in a segment.

## Path Parameters

<ResendParamField type="string">
  The Segment ID.
</ResendParamField>

<QueryParams type="contacts" />

<RequestExample>
  ```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { Resend } from 'resend';

const resend = new Resend('re_xxxxxxxxx');

const { data, error } = await resend.contacts.list({
segmentId: '78261eea-8f8b-4381-83c6-79fa7120f1cf',
});

```

```php PHP theme={"theme":{"light":"github-light","dark":"vesper"}}
$resend = Resend::client('re_xxxxxxxxx');

$resend->contacts->list([
  'segment_id' => '78261eea-8f8b-4381-83c6-79fa7120f1cf',
]);
```
```python
import resend

resend.api_key = 're_xxxxxxxxx'

contacts = resend.Contacts.list('78261eea-8f8b-4381-83c6-79fa7120f1cf')
```
```rust
use resend_rs::{Resend, Result};

#[tokio::main]
async fn main() -> Result<()> {
  let resend = Resend::new("re_xxxxxxxxx");

  let _contacts = resend
    .contacts
    .list("78261eea-8f8b-4381-83c6-79fa7120f1cf", ListOptions::default())
    .await?;

  Ok(())
}
```
```java
import com.resend.*;

public class Main {
    public static void main(String[] args) {
        Resend resend = new Resend("re_xxxxxxxxx");

        ListContactsResponseSuccess response = resend.contacts().list("78261eea-8f8b-4381-83c6-79fa7120f1cf");
    }
}
```
</RequestExample>

