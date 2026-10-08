---
applyTo: "**/{Dockerfile,docker-compose.yml,docker-compose.yaml,*.dockerfile}"
---

# Docker Instructions

- Prefer small, reproducible images.
- Use multi-stage builds when appropriate.
- Avoid running containers as root when practical.
- Do not bake secrets into images.
- Use environment variables or approved secret-management mechanisms.
- Pin important base images/dependencies where project policy requires it.
- Keep build context minimal with an appropriate .dockerignore.
- Preserve existing health checks and container conventions.
