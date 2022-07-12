import json
import yaml


def is_yaml(path):
    return path.endswith('yaml') or path.endswith('yml')


def is_json(path):
    return path.endswith('json')

def get_parsed(path):
    if is_json(path):
        return json.load(open(path))
    elif is_yaml(path):
        return yaml.safe_load(open(path))
    return first, second
