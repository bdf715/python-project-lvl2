import json
import yaml


def is_yaml(path):
    return path.endswith('yaml') or path.endswith('yml')


def is_json(path):
    return path.endswith('json')


def get_parsed_json(first_path, second_path):
    if is_json(first_path) and is_json(second_path):
        first = json.load(open(first_path))
        second = json.load(open(second_path))
    if is_yaml(first_path) and is_yaml(second_path):
        first = yaml.safe_load(open(first_path))
        second = yaml.safe_load(open(second_path))
    return first, second
