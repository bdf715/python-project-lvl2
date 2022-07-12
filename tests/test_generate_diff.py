from gendiff.scripts.gendiff import generate_diff


def test_generate_diff_simple():
    first_path = 'tests/fixtures/file1_simple.yaml'
    second_path = 'tests/fixtures/file2_simple.yaml'
    output_simple = open('tests/fixtures/output_simple').read().rstrip()
    assert generate_diff(first_path, second_path) == output_simple


def test_generate_diff_nested_json():
    first_path = 'tests/fixtures/file1_nested.json'
    second_path= 'tests/fixtures/file2_nested.json'
    output_nested = open('tests/fixtures/output_nested').read().rstrip()
    assert generate_diff(first_path, second_path) == output_nested


def test_generate_diff_nested_yaml():
    first_path = 'tests/fixtures/file1_nested.yaml'
    second_path= 'tests/fixtures/file2_nested.yaml'
    output_nested = open('tests/fixtures/output_nested').read().rstrip()
    assert generate_diff(first_path, second_path) == output_nested

'''
def test_generate_diff_plain():
    first_path = 'tests/fixtures/file1_nested.json'
    second_path= 'tests/fixtures/file2_nested.json'
    output = open('tests/fixtures/output_plain').read().rstrip()
    assert generate_diff(first_path, second_path) == output
'''
