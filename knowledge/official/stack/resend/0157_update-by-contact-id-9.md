# Update by contact id
params: resend.Contacts.UpdateParams = {
  "id": "e169aa45-1ecf-4183-9955-b1499d5701d3",
  "properties": {
    "company_name": "Acme Corp",
  }
}

resend.Contacts.update(params)

