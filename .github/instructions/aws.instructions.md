---
applyTo: "**/*"
---

# AWS Instructions

When working with AWS:
- Prefer least-privilege IAM.
- Never hardcode AWS credentials.
- Use AWS Secrets Manager or the project's approved secret-management mechanism for secrets.
- Consider CloudWatch logging and monitoring for production services.
- Follow existing AWS account, region, naming, tagging, and networking conventions.
- Consider cost, scalability, availability, and security.
- Do not recommend deprecated AWS services or APIs when a supported replacement exists.
