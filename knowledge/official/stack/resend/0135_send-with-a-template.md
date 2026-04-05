# Send with a template
resend emails send \
  --from "Acme <onboarding@resend.dev>" \
  --to delivered@resend.dev \
  --template tmpl_xxxxx \
  --var "name=Alice" --var "company=Acme"
```
### `resend emails batch`

Send up to 100 emails in a single API request from a JSON file.

```bash
resend emails batch --file ./emails.json
```

| Flag                        | Required | Description                                                                                  |
| --------------------------- | -------- | -------------------------------------------------------------------------------------------- |
| `--file <path>`             | Yes      | Path to JSON file containing array of email objects (use`-` for stdin)                       |
| `--react-email <path>`      | No       | Path to a React Email template (`.tsx`) — rendered HTML applies to every email in the batch |
| `--idempotency-key <key>`   | No       | Deduplicate this batch request                                                               |
| `--batch-validation <mode>` | No       | `strict` (default, entire batch fails on any error) or `permissive`                          |

### Other email commands

```bash
resend emails list                # List sent emails
resend emails get <id>            # Retrieve a sent email by ID
resend emails cancel <id>         # Cancel a scheduled email
resend emails update <id>         # Update a scheduled email's send time
```
## Receiving

```bash
resend emails receiving list              # List received (inbound) emails
resend emails receiving get <id>          # Retrieve a received email with full details
resend emails receiving listen            # Poll for new inbound emails as they arrive
resend emails receiving forward <id>      # Forward a received email
resend emails receiving attachments <id>  # List attachments for a received email
resend emails receiving attachment <id> <attachment-id>  # Download a specific attachment
```
## Domains

Manage your sending and receiving domains.

```bash
resend domains create --name example.com --region us-east-1
resend domains list               # List all domains
resend domains get <id>           # Retrieve domain with DNS records
resend domains verify <id>        # Trigger DNS verification
resend domains update <id>        # Update TLS, tracking, or receiving settings
resend domains delete <id>        # Delete a domain
```
## API Keys

```bash
resend api-keys create --name "Production" --permission full_access
resend api-keys list              # List all API keys
resend api-keys delete <id>       # Delete an API key
```
## Broadcasts

Create and send broadcast emails to segments. Supports `--html-file` and `--react-email` for content.

```bash
resend broadcasts create \
  --from "Acme <onboarding@resend.dev>" \
  --subject "Product update" \
  --segment-id seg_xxxxx \
  --html-file ./broadcast.html \
  --send
resend broadcasts list            # List all broadcasts
resend broadcasts get <id>        # Retrieve broadcast details
resend broadcasts send <id>       # Send a draft broadcast
resend broadcasts update <id>     # Update a draft broadcast
resend broadcasts delete <id>     # Delete a broadcast
resend broadcasts open [id]      # Open a broadcast in the dashboard
```
## Contacts

Manage contacts, segment membership, and topic subscriptions.

```bash
resend contacts create --email steve.wozniak@gmail.com --first-name Steve
resend contacts list              # List all contacts
resend contacts get <id>          # Retrieve a contact by ID or email
resend contacts update <id>       # Update contact properties
resend contacts delete <id>       # Delete a contact
resend contacts segments <id>    # List segments a contact belongs to
resend contacts add-segment <id> # Add a contact to a segment
resend contacts remove-segment <id> <segment-id>  # Remove from a segment
resend contacts topics <id>      # List topic subscriptions
resend contacts update-topics <id>  # Update topic subscriptions
```
## Contact Properties

```bash
resend contact-properties create --key "company" --type string
resend contact-properties list | get | update | delete
```
## Segments

```bash
resend segments create --name "VIPs"
resend segments list | get | delete
```
## Topics

```bash
resend topics create --name "Product updates"
resend topics list | get | update | delete
```
## Templates

Create and manage email templates. Supports `--html-file` and `--react-email` for content.

```bash
resend templates create --name "Welcome" --subject "Welcome to Acme" --react-email ./emails/welcome.tsx
resend templates list             # List all templates
resend templates get <id>         # Retrieve a template by ID or alias
resend templates update <id>      # Update a template
resend templates publish <id>     # Publish a draft template
resend templates duplicate <id>   # Duplicate a template
resend templates delete <id>      # Delete a template
resend templates open [id]       # Open a template in the dashboard
```
## Logs

View API request logs.

```bash
resend logs list              # List API request logs
resend logs get <id>          # Retrieve a log with full request/response bodies
resend logs open [id]         # Open logs in the dashboard
```
## Webhooks

### `resend webhooks create`

Register a webhook endpoint.

```bash
resend webhooks create \
  --endpoint https://example.com/webhook \
  --events email.sent email.delivered
```

| Flag                  | Required | Description                                           |
| --------------------- | -------- | ----------------------------------------------------- |
| `--endpoint <url>`    | Yes      | HTTPS URL to receive events                           |
| `--events <types...>` | Yes      | Event types to subscribe to (use`all` for all events) |

### `resend webhooks listen`

Listen for webhook events locally during development. Starts a server, registers a temporary webhook, streams events, and cleans up on exit.

```bash
resend webhooks listen \
  --url https://hostname.tailnet-name.ts.net \
  --events email.received
```

| Flag                  | Required | Description                                                       |
| --------------------- | -------- | ----------------------------------------------------------------- |
| `--url <url>`         | Yes      | Your public URL (e.g., Tailscale Funnel URL)                      |
| `--events <types...>` | No       | Event types to listen for (default:`all`)                         |
| `--forward-to <url>`  | No       | Forward payloads to a local server (passes original Svix headers) |
| `--port <port>`       | No       | Local server port (default: 4318)                                 |

<Info>
  See the [webhook events documentation](/webhooks/event-types) for the full
  list of available event types. For agent-specific webhook patterns, see [CLI
  for AI Agents](/cli-agents#closing-the-loop-with-webhooks).
</Info>

### Other webhook commands

```bash
resend webhooks list              # List all webhook endpoints
resend webhooks get <id>          # Retrieve a webhook configuration
resend webhooks update <id>       # Update endpoint URL, events, or status
resend webhooks delete <id>       # Delete a webhook endpoint
```
<Tip>
  Run `resend <command> --help` for the full list of flags and options on any command.
</Tip>

## Utility

### `resend doctor`

Run environment diagnostics. Verifies your CLI version, API key, credential storage, and domain status.

```bash
resend doctor
```

| Check                  | Pass                                  | Warn                                         | Fail            |
| ---------------------- | ------------------------------------- | -------------------------------------------- | --------------- |
| **CLI Version**        | Running latest                        | Update available                             | —              |
| **API Key**            | Key found (shows masked key + source) | —                                           | No key found    |
| **Credential Storage** | Secure backend (e.g., macOS Keychain) | Plaintext file fallback                      | —              |
| **API Validation**     | Verified domains exist                | Sending-only key, no domains, or all pending | API key invalid |

```bash
