# Выполнил Андрей Кошелев Аналитика | 6 | 3040 | 21.09.2022
# Задача 2 - Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# *Пример:*
# - пусть n = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = int(input('Введите число : '))
first_number = 1
composition = []
for i in range(1, n+1):
    first_number *= i
    composition.append(first_number)
print(composition)
