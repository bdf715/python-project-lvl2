from gendiff.constants import ADDED, REMOVED, SAVED, CHANGED, RECURSIVE


PLAIN_ADDED = "Property '{0}' was added with value: {1}"
PLAIN_REMOVED = "Property '{0}' was removed"
PLAIN_CHANGED = "Property '{0}' was updated. From {1} to {2}"


def flatten(tree):
    result = []

    def walk(subtree):
        for item in subtree:
            if isinstance(item, list):
                walk(item)
            else:
                result.append(item)
    walk(tree)
    return result


def final_format(value):
    if value is True:
        return 'true'
    elif value is False:
        return 'false'
    elif value is None:
        return 'null'
    elif isinstance(value, dict):
        return "[complex value]"
    else:
        return "'" + str(value) + "'"


def formatter_plain(node, path=''):
    status = node['status']
    name = node['name']
    path += '.' + name if name != '/' else path
    path = path.lstrip('.')
    if status == RECURSIVE:
        res = list(map(lambda child: formatter_plain(child, path),
                       node['children']))
        return '\n'.join(filter(lambda x: x != '', flatten(res)))
    elif status == ADDED:
        return PLAIN_ADDED.format(path, final_format(node['value']))
    elif status == REMOVED:
        return PLAIN_REMOVED.format(path)
    elif status == SAVED:
        return ''
    elif status == CHANGED:
        return PLAIN_CHANGED.format(path, final_format(node['old_value']),
                                    final_format(node['value']))
