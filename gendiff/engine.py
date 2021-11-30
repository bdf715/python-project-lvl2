from gendiff.parser import get_parsed
from gendiff.formatter import formatter_rec
from gendiff.constants import ADDED, REMOVED, SAVED, CHANGED, RECURSIVE


def make_diff(first, second):
    result = []
    keys = list(first.keys() | second.keys())
    keys.sort()
    for key in keys:
        if key not in first.keys():
            value = second[key]
            status = ADDED
        elif key not in second.keys():
            value = first[key]
            status = REMOVED
        elif first[key] == second[key]:
            value = first[key]
            status = SAVED
        elif type(first[key]) is dict and type(second[key]) is dict:
            children = make_diff(first[key], second[key])
            status = RECURSIVE
            result.append(
                {
                    'name': key,
                    'children': children,
                    'status': status
                })
            continue
        else:
            value = second[key]
            old_value = first[key]
            status = CHANGED
            result.append(
                {
                    'name': key,
                    'value': value,
                    'old_value': old_value,
                    'status': status
                })
            continue
        result.append(
            {
                'name': key,
                'value': value,
                'status': status
            })
    return result


def make_result(node):
    if node['status'] != RECURSIVE:
        return formatter_rec(node)
    children = node['children']
    return ''.join(map(make_result, children))


def generate_diff(first_path, second_path):
    first_parsed, second_parsed = get_parsed(first_path, second_path)
    tree = {
        'name': '/',
        'children': make_diff(first_parsed, second_parsed),
        'status': RECURSIVE
    }
    result = '{\n'
    result += make_result(tree)
    result += '}'
    return result
