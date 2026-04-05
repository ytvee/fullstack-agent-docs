# Update by contact email
curl -X PATCH 'https://api.resend.com/contacts/acme@example.com' \
     -H 'Authorization: Bearer re_xxxxxxxxx' \
     -H 'Content-Type: application/json' \
     -d $'{
  "unsubscribed": true
}'
```
</CodeGroup>

## Bulk Actions

You can perform actions on multiple Contacts at once by selecting them from the [Contacts](https://resend.com/audience) page.

1. Go to the [Contacts](https://resend.com/audience) page.
2. Select multiple Contacts by clicking the checkbox next to each Contact.
3. Click the **Edit** button in the bulk actions bar.
4. Choose an action:
   * **Add to segments**: Add the selected Contacts to one or more Segments.
   * **Subscribe to topics**: Subscribe the selected Contacts to one or more Topics.

You can also delete multiple Contacts at once by clicking the **Delete** button in the bulk actions bar.

## Delete Contacts

1. Go to the [Contacts](https://resend.com/audience) page.
2. Click on the **More options** <Icon icon="ellipsis" /> button and then **Delete Contact**.
3. Confirm the deletion.

You can also [delete a Contact](/api-reference/contacts/delete-contact) via the API or SDKs.

<CodeGroup>
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

