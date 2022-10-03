# Найдите корни квадратного уравнения Ax² + Bx + C = 0

import math
a = int(input("Введите значение a = "))
b = int(input("Введите значение b = "))
c = int(input("Введите значение c = "))
D = b ** 2 - 4 * a * c
print(f'Discriminant = {D}')
if D < 0:
  print("Корней нет")
elif D == 0:
  x = -b / 2 * a
  print (x)
else:
  x1 = (-b + math.sqrt(D)) / (2 * a)
  x2 = (-b - math.sqrt(D)) / (2 * a)
  print(f'Root 1 = {x1}')
  print(f'Root 1 = {x2}')