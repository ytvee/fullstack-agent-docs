# List Logs

Source: https://resend.com/docs/api-reference/logs/list-logs

GET /logs
Retrieve a list of API request logs.

<QueryParams type="logs" />

<RequestExample>
  ```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { Resend } from 'resend';

const resend = new Resend('re_xxxxxxxxx');

const { data, error } = await resend.logs.list();

```

```php PHP theme={"theme":{"light":"github-light","dark":"vesper"}}
$resend = Resend::client('re_xxxxxxxxx');

$resend->logs->list();
```
```python
