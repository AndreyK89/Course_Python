# Выполнил Андрей Кошелев Аналитика | 6 | 3040 | 21.09.2022
# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.


from random import random

list = []
for j in range(10):
    list.append(int(random() * 10))
print(list)

new_list = []
for i in list:
    if list.count(i) == 1:
        new_list.append(i)
print(new_list)