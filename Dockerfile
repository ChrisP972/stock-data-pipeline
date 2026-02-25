# Base docker image
FROM python:3.13.12

# Copy uv binary from official uv image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

# Set working directory
WORKDIR /app

# Add virtual environment to PATH so we can use installed packages
ENV PATH="/app/.venv/bin:$PATH"

# Copy dependency files
COPY "pyproject.toml" "uv.lock"  ".python-version" ./

# Install dependencies from lock file
RUN uv sync --locked

# Copy application code
COPY collect_stock_data.py db.py ./

# Set entry point
ENTRYPOINT ["uv", "run", "python", "collect_stock_data.py"]