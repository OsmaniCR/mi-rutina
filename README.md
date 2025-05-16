# Mi Rutina

A Django-based routine management application.

## Description

Mi Rutina is a web application built with Django and Django REST Framework for managing daily routines and tasks.

## Features

- User authentication with JWT
- RESTful API
- Routine management
- PostgreSQL database
- Docker containerization
- Poetry for dependency management

## Infrastructure

The project is configured with:

1. **Backend (Django)**
   - Python 3.12
   - Poetry for dependency management
   - Uvicorn development server
   - Port 8000 exposed

2. **Database**
   - PostgreSQL 15
   - Port 5432 exposed
   - Persistent volume for data storage
   - Configurable environment variables

3. **Networks**
   - Custom bridge network `mi-rutina-network`
   - Isolated service communication

## Installation

1. Clone the repository
2. Create a `.env` file in the root directory with the following variables:
   ```env
    DEBUG=True
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=postgres
    POSTGRES_DB=postgres
    POSTGRES_HOST=db
    POSTGRES_PORT=5432
    SECRET_KEY="django-insecure-=m%amjpt0j7gy4mv399#8s&6u^+dfdw35ld^=5s(p)c1wi#8r0"
   ```
3. Use Docker Compose to run the project

## Available Commands

The project includes a Makefile with several useful commands:

```bash
# Start development environment
make run-dev

# Run database migrations
make migrate

# Create new migrations
make makemigrations

# Create superuser
make createsuperuser

# Collect static files
make collectstatic

# Seed database with initial data
make seed
```

## Development

### Using Docker Compose

1. **Start the project**
   ```bash
   make run-dev
   ```

2. **Set up the database**
   ```bash
   # Run migrations
   make migrate
   
   # Create superuser
   make createsuperuser
   
   # Populate database with initial data
   make seed
   ```

### Manual Development (without Docker)

```bash
# Install dependencies
poetry install

# Run migrations
python manage.py migrate

# Start development server
python manage.py runserver
```

## Important Notes

1. The project uses Poetry for dependency management, configured to install within the container
2. PostgreSQL data is stored in a persistent volume named `mi-rutina-postgres_data`
3. The backend is configured to automatically reload when code changes are detected
4. Services are connected through a dedicated Docker network for better isolation and security

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request