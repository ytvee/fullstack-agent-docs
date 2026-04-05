# Resend CLI

Source: https://resend.com/docs/cli

The official command-line tool for Resend. Send emails, manage your account, and develop locally from the terminal.

The [Resend CLI](https://github.com/resend/resend-cli) is the official command-line interface for Resend. It covers the full API surface and is built for humans, AI agents, and CI/CD pipelines.

## Installation

<Tabs>
  <Tab title="cURL">
    ```bash theme={"theme":{"light":"github-light","dark":"vesper"}}
    curl -fsSL https://resend.com/install.sh | bash
    ```
  </Tab>

<Tab title="npm">
    ```bash theme={"theme":{"light":"github-light","dark":"vesper"}}
    npm install -g resend-cli
    ```
  </Tab>

<Tab title="Homebrew">
    ```bash theme={"theme":{"light":"github-light","dark":"vesper"}}
    brew install resend/cli/resend
    ```
  </Tab>

<Tab title="PowerShell (Windows)">
```powershell theme={"theme":{"light":"github-light","dark":"vesper"}} irm https://resend.com/install.ps1 | iex ```
</Tab>
</Tabs>

## Authentication

The CLI resolves your API key using the following priority chain:


| Priority    | Source                   | How to set                                |
| ----------- | ------------------------ | ----------------------------------------- |
| 1 (highest) | `--api-key` flag         | `resend --api-key re_xxx emails send ...` |
| 2           | `RESEND_API_KEY` env var | `export RESEND_API_KEY=re_xxx`            |
| 3 (lowest)  | Saved credentials        | `resend login`                            |

If no key is found from any source, the CLI errors with code `auth_error`.

### `resend login`

Authenticate by storing your API key locally. The key is validated against the Resend API before being saved.

```bash
resend login
```
In a terminal, the command prompts for your key via masked input. In non-interactive environments (CI, pipes), use the `--key` flag:

```bash
resend login --key re_xxxxxxxxxxxxx
```
Credentials are saved to your system's secure credential storage (macOS Keychain, Windows Credential Manager, or Linux secret service).


| Flag          | Description                                         |
| ------------- | --------------------------------------------------- |
| `--key <key>` | API key to store (required in non-interactive mode) |

### `resend logout`

Remove your saved API key.

```bash
resend logout
```
### Switch between profiles

If you work across multiple Resend teams or accounts, switch between profiles without logging in and out:

```bash
resend auth switch
```
Use the global `--profile` flag on any command to run it with a specific profile:

```bash
resend domains list --profile production
```
Other profile management commands:


| Command                          | Description                        |
| -------------------------------- | ---------------------------------- |
| `resend auth list`               | List all profiles                  |
| `resend auth switch [name]`      | Switch the active profile          |
| `resend auth rename [old] [new]` | Rename a profile                   |
| `resend auth remove [name]`      | Remove a profile                   |
| `resend whoami`                  | Show current authentication status |

## Emails

### `resend emails send`

Send an email. Provide all options via flags for scripting, or let the CLI prompt interactively for missing fields.

```bash
resend emails send \
  --from "Acme <onboarding@resend.dev>" \
  --to delivered@resend.dev \
  --subject "Hello World" \
  --text "It works!"
```

| Flag                        | Required         | Description                                                |
| --------------------------- | ---------------- | ---------------------------------------------------------- |
| `--from <address>`          | Yes\*            | Sender email address (must be from a verified domain)      |
| `--to <addresses...>`       | Yes              | One or more recipient email addresses (space-separated)    |
| `--subject <subject>`       | Yes\*            | Email subject line                                         |
| `--text <text>`             | One of text/html | Plain text body                                            |
| `--text-file <path>`        | One of text/html | Path to a plain text file (use`-` for stdin)               |
| `--html <html>`             | One of text/html | HTML body as a string                                      |
| `--html-file <path>`        | One of text/html | Path to an HTML file (use`-` for stdin)                    |
| `--react-email <path>`      | One of text/html | Path to a React Email template (`.tsx`) to render and send |
| `--cc <addresses...>`       | No               | CC recipients                                              |
| `--bcc <addresses...>`      | No               | BCC recipients                                             |
| `--reply-to <address>`      | No               | Reply-to email address                                     |
| `--scheduled-at <datetime>` | No               | Schedule for later — ISO 8601 or natural language         |
| `--attachment <paths...>`   | No               | File path(s) to attach                                     |
| `--headers <key=value...>`  | No               | Custom headers as key=value pairs                          |
| `--tags <name=value...>`    | No               | Email tags as name=value pairs                             |
| `--idempotency-key <key>`   | No               | Deduplicate this send request                              |
| `--template <id>`           | No               | Template ID to use                                         |
| `--var <key=value...>`      | No               | Template variables as key=value pairs                      |

\* Not required when using `--template` — the template provides them.

**Examples:**

```bash
