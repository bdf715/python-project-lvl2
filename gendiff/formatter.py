def formatter(*args):
    sign, key, value = args
    return ' {0} {1}: {2}\n'.format(sign, key, value)
