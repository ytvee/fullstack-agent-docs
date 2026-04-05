# Trigger with a contact ID
curl -X POST 'https://api.resend.com/events/send' \
     -H 'Authorization: Bearer re_xxxxxxxxx' \
     -H 'Content-Type: application/json' \
     -d '{
  "event": "user.created",
  "contact_id": "7f2e4a3b-dfbc-4e9a-8b2c-5f3a1d6e7c8b",
  "payload": {
    "plan": "pro"
  }
}'

