# Remove by contact id
params = {
    "segment_id": '78261eea-8f8b-4381-83c6-79fa7120f1cf',
    "contact_id": 'e169aa45-1ecf-4183-9955-b1499d5701d3',
}

response = resend.Contacts.Segments.remove(params)
```
```ruby
require 'resend'

Resend.api_key = 're_xxxxxxxxx'

