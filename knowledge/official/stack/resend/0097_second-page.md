# Second page
curl -X GET 'https://api.resend.com/contacts?limit=50&after=LAST_ID_FROM_PREVIOUS_PAGE' \
     -H 'Authorization: Bearer re_xxxxxxxxx'
```
</CodeGroup>

### Backward Pagination

To paginate backward through results (older to newer items), use the `before` parameter with the ID of the **first item** from the current page (or the most recent ID you have in your system):

<CodeGroup>
  ```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
  const resend = new Resend('re_xxxxxxxxx');

// Start from a specific point and go backward
const page = await resend.contacts.list({
limit: 50,
before: 'some-contact-id',
});

if (page.data.has_more) {
const firstId = page.data.data[0].id;
const previousPage = await resend.contacts.list({
limit: 50,
before: firstId,
});
}

```

```php PHP theme={"theme":{"light":"github-light","dark":"vesper"}}
$resend = Resend::client('re_xxxxxxxxx');

// Start from a specific point and go backward
$page = $resend->contacts->list([
    'limit' => 50,
    'before' => 'some-contact-id'
]);

if ($page['has_more']) {
    $firstId = $page['data'][0]['id'];
    $previousPage = $resend->contacts->list([
        'limit' => 50,
        'before' => $firstId
    ]);
}
```
```python
import resend

resend.api_key = "re_xxxxxxxxx"

