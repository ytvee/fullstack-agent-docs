# Create template
curl -X POST 'https://api.resend.com/templates' \
 -H 'Authorization: Bearer re_xxxxxxxxx' \
 -H 'Content-Type: application/json' \
 -d $'{
  "name": "order-confirmation",
  "from": "Resend Store <store@resend.com>",
  "subject": "Thanks for your order!",
  "html": "<p>Name: {{{PRODUCT}}}</p><p>Total: {{{PRICE}}}</p>",
  "variables": [
    {
      "key": "PRODUCT",
      "type": "string",
      "fallbackValue": "item"
    },
    {
      "key": "PRICE",
      "type": "number",
      "fallbackValue": 20
    }
  ]
}'

