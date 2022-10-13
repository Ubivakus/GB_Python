# 1. Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели,
# и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

# day_of_week = int(input("Введите день недели цифрой от 1 до 7:\n"))
# if day_of_week <= 5 and day_of_week >= 1:
#   print('Нет')
# elif day_of_week <= 0 or day_of_week >= 8:
#   print('Неверно указан номер дня недели!')
# else:
#   print('Да')

# ____________________________________
# 2. Напишите программу для проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# x = float(input("Введите число x: "))
# y = float(input("Введите число y: "))
# z = float(input("Введите число z: "))
# left = not(x or y or z)
# right = not x and not y and not z
# if  left == right:
#   print("Утверждение истинно")
# else:
#   print("Утверждение ложно")

# ____________________________________
# 3. Напишите программу, которая принимает на вход координаты точки 
# (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

# x = int(input('Введите координату точки по оси X: '))
# y = int(input('Введите координату точки по оси Y: '))
# if x > 0 and y > 0:
#   print('Точка на ходится в 1-ой четверти')
# elif x < 0 and y > 0:
#   print('Точка находится во 2-ой четверти')
# elif x < 0 and y < 0:
#   print('Точка находится в 3-ей четверти')
# elif x > 0 and y < 0:
#   print('Точка находится в 4-ой четверти')
# else:
#   print("Координаты не должны быть равны 0!")

# ____________________________________
# 4. Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

# quarter = int(input('Введите номер четверти от 1 до 4: '))
# if quarter == 1:
#   print('Координаты точки по оси x > 0 и по оси y > 0')
# elif quarter == 2:
#   print('Координаты точки по оси x < 0 и по оси y > 0')
# elif quarter == 3:
#   print('Координаты точки по оси x < 0 и по оси y < 0')
# elif quarter == 4:
#   print('Координаты точки по оси x > 0 и по оси y < 0')
# else:
#   print('Вы ввели недопустимый номер четверти!')

# ____________________________________
# 5. Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

# ax = float(input('Введите координату точки A по оси X: '))
# ay = float(input('Введите координату точки A по оси Y: '))
# bx = float(input('Введите координату точки B по оси X: '))
# by = float(input('Введите координату точки B по оси Y: '))
# ac = bx - ax
# bc = by - ay
# ab = round((ac ** 2 + bc ** 2) ** (0.5), 2)
# print('Расстояние между точками A и B равно ' + str(ab))