.PHONY: clean-pyc clean-build docs clean install uninstall

help:
	@echo "clean - remove all build, test, coverage and Python artifacts"
	@echo "clean-build - remove build artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "clean-sites - remove deploy directory from starter site"
	@echo "clean-test - remove test and coverage artifacts"
	@echo "lint - check style with flake8"
	@echo "test - run tests quickly with the default Python"
	@echo "test-all - run tests on every Python version with tox"
	@echo "coverage - check code coverage quickly with the default Python"
	@echo "docs - generate Sphinx HTML documentation, including API docs"
	@echo "docs-release - generate and upload docs to PyPI"
	@echo "release - package and upload a release"
	@echo "dist - package"

clean: clean-build clean-pyc clean-sites clean-test

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	rm -fr *.egg-info

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-sites:
	find logya/sites/ -type d -name deploy -exec rm -rf {} +

clean-test:
	rm -fr t/
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/

install: clean
	python setup.py install

uninstall:
	pip uninstall -y logya

reinstall: uninstall install

lint:
	flake8 logya tests

test:
	python setup.py test

coverage:
	coverage run --source logya setup.py test
	coverage report -m

docs:
	rm -f docs/logya.rst
	rm -f docs/modules.rst
	sphinx-apidoc -o docs/ logya
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	firefox docs/_build/html/index.html

dist: clean
	python setup.py sdist
	python setup.py bdist_wheel
	ls -l dist

# Call example: make release version=4.7.1
release: dist
	git tag -a $(version) -m 'Create version $(version)'
	git push --tags
	twine upload dist/*
