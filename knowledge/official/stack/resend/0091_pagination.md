# Pagination

Source: https://resend.com/docs/api-reference/pagination

Learn how pagination works in the Resend API.

## Overview

Several Resend API endpoints support **cursor-based pagination** to help you efficiently browse through large datasets. You can safely navigate lists with guaranteed stability, even if new objects are created or deleted while you're still requesting pages.

Paginated endpoints responses include:

* `object`: always set to `list`.
* `has_more`: indicates whether there are more elements available.
* `data`: the list of returned items.

You can navigate through the results using the following parameters:

* `limit`: the number of items to return per page.
* `after`: the cursor to use to get the next page of results.
* `before`: the cursor to use to get the previous page of results.

Use the `id` of objects as the cursor for pagination. The cursor itself is *excluded* from the results. For an example, see [pagination strategies below](#strategies).

## Currently-supported endpoints

Existing list endpoints can optionally return paginated results:

* [List Domains](/api-reference/domains/list-domains)
* [List API Keys](/api-reference/api-keys/list-api-keys)
* [List Broadcasts](/api-reference/broadcasts/list-broadcasts)
* [List Segments](/api-reference/segments/list-segments)
* [List Contacts](/api-reference/contacts/list-contacts)
* [List Receiving Emails](/api-reference/emails/list-received-emails)
* [List Receiving Email Attachments](/api-reference/emails/list-received-email-attachments)

<Info>
  Note that for these endpoints, the `limit` parameter is optional. If you do
  not provide a `limit`, all items will be returned in a single response.
</Info>

Newer list endpoints always return paginated results:

* [List Emails](/api-reference/emails/list-emails)
* [List Templates](/api-reference/templates/list-templates)
* [List Topics](/api-reference/topics/list-topics)

## Parameters

All paginated endpoints support the following query parameters:

<ParamField type="number">
  The number of items to return per page. Default is `20`, maximum is `100`, and
  minimum is `1`.
</ParamField>

<ParamField type="string">
  The cursor after which to start retrieving items. To get the next page, use
  the ID of the last item from the current page. This will return the page that
  **starts after** the object with this ID (excluding the passed ID itself).
</ParamField>

<ParamField type="string">
  The cursor before which to start retrieving items. To get the previous page,
  use the ID of the first item from the current page. This will return the page
  that **ends before** the object with this ID (excluding the passed ID itself).
</ParamField>

<Warning>
  You can only use either `after` or `before`, not both simultaneously.
</Warning>

## Response Format

Paginated endpoints return responses in the following format:

```json
{
  "object": "list",
  "has_more": true,
  "data": [
    /* Array of resources */
  ]
}
```
<ResponseField name="object" type="string">
  Always set to `list` for paginated responses.
</ResponseField>

<ResponseField name="has_more" type="boolean">
  Indicates whether there are more items available beyond the current page.
</ResponseField>

<ResponseField name="data" type="array">
  An array containing the actual resources for the current page.
</ResponseField>

## Strategies

### Forward Pagination

To paginate forward through results (newer to older items), use the `after` parameter with the ID of the **last item** from the current page:

<CodeGroup>
  ```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
  const resend = new Resend('re_xxxxxxxxx');

// First page
const { data: firstPage } = await resend.contacts.list({ limit: 50 });

// Second page (if has_more is true)
if (firstPage.has_more) {
const lastId = firstPage.data[firstPage.data.length - 1].id;
const { data: secondPage } = await resend.contacts.list({
limit: 50,
after: lastId,
});
}

```

```php PHP theme={"theme":{"light":"github-light","dark":"vesper"}}
$resend = Resend::client('re_xxxxxxxxx');

// First page
$firstPage = $resend->contacts->list(['limit' => 50]);

// Second page (if has_more is true)
if ($firstPage['has_more']) {
    $lastId = end($firstPage['data'])['id'];
    $secondPage = $resend->contacts->list([
        'limit' => 50,
        'after' => $lastId
    ]);
}
```
```python
import resend

resend.api_key = "re_xxxxxxxxx"

