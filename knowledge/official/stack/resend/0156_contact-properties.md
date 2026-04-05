# Contact Properties

Source: https://resend.com/docs/dashboard/audiences/properties

Learn how to work with Contact Properties with Resend.

Contact Properties can be used to store additional information about your Contacts and then personalize your Broadcasts.

Resend includes a few default properties:

* `first_name`: The first name of the contact.
* `last_name`: The last name of the contact.
* `unsubscribed`: Whether the contact is unsubscribed from all Broadcasts.
* `email`: The email address of the contact.

## Add Custom Contact Properties

You can create additional custom Contact Properties for your Contacts to store additional information. These properties can be used to personalize your Broadcasts across all Segments.

Each Contact Property has a key, a value, and optional fallback value.

* `key`: The key of the property (must be alphanumeric and underscore only, max `50` characters).
* `value`: The value of the property (may be a `string` or `number`).
* `fallback_value`: The fallback value of the property (must match the type of the property).

<video />

You can also create Contact Properties [via the API or SDKs](/api-reference/contact-properties/create-contact-property).

<CodeGroup>
  ```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { Resend } from 'resend';

const resend = new Resend('re_xxxxxxxxx');

const { data, error } = await resend.contactProperties.create({
key: 'company_name',
type: 'string',
fallbackValue: 'Acme Corp',
});

```

```php PHP theme={"theme":{"light":"github-light","dark":"vesper"}}
$resend = Resend::client('re_xxxxxxxxx');

$resend->contactProperties->create([
  'key' => 'company_name',
  'type' => 'string',
  'fallback_value' => 'Acme Corp',
]);
```
```python
import resend

resend.api_key = 're_xxxxxxxxx'

params = {
    "key": "company_name",
    "type": "string",
    "fallback_value": "Acme Corp",
}

contact_property = resend.ContactProperties.create(params)
```
```ruby
require "resend"

Resend.api_key = "re_xxxxxxxxx"

property = Resend::ContactProperties.create({
  key: "company_name",
  type: "string",
  fallback_value: "Acme Corp"
})
```
```go
package main

import (
	"context"
	"fmt"

	"github.com/resend/resend-go/v3"
)

func main() {
	ctx := context.TODO()
	apiKey := "re_xxxxxxxxx"

	client := resend.NewClient(apiKey)

	params := &resend.CreateContactPropertyRequest{
		Key:           "company_name",
		Type:          "string",
		FallbackValue: "Acme Corp",
	}

	property, err := client.ContactProperties.CreateWithContext(ctx, params)
	if err != nil {
		panic(err)
	}
	fmt.Println(property)
}
```
```rust
use resend_rs::{
  types::{CreateContactPropertyOptions, PropertyType},
  Resend, Result,
};

#[tokio::main]
async fn main() -> Result<()> {
  let resend = Resend::new("re_xxxxxxxxx");

  let contact_property = CreateContactPropertyOptions::new("company_name", PropertyType::String)
    .with_fallback("Acme Corp");

  let _contact_property = resend.contacts.create_property(contact_property).await?;

  Ok(())
}
```
```java
import com.resend.*;

public class Main {
  public static void main(String[] args) {
    Resend resend = new Resend("re_xxxxxxxxx");

    CreateContactPropertyOptions options = CreateContactPropertyOptions.builder()
      .key("company_name")
      .type("string")
      .fallbackValue("Acme Corp")
      .build();

    resend.contactProperties().create(options);
  }
}
```
```csharp
using Resend;

IResend resend = ResendClient.Create( "re_xxxxxxxxx" ); // Or from DI

var resp = await resend.ContactPropCreateAsync( new ContactPropertyData() {
  Key = "company_name",
  PropertyType = ContactPropertyType.String,
  DefaultValue = "Acme Corp",
} );
Console.WriteLine( "Prop Id={0}", resp.Content );
```
```bash
curl -X POST 'https://api.resend.com/contact-properties' \
     -H 'Authorization: Bearer re_xxxxxxxxx' \
     -H 'Content-Type: application/json' \
     -d $'{
  "key": "company_name",
  "type": "string",
  "fallback_value": "Acme Corp"
}'
```
</CodeGroup>

## Add Properties to a Contact

When you create a Contact Property you can provide a fallback value. This value will be used whenever you don't provide a custom value for a Contact.

To provide a custom value for a Contact, you can use the dashboard:

1. Go to the [Contacts](https://resend.com/audience) page.
2. Click the **more options** <Icon icon="ellipsis" /> button and then **Edit Contact**.
3. Add the property key and value.
4. Click on the **Save** button.

<video />

You can also add properties to a Contact when you [create a Contact](/api-reference/contacts/create-contact).

<CodeGroup>
  ```ts Node.js {10-12} theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { Resend } from 'resend';

const resend = new Resend('re_xxxxxxxxx');

const { data, error } = await resend.contacts.create({
email: 'steve.wozniak@gmail.com',
firstName: 'Steve',
lastName: 'Wozniak',
unsubscribed: false,
properties: {
company_name: 'Acme Corp',
},
});

```

```php PHP {9-11} theme={"theme":{"light":"github-light","dark":"vesper"}}
$resend = Resend::client('re_xxxxxxxxx');

$resend->contacts->create(
  parameters: [
    'email' => 'steve.wozniak@gmail.com',
    'first_name' => 'Steve',
    'last_name' => 'Wozniak',
    'unsubscribed' => false,
    'properties' => [
      'company_name' => 'Acme Corp',
    ]
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
  "unsubscribed": False,
  "properties": {
    "company_name": "Acme Corp"
  }
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
  "unsubscribed": false,
  "properties": {
    "company_name": "Acme Corp",
  }
}

Resend::Contacts.create(params)
```
```go
import "github.com/resend/resend-go/v3"

client := resend.NewClient("re_xxxxxxxxx")

params := &resend.CreateContactRequest{
  Email:        "steve.wozniak@gmail.com",
  FirstName:    "Steve",
  LastName:     "Wozniak",
  Unsubscribed: false,
  Properties: map[string]interface{} {
    "company_name": "Acme Corp",
  }
}

contact, err := client.Contacts.Create(params)
```
```rust
use resend_rs::{types::CreateContactOptions, Resend, Result};

#[tokio::main]
async fn main() -> Result<()> {
  let resend = Resend::new("re_xxxxxxxxx");

  let contact = CreateContactOptions::new("steve.wozniak@gmail.com")
    .with_first_name("Steve")
    .with_last_name("Wozniak")
    .with_unsubscribed(false)
    .with_properties(vec![("company_name".to_string(), "Acme Corp".to_string())]);

  let _contact = resend.contacts.create(contact).await?;

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
                .unsubscribed(false)
                .properties(java.util.Map.of("company_name", "Acme Corp"))
                .build();

        CreateContactResponseSuccess data = resend.contacts().create(params);
    }
}
```
```csharp
using Resend;

IResend resend = ResendClient.Create( "re_xxxxxxxxx" ); // Or from DI

var resp = await resend.ContactAddAsync(
    new ContactData()
    {
        Email = "steve.wozniak@gmail.com",
        FirstName = "Steve",
        LastName = "Wozniak",
        IsUnsubscribed = false,
        Properties = new Dictionary<string, object> {
          { "company_name", "Acme Corp" }
        }
    }
);
Console.WriteLine( "Contact Id={0}", resp.Content );
```
```bash
curl -X POST 'https://api.resend.com/contacts' \
     -H 'Authorization: Bearer re_xxxxxxxxx' \
     -H 'Content-Type: application/json' \
     -d $'{
  "email": "steve.wozniak@gmail.com",
  "first_name": "Steve",
  "last_name": "Wozniak",
  "unsubscribed": false,
  "properties": {
    "company_name": "Acme Corp",
  }
}'
```
</CodeGroup>

Or you can update a Contact to add or change a property value [using the update contact endpoint](/api-reference/contacts/update-contact).

<CodeGroup>
  ```ts Node.js {8-10, 16-18} theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { Resend } from 'resend';

const resend = new Resend('re_xxxxxxxxx');

// Update by contact id
const { data, error } = await resend.contacts.update({
id: 'e169aa45-1ecf-4183-9955-b1499d5701d3',
properties: {
company_name: 'Acme Corp',
},
});

// Update by contact email
const { data, error } = await resend.contacts.update({
email: 'acme@example.com',
properties: {
company_name: 'Acme Corp',
},
});

```

```php PHP {7-9, 17-19} theme={"theme":{"light":"github-light","dark":"vesper"}}
$resend = Resend::client('re_xxxxxxxxx');

// Update by contact id
$resend->contacts->update(
  id: 'e169aa45-1ecf-4183-9955-b1499d5701d3',
  parameters: [
    'properties' => [
      'company_name' => 'Acme Corp',
    ]
  ]
);

// Update by contact email
$resend->contacts->update(
  email: 'acme@example.com',
  parameters: [
    'properties' => [
      'company_name' => 'Acme Corp',
    ]
  ]
);
```
```python
import resend

resend.api_key = "re_xxxxxxxxx"

