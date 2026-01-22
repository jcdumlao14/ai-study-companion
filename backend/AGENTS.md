# Backend Development Instructions

This backend uses **uv** for dependency management.

## Commands
- Install dependencies: `uv sync`
- Add dependency: `uv add <package>`
- Run app: `uv run uvicorn app.main:app --reload`
- Run tests: `uv run pytest`

All implementations must strictly follow `openapi.yaml`.