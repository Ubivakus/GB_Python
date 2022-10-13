# 1. Напишите программу, которая принимает на вход 
# вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# Придумал только как разбить строку на элементы,
# привести их к интам и сложить, "." пропускать.
# Как это сделать изначально с флоатами - не придумал.

# number = input('Введите вещественное число: ')
# sum_of_digits = 0
# for i in range(len(number)):
#   if number[i] == '.':
#     continue
#   else:
#     sum_of_digits += int(number[i])
# print(f'Сумма цифр числа {number} равна {sum_of_digits}.')


# ___________________________________________________________
# 2. Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# number = int(input('Введите натуральное число: '))
# multiply = 1
# list_of_multiplies = []
# for i in range(1, number + 1):
#   multiply *= i
#   list_of_multiplies.append(multiply)
# print(f'Набор произведений от 1 до {number} будет {list_of_multiplies}.')


# ___________________________________________________________
# 3. Задайте список из n чисел последовательности 
# $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# number = int(input('Введите любое натуральное число: '))
# sum_po_formule = 0 # формула (1 + 1/n)^n
# for i in range(1, number + 1):
#   sum_po_formule += (1 + 1 / i) ** i
# print(f'Сумма чисел последовательности (1 + 1/n)^n равна {round(sum_po_formule, 2)}.')


# ___________________________________________________________
# 4. Реализуйте алгоритм перемешивания списка.
# import random
# original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(f'Начальный список: {original_list}')
# sorted_list = original_list[:]
# for i in range(len(original_list)):
#   index = random.randint(0, len(original_list) - 1)
#   temp = sorted_list[i]
#   sorted_list[i] = sorted_list[index]
#   sorted_list[index] = temp
# print(f'Перемешанный список: {sorted_list}')

