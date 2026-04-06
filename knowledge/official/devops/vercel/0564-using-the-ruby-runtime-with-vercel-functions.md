---
id: "vercel-0564"
title: "Using the Ruby Runtime with Vercel Functions"
description: "Learn how to use the Ruby runtime to compile Ruby Vercel Functions on Vercel."
category: "vercel-functions"
subcategory: "functions"
type: "guide"
source: "https://vercel.com/docs/functions/runtimes/ruby"
tags: ["ruby", "runtime", "runtimes", "ruby-version", "ruby-dependencies", "setup"]
related: ["0558-using-the-go-runtime-with-vercel-functions.md", "0561-using-the-node-js-runtime-with-vercel-functions.md", "0563-using-the-python-runtime-with-vercel-functions.md"]
last_updated: "2026-04-03T23:47:22.169Z"
---

# Using the Ruby Runtime with Vercel Functions

> **🔒 Permissions Required**: The Ruby runtime

The Ruby runtime is used by Vercel to compile Ruby Vercel functions that define a singular HTTP handler from `.rb` files within an `/api` directory at your project's root.

Ruby files must have one of the following variables defined:

- `Handler` proc that matches the `do |request, response|` signature.
- `Handler` class that inherits from the `WEBrick::HTTPServlet::AbstractServlet` class.

For example, define a `index.rb` file inside a `/api` directory as follows:

```ruby filename="api/index.rb"
require 'cowsay'

Handler = Proc.new do |request, response|
  name = request.query['name'] || 'World'

  response.status = 200
  response['Content-Type'] = 'text/text; charset=utf-8'
  response.body = Cowsay.say("Hello #{name}", 'cow')
end
```

*An example \`index.rb\` file inside an
\`/api\` directory.*

Inside a `Gemfile` define:

```ruby filename="Gemfile"
source "https://rubygems.org"

gem "cowsay", "~> 0.3.0"
```

*An example \`Gemfile\` file that defines
\`cowsay\` as a dependency.*

## Ruby Version

New deployments use Ruby 3.3.x as the default version.

You can specify the version of Ruby by defining `ruby` in a `Gemfile`, like so:

```ruby filename="Gemfile"
source "https://rubygems.org"
ruby "~> 3.3.x"
```

> **💡 Note:** If the patch part of the version is defined, like
> `3.3.1` it will be ignored and assume the latest
> `3.3.x`.

## Ruby Dependencies

This runtime supports installing dependencies defined in the `Gemfile`. Alternatively, dependencies can be vendored with the `bundler install --deployment` command (useful for gems that require native extensions). In this case, dependencies are not built on deployment.


