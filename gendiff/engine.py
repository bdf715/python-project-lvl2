from gendiff.parser import get_parsed
from gendiff.formatter import formatter


def key_removed(key, first_keys, second_keys):
    return key in first_keys - second_keys


def key_added(key, first_keys, second_keys):
    return key in second_keys - first_keys


def key_kept(key, first_keys, second_keys):
    return key in first_keys & second_keys


def get_total_keys(first_keys, second_keys):
    return first_keys | second_keys


def mkdir(name, children=[], meta=''):
    return {
            'name': name,
            'children': children,
            'type': 'dir',
            'meta': meta
            }


def mkfile(name, value, sign):
    return {
            'name': name,
            'value': value,
            'sign': sign
            }


def generate_diff(first_path, second_path):
    first_parsed, second_parsed = get_parsed(first_path, second_path)
    first_keys = set(first_parsed.keys())
    second_keys = set(second_parsed.keys())
    total_keys = list(get_total_keys(first_keys, second_keys))
    total_keys.sort()
    result = []
    for key in total_keys:
        if key_removed(key, first_keys, second_keys):
            result.append(mkfile(key, first_parsed[key], '-'))
        elif key_added(key, first_keys, second_keys):
            result.append(mkfile(key, second_parsed[key], '+'))
        elif key_kept(key, first_keys, second_keys)\
                and first_parsed[key] == second_parsed[key]:
            result.append(mkfile(key, first_parsed[key], ' '))
        else:
            result.append(mkfile(key, first_parsed[key], '-'))
            result.append(mkfile(key, second_parsed[key], '+'))
    return formatter(result)
