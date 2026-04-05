# Delete Contact

Source: https://resend.com/docs/api-reference/contacts/delete-contact

DELETE /contacts/:contact_id
Remove an existing contact.

## Path Parameters

Either `id` or `email` must be provided.

<ParamField type="string">
  The Contact ID.
</ParamField>

<ParamField type="string">
  The Contact email.
</ParamField>

<RequestExample>
  ```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { Resend } from 'resend';

const resend = new Resend('re_xxxxxxxxx');

// Delete by contact id
const { data, error } = await resend.contacts.remove({
id: '520784e2-887d-4c25-b53c-4ad46ad38100',
});

// Delete by contact email
const { data, error } = await resend.contacts.remove({
email: 'acme@example.com',
});

```

```php PHP theme={"theme":{"light":"github-light","dark":"vesper"}}
$resend = Resend::client('re_xxxxxxxxx');

// Delete by contact id
$resend->contacts->remove(
  id: '520784e2-887d-4c25-b53c-4ad46ad38100'
);

// Delete by contact email
$resend->contacts->remove(
  email: 'acme@example.com'
);
```
```python
import resend

resend.api_key = "re_xxxxxxxxx"

