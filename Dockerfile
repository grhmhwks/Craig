# syntax=docker/dockerfile:1
FROM node:22-alpine AS frontend
WORKDIR /source/app/frontend
COPY app/frontend/package.json app/frontend/package-lock.json ./
RUN npm ci
COPY app/frontend/ ./
RUN npm run build

FROM python:3.12-slim AS runtime
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    CRAIG_CONTENT_ROOT=/app/content \
    CRAIG_INDEX_PATH=/data/index.sqlite3 \
    CRAIG_FRONTEND_DIST=/app/app/frontend/dist
WORKDIR /app

COPY pyproject.toml Combinatorics_README.md ./
COPY craig/ ./craig/
RUN python -m pip install --no-cache-dir .

COPY content/ ./content/
COPY --from=frontend /source/app/frontend/dist/ ./app/frontend/dist/
COPY scripts/docker-entrypoint.sh /usr/local/bin/craig-entrypoint

RUN addgroup --system craig \
    && adduser --system --ingroup craig --home /app craig \
    && mkdir -p /data \
    && chown craig:craig /data \
    && chmod 0555 /usr/local/bin/craig-entrypoint

USER craig
VOLUME ["/data"]
EXPOSE 8000
ENTRYPOINT ["/usr/local/bin/craig-entrypoint"]
