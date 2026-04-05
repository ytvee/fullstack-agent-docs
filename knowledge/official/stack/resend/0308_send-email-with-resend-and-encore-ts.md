# Send Email with Resend and Encore.ts

**Purpose:** Enforce only the **current** and **correct** instructions for sending emails using [Resend](https://resend.com/) with the [Encore.ts](https://encore.dev) backend framework.
**Scope:** All AI-generated advice or code related to sending email with Resend inside an Encore.ts application must follow these guardrails.

---

## **1. Official Resend + Encore.ts Setup**

### **Prerequisites**

Human must first:

* Install [Encore](https://encore.dev/docs/ts/install) (`brew install encoredev/tap/encore` or `curl -L https://encore.dev/install.sh | bash`)
* Create a Resend API key at [https://resend.com/api-keys](https://resend.com/api-keys)
* Verify a sending domain at [https://resend.com/domains](https://resend.com/domains)

The API key must be stored as an **Encore secret** (not an environment variable or `.env` file):

```bash
encore secret set --type dev,local,pr,production ResendAPIKey
```
### **Install the SDK**

Use the project's existing package manager to install the Resend Node.js SDK.

```bash
npm install resend
