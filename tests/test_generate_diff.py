from gendiff.scripts.gendiff import get_dict_from_json, generate_diff

first = get_dict_from_json('tests/fixtures/file1.json')
second = get_dict_from_json('tests/fixtures/file2.json')

def test_generate_diff():
    expected = '{\n - follow: false\n   host: hexlet.io\n - proxy: 123.234.53.22\n - timeout: 50\n + timeout: 20\n + verbose: true\n }'

    assert generate_diff(first, second) == expected

