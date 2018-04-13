# Some useful commands.

.venv:
	$(shell which python3) -m venv venv
	touch .venv

.install-deps:
	venv/bin/pip install -Ur requirements-dev.txt
	touch .install-deps

.develop:
	venv/bin/pip install -U pip
	venv/bin/pip install -e . --process-dependency-links
	touch .develop

.setup:
	venv/bin/python setup.py install

.source_env:
	source venv/bin/activate

flake: .venv .install-deps .develop
	venv/bin/flake8 simple_search

install: .venv .install-deps .develop .setup

start: install .source_env
	python wsgi.py

clean:
	rm -rf `find . -name __pycache__`
	rm -f `find . -type f -name '*.py[co]' `
	rm -f `find . -type f -name '*~' `
	rm -f `find . -type f -name '.*~' `
	rm -f `find . -type f -name '@*' `
	rm -f `find . -type f -name '#*#' `
	rm -f `find . -type f -name '*.orig' `
	rm -f `find . -type f -name '*.rej' `
	python setup.py clean
	rm -rf .cache
	rm -f .coverage
	rm -rf coverage

.PHONY: all install flake
