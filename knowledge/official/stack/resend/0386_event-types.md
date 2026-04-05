# Event Types

Source: https://resend.com/docs/webhooks/event-types

List of supported event types and their payload.

## Email Events

<div>
  <div>
    <div>
      <span />

  [`email.bounced`](/webhooks/emails/bounced)
</div>

<div>
  Occurs whenever the recipient's mail server **permanently rejected the
  email**.
</div>
</div>

<div>
    <div>
      <span />

  [`email.clicked`](/webhooks/emails/clicked)
</div>

<div>
  Occurs whenever the **recipient clicks on an email link**.
</div>
</div>

<div>
    <div>
      <span />

  [`email.complained`](/webhooks/emails/complained)
</div>

<div>
  Occurs whenever the email was successfully **delivered, but the recipient
  marked it as spam**.
</div>
</div>

<div>
    <div>
      <span />

  [`email.delivered`](/webhooks/emails/delivered)
</div>

<div>
  Occurs whenever Resend **successfully delivered the email** to the
  recipient's mail server.
</div>
</div>

<div>
    <div>
      <span />

  [`email.delivery_delayed`](/webhooks/emails/delivery-delayed)
</div>

<div>
  Occurs whenever the **email couldn't be delivered due to a temporary
  issue**. Delivery delays can occur, for example, when the recipient's
  inbox is full, or when the receiving email server experiences a transient
  issue.
</div>
</div>

<div>
    <div>
      <span />

  [`email.failed`](/webhooks/emails/failed)
</div>

<div>
  Occurs whenever the **email failed to send due to an error**. This event
  is triggered when there are issues such as invalid recipients, API key
  problems, domain verification issues, email quota limits, or other sending
  failures.
</div>
</div>

<div>
    <div>
      <span />

  [`email.opened`](/webhooks/emails/opened)
</div>

<div>
  Occurs whenever the **recipient opened the email**.
</div>
</div>

<div>
    <div>
      <span />

  [`email.received`](/webhooks/emails/received)
</div>

<div>
  Occurs whenever Resend **successfully receives an email**.
</div>
</div>

<div>
    <div>
      <span />

  [`email.scheduled`](/webhooks/emails/scheduled)
</div>

<div>
  Occurs whenever the **email is scheduled to be sent**.
</div>
</div>

<div>
    <div>
      <span />

  [`email.sent`](/webhooks/emails/sent)
</div>

<div>
  Occurs whenever the **API request was successful**. Resend will attempt to
  deliver the message to the recipient's mail server.
</div>
</div>

<div>
    <div>
      <span />

  [`email.suppressed`](/webhooks/emails/suppressed)
</div>

<div>
  Occurs whenever the **email is suppressed** by Resend.
</div>
</div>
</div>


## Domain Events

<div>
  <div>
    <div>
      <span />

  [`domain.created`](/webhooks/domains/created)
</div>

<div>
  Occurs when a **domain was successfully created**.
</div>
</div>

<div>
    <div>
      <span />

  [`domain.updated`](/webhooks/domains/updated)
</div>

<div>
  Occurs when a **domain was successfully updated**.
</div>
</div>

<div>
    <div>
      <span />

  [`domain.deleted`](/webhooks/domains/deleted)
</div>

<div>
  Occurs when a **domain was successfully deleted**.
</div>
</div>
</div>


## Contact Events

<div>
  <div>
    <div>
      <span />

  [`contact.created`](/webhooks/contacts/created)
</div>

<div>
  Occurs whenever a **contact was successfully created**.
</div>

<div>
  *Note: When importing multiple contacts using CSV, these events won't be
  triggered. [Contact support](https://resend.com/contact) if you have any
  questions.*
</div>
</div>

<div>
    <div>
      <span />

  [`contact.updated`](/webhooks/contacts/updated)
</div>

<div>
  Occurs whenever a **contact was successfully updated**.
</div>
</div>

<div>
    <div>
      <span />

  [`contact.deleted`](/webhooks/contacts/deleted)
</div>

<div>
  Occurs whenever a **contact was successfully deleted**.
</div>
</div>
</div>


