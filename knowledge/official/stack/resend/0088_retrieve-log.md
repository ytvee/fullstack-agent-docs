# Retrieve Log

Source: https://resend.com/docs/api-reference/logs/retrieve-log

GET /logs/:log_id
Retrieve a single API request log.

## Path Parameters

<ParamField type="string">
  The Log ID.
</ParamField>

<Info>
  The `request_body` and `response_body` fields vary depending on the original
  API request that was logged.
</Info>

<RequestExample>
  ```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { Resend } from 'resend';

const resend = new Resend('re_xxxxxxxxx');

const { data, error } = await resend.logs.get(
'37e4414c-5e25-4dbc-a071-43552a4bd53b',
);

```

```php PHP theme={"theme":{"light":"github-light","dark":"vesper"}}
$resend = Resend::client('re_xxxxxxxxx');

$resend->logs->get('37e4414c-5e25-4dbc-a071-43552a4bd53b');
```
```python
