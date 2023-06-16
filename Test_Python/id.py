import json


def search_id(file, note):
    id_num = 0
    with open(file, 'a', encoding='UTF-8') as id_search:
        if note == 0:
            return id_num
        else:
            for el in note:
                if el['id']:
                    id_num += 1
            return id_num
