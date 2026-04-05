# Update Contact Topics

Source: https://resend.com/docs/api-reference/contacts/update-contact-topics

PATCH /contacts/:contact_id/topics
Update topic subscriptions for a contact.

## Path Parameters

Either `id` or `email` must be provided.

<ParamField type="string">
  The Contact ID.
</ParamField>

<ParamField type="string">
  The Contact Email.
</ParamField>

## Body Parameters

<ParamField type="array">
  Array of topic subscription updates.

<Expandable title="properties">
    <ParamField type="string">
      The Topic ID.
    </ParamField>

<ParamField type="string">
  The subscription action. Must be either `opt_in` or `opt_out`.
</ParamField>
</Expandable>
</ParamField>

<RequestExample>
  ```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { Resend } from 'resend';

const resend = new Resend('re_xxxxxxxxx');

// Update by contact id
const { data, error } = await resend.contacts.topics.update({
id: 'e169aa45-1ecf-4183-9955-b1499d5701d3',
topics: [
{
id: 'b6d24b8e-af0b-4c3c-be0c-359bbd97381e',
subscription: 'opt_out',
},
{
id: '07d84122-7224-4881-9c31-1c048e204602',
subscription: 'opt_in',
},
],
});

// Update by contact email
const { data, error } = await resend.contacts.topics.update({
email: 'steve.wozniak@gmail.com',
topics: [
{
id: '07d84122-7224-4881-9c31-1c048e204602',
subscription: 'opt_out',
},
{
id: '07d84122-7224-4881-9c31-1c048e204602',
subscription: 'opt_in',
},
],
});

```

```php PHP theme={"theme":{"light":"github-light","dark":"vesper"}}
$resend = Resend::client('re_xxxxxxxxx');

// Update by contact id
$resend->contacts->topics->update('e169aa45-1ecf-4183-9955-b1499d5701d3', [
  [
    'id' => '07d84122-7224-4881-9c31-1c048e204602',
    'subscription' => 'opt_out',
  ],
  [
    'id' => '07d84122-7224-4881-9c31-1c048e204602',
    'subscription' => 'opt_in',
  ],
]);

// Update by contact email
$resend->contacts->topics->update('steve.wozniak@gmail.com', [
  [
    'id' => '07d84122-7224-4881-9c31-1c048e204602',
    'subscription' => 'opt_out',
  ],
  [
    'id' => '07d84122-7224-4881-9c31-1c048e204602',
    'subscription' => 'opt_in',
  ],
]);
```
```python
import resend

resend.api_key = 're_xxxxxxxxx'

