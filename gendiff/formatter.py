from gendiff.constants import ADDED, REMOVED, SAVED, CHANGED


def formatter_rec(key, value, status, old_value=None):
    if status == ADDED:
        return ' + {0}: {1}\n'.format(key, value)
    elif status == REMOVED:
        return ' - {0}: {1}\n'.format(key, value)
    elif status == SAVED:
        return '   {0}: {1}\n'.format(key, value)
    elif status == CHANGED:
        return ' - {0}: {1}\n + {0}: {2}\n'.format(key, old_value, value)
