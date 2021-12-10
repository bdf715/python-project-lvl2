install:
	poetry install
gendiff:
	poetry run gendiff -h
gentest:
	poetry run gendiff tests/fixtures/file1.json tests/fixtures/file2.json
gentest1:
	poetry run gendiff tests/fixtures/file1_recursive.yaml tests/fixtures/file2_recursive.yaml
gentest2:
	poetry run gendiff tests/fixtures/file1_simple.json tests/fixtures/file2_simple.json
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip install --user dist/*.whl
make lint:
	poetry run flake8 gendiff
make test:
	poetry run pytest
make test-detail:
	poetry run pytest -vv
selfcheck:
	poetry check

check:  selfcheck test lint

build:  check
	poetry build
test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml
.PHONY: install test lint selfcheck check build gendiff
