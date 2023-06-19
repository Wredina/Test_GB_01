import datetime
from time import sleep
from datetime import date
import json


# Программа должна уметь сохранять данные в файл,
# уметь читать данные из файла,
# делать выборку по дате,
# выводить на экран выбранную запись,
# выводить на экран весь список записок,
# редактировать
# удалять.


def add_info_note(file, note):
    with open(file, 'w+', encoding='UTF-8') as info:
        id = len(note) + 1
        name_note = input('напишите название заметки: ')
        text_note = input(
            'напишите содержание заметки: ')
        data_note = datetime.datetime.today()
        note_dic = {"id": id, 'name': name_note, 'body': text_note,
                    'data': data_note.strftime("%m/%d/%Y")}
        note.append(note_dic)
        json.dump(note, info)


# def search_info_note(notes):
#     id = int(input('Введите ID заметки: '))
#     note = [note for note in notes if note['id'] == id]
#     if not notes:
#         print("заметок не найдено")
#     else:
#         for note in notes:
#             print(f'ID: {note["id"]}')
#             print(f'Заголовок: {note["name"]}')
#             print(f'Тело заметки: {note["body"]}')
#             print(f'Дата/время: {note["data"]}')

# def print_all_info_note():


# def chenge_info_note():

# def dell_info_note():
