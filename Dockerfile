# Multi-stage Dockerfile for production deployment on Render
# Stage 1: Build frontend
FROM node:18-alpine as frontend-build

WORKDIR /app/frontend

COPY frontend/package*.json ./
RUN npm ci

COPY frontend/ ./
RUN npm run build

# Stage 2: Build backend
FROM python:3.11-slim as backend-build

WORKDIR /app/backend

# Install uv
RUN pip install uv

COPY backend/pyproject.toml backend/uv.lock ./
RUN uv sync --frozen --no-install-project --system

COPY backend/ ./

# Stage 3: Production image
FROM python:3.11-slim

# Install nginx and supervisor
RUN apt-get update && apt-get install -y nginx supervisor && rm -rf /var/lib/apt/lists/*

# Copy built frontend
COPY --from=frontend-build /app/frontend/dist /usr/share/nginx/html

# Copy backend
COPY --from=backend-build /app/backend /app/backend

# Copy nginx config
COPY nginx.conf /etc/nginx/nginx.conf

# Copy supervisor config
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Copy startup script
COPY start.sh /start.sh
RUN chmod +x /start.sh

# Expose port (Render will set PORT env var)
EXPOSE 10000

# Start services
CMD ["/start.sh"]