# Выполнил Андрей Кошелев Аналитика | 6 | 3040 | 21.09.2022
# DZ_3  Задача 2 - Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# def mult_lst(lst):
#     length = len(lst)//2 + 1 if len(lst) % 2 != 0 else len(lst)//2
#     print(length)
#     new_lst = [lst[i]*lst[len(lst)-i-1] for i in range(length)]
#     return new_lst
#
# lst_numbers = [2, 3, 4, 5, 6]
# print(mult_lst(lst_numbers))


def mult_lst(lst):
    length = len(lst)//2 + 1 if len(lst) % 2 != 0 else len(lst)//2
    new_lst = [lst[i]*lst[len(lst)-i-1] for i in range(length)]
    print(new_lst)

lst = list(map(int, input("Введите числа через пробел: ").split()))       # Улучшение кода функцией map.
mult_lst(lst)