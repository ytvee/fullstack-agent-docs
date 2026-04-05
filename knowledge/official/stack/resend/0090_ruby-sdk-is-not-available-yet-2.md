# Ruby SDK is not available yet
```
```go
// Go SDK is not available yet
```
```rust
// Rust SDK is not available yet
```
```java
// Java SDK is not available yet
```
```csharp
// C# SDK is not available yet
```
```bash
curl -X GET 'https://api.resend.com/logs/37e4414c-5e25-4dbc-a071-43552a4bd53b' \
     -H 'Authorization: Bearer re_xxxxxxxxx'
```
</RequestExample>

<ResponseExample>
  ```json Response theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "object": "log",
    "id": "37e4414c-5e25-4dbc-a071-43552a4bd53b",
    "created_at": "2026-03-30 13:43:54.622865+00",
    "endpoint": "/emails",
    "method": "POST",
    "response_status": 200,
    "user_agent": "resend-node:6.0.3",
    "request_body": {
      "from": "Acme <onboarding@resend.dev>",
      "to": ["delivered@resend.dev"],
      "subject": "Hello World"
    },
    "response_body": {
      "id": "4ef9a417-02e9-4d39-ad75-9611e0fcc33c"
    }
  }
  ```
</ResponseExample>

