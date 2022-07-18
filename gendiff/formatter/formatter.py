from gendiff.formatter.stylish import formatter_rec
from gendiff.formatter.plain import formatter_plain


def formatter(tree, format_name):
    if format_name == 'stylish':
        return formatter_rec(tree)
    if format_name == 'plain':
        return formatter_plain(tree)
