# Update Contact

Source: https://resend.com/docs/api-reference/contacts/update-contact

PATCH /contacts/:contact_id
Update an existing contact.

## Path Parameters

Either `id` or `email` must be provided.

<ParamField type="string">
  The Contact ID.
</ParamField>

<ParamField type="string">
  The Contact Email.
</ParamField>

## Body Parameters

<ResendParamField type="string">
  The first name of the contact.
</ResendParamField>

<ResendParamField type="string">
  The last name of the contact.
</ResendParamField>

<ParamField type="boolean">
  The Contact's global subscription status. If set to `true`, the contact will
  be unsubscribed from all Broadcasts.
</ParamField>

<ParamField type="object">
  A map of custom property keys and values to update.

<Expandable title="custom properties">
<ParamField type="string">
The property key.
</ParamField>

<ParamField type="string">
  The property value.
</ParamField>
</Expandable>
</ParamField>

<RequestExample>
  ```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { Resend } from 'resend';

const resend = new Resend('re_xxxxxxxxx');

// Update by contact id
const { data, error } = await resend.contacts.update({
id: 'e169aa45-1ecf-4183-9955-b1499d5701d3',
unsubscribed: true,
});

// Update by contact email
const { data, error } = await resend.contacts.update({
email: 'acme@example.com',
unsubscribed: true,
});

```

```php PHP theme={"theme":{"light":"github-light","dark":"vesper"}}
$resend = Resend::client('re_xxxxxxxxx');

// Update by contact id
$resend->contacts->update(
  id: 'e169aa45-1ecf-4183-9955-b1499d5701d3',
  parameters: [
    'unsubscribed' => true
  ]
);

// Update by contact email
$resend->contacts->update(
  email: 'acme@example.com',
  parameters: [
    'unsubscribed' => true
  ]
);
```
```python
import resend

resend.api_key = "re_xxxxxxxxx"

