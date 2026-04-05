# Retrieve Contact Topics

Source: https://resend.com/docs/api-reference/contacts/get-contact-topics

GET /contacts/:contact_id/topics
Retrieve a list of topics subscriptions for a contact.

## Path Parameters

Either `id` or `email` must be provided.

<ParamField type="string">
  The Contact ID.
</ParamField>

<ParamField type="string">
  The Contact Email.
</ParamField>

<QueryParams type="topics" />

<RequestExample>
  ```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { Resend } from 'resend';

const resend = new Resend('re_xxxxxxxxx');

// Get by contact id
const { data, error } = await resend.contacts.topics.list({
id: 'e169aa45-1ecf-4183-9955-b1499d5701d3',
});

// Get by contact email
const { data, error } = await resend.contacts.topics.list({
email: 'steve.wozniak@gmail.com',
});

```

```php PHP theme={"theme":{"light":"github-light","dark":"vesper"}}
$resend = Resend::client('re_xxxxxxxxx');

// Get by contact id
$resend->contacts->topics->get('e169aa45-1ecf-4183-9955-b1499d5701d3');

// Get by contact email
$resend->contacts->topics->get('steve.wozniak@gmail.com');
```
```python
import resend

resend.api_key = 're_xxxxxxxxx'

