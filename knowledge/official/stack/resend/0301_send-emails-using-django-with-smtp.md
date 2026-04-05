# Send emails using Django with SMTP

Source: https://resend.com/docs/send-with-django-smtp

Learn how to integrate Django with Resend SMTP.

## Prerequisites

To get the most out of this guide, you'll need to:

* [Create an API key](https://resend.com/api-keys)
* [Verify your domain](https://resend.com/domains)
* Install `virtualenv` by running `pip install virtualenv`

## 1. Setup your environment

Create and activate your new virtualenv.

```bash
virtualenv venv
source venv/bin/activate
```
Install dependencies.

```sh
pip install -r requirements.txt
```
Set your `RESEND_API_KEY` environment variable by running.

```sh
export RESEND_API_KEY="re_xxxxxxxxx"
```
## 2. Send email using Django's SMTP EmailMessage

Set the necessary attributes in your `settings.py` file.

```py
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
RESEND_SMTP_PORT = 587
RESEND_SMTP_USERNAME = 'resend'
RESEND_SMTP_HOST = 'smtp.resend.com'
```
Use Django's `get_connection` and `EmailMessage`

```py
import os
from django.conf import settings
from django.http import JsonResponse
from django.core.mail import EmailMessage, get_connection

