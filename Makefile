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
	@py.test -q tests

lint:
	@flake8 src/statici18n tests

coverage:
	@py.test --cov=src/statici18n --cov-report=html

clean:
	@rm -fr build dist

.PHONY: build