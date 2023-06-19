import json


def checkout_file(file_json):
    with open(file_json, 'r+', encoding='utf-8') as info:
        if info.read() == '':
            info.write('''[]''')


def read_file(file_json):
    with open(file_json, 'r', encoding='utf-8') as info:
        notes = json.load(info)
        return notes
