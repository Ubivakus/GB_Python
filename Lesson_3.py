# 1. Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9,
# ответ: 12

# some_list = [2, 3, 5, 9, 3]
# sum_odd_elements = 0
# for i in range(len(some_list)): # если я ставлю в in some_list, то почему-то не работает
#   if i % 2 != 0:
#     sum_odd_elements += some_list[i]
#   i += 1
# print(sum_odd_elements)


# _______________________________________
# 2. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# some_list = [2, 3, 4, 5, 6, 7, 6]
# length = len(some_list)
# new_list = []
# for i in range(int((length + 1) / 2)):
#   value_multiply = some_list[i] * some_list[length - 1 - i]
#   new_list.append(value_multiply)
# print(f'Задан начальный список: {some_list}')
# print(f'Произведение пар элементов списка равно: {new_list}')


# _______________________________________
# 3. Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между 
# максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# some_list = [1.1, 1.2, 3.1, 5, 10.01]
# min = 1
# max = 0
# for i in some_list:
#     if '.' in str(i):
#         dr = str(i).split('.')[1]
#         if float('0.' + dr) > max:
#             max = float('0.' + dr)
#         elif float('0.' + dr) < min:
#             min = float('0.' + dr)
# print(max - min)


# _______________________________________
# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# a = int(input())
# b = ''
# while a != 0:
#   b = str(a % 2) + b
#   a //= 2
# print(b)