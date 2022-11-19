from push_data import *
from read_data import *
from print_data import *
from search_data import *


def greeting():
    print("Добро пожаловать в информационную систему по работе с учениками!")

def start():
    print("Доступные операции:\n\
    1 - Получить информацию о учениках\n\
    2 - Добавить ученика\n\
    3 - Поиск ученика\n\
    4 - Выход")
    ch = input("Выберите пункт меню: ")
    while True:
        if ch == '1':
            data = read_data()
            print_data(data)
            start()
        elif ch == '2':
            push_data()
            start()
        elif ch == '3':
            info = input("Введите данные для поиска: ")
            data = read_data()
            item = search_data(info, data)
            if item != None:
                print_data(item, True)
            else:
                print("Данные не обнаружены")                
            start()
        elif ch == '4':
            print("Спасибо, до свидания!")
            sys.exit
        else:
            print("Введите корректную цифру!")
            start()