# Send emails using Supabase with SMTP

Source: https://resend.com/docs/send-with-supabase-smtp

Learn how to integrate Supabase Auth with Resend SMTP.

## Prerequisites

To get the most out of this guide, you'll need to:

* [Create an API key](https://resend.com/api-keys)
* [Verify your domain](https://resend.com/domains)

## 1. Get the Resend SMTP credentials

When configuring your SMTP integration, you'll need to use the following credentials:

* **Host**: `smtp.resend.com`
* **Port**: `465`
* **Username**: `resend`
* **Password**: `YOUR_API_KEY`

## 2. Integrate with Supabase SMTP

After logging into your Supabase account, you'll need to enable the SMTP integration.

1. Go to your Supabase project
2. Click on **Authentication** in the left sidebar
3. Click **Email** under the **Notifications** section
4. Click **SMTP Settings**
5. Add your Sender email and name (these are required fields). For example: `support@acme.com` and `ACME Support`.

<img alt="Supabase Auth - SMTP Sender email and name settings" />

6. You can copy-and-paste the [SMTP credentials](https://resend.com/settings/smtp) from Resend to Supabase.

<img alt="Supabase Auth - SMTP Settings" />

After that, you can click the **Save** button and all of your emails will be sent through Resend.

