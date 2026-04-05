# Deleted by contact email
curl -X DELETE 'https://api.resend.com/contacts/acme@example.com' \
     -H 'Authorization: Bearer re_xxxxxxxxx'
```
</RequestExample>

<ResponseExample>
  ```json Response theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "object": "contact",
    "contact": "520784e2-887d-4c25-b53c-4ad46ad38100",
    "deleted": true
  }
  ```
</ResponseExample>

