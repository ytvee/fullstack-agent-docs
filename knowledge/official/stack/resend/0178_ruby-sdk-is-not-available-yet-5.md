# Ruby SDK is not available yet
```

```go Go theme={"theme":{"light":"github-light","dark":"vesper"}}
// Go SDK is not available yet
```

```rust Rust theme={"theme":{"light":"github-light","dark":"vesper"}}
// Rust SDK is not available yet
```

```java Java theme={"theme":{"light":"github-light","dark":"vesper"}}
// Java SDK is not available yet
```

```csharp .NET theme={"theme":{"light":"github-light","dark":"vesper"}}
// C# SDK is not available yet
```
</CodeGroup>

<span />

[Contact us](https://resend.com/contact) if you're interested in testing
this feature.
</Warning>

A tracking domain will always share the same root domain as your sending domain. This improves deliverability and brand
consistency.

Similar to verifying your sending domain, you will need to add a CNAME record to your DNS settings to verify your
tracking domain.

Once verified, all tracked links in your emails will use your custom tracking domain (e.g., `links.emails.yourdomain.com`).

Here's how to configure a custom tracking domain.

<Tabs>
  <Tab title="Using the dashboard">
    Look for the **Custom Tracking Domain** section, and click on **Configure**.

<img alt="Configure Custom Tracking Domain" />

Then, you will need to add a CNAME record to verify your tracking domain.

<img alt="Verify Custom Tracking Domain" />

Once verified, all tracked links in your emails will use your custom tracking domain.

<img alt="Custom Tracking Domain Verified" />
</Tab>

<Tab title="Using the API">
You can also create a custom tracking domain by using the API.

<CodeGroup>
  ```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { Resend } from 'resend';

  const resend = new Resend('re_xxxxxxxxx');

  const { data, error } = await resend.domains.trackingDomains.create(
    'd91cd9bd-1176-453e-8fc1-35364d380206',
    {
      subdomain: 'links',
    },
  );
  ```

  ```php PHP theme={"theme":{"light":"github-light","dark":"vesper"}}
  // PHP SDK is not available yet
  ```

  ```python Python theme={"theme":{"light":"github-light","dark":"vesper"}}
  # Python SDK is not available yet
  ```

  ```ruby Ruby theme={"theme":{"light":"github-light","dark":"vesper"}}
  # Ruby SDK is not available yet
  ```

  ```go Go theme={"theme":{"light":"github-light","dark":"vesper"}}
  // Go SDK is not available yet
  ```

  ```rust Rust theme={"theme":{"light":"github-light","dark":"vesper"}}
  // Rust SDK is not available yet
  ```

  ```java Java theme={"theme":{"light":"github-light","dark":"vesper"}}
  // Java SDK is not available yet
  ```

  ```csharp .NET theme={"theme":{"light":"github-light","dark":"vesper"}}
  // C# SDK is not available yet
  ```

  ```bash cURL theme={"theme":{"light":"github-light","dark":"vesper"}}
  curl -X POST 'https://api.resend.com/domains/d91cd9bd-1176-453e-8fc1-35364d380206/tracking-domains' \
    -H 'Authorization: Bearer re_xxxxxxxxx' \
    -H 'Content-Type: application/json' \
    -d '{"subdomain": "links"}'
  ```
</CodeGroup>

Then, you will need to verify the tracking domain.

<CodeGroup>
  ```ts Node.js theme={"theme":{"light":"github-light","dark":"vesper"}}
  import { Resend } from 'resend';

  const resend = new Resend('re_xxxxxxxxx');

  const { data, error } = await resend.domains.trackingDomains.verify(
    'd91cd9bd-1176-453e-8fc1-35364d380206',
    'a1b2c3d4-e5f6-7890-abcd-ef1234567890',
  );
  ```

  ```php PHP theme={"theme":{"light":"github-light","dark":"vesper"}}
  // PHP SDK is not available yet
  ```

  ```python Python theme={"theme":{"light":"github-light","dark":"vesper"}}
  # Python SDK is not available yet
  ```

  ```ruby Ruby theme={"theme":{"light":"github-light","dark":"vesper"}}
  # Ruby SDK is not available yet
  ```

  ```go Go theme={"theme":{"light":"github-light","dark":"vesper"}}
  // Go SDK is not available yet
  ```

  ```rust Rust theme={"theme":{"light":"github-light","dark":"vesper"}}
  // Rust SDK is not available yet
  ```

  ```java Java theme={"theme":{"light":"github-light","dark":"vesper"}}
  // Java SDK is not available yet
  ```

  ```csharp .NET theme={"theme":{"light":"github-light","dark":"vesper"}}
  // C# SDK is not available yet
  ```

  ```bash cURL theme={"theme":{"light":"github-light","dark":"vesper"}}
  curl -X POST 'https://api.resend.com/domains/d91cd9bd-1176-453e-8fc1-35364d380206/tracking-domains/a1b2c3d4-e5f6-7890-abcd-ef1234567890/verify' \
    -H 'Authorization: Bearer re_xxxxxxxxx'
  ```
</CodeGroup>

Once verified, all tracked links in your emails will use your custom tracking domain.
</Tab>
</Tabs>

