def print_data(data, search = False):
    if len(data) > 0:
        print("id".ljust(5), "Фамилия".ljust(20), "Имя".ljust(10), "Класс".rjust(6), "Статус".rjust(6),\
           "Ряд".rjust(4), "Парта".rjust(6),\
            "Город".ljust(15), "Улица".ljust(15), "Дом".rjust(6), "Квартира".rjust(4), "Примечание".rjust(20))
        print("-"*130)
        if not search:
            del data[0]
        for item in data:
            print(item[0].ljust(5), item[1].ljust(20), item[2].ljust(10), item[3].rjust(6), item[4].rjust(6),\
           item[5].rjust(4), item[6].rjust(6),\
            item[7].ljust(15), item[8].ljust(15), item[9].rjust(6), item[10].rjust(4), item[11].rjust(20))
    else:
        print("\n")
        print("*"*120 + "\nСправочник пуст!\n" + "*"*120)
        print("\n")