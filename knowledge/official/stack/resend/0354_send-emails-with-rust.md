# Send emails with Rust

Source: https://resend.com/docs/send-with-rust

Learn how to send your first email using the Resend Rust SDK.

## Prerequisites

To get the most out of this guide, you'll need to:

* [Create an API key](https://resend.com/api-keys)

## Install

First, create a rust project with cargo and `cd` into it.

```bash
cargo init resend-rust-example
cd resend-rust-example
```
Next, add add the Rust Resend SDK as well as [Tokio](https://tokio.rs):

```bash
cargo add resend-rs
cargo add tokio -F macros,rt-multi-thread
```
The Rust SDK is Async-first so Tokio is needed.

## Send email

```rust
use resend_rs::types::CreateEmailBaseOptions;
use resend_rs::{Resend, Result};

#[tokio::main]
async fn main() -> Result<()> {
  let resend = Resend::new("re_xxxxxxxxx");

  let from = "Acme <onboarding@resend.dev>";
  let to = ["delivered@resend.dev"];
  let subject = "Hello World";

  let email = CreateEmailBaseOptions::new(from, to, subject)
    .with_html("<strong>It works!</strong>");

  let _email = resend.emails.send(email).await?;

  Ok(())
}
```
## Reading the API key

Instead of using `Resend::new` and hardcoding the API key, the `RESEND_API_KEY` environment variable
can be used instead. The `Resend::default()` should be used in that scenario instead.

### Reading the API key from a `.env` file

Another popular option is to use a `.env` file for environment variables. You can use the
[`dotenvy`](https://crates.io/crates/dotenvy) crate for that:

```bash
cargo add dotenvy
```
```rust
// main.rs
use dotenvy::dotenv;
use resend_rs::types::CreateEmailBaseOptions;
use resend_rs::{Resend, Result};

#[tokio::main]
async fn main() -> Result<()> {
  let _env = dotenv().unwrap();

  let resend = Resend::default();

  let from = "Acme <onboarding@resend.dev>";
  let to = ["delivered@resend.dev"];
  let subject = "Hello World";

  let email = CreateEmailBaseOptions::new(from, to, subject)
    .with_html("<strong>It works!</strong>");

  let _email = resend.emails.send(email).await?;

  Ok(())
}
```
```toml
