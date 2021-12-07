from gendiff.scripts.gendiff import generate_diff

first_json = 'tests/fixtures/file1.json'
second_json = 'tests/fixtures/file2.json'
first_yaml = 'tests/fixtures/file1.yaml'
second_yaml = 'tests/fixtures/file2.yml'


expected = '{\n - follow: False\n   host: hexlet.io\n - proxy: 123.234.53.22\n - timeout: 50\n + timeout: 20\n + verbose: True\n}'

'''
def test_generate_diff_json():
    assert generate_diff(first_json, second_json) == expected


def test_generate_diff_yaml():
    assert generate_diff(first_yaml, second_yaml) == expected
'''

def test_generate_diff_nested():
    first_path = 'tests/fixtures/file1_nested.yaml'
    second_path= 'tests/fixtures/file2_nested.yaml'
    output = open('tests/fixtures/output_nested_format').read().rstrip()
    assert generate_diff(first_path, second_path) == output
