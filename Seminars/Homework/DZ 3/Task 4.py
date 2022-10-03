# Выполнил Андрей Кошелев Аналитика | 6 | 3040 | 21.09.2022
# Задача 4 - Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# Вариант 1 :
# def conversion_binary(number):
#     binary_number = ''
#     while number !=0:
#         binary_number = str(number%2) + binary_number
#         number //=2
#     return binary_number
#
# number = int(input('Введите число: '))
# print(conversion_binary(number))

# Вариант 2 :

number = int(input('Введите число: '))
print('{0:b}'.format(number))
