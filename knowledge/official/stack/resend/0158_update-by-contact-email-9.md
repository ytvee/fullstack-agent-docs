# Update by contact email
params: resend.Contacts.UpdateParams = {
  "email": "acme@example.com",
  "properties": {
    "company_name": "Acme Corp",
  }
}

resend.Contacts.update(params)
```
```ruby
require "resend"

Resend.api_key = "re_xxxxxxxxx"

