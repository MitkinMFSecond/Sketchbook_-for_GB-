import time
from datetime import datetime


def read_file():
    with open('notes.csv', 'r', encoding='utf-8') as f:
        sb = [tuple(my_str.rstrip('\n').split(';'))
              for my_str in f if my_str != '\n']
    print('Файл загружен')
    return sb

def notes_to_screen(my_list: list):
    print_table_head()
    for note in my_list:
        print(
            f'{note[0]} |{get_note_date(note[1])} | {get_note_date(note[2])} | {note[3][:20]} | {note[4][:20]} |')
    print('\n')
    
def note_to_screen(note : tuple):
    print('id |   Дата посл.изм.   |    Дата созд.   |')
    print('______________________________________________________')
    print(
            f'{note[0]} |{get_note_date(note[1])} | {get_note_date(note[2])} |')
    print('Заголовок:')
    print(note[3])
    print('Текст записи:')
    print(note[4], '\n')

def get_note_date(my_date):
    return datetime.fromtimestamp(int(my_date))

def id_input():
    id = (input('Введите id записи\n')).strip()
    return id
    
def head_input():
    head = (input('Введите заголовок записи\n')).strip()
    if len(head) == 0:
        head = "none"
    else:
        head = head.replace(";", ":")
    return head

def text_input():
    text = input('Введите текст записи\n').strip()
    if len(text) == 0:
        text = "none"
    else:
        text = text.replace(";", ":")
    return text

def cmd_input():
    return input('Введите команду: ').strip()

def main_menu():
    print('''Главное меню:
1 - Вывести все записи в сокращенном виде
2 - Вывести запись полностью по id 
3 - Вывести последнюю измененную запись
4 - Добавление записи
5 - Редактирование записи
6 - Удаление записи 
7 - Сохранение файла
0 - Выход''')

def print_table_head():
    print('id |   Дата посл.изм.   |    Дата созд.   | Заголовок | Текст заметки')
    print('______________________________________________________')
    
    
    # current_datetime = datetime.now()
    
    # print(current_datetime)
    # print(round(time.time()))
    # print (datetime.fromtimestamp(round(time.time())))


def out_file(my_list: list):
    with open('notes.csv', 'w', encoding='utf-8') as file:
        for elem in my_list:
            file.write(f'{elem[0]};{elem[1]};{elem[2]};{elem[3]};{elem[4]}\n')
        print('Файл сохранен')
    return

def wrong_input():
    print('Неверный ввод')

def wrong_id():
    print('id не существует')
    
def notes_empty():
    print('Записей нет')
