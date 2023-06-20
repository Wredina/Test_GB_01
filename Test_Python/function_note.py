import json
import datetime
from time import sleep
from id import *
from search_func import *

# Заметка должна содержать идентификатор, заголовок, тело заметки и дату создания или последнего изменения заметки


def add_info_note(file, note):
    with open(file, 'w+', encoding='utf-8') as info:
        id = new_id(note)
        name_note = input(
            'напишите название заметки: ')
        text_note = input(
            'напишите содержание заметки: ')
        data_note = datetime.datetime.today()
        note_dic = {"id": id, 'name': name_note, 'body': text_note,
                    'data': data_note.strftime("%d/%m/%Y")}
        note.append(note_dic)
        # Программа должна уметь сохранять данные в файл,
        json.dump(note, info, ensure_ascii=False)

# выводить на экран выбранную запись,


def search_info_note(notes):
    user_choise = choise_func()
    if user_choise == 1:
        id = int(input('Введите ID заметки: '))
        for note in notes:
            if note['id'] == id:
                print_src_note(note)
        sleep(5)
        # делать выборку по дате
    elif user_choise == 2:
        choise_src_data = src_data()
        if choise_src_data == 1:
            date_src = input(
                'введите дату формата день/месяц/год: ')
            for note in notes:
                if note['data'] == date_src:
                    print_src_note(note)
        sleep(5)
        if choise_src_data == 2:
            min_data = input(
                'введите дату ОТ в формате день/месяц/год: ')
            max_day = input(
                'введите дату ДО в формате день/месяц/год: ')
            for note in notes:
                if datetime.datetime.strptime(max_day, '%d/%m/%Y') >= datetime.datetime.strptime(note['data'], '%d/%m/%Y') >= datetime.datetime.strptime(min_data, '%d/%m/%Y'):
                    print_src_note(note)
        sleep(5)

# выводить на экран весь список записок,


def print_all_info_note(notes):
    for note in notes:
        print_src_note(note)
    sleep(5)

# редактировать


def chenge_info_note(notes, file):
    id_src = int(input(
        'введите номер id заметки, которую хотите изменить: '))
    choise = int(input('''что меняем?
1 - имя заметки
2 - тело заметки: '''))
    if choise == 1:
        for note in notes:
            if note['id'] == id_src:
                new_name = input(
                    f'введите новый заголовок вместо "{note["name"]}": ')
                note['name'] = new_name
                new_data = datetime.datetime.today()
                note['data'] = new_data.strftime("%d/%m/%Y")
                break
    if choise == 2:
        for note in notes:
            if note['id'] == id_src:
                new_body = input(
                    f'введите новый текст заетки вместо "{note["body"]}": ')
                note['body'] = new_body
                new_data = datetime.datetime.today()
                note['data'] = new_data.strftime("%d/%m/%Y")
                break
    print('заметка изменена')
    with open(file, 'w+', encoding='utf-8') as info:
        json.dump(notes, info, ensure_ascii=False)
    sleep(2)

# удалять.


def dell_info_note(notes, file):
    dell_id = int(input(
        'введите номер id заметки, которую хотите удалить: '))
    for note in notes:
        if note['id'] == dell_id:
            notes.remove(note)
            break
    print("заметка удалена")
    with open(file, 'w+', encoding='utf-8') as info:
        json.dump(notes, info, ensure_ascii=False)
    sleep(2)
