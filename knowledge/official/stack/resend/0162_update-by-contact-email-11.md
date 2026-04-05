# Update by contact email
curl -X PATCH 'https://api.resend.com/contacts/acme@example.com' \
     -H 'Authorization: Bearer re_xxxxxxxxx' \
     -H 'Content-Type: application/json' \
     -d $'{
  "properties": {
    "company_name": "Acme Corp",
  }
}'
```
</CodeGroup>

When you create or update a Contact with properties, the properties are added to the Contact, but only if the property key already exists and the value type is valid. You can [list all Contact Properties](/api-reference/contact-properties/list-contact-properties) to see all available properties.

<AccordionGroup>
  <Accordion title="What happens if the properties don't exist?">
    If the properties don't exist, they are not added to the Contact and the
    call fails. An error is returned.
  </Accordion>

<Accordion title="Property keys are case sensitive, right?">
Yes, property keys are case sensitive. If you create a property with a key
of "company\_name", you cannot use "CompanyName" or "company\_Name" in your
Contacts.
</Accordion>

<Accordion title="What happens if the value isn't the right type?">
If the value isn't the right type, the property value is not added to the
Contact and the call fails. An error is returned.
</Accordion>
</AccordionGroup>

## Use Contact Properties in Broadcasts

You can use Contact Properties in your Broadcasts to personalize your emails.

<video />

You can also use Contact Properties in your Broadcast HTML and Text content when you [create a Broadcast using the API or SDKs](/api-reference/broadcasts/create-broadcast).

