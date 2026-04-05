# Update by contact email
params_by_email = {
    "email": "steve.wozniak@gmail.com",
    "topics": [
        {"id": "07d84122-7224-4881-9c31-1c048e204602", "subscription": "opt_out"},
        {"id": "07d84122-7224-4881-9c31-1c048e204602", "subscription": "opt_in"},
    ],
}

response = resend.Contacts.Topics.update(params_by_email)
```
```ruby
require "resend"

Resend.api_key = "re_xxxxxxxxx"

