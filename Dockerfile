FROM python:3.12-slim

LABEL maintainer="Hamzeh Aljolani"

ARG APP_VERSION=1.0

ENV APP_NAME="My First Docker App" \
    APP_VERSION=$APP_VERSION \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY server.py .

RUN useradd -m appuser

USER appuser

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=3s CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000')" || exit 1

ENTRYPOINT ["python", "server.py"]
CMD ["8000"]
