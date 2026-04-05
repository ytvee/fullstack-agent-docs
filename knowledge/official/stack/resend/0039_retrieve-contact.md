# Retrieve Contact

Source: https://resend.com/docs/api-reference/contacts/get-contact

GET /contacts/:contact_id
Retrieve a single contact.

## Path Parameters

Either `id` or `email` must be provided.

<ParamField type="string">
  The Contact ID.
</ParamField>

<ParamField type="string">
  The Contact Email.
</ParamField>

<RequestExample>
  ```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { Resend } from 'resend';

const resend = new Resend('re_xxxxxxxxx');

// Get by contact id
const { data, error } = await resend.contacts.get({
id: 'e169aa45-1ecf-4183-9955-b1499d5701d3',
});

// Get by contact email
const { data, error } = await resend.contacts.get({
email: 'steve.wozniak@gmail.com',
});

```

```php PHP theme={"theme":{"light":"github-light","dark":"vesper"}}
$resend = Resend::client('re_xxxxxxxxx');

// Get by contact id
$resend->contacts->get(
  id: 'e169aa45-1ecf-4183-9955-b1499d5701d3'
);

// Get by contact email
$resend->contacts->get(
  email: 'steve.wozniak@gmail.com'
);
```
```python
import resend

resend.api_key = "re_xxxxxxxxx"

