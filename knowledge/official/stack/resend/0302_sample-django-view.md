# Sample Django view
def index(request):

    subject = "Hello from Django SMTP"
    recipient_list = ["delivered@resend.dev"]
    from_email = "onboarding@resend.dev"
    message = "<strong>it works!</strong>"

    with get_connection(
        host=settings.RESEND_SMTP_HOST,
        port=settings.RESEND_SMTP_PORT,
        username=settings.RESEND_SMTP_USERNAME,
        password=os.environ["RESEND_API_KEY"],
        use_tls=True,
        ) as connection:
            r = EmailMessage(
                  subject=subject,
                  body=message,
                  to=recipient_list,
                  from_email=from_email,
                  connection=connection).send()
    return JsonResponse({"status": "ok"})
```
## 3. Try it yourself

<Card title="Django SMTP Example" icon="arrow-up-right-from-square" href="https://github.com/resend/resend-django-smtp-example">
See the full source code.
</Card>

