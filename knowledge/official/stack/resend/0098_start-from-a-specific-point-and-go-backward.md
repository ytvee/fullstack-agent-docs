# Start from a specific point and go backward
page = resend.Contacts.list(limit=50, before="some-contact-id")

if page["has_more"]:
    first_id = page["data"][0]["id"]
    previous_page = resend.Contacts.list(limit=50, before=first_id)
```
```ruby
Resend.api_key = "re_xxxxxxxxx"

