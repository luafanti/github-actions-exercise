# GitHub Actions Exercise

Simple FastAPI application with CI/CD pipeline configured using GitHub Actions. This project demonstrates building Docker images, running tests, code quality checks, and security scanning.

## Overview

- FastAPI HTTP server with two endpoints (`/health-check` and `/hello-world`)
- Docker containerization with security best practices
- CI/CD pipeline with GitHub Actions
- Code quality checks (linting, formatting, type checking)
- Security scanning (dependency vulnerabilities, Docker image scanning)

## Tools & Configuration

- **FastAPI** - Web framework
- **Docker** - Containerization (Debian-slim base image)
- **GitHub Actions** - CI/CD pipelines
- **Pytest** - Testing framework with coverage
- **Ruff** - Fast Python linter and formatter
- **MyPy** - Static type checking
- **Bandit** - Security linter for Python
- **Safety** - Dependency vulnerability scanning
- **Trivy** - Docker image vulnerability scanner

## Quick Start


### Docker

```bash
docker build -t github-actions-exercise .
docker run -p 8000:8000 -e SERVER_HELLO="Hello Welyo" github-actions-exercise
```

### Running on macOS

The Docker image is built for Linux (Ubuntu) on AMD64 architecture. On Apple Silicon Macs (M1/M2), you need to specify the platform explicitly:

```bash
docker login ghcr.io
docker pull --platform=linux/amd64 ghcr.io/luafanti/github-actions-exercise:latest
docker run --platform=linux/amd64 -p 8000:8000 -e SERVER_HELLO="Hello Welyo" ghcr.io/luafanti/github-actions-exercise:latest
```


## ADR

### Docker

- **Base image**: Python 3.13 on Debian-slim instead of Alpine. Debian-slim is simpler, more predictable, and has better compatibility with Python packages, avoiding Alpine-specific surprises.
- **Layer caching**: Optimized order - dependencies first, application code last to maximize cache hits.
- **Security**: Non-root user (`appuser`) runs the container, limiting potential impact of security vulnerabilities.

### CI/CD Pipeline

- **Parallel jobs**: Checkout and setup steps are repeated across jobs instead of combining them. While slightly slower, this approach makes it easier to identify which step failed and allows jobs to run in parallel.
- **Simple tagging**: Docker images are tagged with branch name, branch-SHA, and latest (for main branch). More advanced tagging strategies (semantic versioning, release tags) can be implemented as needed.
- **SonarQube**: Provided as a sample. Requires SonarQube server access and configuration, so it's kept as reference only.
- **ECR sample**: AWS ECR push example is included as a commented sample for reference.

### GitHub Enterprise Integration

Many features can be integrated with GitHub Enterprise (advanced security, dependency review, code scanning), but these require Enterprise licensing. GitHub's ecosystem has significantly expanded over recent years with powerful CI/CD and security features.
