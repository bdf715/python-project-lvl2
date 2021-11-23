from gendiff.parser import get_parsed
from gendiff.formatter import formatter


def key_added(key, first, second):
    return key not in first and key in second


def key_removed(key, first, second):
    return key in first and key not in second


def key_changed(key, first, second):
    return key in first and key in second and first[key] != second[key]


def key_saved(key, first, second):
    return key in first and key in second and first[key] == second[key]


def key_recursive(key, first, second):
    return key in first and key in second\
        and type(first[key]) is dict and type(second[key]) is dict


def get_total_keys(first, second):
    total_keys = list(first.keys() | second.keys())
    total_keys.sort()
    return total_keys


def mknode(name, children, status):
    return {
            'name': name,
            'children': children,
            'status': status
            }


def mkleaf(name, value, status, old_value=''):
    return {
            'name': name,
            'value': value,
            'old_value': old_value,
            'status': status
            }


def make_diff(first, second):
    result = []
    keys = get_total_keys(first, second)
    for key in keys:
        if key_recursive(key, first, second):
            result.append(mknode(key, make_diff(first[key], second[key]), 'rec'))
        elif key_added(key, first, second):
            result.append(mkleaf(key, second[key], 'add'))
        elif key_removed(key, first, second):
            result.append(mkleaf(key, first[key], 'del'))
        elif key_changed(key, first, second):
            result.append(mkleaf(key, second[key], 'chg', first[key]))
        elif key_saved(key, first, second):
            result.append(mkleaf(key, first[key], 'sav'))
    return result


def generate_diff(first_path, second_path):
    first_parsed, second_parsed = get_parsed(first_path, second_path)
    return mknode('/', make_diff(first_parsed, second_parsed), 'rec')
