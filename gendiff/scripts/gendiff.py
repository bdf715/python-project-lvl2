#!/usr/bin/env python

'''gendiff start script'''


from gendiff.engine import generate_diff
from gendiff.cli import get_path_to_files
from pprint import pprint


def main():
    first_path, second_path = get_path_to_files()
    pprint(generate_diff(first_path, second_path))


if __name__ == '__main__':
    main()
