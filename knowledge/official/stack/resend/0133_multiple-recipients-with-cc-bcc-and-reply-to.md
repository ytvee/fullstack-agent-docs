# Multiple recipients with CC, BCC, and reply-to
resend emails send \
  --from "Acme <onboarding@resend.dev>" \
  --to delivered@resend.dev \
  --subject "Hello World" \
  --text "It works!" \
  --cc manager@example.com \
  --bcc archive@example.com \
  --reply-to noreply@example.com

