# Resend Chat SDK Adapter

**Purpose:** Instructions for building bidirectional email bots using the `@resend/chat-sdk-adapter` package with the Vercel Chat SDK.

---

## Setup

### Prerequisites

* Resend API key stored in `RESEND_API_KEY` env var
* Verified domain at [https://resend.com/domains](https://resend.com/domains)
* Webhook configured for `email.received` events (see [https://resend.com/docs/webhooks/introduction](https://resend.com/docs/webhooks/introduction))
* Inbound email receiving enabled (see [https://resend.com/docs/dashboard/receiving/introduction](https://resend.com/docs/dashboard/receiving/introduction))

### Install

```bash
npm install @resend/chat-sdk-adapter chat @chat-adapter/state-memory
