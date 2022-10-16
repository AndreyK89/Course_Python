# Выполнил Андрей Кошелев Аналитика | 6 | 3040 | 21.09.2022
# Задача 3: Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Пример:
# На сжатие входные данные: aaabbbccccdddddeeeee
# Выходные данные:          3a3b4c5d5e



def rle_coding(data):
    count = 1
    res = ''
    for i in range(len(data)-1):
        if data[i] == data[i+1]:
            count += 1
        else:
            res = res + str(count) + data[i]
            count = 1
    if count > 1 or (data[len(data)-2] != data[-1]):
        res = res + str(count) + data[-1]
    return res

def decoding(data):
    number = ''
    res = ''
    for i in range(len(data)):
        if not data[i].isalpha():   # Метод .isalpha() проверяем что строка состоит только из букв.


            number += data[i]
        else:
            res = res + data[i] * int(number)
            number = ''
    return res


string = input("Введите текст для сжатия данных: ")
print(f"Данные после сжатия: {rle_coding(string)}")
print(f"Данные после дешифровки: {decoding(rle_coding(string))}")