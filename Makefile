all: help

VIRTUAL_ENV ?= .
SOURCE_DIRS = apps a4_advocate_europe cms tests

help:
	@echo a4-advocate-europe development tools
	@echo
	@echo It will either use a exisiting virtualenv if it was entered
	@echo before or create a new one in the same directory.
	@echo
	@echo usage:
	@echo
	@echo   make install      -- install dev setup
	@echo   make server	  -- development server
	@echo   make test         -- tests on exiting database
	@echo   make lint	  -- lint javascript and python
	@echo

install:
	npm install
	npm run build
	if [ ! -f $(VIRTUAL_ENV)/bin/python3 ]; then python3 -m venv .; fi
	$(VIRTUAL_ENV)/bin/python3 -m pip install --upgrade -r requirements/dev.txt
	$(VIRTUAL_ENV)/bin/python3 manage.py migrate

watch:
	trap 'kill %1' KILL; \
	npm run watch & \
	$(VIRTUAL_ENV)/bin/python3 manage.py runserver 8000

server:
	$(VIRTUAL_ENV)/bin/python3 manage.py runserver 8000

test:
	$(VIRTUAL_ENV)/bin/py.test --reuse-db

test-lastfailed:
	$(VIRTUAL_ENV)/bin/py.test --reuse-db --last-failed

coverage:
	$(VIRTUAL_ENV)/bin/py.test --reuse-db --cov --cov-report=html

lint:
	EXIT_STATUS=0; \
	$(VIRTUAL_ENV)/bin/isort -rc -c $(SOURCE_DIRS) ||  EXIT_STATUS=$$?; \
	$(VIRTUAL_ENV)/bin/flake8 $(SOURCE_DIRS) --exclude migrations,settings ||  EXIT_STATUS=$$?; \
	npm run lint --silent ||  EXIT_STATUS=$$?; \
	exit $${EXIT_STATUS}
