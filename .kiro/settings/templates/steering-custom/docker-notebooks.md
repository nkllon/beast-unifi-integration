# Docker-Based Notebook Execution

## Problem Statement

Stopping processes (Jupyter servers, browser automation, etc.) can leave the system in an inconsistent state:
- Hanging processes
- Broken browser sessions
- Orphaned containers
- Locked files
- Port conflicts

## Solution: Container-Based Execution

Run notebooks in Docker containers with proper lifecycle management:

### Benefits
1. **Isolation:** Each notebook run is isolated
2. **Clean Shutdown:** Container cleanup handles all processes
3. **Consistent Environment:** Same environment every time
4. **Resource Limits:** Prevent runaway processes
5. **Easy Cleanup:** `docker rm` removes everything

## Docker Compose Configuration

```yaml
services:
  notebook:
    build:
      context: .
      dockerfile: docker/Dockerfile.notebook
    volumes:
      - .:/workspace:rw
      - notebook-data:/data
    ports:
      - "8888:8888"
    environment:
      - PROJECT_ROOT=/workspace
      - JUPYTER_ENABLE_LAB=yes
    command: jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root
    restart: "no"  # Don't auto-restart on exit
    
  notebook-executor:
    build:
      context: .
      dockerfile: docker/Dockerfile.notebook
    volumes:
      - .:/workspace:ro
      - notebook-output:/output
    environment:
      - PROJECT_ROOT=/workspace
    entrypoint: ["jupyter", "nbconvert", "--execute", "--to", "notebook"]
    # Run single notebook: docker compose run notebook-executor -- notebook.ipynb
```

## Dockerfile Pattern

```dockerfile
FROM python:3.10-slim

WORKDIR /workspace

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install UV
RUN pip install uv

# Install Python dependencies
COPY pyproject.toml uv.lock ./
RUN uv sync

# Install Jupyter
RUN uv pip install jupyter jupyterlab ipykernel

# Copy project
COPY . /workspace

# Set environment
ENV PYTHONPATH=/workspace/src
ENV PROJECT_ROOT=/workspace

# Default command
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
```

## Execution Patterns

### Interactive Development
```bash
# Start notebook server
docker compose up notebook

# Access at http://localhost:8888
# Stop with: docker compose down notebook
```

### One-Off Execution
```bash
# Execute single notebook
docker compose run --rm notebook-executor -- \
  notebooks/analysis/unifi_data_analysis.ipynb
```

### Automated Execution
```bash
# Execute all notebooks in a directory
docker compose run --rm notebook-executor -- \
  --execute --inplace notebooks/analysis/*.ipynb
```

## Process Management

### Container Lifecycle
1. **Start:** Container starts, processes initialized
2. **Run:** Notebook executes, processes run
3. **Stop:** `docker compose down` or `docker stop` sends SIGTERM
4. **Cleanup:** Container removed, all processes terminated

### Clean Shutdown Pattern
```bash
# Graceful shutdown
docker compose down --timeout 10

# Force shutdown if needed
docker compose kill

# Remove containers
docker compose rm -f
```

## Resource Limits

```yaml
services:
  notebook:
    # ... config ...
    deploy:
      resources:
        limits:
          cpus: '2'
          memory: 4G
        reservations:
          cpus: '1'
          memory: 2G
```

## Volume Strategy

- **Source Code:** Bind mount (read-write for development)
- **Output Data:** Named volume (persists between runs)
- **Cache:** Named volume (speeds up subsequent runs)

## Integration with _setup_paths.py

`PROJECT_ROOT` in containers is `/workspace` (or whatever WORKDIR is set to). The `_setup_paths.py` module works identically in containers.

## Recommendation

**Use Docker for all notebook execution:**
1. Interactive development: `docker compose up notebook`
2. Automated runs: `docker compose run notebook-executor`
3. CI/CD: Same container, different entrypoint

This ensures:
- ✅ Consistent environment
- ✅ Clean process management
- ✅ No orphaned processes
- ✅ Easy cleanup
- ✅ Resource limits enforced

