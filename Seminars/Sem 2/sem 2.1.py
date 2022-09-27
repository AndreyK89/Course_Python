# Напишите программу, которая выводит нечетные числа из заданного списка
# и останавливается, если встречает число 554.


import random

lst=[554]

for i in range(random.randint(5,15)): # сколько чисел в списке
    x = random.randint(500,600)
    lst.append(x) # добавляем переменную в конец списка

print(lst)
random.shuffle(lst)  # перемешали список
print(lst)

for i in lst:
    if i %2 != 0:
        print(i)
    if i == 554:
        break

