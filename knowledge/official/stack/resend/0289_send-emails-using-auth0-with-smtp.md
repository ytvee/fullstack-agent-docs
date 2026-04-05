# Send emails using Auth0 with SMTP
Source: https://resend.com/docs/send-with-auth0-smtp

Learn how to integrate Auth0 with Resend SMTP.

## Prerequisites

To get the most out of this guide, you'll need to:

* [Create an API key](https://resend.com/api-keys)
* [Verify your domain](https://resend.com/domains)

## 1. Get the Resend SMTP credentials

When configuring your SMTP integration, you'll need to use the following credentials:

* **Host**: `smtp.resend.com`
* **Port**: `465` or `587` (see [port options](#port-options) below)
* **Username**: `resend`
* **Password**: `YOUR_API_KEY`

### Port options

Resend supports multiple ports for different security configurations:

| Type     | Port                | Security                                                                  |
| -------- | ------------------- | ------------------------------------------------------------------------- |
| SMTPS    | `465`, `2465`       | Implicit SSL/TLS (Immediately connects via SSL/TLS)                       |
| STARTTLS | `25`, `587`, `2587` | Explicit SSL/TLS (First connects via plaintext, then upgrades to SSL/TLS) |

For Auth0, we recommend using port `465` (SMTPS) or `587` (STARTTLS).

## 2. Integrate with Auth0 SMTP

After logging into your [Auth0](https://auth0.com/) dashboard, you'll need to enable the SMTP integration.

1. From your Auth0 dashboard, go to [Branding > Email Provider](https://manage.auth0.com/#/templates/provider).
2. Enable the **Use my own email provider** toggle.
3. Select **SMTP Provider**.
4. Enter a **From** email address, and then enter the Resend SMTP server's **Host**, **Port**, **Username**, and your API key as the **Password**.

<img alt="Auth0 SMTP - Email Provider Settings" />

## 3. Send a test email

Once you have configured the SMTP settings, click **Save**. Next send a test email using the **Send Test Email** button. If everything is configured correctly, you will receive a confirmation email. If you did not receive an email, check your [Auth0 Logs](https://manage.auth0.com/#/logs).


