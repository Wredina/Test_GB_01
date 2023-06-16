import json


def read_file(file_json):
    with open(file_json, 'r', encoding='UTF-8') as info:
            notes = json.load(info)
            return notes
