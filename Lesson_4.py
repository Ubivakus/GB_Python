# Урок 4. Данные, функции и модули в Python. Продолжение

# 1. Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# number = float(input('Введите число для округления: '))
# accuracy = float(input('Введите точность округления: '))
# if accuracy == 0 or accuracy == 1:
#   print(int(number))
# else:
#   accuracy = str(accuracy)
#   accuracy = accuracy.split('.')
#   accuracy = len(accuracy[1])
#   print(f'Ваше число {number} с точностью до {accuracy} знаков после запятой равно: {round(number, accuracy)}')

  
#___________________________________________________  
# 2. Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.

# number = int(input("Введите число: "))
# list_multipliers = []
# for i in range(2, number + 1):
#   if number % i == 0:
#     for j in range(2, i // 2 + 1):
#       if i % j == 0:
#         break
#     else:
#       list_multipliers.append(i)
# print(f'Список простых множителей числа {number}: {list_multipliers}')
    

#___________________________________________________ 
# 3. Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# a = [3, 2, 2, 3, 4, 1, 4, 0, 3, 4, 5, 2, 5, 5]
# b = set(a)
# b = list(b)
# print(f'Дана последовательность: {a}')
# print(f'Список неповторяющихся элементов: {b}')

# Алгоритм
# a = [3, 2, 2, 3, 4, 1, 4, 0, 3, 4, 5, 2, 5, 5]
# b = []
# print(f'Дана последовательность: {a}')
# for i in a:
#   count = 0
#   for j in a:
#     if i == j:
#       count += 1
#       if count == 2:
#         break
#   if count == 1:
#     b.append(i)
# print(f'Список неповторяющихся элементов: {b}')


#___________________________________________________   
# 4. Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и 
# записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

#  Сам бы я в жизни до такого не додумался :)

# from random import randint
# import random

# k = int(input('Введите натуральную степень k: '))
# while k <= 0:
#     k = int(input('Введены не корректные данные! Введите натуральную степень k: '))

# result = [0 for i in range(k)]
# koef = random.sample(range(0, 101), k + 1)
# print(f'Рандомные коэффициенты: {koef}')
# for i in range(len(result)):
#     result[i] = f'{koef[i]}x^{k}'
#     k -= 1
# result.append(str(koef[-1]))
# print(f'До обработки: {result}')
# for elem in result:
#     if elem == 0:
#         result.remove(elem)
#     try:
#         ind_x = elem.find('x')
#         d = int(elem[:ind_x])
#     except AttributeError:
#         continue
#     if d == 0 or elem == '0':
#         result.remove(elem)
#     if '^1' in elem:
#         result.remove(elem)
#         result.insert(-1, elem[:elem.find('^1')])
# print(f'После обработки: {result}')
# polynom = ''
# for i in range(len(result) - 1):
#     polynom += f'{result[i]} + '
# polynom += f'{result[-1]} = 0'
# print(polynom)

# with open('text.txt', 'w') as f:
#     f.write(polynom)

  
#___________________________________________________ 
