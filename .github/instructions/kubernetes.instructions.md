---
applyTo: "**/*.{yaml,yml}"
---

# Kubernetes Instructions

When modifying Kubernetes manifests:
- Follow existing namespace, labels, selectors, and naming conventions.
- Never hardcode secrets in manifests.
- Preserve readiness and liveness behavior unless intentionally changing it.
- Set resource requests/limits when the project convention requires them.
- Prefer declarative configuration.
- Review selector compatibility before changing labels.
- Consider rollout and rollback behavior.
