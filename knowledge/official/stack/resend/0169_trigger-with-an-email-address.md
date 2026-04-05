# Trigger with an email address
curl -X POST 'https://api.resend.com/events/send' \
     -H 'Authorization: Bearer re_xxxxxxxxx' \
     -H 'Content-Type: application/json' \
     -d '{
  "event": "user.created",
  "email": "steve.wozniak@gmail.com",
  "payload": {
    "plan": "pro"
  }
}'
```
</CodeGroup>

View the [API reference](/api-reference/events/send-event) for more details.

