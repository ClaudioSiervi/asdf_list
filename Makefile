help:
	@$(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$'

# Pipenv
install:
	pipenv install

activate:
	pipenv shell

# Django
run:
	python manage.py runserver 8099

migration:
	python manage.py makemigrations

migrate:
	python manage.py migrate

superuser:
	python manage.py createsuperuser

shell:
	python manage.py shell_plus

loaddata:
	python manage.py loaddata fixtures/*

# Heroku
heroku-deploy:
	git push heroku master

heroku-migrations:
	heroku run python manage.py makemigrations

heroku-migrate:
	heroku run python manage.py migrate