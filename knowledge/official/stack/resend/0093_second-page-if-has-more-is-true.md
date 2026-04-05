# Second page (if has_more is true)
if first_page['has_more']:
    last_id = first_page['data'][-1]['id']
    second_page = resend.Contacts.list(limit=50, after=last_id)
```
```ruby
Resend.api_key = "re_xxxxxxxxx"

