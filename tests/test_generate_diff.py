from gendiff.scripts.gendiff import generate_diff

first_json = 'tests/fixtures/file1.json'
second_json = 'tests/fixtures/file2.json'
first_yaml = 'tests/fixtures/file1.yaml'
second_yaml = 'tests/fixtures/file2.yml'

def test_generate_diff():
    expected = '{\n - follow: False\n   host: hexlet.io\n - proxy: 123.234.53.22\n - timeout: 50\n + timeout: 20\n + verbose: True\n}'

    assert generate_diff(first_json, second_json) == expected
    assert generate_diff(first_yaml, second_yaml) == expected

