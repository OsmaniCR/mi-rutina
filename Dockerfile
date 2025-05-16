FROM python:3.12-slim

WORKDIR /app

RUN pip install poetry

ENV PYTHONUNBUFFERED 1
ENV PATH="/root/.local/bin:$PATH"

RUN apt-get update && apt-get install -y libgirepository1.0-dev gcc libcairo2-dev pkg-config python3-dev gir1.2-gtk-3.0 libglib2.0-dev

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

RUN apt-get clean && rm -rf /var/lib/apt/lists/*

COPY . .

EXPOSE 8000

CMD ["sh", "-c", "poetry run python manage.py makemigrations && poetry run python manage.py migrate && poetry run python manage.py runserver 0.0.0.0:8000"]
