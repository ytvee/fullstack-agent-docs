# Version History

Source: https://resend.com/docs/dashboard/templates/version-history

Best practices for using templates in production environments.

Templates in production require a workflow that lets you make changes safely without disrupting active emails. As you build your Template, your entire team can collaborate on the content and design in real-time with full version history.

## Draft vs Published

Templates start in a **draft** state and must be published before they can be used to send emails.

This separation allows you to:

* Test templates thoroughly before going live
* Make changes without affecting active emails
* Maintain version control over your email content

Once you **publish** a template, this published version will be used to send emails until you publish again. You can continue to work on a template in draft state without affecting the published version and the editor will automaticalyl save your progress.

<CodeGroup>
  ```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
  // Create template
  import { Resend } from 'resend';

const resend = new Resend('re_xxxxxxxxx');

await resend.templates.create({
name: 'order-confirmation',
from: 'Resend Store <store@resend.com>',
subject: 'Thanks for your order!',
html: "<p>Name: {{{PRODUCT}}}</p><p>Total: {{{PRICE}}}</p>",
variables: [
{
key: 'PRODUCT',
type: 'string',
fallbackValue: 'item'
},
{
key: 'PRICE',
type: 'number',
fallbackValue: 20
}
]
});

// Publish template
await resend.templates.publish('template_id');

// Or create and publish a template in one step
await resend.templates.create({ ... }).publish();

```

```php PHP theme={"theme":{"light":"github-light","dark":"vesper"}}
$resend = Resend::client('re_xxxxxxxxx');

// Create template
$resend->templates->create([
  'name' => 'order-confirmation',
  'from' => 'Resend Store <store@resend.com>',
  'subject' => 'Thanks for your order!',
    'html' => "<p>Name: {{{PRODUCT}}}</p><p>Total: {{{PRICE}}}</p>",
  'variables' => [
    [
      'key' => 'PRODUCT',
      'type' => 'string',
      'fallbackValue' => 'item'
    ],
    [
      'key' => 'PRICE',
      'type' => 'number',
      'fallbackValue' => 49.99
    ]
  ]
]);

// Publish template
$resend->templates->publish('template_id');
```
```py
import resend

resend.api_key = "re_xxxxxxxxx"

// Create template
params: resend.Templates.CreateParams = {
  "name": "order-confirmation",
  "from": "Resend Store <store@resend.com>",
  "subject": "Thanks for your order!",
  "html": "<p>Name: {{{PRODUCT}}}</p><p>Total: {{{PRICE}}}</p>",
  "variables": [
    {
      "key": "PRODUCT",
      "type": "string",
      "fallbackValue": "item"
    },
    {
      "key": "PRICE",
      "type": "number",
      "fallbackValue": 20
    },
  ]
}

resend.Templates.create(params)

// Publish template
resend.Templates.publish('template_id');
```
```ruby
require "resend"

Resend.api_key = "re_xxxxxxxxx"

// Create template
params = {
  "name": 'order-confirmation',
  "from": 'Resend Store <store@resend.com>',
  "subject": 'Thanks for your order!',
  "html": "<p>Name: #{{{PRODUCT}}}</p><p>Total: #{{{PRICE}}}</p>",
  "variables": [{
      "key": 'PRODUCT',
      "type": 'string',
      "fallbackValue": 'item'
    },
    {
      "key": 'PRICE',
      "type": 'number',
      "fallbackValue": 20
    }
  ]
}

Resend::Templates.create(params)

// Publish template
Resend::Templates.publish('template_id');
```
```go
import "github.com/resend/resend-go/v2"

client := resend.NewClient("re_xxxxxxxxx")

// Create template
params := &resend.CreateTemplateRequest{
  Name: "order-confirmation",
  From: "Resend Store <store@resend.com>",
  Subject: "Thanks for your order!",
  Html: "<p>Name: {{{PRODUCT}}}</p><p>Total: {{{PRICE}}}</p>",
  Variables: []resend.TemplateVariable{
    {
      Key: "PRODUCT",
      Type: "string",
      FallbackValue: "item",
    },
    {
      Key: "PRICE",
      Type: "number",
      FallbackValue: 20,
    },
  },
}

template, _ := client.Templates.Create(params)

// Publish template
client.Templates.Publish(template.Id)
```
```rust
use resend_rs::{types::CreateTemplateOptions, Resend, Result};

#[tokio::main]
async fn main() -> Result<()> {
  let resend = Resend::new("re_xxxxxxxxx");

  // Create template
  let name = "order-confirmation";
  let from = "Resend Store <store@resend.com>";
  let subject = "Thanks for your order!";
  let html = "<p>Name: {{{PRODUCT}}}</p><p>Total: {{{PRICE}}}</p>";

  let variables = vec![
    TemplateVariable {
      key: "PRODUCT",
      type_: "string",
      fallback_value: Some("item"),
    },
    TemplateVariable {
      key: "PRICE",
      type_: "number",
      fallback_value: Some(20),
    },
  ];

  let opts = CreateTemplateOptions::new(name, from, subject)
    .with_html(html)
    .with_variables(variables);

  let _template = resend.templates.create(opts).await?;

  // Publish template
  resend.templates.publish(&template.id).await?;

  Ok(())
}
```
```java
Resend resend = new Resend("re_xxxxxxxxx");

// Create template
List<TemplateVariable> variables = Arrays.asList(
  new TemplateVariable("PRODUCT", "string", "item"),
  new TemplateVariable("PRICE", "number", 20),
);

CreateTemplateOptions params = CreateTemplateOptions.builder()
  .name("order-confirmation")
  .from("Resend Store <store@resend.com>")
  .subject("Thanks for your order!")
    .html("<p>Name: {{{PRODUCT}}}</p><p>Total: {{{PRICE}}}</p>")
  .variables(variables)
  .build();

CreateTemplateResponseSuccess data = resend.templates().create(params);

// Publish template
resend.templates().publish(data.content);
```
```csharp
using Resend;

IResend resend = ResendClient.Create("re_xxxxxxxxx");

// Create template
var variables = new List<TemplateVariable>
{
  new TemplateVariable() {
    Key = "PRODUCT",
    Type = TemplateVariableType.String,
    Default = "item",
  },
  new TemplateVariable() {
    Key = "PRICE",
    Type = TemplateVariableType.Number,
    Default = 20,
  },
};

var resp = await resend.TemplateCreateAsync(
  new TemplateData()
  {
    Name = "order-confirmation",
    From = "Resend Store <store@resend.com>",
    Subject = "Thanks for your order!",
    HtmlBody = @"
      <p>Name: {{{PRODUCT}}}</p>
      <p>Total: {{{PRICE}}}</p>
    ",
    Variables = variables,
  }
);

// Publish template
await resend.TemplatePublishAsync(resp.Content);

Console.WriteLine($"Template Id={resp.Content}");
```
```bash
