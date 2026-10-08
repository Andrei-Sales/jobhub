---
applyTo: "**/*.{java,php,js,ts}"
---

# Backend Instructions

- Keep API contracts explicit and backward compatible where possible.
- Validate request input.
- Return appropriate HTTP status codes.
- Do not expose internal exceptions, stack traces, credentials, or sensitive data.
- Separate transport, business, and persistence concerns according to the existing architecture.
- Reuse existing authentication and authorization mechanisms.
- Add tests for new business rules and failure paths.
