# Ruby SDK is not available yet
```

```go Go theme={"theme":{"light":"github-light","dark":"vesper"}}
// Go SDK is not available yet
```

```rust Rust theme={"theme":{"light":"github-light","dark":"vesper"}}
// Rust SDK is not available yet
```

```java Java theme={"theme":{"light":"github-light","dark":"vesper"}}
// Java SDK is not available yet
```

```csharp .NET theme={"theme":{"light":"github-light","dark":"vesper"}}
// C# SDK is not available yet
```
</CodeGroup>

<span />

[Contact us](https://resend.com/contact) if you're interested in testing
this feature.
</Warning>

Automations allow you to automate email sending based on custom events from your application.

You can use Automations for use cases like:

* Welcome emails (e.g. `user.created`)
* Feature adoption (e.g. `invite.sent`)
* Payment recovery (e.g. `payment.failed`)
* Abandoned cart (e.g. `cart.abandoned`)
* Trial expiration (e.g. `trial.ended`)
* And more

## Getting started

To start executing an Automation, you need to:

<Steps>
  <Step title="Create Automation">
    First, you need to build the sequence of steps that will be executed.
  </Step>

<Step title="Add Trigger">
Then, you need to define the event name that will trigger the Automation.
</Step>

<Step title="Define Actions">
Then, you need to define the actions that will be executed.
</Step>

<Step title="Send an Event">
Finally, you need to send the event to trigger the Automation.
</Step>
</Steps>

## 1. Create Automation

<Tabs>
  <Tab title="Using the dashboard">
    The [Automations page](https://resend.com/automations) shows all existing automations.

Click **Create automation** to start a new Automation.

<img alt="Create Automation" />
</Tab>

<Tab title="Using the API">
You can also programmatically create an Automation by using the API.

<CodeGroup>
  ```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { Resend } from 'resend';

  const resend = new Resend('re_xxxxxxxxx');

  const { data, error } = await resend.automations.create({
    name: 'Welcome series',
    steps: [
      {
        ref: 'trigger',
        type: 'trigger',
        config: { eventName: 'user.created' },
      },
    ],
    edges: [],
  });
  ```

  ```php PHP theme={"theme":{"light":"github-light","dark":"vesper"}}
  // PHP SDK is not available yet
  ```

  ```python Python theme={"theme":{"light":"github-light","dark":"vesper"}}
  # Python SDK is not available yet
  ```

  ```ruby Ruby theme={"theme":{"light":"github-light","dark":"vesper"}}
  # Ruby SDK is not available yet
  ```

  ```go Go theme={"theme":{"light":"github-light","dark":"vesper"}}
  // Go SDK is not available yet
  ```

  ```rust Rust theme={"theme":{"light":"github-light","dark":"vesper"}}
  // Rust SDK is not available yet
  ```

  ```java Java theme={"theme":{"light":"github-light","dark":"vesper"}}
  // Java SDK is not available yet
  ```

  ```csharp .NET theme={"theme":{"light":"github-light","dark":"vesper"}}
  // C# SDK is not available yet
  ```

  ```bash cURL theme={"theme":{"light":"github-light","dark":"vesper"}}
  curl -X POST 'https://api.resend.com/automations' \
       -H 'Authorization: Bearer re_xxxxxxxxx' \
       -H 'Content-Type: application/json' \
       -d '{
    "name": "Welcome series",
    "steps": [{
        "ref": "trigger",
        "type": "trigger",
        "config": { "event_name": "user.created" }
      }],
    "edges": []
  }'
  ```
</CodeGroup>

View the [API reference](/api-reference/automations/create-automation) for more details.
</Tab>
</Tabs>

## 2. Add Trigger

A trigger is the first step that will run when the Automation is executed.

<img alt="Add Trigger to Automation" />

On this example, we will receive an event called `user.created` as a trigger.

<img alt="Add Event Received Trigger" />

<Warning>
  Event names cannot start with the `resend:` prefix, which is reserved for
  system events.
</Warning>

## 3. Define Actions

Now, we need to define the actions that will be executed.

On this example, we will use the `Send email` action.

But you could also add a `Time delay` or `True/false branch` action.

<img alt="Define Actions" />

Once you select the `Send email` action, you will be able to select an existing template.

<Note>
  Note: Only `published` templates are available to be used in an Automation.
</Note>

<img alt="Add Send Email Action" />

With the template selected, you will be able to configure the email subject and sender address.

<img alt="Send Email Action Settings" />

Once you're done with the email, you can click on **Start automation** to enable the Automation.

<img alt="Automation Enabled" />

## 4. Send an Event

Now, we're ready to send an event to trigger the Automation.

On your application, you can send an event to trigger the Automation by using the API.

<CodeGroup>
  ```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { Resend } from 'resend';

const resend = new Resend('re_xxxxxxxxx');

// Trigger with a contact ID
const { data, error } = await resend.events.send({
event: 'user.created',
contactId: '7f2e4a3b-dfbc-4e9a-8b2c-5f3a1d6e7c8b',
payload: {
plan: 'pro',
},
});

// Trigger with an email address
const { data, error } = await resend.events.send({
event: 'user.created',
email: 'steve.wozniak@gmail.com',
payload: {
plan: 'pro',
},
});

```

```php PHP theme={"theme":{"light":"github-light","dark":"vesper"}}
// PHP SDK is not available yet
```
```python
