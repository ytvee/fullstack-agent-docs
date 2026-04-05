# Add Contact to Segment

Source: https://resend.com/docs/api-reference/contacts/add-contact-to-segment

POST /contacts/:contact_id/segments/:segment_id
Add an existing contact to a segment.

## Path Parameters

Either `id` or `email` must be provided.

<ParamField type="string">
  The Contact ID.
</ParamField>

<ParamField type="string">
  The Contact Email.
</ParamField>

<ResendParamField type="string">
  The Segment ID.
</ResendParamField>

<RequestExample>
  ```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { Resend } from 'resend';

const resend = new Resend('re_xxxxxxxxx');

// Add by contact id
const { data, error } = await resend.contacts.segments.add({
contactId: 'e169aa45-1ecf-4183-9955-b1499d5701d3',
segmentId: '78261eea-8f8b-4381-83c6-79fa7120f1cf',
});

// Add by contact email
const { data, error } = await resend.contacts.segments.add({
email: 'steve.wozniak@gmail.com',
segmentId: '78261eea-8f8b-4381-83c6-79fa7120f1cf',
});

```

```php PHP theme={"theme":{"light":"github-light","dark":"vesper"}}
$resend = Resend::client('re_xxxxxxxxx');

// Add by contact id
$resend->contacts->segments->add(
  contact: 'e169aa45-1ecf-4183-9955-b1499d5701d3',
  segmentId: '78261eea-8f8b-4381-83c6-79fa7120f1cf'
);

// Add by contact email
$resend->contacts->segments->add(
  contact: 'steve.wozniak@gmail.com',
  segmentId: '78261eea-8f8b-4381-83c6-79fa7120f1cf'
);
```

```python
import resend

resend.api_key = 're_xxxxxxxxx'

