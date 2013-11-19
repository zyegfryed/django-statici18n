build:
	@python setup.py sdist
	@python setup.py bdist_wheel

upload-test: build
	@python setup.py register -r test
	@python setup.py sdist upload -r test
	@python setup.py bdist_wheel upload -r test

upload: build
	@python setup.py register -r pypi
	@python setup.py sdist upload -r pypi
	@python setup.py bdist_wheel upload -r pypi

test:
	@py.test -q tests || exit 1

lint:
	@flake8 src/statici18n tests

coverage:
	@py.test -q tests --cov=src/statici18n --cov-report=html || exit 1

clean:
	@rm -fr build dist

.PHONY: build