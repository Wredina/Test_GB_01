import datetime
from time import sleep
from datetime import date
import json
from search_func import *
import os
from id import *


# Программа должна уметь сохранять данные в файл,
# уметь читать данные из файла,
# делать выборку по дате,
# выводить на экран выбранную запись,
# выводить на экран весь список записок,
# редактировать
# удалять.


# Заметка должна содержать идентификатор, заголовок, тело заметки и дату создания или последнего изменения заметки
def add_info_note(file, note):
    with open(file, 'w+', encoding='utf-8') as info:
        id = new_id(note)
        name_note = input('напишите название заметки: ')
        text_note = input(
            'напишите содержание заметки: ')
        data_note = datetime.datetime.today()
        note_dic = {"id": id, 'name': name_note, 'body': text_note,
                    'data': data_note.strftime("%d/%m/%Y")}
        note.append(note_dic)
        json.dump(note, info, ensure_ascii=False)


def search_info_note(notes):
    user_choise = choise_func()
    if user_choise == 1:
        id = int(input('Введите ID заметки: '))
        for note in notes:
            if note['id'] == id:
                print_src_note(note)
        sleep(5)
    elif user_choise == 2:
        date_src = input(
            'введите дату формата день/месяц/год: ')
        for note in notes:
            if note['data'] == date_src:
                print_src_note(note)
        sleep(5)
    elif user_choise == 3:
        name_src = input('введите название заметки: ')
        for note in notes:
            if note['name'] == name_src:
                print_src_note(note)
        sleep(5)
    elif user_choise == 4:
        src_text = input(
            'введите слово/словосочетание: ')
        for note in notes:
            if src_text in note['body']:
                print_src_note(note)
        sleep(5)

def print_all_info_note(notes):


# def chenge_info_note():

# def dell_info_note():
