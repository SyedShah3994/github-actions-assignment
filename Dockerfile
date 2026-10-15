
FROM python:3.12-slim
WORKDIR /app
RUN pip install --no-cache-dir uv
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev --no-install-project
COPY main.py ./
ENV PATH=/app/.venv/bin:$PATH
ENV PORT=10000
EXPOSE 10000
CMD uvicorn main:app --host 0.0.0.0 --port $PORT