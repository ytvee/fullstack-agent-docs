# Send emails using Metabase with SMTP

Source: https://resend.com/docs/send-with-metabase-smtp

Learn how to integrate Metabase with Resend SMTP.

### Prerequisites

To get the most out of this guide, you'll need to:

* [Create an API key](https://resend.com/api-keys)
* [Verify your domain](https://resend.com/domains)

## 1. Get the Resend SMTP credentials

When configuring your SMTP integration, you'll need to use the following credentials:

* **Host**: `smtp.resend.com`
* **Port**: `465`
* **Username**: `resend`
* **Password**: `YOUR_API_KEY`

## 2. Integrate with Metabase SMTP

After logging into your [Metabase Cloud](https://www.metabase.com/cloud/login) account, you’ll need to enable the SMTP integration.

1. From your Metabase Cloud Admin Panel, go to **Settings > Email** in the left menu. You should see the form below.

<img alt="Metabase Cloud SMTP" />

2. Copy-and-paste the SMTP credentials from Resend to Metabase Cloud. Finally, click the **Save** button and all of your emails will be sent through Resend.

<img alt="Metabase Cloud SMTP" />

