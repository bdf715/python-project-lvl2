.PHONY: gendiff
install:
	poetry install
gendiff:
	poetry run gendiff -h
gentest:
	poetry run gendiff tests/fixtures/file1.json tests/fixtures/file2.json
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip install --user dist/*.whl
make lint:
	poetry run flake8 gendiff
make test:
	poetry run pytest
