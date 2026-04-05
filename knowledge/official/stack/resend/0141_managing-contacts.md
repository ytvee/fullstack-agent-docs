# Managing Contacts

Source: https://resend.com/docs/dashboard/audiences/contacts

Learn how to work with Contacts with Resend.

Contacts in Resend are global entities linked to a specific email address. After adding Contacts, send [Broadcasts](/dashboard/broadcasts/introduction) to groups of Contacts.

<Tip>
  If you previously used our Audience model, learn how to [migrate to the new
  Contacts model](/dashboard/segments/migrating-from-audiences-to-segments).
</Tip>

## Add Contacts

You can add a Contact in three different ways: via API, CSV upload, or manually.

### 1. Add Contacts programmatically via API

You can add contacts programmatically using the [contacts](/api-reference/contacts/create-contact) endpoint.

<CodeGroup>
  ```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { Resend } from 'resend';

const resend = new Resend('re_xxxxxxxxx');

resend.contacts.create({
email: 'steve.wozniak@gmail.com',
firstName: 'Steve',
lastName: 'Wozniak',
});

```

```php PHP theme={"theme":{"light":"github-light","dark":"vesper"}}
$resend = Resend::client('re_xxxxxxxxx');

$resend->contacts->create(
  parameters: [
    'email' => 'steve.wozniak@gmail.com',
    'first_name' => 'Steve',
    'last_name' => 'Wozniak',
  ]
);
```
```python
import resend

resend.api_key = "re_xxxxxxxxx"

params: resend.Contacts.CreateParams = {
  "email": "steve.wozniak@gmail.com",
  "first_name": "Steve",
  "last_name": "Wozniak",
}

resend.Contacts.create(params)
```
```ruby
require "resend"

Resend.api_key = "re_xxxxxxxxx"

params = {
  "email": "steve.wozniak@gmail.com",
  "first_name": "Steve",
  "last_name": "Wozniak",
}

Resend::Contacts.create(params)
```
```go
package main

import "github.com/resend/resend-go/v3"

func main() {
	client := resend.NewClient("re_xxxxxxxxx")

	params := &resend.CreateContactRequest{
		Email:        "steve.wozniak@gmail.com",
		FirstName:    "Steve",
		LastName:     "Wozniak",
		Unsubscribed: false,
	}

	client.Contacts.Create(params)
}
```
```rust
use resend_rs::{types::ContactData, Resend, Result};

#[tokio::main]
async fn main() -> Result<()> {
  let resend = Resend::new("re_xxxxxxxxx");

  let contact = ContactData::new("steve.wozniak@gmail.com")
    .with_first_name("Steve")
    .with_last_name("Wozniak");

  let _contact = resend
    .contacts
    .create(contact)
    .await?;

  Ok(())
}
```
```java
import com.resend.*;

public class Main {
    public static void main(String[] args) {
        Resend resend = new Resend("re_xxxxxxxxx");

        CreateContactOptions params = CreateContactOptions.builder()
                .email("steve.wozniak@gmail.com")
                .firstName("Steve")
                .lastName("Wozniak")
                .build();

        CreateContactResponseSuccess data = resend.contacts().create(params);
    }
}
```
```bash
curl -X POST 'https://api.resend.com/contacts' \
     -H 'Authorization: Bearer re_xxxxxxxxx' \
     -H 'Content-Type: application/json' \
     -d $'{
  "email": "steve.wozniak@gmail.com",
  "first_name": "Steve",
  "last_name": "Wozniak"
}'
```
</CodeGroup>

When creating a Contact, you can optionally set the following properties:

* `first_name`: The first name of the contact.
* `last_name`: The last name of the contact.
* `unsubscribed`: Whether the contact is unsubscribed from all Broadcasts.
* `properties`: A map of custom property keys and values to create (learn more about [custom properties](/dashboard/audiences/properties)).

Once a Contact is created, you can update it using the [update contact](/api-reference/contacts/update-contact) endpoint or [add the contact to a Segment](/api-reference/contacts/add-contact-to-segment).

### 2. Add Contacts by uploading a .csv

You can also add Contacts by uploading a .csv file. This is a convenient way to add multiple Contacts at once.

1. Go to the [Contacts](https://resend.com/audience) page, and select **Add Contacts**.
2. Select **Import CSV**.
3. Upload your CSV file from your computer.
4. Map the fields you want to use. You can map the fields to: `email`, `first_name`, `last_name`, and `unsubscribed`, or any Contact properties you've already created.
5. Optionally add the contacts to an existing Segment.
6. Select **Continue**, review the contacts, and finish the upload.

### 3. Add Contacts manually

1. Go to the [Contacts](https://resend.com/audience) page, and select **Add Contacts**.
2. Select **Add Manually**.
3. Add the email address of the contact in the text field (separated by commas or new lines for multiple contacts).
4. Optionally add the contact to an existing Segment.
5. Confirm and click **Add**.

## Contact Properties

Contact Properties can be used to store additional information about your Contacts and then personalize your Broadcasts.

<img alt="Properties" />

Resend includes a few default properties:

* `first_name`: The first name of the contact.
* `last_name`: The last name of the contact.
* `unsubscribed`: Whether the contact is unsubscribed from all Broadcasts.
* `email`: The email address of the contact.

You can create additional custom Contact Properties for your Contacts to store additional information. These properties can be used to personalize your Broadcasts across all Segments.

Learn more about [Contact Properties](/dashboard/audiences/properties).

## View Contacts

You can view your Contacts in the [Contacts](https://resend.com/audience) page.

1. Go to the [Contacts](https://resend.com/audience) page.
2. Click on the Contact you want to view.
3. View the Contact details.

Each Contact includes the metadata associated with the contact, as well as a full history of all marketing interactions with the Contact.

<img alt="View Contact" />

You can also retrieve a [single Contact](/api-reference/contacts/get-contact) or [list all Contacts](/api-reference/contacts/list-contacts) via the API or SDKs.

## Edit Contacts

1. Go to the [Contacts](https://resend.com/audience) page.
2. Click on the **More options** <Icon icon="ellipsis" /> button and then **Edit Contact**.
3. Edit the Contact details and choose **Save**.

You can edit any Contact property (excluding the email address), assign
the Contact to a [Segment](/dashboard/segments/introduction) or [Topic](/dashboard/topics/introduction), or unsubscribe the Contact from all Broadcasts.

You can also [update a Contact](/api-reference/contacts/update-contact) via the API or SDKs using the `id` or `email` of the Contact.

<CodeGroup>
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

