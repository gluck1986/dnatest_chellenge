.PHONY: build up down migrate shell

build:
	docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down

migrate:
	docker-compose run --rm web python manage.py migrate

makemigrations:
	docker-compose run --rm web python manage.py makemigrations