import datetime
from time import sleep
from datetime import date
from id import *
import json

# добавление заметки


def add_info_note(file, note):
    with open(file, 'a', encoding='UTF-8') as info:
        id = len(note) + 1
        name_note = input('напишите название заметки: ')
        text_note = input(
            'напишите содержание заметки: ')
        data_note = datetime.datetime.today()
        note_dic = {"id": id, 'name': name_note, 'body': text_note,
                    'data': data_note.strftime("%m/%d/%Y")}
        note.append(note_dic)
        json.dump(note, info)


# def search_info_note():

# def print_all_info_note():


# def chenge_info_note():

# def dell_info_note():
