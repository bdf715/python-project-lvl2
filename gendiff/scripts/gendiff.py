#!/usr/bin/env python

'''gendiff start script'''


import argparse
import json


def get_dict_from_json(file_path):
    return json.load(open(file_path))


def generate_diff(first_file, second_file):
    first_file_keys = set(first_file.keys())
    second_file_keys = set(second_file.keys())
    unique_keys_in_first = first_file_keys - second_file_keys
    unique_keys_in_second = second_file_keys - first_file_keys
    keys_in_both_files = first_file_keys & second_file_keys
    total_keys = list(first_file_keys | second_file_keys)
    total_keys.sort()
    result = "{\n"
    for key in total_keys:
        if key in unique_keys_in_first:
            key_string = " - {0}: {1}\n".format(key, first_file[key])
        elif key in unique_keys_in_second:
            key_string = " + {0}: {1}\n".format(key, second_file[key])
        elif key in keys_in_both_files and first_file[key] == second_file[key]:
            key_string = "   {0}: {1}\n".format(key, first_file[key])
        else:
            key_string = "" \
                         " - {0}: {1}\n" \
                         " + {2}: {3}\n" \
                         "".format(key, first_file[key], key, second_file[key])
        result += key_string
    result += "}"
    return result


def main():
    parser = argparse.ArgumentParser(description="Generate diff")
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f", "--format", help="set format of output")
    args = parser.parse_args()
    first_file = get_dict_from_json(args.first_file)
    second_file = get_dict_from_json(args.second_file)
    print(first_file, second_file, sep = '\n')
    print(generate_diff(first_file, second_file))

if __name__ == '__main__':
    main()
