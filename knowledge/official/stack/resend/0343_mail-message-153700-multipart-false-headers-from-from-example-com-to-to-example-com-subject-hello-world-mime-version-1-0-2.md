# => #<Mail::Message:153700, Multipart: false, Headers: <From: from@example.com>, <To: to@example.com>, <Subject: hello world>, <Mime-Version: 1.0>...
```
Finally, you can now send emails using the `deliver_now!` method:

```rb
mailer.deliver_now!

