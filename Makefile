install:
	poetry install
gendiff:
	poetry run gendiff -h
gentest:
	poetry run gendiff tests/fixtures/file1.json tests/fixtures/file2.json
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip install --user dist/*.whl
make lint:
	poetry run flake8 gendiff
make test:
	poetry run pytest
selfcheck:
	poetry check

check:  selfcheck test lint

build:  check
	poetry build

.PHONY: install test lint selfcheck check build gendiff
