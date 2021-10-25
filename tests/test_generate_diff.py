from gendiff.scripts.gendiff import generate_diff

first_json = 'tests/fixtures/file1.json'
second_json = 'tests/fixtures/file2.json'
first_yaml = 'tests/fixtures/file1.yaml'
second_yaml = 'tests/fixtures/file2.yml'
first_json_recursive = 'tests/fixtures/file1_recursive.json'
second_json_recursive = 'tests/fixtures/file2_recursive.json'


expected = '{\n - follow: False\n   host: hexlet.io\n - proxy: 123.234.53.22\n - timeout: 50\n + timeout: 20\n + verbose: True\n}'

expectes_recursive = '''{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}'''

def test_generate_diff_json():
    assert generate_diff(first_json, second_json) == expected


def test_generate_diff_yaml():
    assert generate_diff(first_yaml, second_yaml) == expected


def test_generate_diff_json_recursive():
    assert generate_diff(first_json_recursive, second_json_recursive) == expected
