from gendiff.parser import get_parsed_json
from gendiff.cli import get_path_to_files
from gendiff.formatter import formatter


def key_removed(key, first_keys, second_keys):
    return key in first_keys - second_keys


def key_added(key, first_keys, second_keys):
    return key in second_keys - first_keys


def key_keept(key, first_keys, second_keys):
    return key in first_keys & second_keys


def get_total_keys(first_keys, second_keys):
    return first_keys | second_keys


def generate_diff(first_path, second_path):
    first_parsed, second_parsed = get_parsed_json(first_path, second_path)
    first_keys = set(first_parsed.keys())
    second_keys = set(second_parsed.keys())
    total_keys = list(get_total_keys(first_keys, second_keys))
    total_keys.sort()
    result = '{\n'
    for key in total_keys:
        if key_removed(key, first_keys, second_keys):
            result += formatter('-', key, first_parsed[key])
        elif key_added(key, first_keys, second_keys):
            result += formatter('+', key, second_parsed[key])
        elif key_keept(key, first_keys, second_keys)\
                and first_parsed[key] == second_parsed[key]:
            result += formatter(' ', key, first_parsed[key])
        else:
            result += formatter('-', key, first_parsed[key])
            result += formatter('+', key, second_parsed[key])
    result += '}'
    return result
