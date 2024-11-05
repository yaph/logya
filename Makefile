.PHONY: clean-cache clean-build docs clean

help:
	@echo "clean - remove all build, test, coverage and Python artifacts"
	@echo "clean-build - remove build artifacts"
	@echo "clean-cache - remove Python file artifacts"
	@echo "clean-sites - remove deploy directory from starter site"
	@echo "clean-test - remove test and coverage artifacts"
	@echo "docs - generate HTML documentation"

clean: clean-build clean-cache clean-sites clean-test

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	rm -fr *.egg-info

clean-cache:
	find . -name '__pycache__' -type d -exec rm -fr {} +
	find . -name '.pytest_cache' -type d -exec rm -fr {} +
	find . -name '.ruff_cache' -type d -exec rm -fr {} +
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

clean-sites:
	find logya/sites/ -type d -name public -exec rm -rf {} +

clean-test:
	rm -fr t/
	rm -f .coverage
	rm -fr htmlcov/

docs:
	hatch run logya gen -d logya/sites/docs

logo:
	convert images/wordmark.svg -define icon:auto-resize=64,48,32,16 logya/sites/docs/static/favicon.ico
	convert images/logo.svg -resize x40 -transparent white logya/sites/docs/static/img/logya-small.png

	cp logya/sites/docs/static/favicon.ico logya/sites/base/static/favicon.ico
	cp logya/sites/docs/static/favicon.ico logya/sites/i18n/static/favicon.ico

	cp logya/sites/docs/static/img/logya-small.png logya/sites/base/static/img/logya-small.png

# Upgrade packages and requirements files
requirements:
	pip freeze --local > requirements.txt
	sed -i 's/==/>=/g' requirements.txt
	pip install -r requirements.txt --upgrade
	pip freeze --local > requirements.txt

	rm -f requirements.tmp
	grep -f requirements-base.txt requirements.txt > requirements.tmp
	mv requirements.tmp requirements.txt
