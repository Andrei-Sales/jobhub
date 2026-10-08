# JobHub

JobHub is a full-stack job marketplace and recruitment platform designed to connect applicants and employers through a secure, role-based platform for job discovery, applications, recruitment, and hiring management.

The application is being developed with a focus on clean architecture, secure authentication, RESTful APIs, automated testing, containerization, CI/CD, and cloud-ready deployment.

---

## Project Overview

JobHub provides a platform for three primary user roles:

- **Applicant** — manages a professional profile, searches for jobs, submits applications, and tracks application progress.
- **Employer** — manages a company profile, publishes job opportunities, reviews applicants, and manages the hiring process.
- **Administrator** — manages users, employers, job postings, and platform-level operations.

The system is designed as a modern full-stack application with a React frontend, FastAPI backend, and PostgreSQL database.

---

## Features

### Authentication

- User registration
- Email validation
- Secure password hashing
- Login
- JWT access tokens
- JWT refresh tokens
- Protected API endpoints
- Role-based authorization

### Applicant

- Applicant profile
- Skills management
- Education management
- Work experience
- Resume management
- Job search
- Job filtering
- Job applications
- Application tracking
- Notifications
- Messaging

### Employer

- Company profile
- Job posting
- Job management
- Job publishing and closing
- Applicant management
- Application review
- Hiring pipeline
- Notifications
- Messaging

### Administrator

- User management
- Employer management
- Job moderation
- Platform administration
- Activity monitoring

---

# Architecture

JobHub follows a layered architecture that separates presentation, API, business logic, security, and persistence responsibilities.

```text
                         ┌──────────────────────┐
                         │       Browser        │
                         │                      │
                         │ React + TypeScript   │
                         │        + MUI         │
                         └──────────┬───────────┘
                                    │
                                    │ HTTP / REST
                                    ▼
                         ┌──────────────────────┐
                         │      FastAPI API     │
                         │    Python Backend    │
                         └──────────┬───────────┘
                                    │
                   ┌────────────────┼────────────────┐
                   │                │                │
                   ▼                ▼                ▼
              API Layer        Service Layer     Security
              Routes/Deps      Business Logic    JWT/Auth
                   │                │                │
                   └────────────────┼────────────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │     SQLAlchemy       │
                         │         ORM          │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │     PostgreSQL       │
                         │      Database        │
                         └──────────────────────┘

                         Alembic
                            │
                            ▼
                    Database Migrations
```

### Architectural Principles

- Separation of concerns
- RESTful API design
- Layered backend architecture
- Secure authentication and authorization
- Database abstraction through SQLAlchemy
- Version-controlled database migrations
- Environment-based configuration
- Containerized development
- Automated testing
- CI/CD-ready architecture
- Cloud-ready deployment

---

# Technology Stack

## Backend

| Technology        | Purpose                           |
| ----------------- | --------------------------------- |
| Python            | Backend programming language      |
| FastAPI           | REST API framework                |
| Pydantic          | Data validation and serialization |
| SQLAlchemy        | ORM and database access           |
| Alembic           | Database migrations               |
| PostgreSQL        | Relational database               |
| JWT               | Authentication                    |
| bcrypt            | Password hashing                  |
| Uvicorn           | ASGI application server           |
| OpenAPI / Swagger | API documentation                 |

## Frontend

| Technology        | Purpose                       |
| ----------------- | ----------------------------- |
| React             | Frontend framework            |
| TypeScript        | Frontend programming language |
| Vite              | Frontend build tooling        |
| Material UI (MUI) | UI component library          |
| React Router      | Client-side routing           |
| React Query       | Server-state management       |

## DevOps and Cloud

| Technology          | Purpose                |
| ------------------- | ---------------------- |
| Git                 | Version control        |
| GitHub              | Source control         |
| Docker              | Containerization       |
| Docker Compose      | Local development      |
| Jenkins             | CI/CD                  |
| AWS                 | Cloud platform         |
| Amazon ECR          | Container registry     |
| Amazon EKS          | Kubernetes platform    |
| Amazon RDS          | PostgreSQL hosting     |
| Amazon S3           | Object/file storage    |
| AWS Secrets Manager | Secret management      |
| Amazon CloudWatch   | Monitoring and logging |
| CloudFront          | Content delivery       |

---

# User Roles

## Applicant

Applicants can:

- Create and manage an account
- Maintain a professional profile
- Add skills
- Add education
- Add work experience
- Manage resumes
- Search and filter job opportunities
- View job details
- Apply for jobs
- Track applications
- Receive notifications
- Communicate with employers

## Employer

Employers can:

- Create and manage an employer account
- Manage company information
- Create job postings
- Edit job postings
- Publish and close jobs
- Review applicants
- Manage applications
- Manage the hiring pipeline
- Communicate with applicants
- Monitor recruitment activity

## Administrator

Administrators can:

- Manage users
- Manage employers
- Moderate job postings
- Monitor platform activity
- Manage platform-level configuration

---

# Authentication and Authorization

JobHub uses JWT-based authentication with access and refresh tokens.

The authentication flow is:

```text
Register
   │
   ▼
Validate Input
   │
   ▼
Hash Password
   │
   ▼
Store User
   │
   ▼
Login
   │
   ▼
Verify Password
   │
   ▼
Generate Access + Refresh Tokens
   │
   ▼
Client Sends Access Token
   │
   ▼
Validate JWT
   │
   ▼
Load Current User
   │
   ▼
Authorize Request
```

## Roles

```text
APPLICANT
EMPLOYER
ADMIN
```

Role-based authorization protects functionality according to the user's role.

Example:

```text
/api/applicant/*
        │
        └── APPLICANT

/api/employer/*
        │
        └── EMPLOYER

/api/admin/*
        │
        └── ADMIN
```

The user's database record is used as the source of truth for authorization.

---

# API Documentation

FastAPI automatically generates OpenAPI documentation.

## Swagger UI

```text
http://127.0.0.1:8000/docs
```

## OpenAPI JSON

```text
http://127.0.0.1:8000/openapi.json
```

---

# Authentication API

## Register

```http
POST /api/auth/register
```

Example request:

```json
{
  "email": "applicant@jobhub.com",
  "password": "Password123!",
  "role": "APPLICANT"
}
```

## Login

```http
POST /api/auth/login
```

Example request:

```json
{
  "email": "applicant@jobhub.com",
  "password": "Password123!"
}
```

Example response:

```json
{
  "access_token": "...",
  "refresh_token": "...",
  "token_type": "bearer"
}
```

## Current User

```http
GET /api/users/me
Authorization: Bearer <access_token>
```

Example response:

```json
{
  "id": 1,
  "email": "applicant@jobhub.com",
  "role": "APPLICANT",
  "is_active": true
}
```

---

# Database Architecture

JobHub uses PostgreSQL as its primary relational database.

SQLAlchemy provides ORM-based database access, while Alembic manages database schema migrations.

## Core User Entity

```text
users
├── id
├── email
├── password_hash
├── role
├── is_active
├── created_at
└── updated_at
```

The application is designed to support additional domain entities such as:

```text
users
│
├── applicant_profiles
│       ├── skills
│       ├── experiences
│       ├── educations
│       └── resumes
│
├── companies
│       └── jobs
│              │
│              └── applications
│                     │
│                     └── application_status_history
│
├── messages
│
└── notifications
```

Relationships, constraints, and indexes are implemented as the corresponding business domains are introduced.

---

# Project Structure

```text
JobHub/
│
├── backend/
│   │
│   ├── app/
│   │   ├── api/
│   │   │   ├── auth.py
│   │   │   ├── dependencies.py
│   │   │   └── users.py
│   │   │
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   ├── jwt.py
│   │   │   └── security.py
│   │   │
│   │   ├── db/
│   │   │   └── database.py
│   │   │
│   │   ├── models/
│   │   │   └── user.py
│   │   │
│   │   ├── schemas/
│   │   │   ├── auth.py
│   │   │   └── user.py
│   │   │
│   │   ├── services/
│   │   │
│   │   └── main.py
│   │
│   ├── alembic/
│   ├── tests/
│   ├── .env.example
│   ├── alembic.ini
│   ├── Dockerfile
│   └── requirements.txt
│
├── frontend/
│   │
│   ├── src/
│   │   ├── api/
│   │   ├── components/
│   │   ├── layouts/
│   │   ├── pages/
│   │   ├── routes/
│   │   ├── types/
│   │   └── App.tsx
│   │
│   ├── Dockerfile
│   └── package.json
│
├── docker-compose.yml
├── Jenkinsfile
├── .gitignore
└── README.md
```

---

# Local Setup

## Prerequisites

Install:

- Python 3.x
- Node.js and npm
- Docker Desktop
- Git

---

## Start PostgreSQL

From the project root:

```powershell
docker compose up -d postgres
```

Check the running containers:

```powershell
docker compose ps
```

---

# Backend Setup

Navigate to the backend:

```powershell
cd backend
```

Create a virtual environment:

```powershell
python -m venv venv
```

Activate the virtual environment:

```powershell
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

Create a local environment file:

```text
backend/.env
```

Use `backend/.env.example` as the configuration template.

Run database migrations:

```powershell
python -m alembic upgrade head
```

Start FastAPI:

```powershell
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Swagger:

```text
http://127.0.0.1:8000/docs
```

---

# Frontend Setup

Navigate to the frontend:

```powershell
cd frontend
```

Install dependencies:

```powershell
npm install
```

Start the development server:

```powershell
npm run dev
```

The frontend development URL will be displayed by Vite.

---

# Docker

Docker is used to provide a consistent local development environment.

The intended local architecture is:

```text
┌─────────────────────┐
│ React + TypeScript  │
│ Frontend Container  │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ FastAPI Backend     │
│ Python Container    │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ PostgreSQL          │
│ Database Container  │
└─────────────────────┘
```

PostgreSQL is currently provided through Docker Compose.

The application is designed to run as a complete containerized stack as the frontend and backend container configurations mature.

---

# Health Checks

## API Health

```http
GET /api/health
```

Response:

```json
{
  "status": "ok",
  "service": "jobhub-api"
}
```

## Database Health

```http
GET /api/health/db
```

Response:

```json
{
  "status": "ok",
  "database": "postgresql"
}
```

---

# Testing

JobHub uses automated testing at multiple levels.

## Backend Testing

Tools:

- Pytest
- FastAPI TestClient
- SQLAlchemy test database

Testing areas include:

- Authentication
- Authorization
- User management
- API validation
- Database operations
- Business logic
- Error handling

## Frontend Testing

Tools:

- React Testing Library
- Vitest

Testing areas include:

- Components
- Forms
- Authentication flows
- Protected routes
- API integration
- Role-based UI behavior

---

# Security

Security is a core requirement of JobHub.

The application uses or is designed to use:

- Secure password hashing
- JWT access tokens
- JWT expiration
- Refresh-token validation
- Role-based authorization
- Input validation
- SQLAlchemy-based database access
- CORS configuration
- Rate limiting
- Secure file upload validation
- File access authorization
- Security headers
- Environment-based configuration
- Secure secret management
- HTTPS in production

Sensitive configuration must never be committed to source control.

The real `.env` file should remain local. Only `.env.example` should be committed.

Production secrets are intended to be managed through AWS Secrets Manager.

---

# CI/CD Architecture

JobHub is designed for automated CI/CD using Jenkins and GitHub.

The intended pipeline is:

```text
Developer
    │
    ▼
GitHub
    │
    ▼
Jenkins
    │
    ├── Checkout
    │
    ├── Backend Tests
    │
    ├── Frontend Tests
    │
    ├── Backend Build
    │
    ├── Frontend Build
    │
    ├── Docker Image Build
    │
    └── Deployment
```

The CI/CD implementation will initially focus on local Jenkins execution before being extended to AWS.

---

# AWS Architecture

The application is designed to support eventual AWS deployment.

A target production architecture is:

```text
                         AWS
                          │
             ┌────────────┴────────────┐
             │                         │
             ▼                         ▼
        CloudFront               Load Balancer
             │                         │
             ▼                         ▼
        Frontend                 Amazon EKS
                                      │
                                      │
                                      ▼
                                FastAPI Pods
                                      │
                                      ▼
                                Amazon RDS
                                  PostgreSQL
```

Supporting AWS services may include:

- Amazon ECR
- Amazon EKS
- Amazon RDS PostgreSQL
- Amazon S3
- AWS Secrets Manager
- Amazon CloudWatch
- IAM
- Application Load Balancer
- CloudFront

---

# Git Workflow

Git is used for source control.

Recommended branch naming:

```text
main
develop
feature/*
bugfix/*
```

Examples:

```text
feature/applicant-profile
feature/job-search
feature/application-management
bugfix/duplicate-application
```

Recommended commit format:

```text
feat: add applicant profile
fix: prevent duplicate job applications
test: add authentication tests
docs: update API documentation
refactor: improve authentication service
```

Sensitive files and generated dependencies should not be committed.

Examples:

```text
.env
venv/
.venv/
node_modules/
__pycache__/
```

---

# License

This project is currently intended as a personal software engineering and portfolio project.

License terms can be added when the project is prepared for public distribution.
