import json


def get_parsed_json(first_path, second_path):
    return json.load(open(first_path)), json.load(open(second_path))
