#!/usr/bin/env python

'''gendiff start script'''


from gendiff.engine import generate_diff
from gendiff.cli import get_path_to_files


def main():
    first_path, second_path = get_path_to_files()
    print(generate_diff(first_path, second_path))


if __name__ == '__main__':
    main()
