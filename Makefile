build:
	@python setup.py sdist
	@python setup.py bdist_wheel

upload: build
	@twine upload dist/*

test:
	@pytest -q tests || exit 1

lint:
	@flake8 src/statici18n tests

coverage:
	@pytest -q tests --cov=src/statici18n --cov-report=html || exit 1

clean:
	@rm -fr build dist

.PHONY: build upload test lint coverage clean
