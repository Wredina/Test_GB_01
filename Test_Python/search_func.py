import datetime
from time import sleep


def choise_func():
    print('''возможен поиск по данным:
  1 - id
  2 - дата
  3 - название заметки
  4 - сожержит слово/словосочетание''')
    try:
        user_info = int(input("введите номер команды: "))
        if type(user_info) == int:
            return user_info
    except ValueError:
        user_info = 6
        return user_info


def print_src_note(note):
    print(f'''ID {note["id"]}
Заголовок: {note["name"]}
Описание: {note["body"]}
Дата: {note["data"]}''')
    print("---------------")
