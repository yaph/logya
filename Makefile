# Suppress all recipe lines from being printed to the terminal, for cleaner output
.SILENT:

# Suppress "Entering/Leaving directory" messages for cleaner output
MAKEFLAGS += --no-print-directory

.PHONY: help clean clean-build clean-cache clean-sites clean-test docs logo requirements

# Help
help:
	@echo "clean          - remove all build, test, coverage and Python artifacts"
	@echo "clean-build    - remove build artifacts"
	@echo "clean-cache    - remove Python cache files and temp files"
	@echo "clean-sites    - remove deploy directories from starter sites"
	@echo "clean-test     - remove test and coverage artifacts"
	@echo "docs           - generate HTML documentation"
	@echo "logo           - generate favicons and small logos for docs"
	@echo "requirements   - update requirements.txt and upgrade packages"

# Clean
clean: clean-build clean-cache clean-sites clean-test

clean-build:
	rm -rf build/ dist/ .eggs/ *.egg-info

clean-cache:
	find . \( \
		-type d \( \
			-name '__pycache__' -o \
			-name '.mypy_cache' -o \
			-name '.pytest_cache' -o \
			-name '.ruff_cache' \
		\) -prune -exec rm -rf {} + \
		-o \
		-type f \( \
			-name '*.pyc' -o \
			-name '*.pyo' -o \
			-name '*~' \
		\) -exec rm -f {} + \
	\)

clean-sites:
	find logya/sites/ -type d -name public -exec rm -rf {} +

clean-test:
	rm -rf .coverage* htmlcov/ .tox/ .nox/ t/

# Documentation
docs:
	hatch run logya gen -d logya/sites/docs

# Logo / favicon generation
logo:
	convert images/wordmark.svg -define icon:auto-resize=64,48,32,16 logya/sites/docs/static/favicon.ico
	convert images/logo.svg -resize x40 -transparent white logya/sites/docs/static/img/logya-small.png

	cp logya/sites/docs/static/favicon.ico logya/sites/base/static/favicon.ico
	cp logya/sites/docs/static/favicon.ico logya/sites/i18n/static/favicon.ico

	cp logya/sites/docs/static/img/logya-small.png logya/sites/base/static/img/logya-small.png

# Requirements management
requirements:
	pip freeze --local > requirements.txt
	sed -i 's/==/>=/g' requirements.txt
	pip install --upgrade -r requirements.txt
	# Keep base requirements only
	grep -f requirements-base.txt requirements.txt > requirements.tmp
	mv requirements.tmp requirements.txt
