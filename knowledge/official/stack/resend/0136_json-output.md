# JSON output
resend doctor --json
```
```json
{
  "ok": true,
  "checks": [
    { "name": "CLI Version", "status": "pass", "message": "v1.7.0 (latest)" },
    {
      "name": "API Key",
      "status": "pass",
      "message": "re_...xxxx (source: env)"
    },
    {
      "name": "Credential Storage",
      "status": "pass",
      "message": "macOS Keychain"
    },
    { "name": "Domains", "status": "pass", "message": "2 verified, 0 pending" }
  ]
}
```
Exits `0` when all checks pass or warn. Exits `1` if any check fails.

### Other utility commands


| Command                       | Description                                                     |
| ----------------------------- | --------------------------------------------------------------- |
| `resend whoami`               | Show current authentication status                              |
| `resend open`                 | Open the Resend dashboard in your browser                       |
| `resend update`               | Check for available CLI updates                                 |
| `resend completion [shell]`   | Generate shell completion scripts (bash, zsh, fish, powershell) |
| `resend completion --install` | Auto-install completions into your shell profile                |

## Global options

These flags work on every command:

```bash
resend [global options] <command> [command options]
```

| Flag                   | Description                                           |
| ---------------------- | ----------------------------------------------------- |
| `--api-key <key>`      | Override API key for this invocation                  |
| `-p, --profile <name>` | Profile to use (overrides`RESEND_PROFILE` env var)    |
| `--json`               | Force JSON output even in interactive terminals       |
| `-q, --quiet`          | Suppress spinners and status output (implies`--json`) |
| `--insecure-storage`   | Save API key as plaintext instead of secure storage   |
| `--version`            | Print version and exit                                |
| `--help`               | Show help text                                        |

## Output behavior

The CLI has two output modes that switch automatically:


| Mode            | When                  | Stdout         | Stderr            |
| --------------- | --------------------- | -------------- | ----------------- |
| **Interactive** | Terminal (TTY)        | Formatted text | Spinners, prompts |
| **Machine**     | Piped, CI, or`--json` | JSON           | Nothing           |

Pipe to another command and JSON output activates:

```bash
resend doctor | jq '.checks[].name'
resend emails send \
  --from "Acme <onboarding@resend.dev>" \
  --to delivered@resend.dev \
  --subject "Hello World" \
  --text "It works!" | jq '.id'
```
Errors always exit with code `1` and output structured JSON:

```json
{ "error": { "message": "No API key found", "code": "auth_error" } }
```
## CI/CD

Set `RESEND_API_KEY` as an environment variable — no `resend login` needed:

```yaml
