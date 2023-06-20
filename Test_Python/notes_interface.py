import os
from function_note import *
from read_file_json import *


def user_interface():
    file_json = 'D:\программирование\Обучение_тестировщик\Test_GB_01\Test_Python\\note.json'
    checkout_file(file_json)
    notes = read_file(file_json)
    os.system('cls')
    print('''1 - создать заметку
2 - поиск заметки
3 - вывод всех заметок
4 - редактирование заметки
5 - удаление заметки 
6 - выход''')

    def try_ex():
        try:
            user_input = int(
                input("введите номер операции: "))
            if type(user_input) == int:
                return user_input
        except ValueError:
            user_input = 7
            return user_input

    user_input = try_ex()
    while user_input != 6:
        if user_input == 1:
            add_info_note(file_json, notes)
        elif user_input == 2:
            search_info_note(notes)
        elif user_input == 3:
            print_all_info_note(notes)
        elif user_input == 4:
            chenge_info_note(notes, file_json)
        elif user_input == 5:
            dell_info_note(notes, file_json)
        else:
            print('попробуйте ещё раз')
            sleep(2)
        os.system('cls')
        print('''1 - создать заметку
2 - поиск заметки
3 - вывод всех заметок
4 - редактирование заметки
5 - удаление заметки
6 - выход''')
        user_input = try_ex()
