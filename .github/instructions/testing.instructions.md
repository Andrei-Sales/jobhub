---
applyTo: "**/*"
---

# Testing Instructions

When implementing behavior changes:
- Inspect existing tests before creating new ones.
- Follow the project's current test framework and conventions.
- Prefer focused tests over brittle implementation-detail tests.
- Cover success, validation failure, error handling, and important edge cases.
- Do not remove tests simply to make a build pass.
- Do not weaken assertions without a clear reason.
- Keep tests deterministic and isolated.
