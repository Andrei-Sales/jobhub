---
applyTo: "**/*.tf"
---

# Terraform Instructions

- Follow the existing Terraform version and provider constraints.
- Reuse existing modules and conventions.
- Avoid hardcoded secrets.
- Prefer variables and locals for reusable configuration.
- Consider state impact before changing resources.
- Avoid destructive changes unless explicitly requested.
- Keep IAM permissions least-privilege.
- Explain potentially destructive infrastructure changes before applying them.
