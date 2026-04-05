# Update by contact id
params = {
    "id": "e169aa45-1ecf-4183-9955-b1499d5701d3",
    "topics": [
        {"id": "b6d24b8e-af0b-4c3c-be0c-359bbd97381e", "subscription": "opt_out"},
        {"id": "07d84122-7224-4881-9c31-1c048e204602", "subscription": "opt_in"},
    ],
}

response = resend.Contacts.Topics.update(params)

