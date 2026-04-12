# Next.js Security Checklist

- Confirm sensitive server-only code stays off the client.
- Check public entry points such as Route Handlers and Server Actions.
- Verify auth and authorization are close to the data boundary.
- Review secret handling and `NEXT_PUBLIC_*` exposure.
- Check redirects, headers, and metadata behavior where trust boundaries matter.
