# email.bounced

Source: https://resend.com/docs/webhooks/emails/bounced

Received when an email bounces.

Event triggered whenever the recipient's mail server **permanently rejected the email**.

<ResponseBodyParameters type="email.bounced">
  <ParamField type="string">
    Unique identifier for the broadcast campaign (if applicable)
  </ParamField>

<ParamField type="string">
    ISO 8601 timestamp when the email was created
  </ParamField>

<ParamField type="string">
    Unique identifier for the specific email
  </ParamField>

<ParamField type="string">
    Sender email address and name in the format "Name
    \<[email@domain.com](mailto:email@domain.com)>"
  </ParamField>

<ParamField type="array">
    Array of impacted recipient email addresses
  </ParamField>

<ParamField type="string">
    Email subject line
  </ParamField>

<ParamField type="string">
    Unique identifier for the template used (if applicable)
  </ParamField>

<ParamField type="Record<string, string>">
Object of tag key-value pairs associated with the email.

Example:

```json theme={"theme":{"light":"github-light","dark":"vesper"}}
{
  "category": "welcome",
  "user_id": "1234567890"
}
```
</ParamField>

<ParamField type="object">
    Bounce details from the receiving server

<Expandable title="bounce object">
  <ParamField type="array">
    Array of SMTP diagnostic responses from the receiving server, including the status code and reason for the bounce (e.g., `smtp; 550 5.5.0 Requested action not taken: mailbox unavailable`)
  </ParamField>

  <ParamField type="string">
    Detailed bounce message from the receiving server
  </ParamField>

  <ParamField type="string">
    Bounce sub-type (e.g., `Suppressed`, `MessageRejected`)
  </ParamField>

  <ParamField type="string">
    Bounce type (e.g., `Permanent`, `Temporary`)
  </ParamField>

  <Info>
    Learn more about [bounce types and subtypes](/dashboard/emails/email-bounces).
  </Info>
</Expandable>
</ParamField>
</ResponseBodyParameters>

<ResponseExample>
  ```json theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "type": "email.bounced",
    "created_at": "2024-11-22T23:41:12.126Z",
    "data": {
      "broadcast_id": "8b146471-e88e-4322-86af-016cd36fd216",
      "created_at": "2024-11-22T23:41:11.894719+00:00",
      "email_id": "56761188-7520-42d8-8898-ff6fc54ce618",
      "from": "Acme <onboarding@resend.dev>",
      "to": ["delivered@resend.dev"],
      "subject": "Sending this example",
      "template_id": "43f68331-0622-4e15-8202-246a0388854b",
      "bounce": {
        "message": "The recipient's email address is on the suppression list because it has a recent history of producing hard bounces.",
        "subType": "Suppressed",
        "type": "Permanent"
      },
      "tags": {
        "category": "confirm_email"
      }
    }
  }
  ```
</ResponseExample>

