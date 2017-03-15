all: help

VIRTUAL_ENV ?= .
SOURCE_DIRS = apps a4_advocate_europe tests

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
	if [ ! -f $(VIRTUAL_ENV)/bin/python3 ]; then python3 -m venv .; fi
	$(VIRTUAL_ENV)/bin/python3 -m pip install --upgrade -r requirements/dev.txt
	$(VIRTUAL_ENV)/bin/python3 manage.py migrate

server:
	$(VIRTUAL_ENV)/bin/python3 manage.py runserver 8000

test:
	$(VIRTUAL_ENV)/bin/py.test --reuse-db

test-lastfailed:
	$(VIRTUAL_ENV)/bin/py.test --reuse-db --last-failed

coverage:
	$(VIRTUAL_ENV)/bin/py.test --reuse-db --cov --cov-report=html
