# ai-study-companion
End-to-End Full-Stack App

## Problem Description

AI Study Companion is a full-stack web application designed to help students with AI-powered study assistance. It provides features like AI question generation, leaderboard tracking, user profiles, and authentication.

## Architecture Diagram

```
Frontend (React + TypeScript + Vite)
    |
    | (HTTP API calls)
    v
Backend (FastAPI + SQLAlchemy)
    |
    | (Database queries)
    v
Database (PostgreSQL for production, SQLite for development)
```

## Tech Stack

### Frontend
- React 18 with TypeScript
- Vite for build tooling
- Vitest for unit testing
- Fetch API for HTTP requests

### Backend
- FastAPI for REST API
- SQLAlchemy for ORM
- Pydantic for data validation
- JWT for authentication
- pytest for testing

### Database
- PostgreSQL (production)
- SQLite (development)

### DevOps
- Docker & Docker Compose
- GitHub Actions for CI/CD
- Render for deployment

## OpenAPI Specification

The API is fully documented with OpenAPI 3.0. The specification file is located at `openapi.yaml` and includes endpoints for:
- Authentication (login/signup)
- AI question generation
- Leaderboard management
- User profile operations

## MCP Usage (Context7)

We used Context7 MCP to:

- Fetch latest FastAPI patterns
- Resolve SQLAlchemy session issues
- Validate OpenAPI correctness

## Local Setup

### Prerequisites
- Node.js 18+
- Python 3.11+
- uv (Python package manager)

### Backend Setup
```bash
cd backend
uv sync
uv run uvicorn app.main:app --reload
```

### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

### Database
The app uses SQLite for development. For production, configure PostgreSQL via `DATABASE_URL` environment variable.

## Docker Setup

### Development
```bash
docker-compose up --build
```

### Production
```bash
docker build -t ai-study-companion .
docker run -p 10000:10000 -e PORT=10000 ai-study-companion
```

## CI/CD Pipeline

GitHub Actions workflow (`.github/workflows/ci.yml`) includes:
- Frontend tests (Vitest)
- Backend tests (pytest)
- Integration tests
- Deploy to Render on main branch push

## Deployment URL

[https://ai-study-companion.onrender.com](https://ai-study-companion.onrender.com)
