from gendiff.formatter.stylish import formatter_rec


def formatter(tree, format_name):
    if format_name == 'stylish':
        return formatter_rec(tree)
