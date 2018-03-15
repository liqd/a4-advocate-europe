all: help

VIRTUAL_ENV ?= venv
SOURCE_DIRS = apps advocate_europe cms tests

help:
	@echo advocate-europe development tools
	@echo
	@echo It will either use a exisiting virtualenv if it was entered
	@echo before or create a new one in the same directory.
	@echo
	@echo usage:
	@echo
	@echo "  make install      -- install dev setup"
	@echo "  make server       -- development server"
	@echo "  make test         -- tests on exiting database"
	@echo "  make lint         -- lint javascript and python"
	@echo "  make release      -- build everything required for a release"
	@echo

install:
	npm install
	npm run build
	if [ ! -f $(VIRTUAL_ENV)/bin/python3 ]; then python3 -m venv $(VIRTUAL_ENV); fi
	$(VIRTUAL_ENV)/bin/python3 -m pip install --upgrade -r requirements/dev.txt
	$(VIRTUAL_ENV)/bin/python3 manage.py migrate

fixtures:
	$(VIRTUAL_ENV)/bin/python3 manage.py loaddata advocate_europe/fixtures/site-dev.json
	$(VIRTUAL_ENV)/bin/python3 manage.py loaddata advocate_europe/fixtures/users-dev.json
	$(VIRTUAL_ENV)/bin/python3 manage.py loaddata advocate_europe/fixtures/projects-dev.json
	$(VIRTUAL_ENV)/bin/python3 manage.py loadtestdata advocate_europe_ideas.IdeaSketch:7

watch:
	trap 'kill %1; kill %2' KILL; \
	npm run watch & \
	$(VIRTUAL_ENV)/bin/python3 manage.py process_tasks & \
	$(VIRTUAL_ENV)/bin/python3 manage.py runserver 8002

server:
	$(VIRTUAL_ENV)/bin/python3 manage.py runserver 8002

background-tasks:
	$(VIRTUAL_ENV)/bin/python3 manage.py process_tasks

test:
	$(VIRTUAL_ENV)/bin/py.test --reuse-db

test-lastfailed:
	$(VIRTUAL_ENV)/bin/py.test --reuse-db --last-failed

coverage:
	$(VIRTUAL_ENV)/bin/py.test --reuse-db --cov --cov-report=html

locales-collect:
	$(VIRTUAL_ENV)/bin/python manage.py makemessages -d djangojs
	$(VIRTUAL_ENV)/bin/python manage.py makemessages -d django
	sed -i 's%#: .*/node_modules.*/adhocracy4%#: adhocracy4.js%' locale/*/LC_MESSAGES/django*.po
	sed -i 's%#: .*/adhocracy4%#: adhocracy4.py%' locale/*/LC_MESSAGES/django*.po

lint:
	EXIT_STATUS=0; \
	$(VIRTUAL_ENV)/bin/isort --diff -rc -c $(SOURCE_DIRS) ||  EXIT_STATUS=$$?; \
	$(VIRTUAL_ENV)/bin/flake8 $(SOURCE_DIRS) --exclude migrations,settings ||  EXIT_STATUS=$$?; \
	npm run lint --silent ||  EXIT_STATUS=$$?; \
	$(VIRTUAL_ENV)/bin/python manage.py makemigrations --dry-run --check --noinput || EXIT_STATUS=$$?; \
	exit $${EXIT_STATUS}

.PHONY: release
release: export DJANGO_SETTINGS_MODULE ?= advocate_europe.settings.build
release:
	npm install --silent
	npm run build
	$(VIRTUAL_ENV)/bin/python3 -m pip install -r requirements.txt -q
	$(VIRTUAL_ENV)/bin/python3 manage.py collectstatic --noinput -v0

make:
	@echo Hello dwarf planet!
