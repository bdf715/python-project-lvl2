from gendiff.constants import ADDED, REMOVED, SAVED, CHANGED, RECURSIVE


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


def formatter_rec(node, shift=-4):
    '''
    if type(node['value']) is dict:
        res = []
        shift += 4
        res.append(' ' * shift + name + ' :{')
        res.append(formatter_rec(node['value'], shift))
        res.append(' ' * shift + '}')
        return res
    '''
    status = node['status']
    name = node['name']
    
    if status == RECURSIVE:
        res = []
        shift += 4
        res.append(' ' * shift + name + ' :{')
        res.append(list(map(lambda child: formatter_rec(child, shift), node['children'])))
        res.append(' ' * shift + '}')
        #print(res[0])
        return '\n'.join(flatten(res))
    elif status == ADDED:
        return '{2}  + {0}: {1}'.format(name, node['value'], shift * ' ')
    elif status == REMOVED:
        return '{2}  - {0}: {1}'.format(name, node['value'], shift * ' ')
    elif status == SAVED:
        return '{2}    {0}: {1}'.format(name, node['value'], shift * ' ')
    elif status == CHANGED:
        old_value = node['old_value']
        return '{3}  - {0}: {1}\n{3}  + {0}: {2}'.format(name, old_value, node['value'], shift * ' ')
