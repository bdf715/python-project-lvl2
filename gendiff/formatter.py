from gendiff.constants import ADDED, REMOVED, SAVED, CHANGED, RECURSIVE


def formatter(tree, format_name):
    if format_name == 'stylish':
        return formatter_rec(tree)


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


def format_dict(data, shift):
    if type(data) is dict:
        res = []
        res.append('{')
        shift += 4
        for key, value in data.items():
            res.append(' ' * shift + str(key) + ': ' + str(format_dict(value,
                                                                       shift)))
        res.append(' ' * (shift - 4) + '}')
        result = '\n'.join(flatten(res))
    else:
        result = final_format(data)
    return result


def final_format(value):
    if value is True:
        return 'true'
    elif value is False:
        return 'false'
    elif value is None:
        return 'null'
    else:
        return value


def formatter_rec(node, shift=-4):
    status = node['status']
    name = node['name']
    if status == RECURSIVE:
        res = []
        shift += 4
        res.append(' ' * shift + name + ': {' if name != '/' else '{')
        res.append(list(map(lambda child: formatter_rec(child, shift),
                            node['children'])))
        res.append(' ' * shift + '}')
        return '\n'.join(flatten(res))
    elif status == ADDED:
        return '{2}  + {0}: {1}'.format(name, format_dict(node['value'],
                                        shift + 4), shift * ' ')
    elif status == REMOVED:
        return '{2}  - {0}: {1}'.format(name, format_dict(node['value'],
                                        shift + 4), shift * ' ')
    elif status == SAVED:
        return '{2}    {0}: {1}'.format(name, format_dict(node['value'],
                                        shift + 4), shift * ' ')
    elif status == CHANGED:
        old_value = node['old_value']
        output = '{3}  - {0}: {1}\n{3}  + {0}: {2}'
        return output.format(name,
                             format_dict(old_value, shift + 4),
                             format_dict(node['value'], shift + 4),
                             shift * ' ')
