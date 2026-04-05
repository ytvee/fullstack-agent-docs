# Get by contact email
curl -X GET 'https://api.resend.com/contacts/steve.wozniak@gmail.com' \
     -H 'Authorization: Bearer re_xxxxxxxxx'
```
</RequestExample>

<ResponseExample>
  ```json Response theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "object": "contact",
    "id": "e169aa45-1ecf-4183-9955-b1499d5701d3",
    "email": "steve.wozniak@gmail.com",
    "first_name": "Steve",
    "last_name": "Wozniak",
    "created_at": "2023-10-06T23:47:56.678Z",
    "unsubscribed": false,
    "properties": {
      "company_name": "Acme Corp",
      "department": "Engineering"
    }
  }
  ```
</ResponseExample>

