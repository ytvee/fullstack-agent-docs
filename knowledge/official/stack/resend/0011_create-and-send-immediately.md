# Create and send immediately
curl -X POST 'https://api.resend.com/broadcasts' \
 -H 'Authorization: Bearer re_xxxxxxxxx' \
 -H 'Content-Type: application/json' \
 -d $'
{
  "segment_id": "78261eea-8f8b-4381-83c6-79fa7120f1cf",
  "from": "Acme <onboarding@resend.dev>",
  "subject": "hello world",
  "html": "Hi {{{FIRST_NAME|there}}}, you can unsubscribe here: {{{RESEND_UNSUBSCRIBE_URL}}}",
  "send": true
}'

