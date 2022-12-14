# Выполнил Андрей Кошелев Аналитика | 6 | 3040 | 21.09.2022
# Вычислить число π c заданной точностью d.
# Пример:
# - при d = 0.001, π = 3.141.  10^{-1} ≤ d ≤ 10^{-10}

# Вариант 1:

# k = 1
# x = 0
# for k in range(1, 1000000):
#     x = x+4*((-1)**(k+1))/(2*k-1)   # формула Лейбница
# print(f'Число Пи с заданной точностью d = 0.001, равно {round(x, 3)}')

# Вариант 2:

from math import pi  # Константа модуля  math.pi

d =  int(input("Введите число (в пределах 1-10) для заданной точности числа Пи: "))
print(f'Число Пи с заданной точностью {d} равно {round(pi, d)}')