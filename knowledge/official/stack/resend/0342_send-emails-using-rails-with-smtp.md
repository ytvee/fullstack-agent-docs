# Send emails using Rails with SMTP

Source: https://resend.com/docs/send-with-rails-smtp

Learn how to integrate Rails with Resend SMTP.

## Prerequisites

To get the most out of this guide, you'll need to:

* [Create an API key](https://resend.com/api-keys)
* [Verify your domain](https://resend.com/domains)

## 1. Setup your environment

Add these lines of code into your environment config file.

```rb
config.action_mailer.delivery_method = :smtp
config.action_mailer.smtp_settings = {
  :address   => 'smtp.resend.com',
  :port      => 465,
  :user_name => 'resend',
  :password  => ENV['RESEND_API_KEY'],
  :tls => true
}
```
## 2. Send email using Rails Action Mailer

Then create a `UserMailer` class definition.

```rb
class UserMailer < ApplicationMailer
  default from: 'Acme <onboarding@resend.dev>' # this domain must be verified with Resend
  def welcome_email
    @user = params[:user]
    @url = 'http://example.com/login'
    mail(to: ["delivered@resend.dev"], subject: 'hello world')
  end
end
```
And create your ERB email template.

```html
<!doctype html>
<html>
  <head>
    <meta content="text/html; charset=UTF-8" http-equiv="Content-Type" />
  </head>
  <body>
    <h1>Welcome to example.com, <%= @user.name %></h1>
    <p>You have successfully signed up to example.com,</p>
    <p>To log in to the site, just follow this link: <%= @url %>.</p>
    <p>Thanks for joining and have a great day!</p>
  </body>
</html>
```
Initialize your `UserMailer` class. This should return a `UserMailer` instance.

```rb
u = User.new name: "derich"
mailer = UserMailer.with(user: u).welcome_email

