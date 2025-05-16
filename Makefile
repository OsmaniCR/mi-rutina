run-dev:
	docker compose -f ./docker-compose.yml up --build

migrate:
	docker compose -f ./docker-compose.yml run backend python manage.py migrate

makemigrations:
	docker compose -f ./docker-compose.yml run backend python manage.py makemigrations

createsuperuser:
	docker compose -f ./docker-compose.yml run backend python manage.py createsuperuser

collectstatic:
	docker compose -f ./docker-compose.yml run backend python manage.py collectstatic --noinput

seed:
	docker compose -f ./docker-compose.yml run backend python manage.py seed
