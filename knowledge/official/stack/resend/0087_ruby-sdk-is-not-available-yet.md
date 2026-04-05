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
curl -X GET 'https://api.resend.com/logs' \
     -H 'Authorization: Bearer re_xxxxxxxxx'
```
</RequestExample>

<ResponseExample>
  ```json Response theme={"theme":{"light":"github-light","dark":"vesper"}}
  {
    "object": "list",
    "has_more": false,
    "data": [
      {
        "id": "37e4414c-5e25-4dbc-a071-43552a4bd53b",
        "created_at": "2026-03-30 13:43:54.622865+00",
        "endpoint": "/emails",
        "method": "POST",
        "response_status": 200,
        "user_agent": "resend-node:6.0.3"
      },
      {
        "id": "a1b2c3d4-5e6f-7a8b-9c0d-1e2f3a4b5c6d",
        "created_at": "2026-03-30 12:15:00.123456+00",
        "endpoint": "/emails/4ef9a417-02e9-4d39-ad75-9611e0fcc33c",
        "method": "GET",
        "response_status": 200,
        "user_agent": "curl/8.7.1"
      }
    ]
  }
  ```
</ResponseExample>

