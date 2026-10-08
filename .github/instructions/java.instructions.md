---
applyTo: "**/*.java"
---

# Java Instructions

- Follow the project's existing Java version and build configuration.
- Prefer clear, maintainable object-oriented design.
- Keep business logic out of controllers or transport-layer code.
- Reuse existing services, repositories, utilities, and exception patterns.
- Validate external input.
- Avoid catching exceptions without meaningful handling.
- Do not log secrets or sensitive data.
- Prefer parameterized database access.
- Add focused unit/integration tests for behavior changes.
- Do not introduce Spring or another framework unless the project already uses it or the task explicitly requires it.
