# Send emails using Nodemailer with SMTP

Source: https://resend.com/docs/send-with-nodemailer-smtp

Learn how to send your first email using Nodemailer with SMTP.

## Prerequisites

To get the most out of this guide, you'll need to:

* [Create an API key](https://resend.com/api-keys)
* [Verify your domain](https://resend.com/domains)

## 1. Install

Get the [Nodemailer](https://www.npmjs.com/package/nodemailer) package.

<CodeGroup>
  ```bash npm theme={"theme":{"light":"github-light","dark":"vesper"}}
  npm install nodemailer
  ```

```bash
yarn add nodemailer
```
```bash
pnpm add nodemailer
```
```bash
bun add nodemailer
```
</CodeGroup>

## 2. Send email using SMTP

When configuring your SMTP integration, you'll need to use the following credentials:

* **Host**: `smtp.resend.com`
* **Port**: `465`
* **Username**: `resend`
* **Password**: `YOUR_API_KEY`

Then use these credentials to create a transport:

```js
import nodemailer from 'nodemailer';

async function main() {
  const transporter = nodemailer.createTransport({
    host: 'smtp.resend.com',
    secure: true,
    port: 465,
    auth: {
      user: 'resend',
      pass: 're_xxxxxxxxx',
    },
  });

  const info = await transporter.sendMail({
    from: 'onboarding@resend.dev',
    to: 'delivered@resend.dev',
    subject: 'Hello World',
    html: '<strong>It works!</strong>',
  });

  console.log('Message sent: %s', info.messageId);
}

main().catch(console.error);
```
## 3. Try it yourself

<Card title="Nodemailer SMTP Example" icon="arrow-up-right-from-square" href="https://github.com/resend/resend-nodemailer-smtp-example">
See the full source code.
</Card>

