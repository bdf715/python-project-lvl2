install:
	poetry install
gendiff:
	poetry run gendiff -h
gentest:
	poetry run gendiff tests/fixtures/file1_simple.yaml tests/fixtures/file2_simple.yaml
gentest1:
	poetry run gendiff tests/fixtures/file1_nested.json tests/fixtures/file2_nested.json
gentest2:
	poetry run gendiff tests/fixtures/file1_nested.yaml tests/fixtures/file2_nested.yaml
gentest3:
	poetry run gendiff tests/fixtures/file1_nested.yaml tests/fixtures/file2_nested.yaml -f plain
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip install --user dist/*.whl
lint:
	poetry run flake8 gendiff
test:
	poetry run pytest
test-detail:
	poetry run pytest -vv
selfcheck:
	poetry check

check:  selfcheck test lint

build:  check
	poetry build
test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml
.PHONY: install test lint selfcheck check build gendiff test-detail gentest
