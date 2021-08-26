from gendiff.scripts.gendiff import generate_diff

first_file = 'tests/fixtures/file1.json'
second_file = 'tests/fixtures/file2.json'

def test_generate_diff():
    expected = '{\n - follow: False\n   host: hexlet.io\n - proxy: 123.234.53.22\n - timeout: 50\n + timeout: 20\n + verbose: True\n}'

    assert generate_diff(first_file, second_file) == expected

