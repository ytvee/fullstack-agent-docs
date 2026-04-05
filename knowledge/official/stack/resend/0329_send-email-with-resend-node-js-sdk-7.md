# Send Email with Resend Node.js SDK

**Purpose:** Enforce only the **current** and **correct** instructions for sending emails using the [Resend](https://resend.com/) Node.js SDK.
**Scope:** All AI-generated advice or code related to sending email with Resend must follow these guardrails.

---

## **1. Official Resend Node.js Setup**

### **Prerequisites**

Human must first create an API key and verify their domain at [https://resend.com/domains](https://resend.com/domains).

The API key must be stored in an environment variable called `RESEND_API_KEY`.

```typescript
const resend = new Resend(process.env.RESEND_API_KEY);
```
The domain should be verified at [https://resend.com/domains](https://resend.com/domains) and added to the `from` address.

### **Install the SDK**

Use the project's existing package manager to install the Resend Node.js SDK.

```bash
npm install resend
