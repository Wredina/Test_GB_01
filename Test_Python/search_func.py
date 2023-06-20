import datetime
from time import sleep


def choise_func():
    print('''возможен поиск по данным:
  1 - id
  2 - дата''')
    user_info = int(input("введите номер команды: "))
    return user_info


def src_data():
    print('''команды:
1 - вывести все заметки за определённую дату
2 - вывести все заметки за период включительно''')
    choise = int(input("введите номер операции: "))
    return choise


def print_src_note(note):
    print(f'''ID {note["id"]}
Заголовок: {note["name"]}
Описание: {note["body"]}
Дата: {note["data"]}''')
    print("---------------")
