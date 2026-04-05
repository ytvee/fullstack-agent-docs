# GitHub Actions
env:
  RESEND_API_KEY: ${{ secrets.RESEND_API_KEY }}
steps:
  - run: |
      resend emails send \
        --from "Acme <onboarding@resend.dev>" \
        --to delivered@resend.dev \
        --subject "Deploy complete" \
        --text "Version ${{ github.sha }} deployed."
```
## Configuration


| Item              | Path                  | Notes                                                               |
| ----------------- | --------------------- | ------------------------------------------------------------------- |
| Config directory  | `~/.config/resend/`   | Respects`$XDG_CONFIG_HOME` on Linux, `%APPDATA%` on Windows         |
| Credentials       | System secure storage | macOS Keychain, Windows Credential Manager, or Linux secret service |
| Install directory | `~/.resend/bin/`      | Respects`$RESEND_INSTALL`                                           |

<Card title="Using the CLI with AI Agents" icon="microchip-ai" href="/cli-agents">
Learn about Agent Skills, non-interactive mode, and local webhook development
for AI agents.
</Card>

