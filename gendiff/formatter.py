from gendiff.constants import ADDED, REMOVED, SAVED, CHANGED


def formatter_rec(node):
    status = node['status']
    name = node['name']
    value = node['value']
    if status == ADDED:
        return ' + {0}: {1}\n'.format(name, value)
    elif status == REMOVED:
        return ' - {0}: {1}\n'.format(name, value)
    elif status == SAVED:
        return '   {0}: {1}\n'.format(name, value)
    elif status == CHANGED:
        old_value = node['old_value']
        return ' - {0}: {1}\n + {0}: {2}\n'.format(name, old_value, value)
