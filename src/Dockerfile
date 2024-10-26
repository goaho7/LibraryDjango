FROM python:3.12

RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python3 - && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

ENV PATH="/root/.local/bin:$PATH"

WORKDIR /app

COPY ../pyproject.toml ../poetry.lock ./

RUN poetry install --no-root

COPY .. .

WORKDIR /app/src

# CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
