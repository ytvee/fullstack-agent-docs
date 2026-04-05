# Update by contact email
params: resend.Contacts.UpdateParams = {
  "email": "acme@example.com",
  "unsubscribed": True,
}

resend.Contacts.update(params)
```
```ruby
require "resend"

Resend.api_key = "re_xxxxxxxxx"

