from gendiff.scripts.gendiff import generate_diff


def test_generate_diff():
    first_path = 'tests/fixtures/file1_simple.yaml'
    second_path = 'tests/fixtures/file2_simple.yaml'
    output = open('tests/fixtures/output_simple').read().rstrip()
    assert generate_diff(first_path, second_path) == output


def test_generate_diff_nested():
    first_path = 'tests/fixtures/file1_nested.json'
    second_path= 'tests/fixtures/file2_nested.json'
    output = open('tests/fixtures/output_nested').read().rstrip()
    assert generate_diff(first_path, second_path) == output


def test_generate_diff_plain():
    first_path = 'tests/fixtures/file1_nested.json'
    second_path= 'tests/fixtures/file2_nested.json'
    output = open('tests/fixtures/output_plain').read().rstrip()
    assert generate_diff(first_path, second_path) == output
