# print('hello world')
# типы данных переменная
# int, float, boolean, str, list, None

# value = None # для дальнейшего присваевания
# a = 123 # int
# b = 1.23 # float
# print(type(a)) # print - выводим на печать, type - узнаём тип переменной
# print(type(b))
#value = 1234
# print(type(value))
# s = 'hello world' # str
# print(s)
# s = "hello 'world" # можно двойные ковычки
# print(s)
#s = 'hello "world'
# print(s)
# s = 'hello \'world' # обратный слэш и апостроф отоброжается
# print(s)
# s = 'hello \nworld' # перенос слов на другую строчку
# print(s)

# Интерполяция

#a = 123
#b = 1.23
#s = 'hello world'
#print(a, b, s)

#print(a, '-',b, '-',s)
#print('{} - {} - {}'.format(a,b,s))
#print(f'{a} - {b} - {s}')
#print('{1} - {2} - {0}'.format(a, b, s))

#f = True
# print(f)
#f = False
# print(f)

# Списки (Массив)

# list = []  # назначение списка(массива)
# print(list)
# list = [1, 2, 3, 4, 5]
# print(list)
# list = ['1', '2', '3', 'hello']  # список строк
# print(list)
# list = ['1', '2', '3', 'hello', 1, 2, 3, 1.21, 2.24, True] # типы данных в списке можно миксовать но не стоист
# print(list)

# Ввод и Вывод данных
# print, input

# print('Введите а');
# a = input()
# print('Введите b');
# b = input()
# print(a, b)
# print('{} {}'.format(a, b))
# print(f'{a} {b}')

# Вывод сложения строк
# print('Введите а');
# a = input()
# print('Введите b');
# b = input()
# print(a, '+',b, '=', a+b)

# Вывод сложения строк Перед input указываем ТИП
# print('Введите а');
# a = int(input())
# print('Введите b');
# b = int(input())
# print(a, '+',b, '=', a+b)

# Вывод сложения строк Перед input указываем ТИП
# print('Введите а');
# a = float(input())
# print('Введите b');
# b = float(input())
# print(a, '+',b, '=', a+b)

# a = int(input('Введите a: ')) # Ввод данных в одну строчку
# a = int(input('Введите \nа: ')) # Ввод данных на след. строчке

# Арифметические операции
# +, -, *, /, %, //, **
# Приоритет операций
# **, ⊕, ⊖, *, /, //, %, +, -
# ( ) Скобки меняют приоритет

# a = 123
# b = 321
# c = a+b
# print(c)
# a = 123
# b = -321
# c = a+b
# print(c)
# a = 2
# b = 8
# c = a-b
# print(c)
# a = 2
# b = 8
# c = a*b
# print(c)
# a = 2
# b = 8
# c = a/b
# print(c)
# a = 12
# b = 5
# c = a/b
# print(c)
# a = 12
# b = 5
# c = a//b # деление в целлых числах
# print(c)
# a = 12
# b = 8
# c = a % b # остаток от деления
# print(c)
# a = 2
# b = 8
# c = a ** b # Возвидение в степень
# print(c)
# a = 1.3
# b = 3
# c = a * b
# print(c)
# a = 1.3
# b = 3
# c = round(a * b) # round - округление
# print(c)
# a = 1.3
# b = 3
# c = round(a * b,3) # round - округление. ,3 - кол-во знаков после запитой
# print(c)
# a = 1.3123
# b = 3
# c = round(a * b,5) # round - округление. ,5 - кол-во знаков после запитой
# print(c)

# a = 3
# a = a + 5
# print(a)
# a = 3
# a += 5
# print(a)

# Логические операции
# >, >=, <, <=, ==, !=
# not, and, or – не путать с &, |, ^
# Кое-что ещё: is, is not, in, not in

# a = 1 > 4
# print(a)
# a = 1 < 4
# print(a)
# a = 1 < 4 and 5 > 2
# print(a)
# a = 1==2 # опреция сравнение
# print(a)
# a = 1 != 2 # операция не равенства
# print(a)

# func = 1
# T = 4
# x = 2
# print(func<T>(x))
# print(func<T>x)

# f = 1 > 2 or 4 < 6
# print(f)

# f = [1,2,3,4]
# print(f)
# # print(2 in f) # нахождение 2 в списке
# # print(not 2 in f) # отрицание 2 в списке

# is_odd = f[0] % 2 == 0 # проверка на четность
# print(is_odd)
# is_odd = not f[0] % 2 # ВАРИАНТ Python проверки на четность

# Управляющие конструкции:
# if, if-else

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)

# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же МАША!')
# elif username == 'Марина':
#     print('Я так ждал Вас, Марина!')
# elif username == 'Ильнар':
#     print('Ильнар - топ)')
# else:
#     print('Привет,', username)

# Управляющие конструкции: while
# Цикл позволяет выполнить блок операторов какое-то количество раз

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10) # развернули число
#     original //= 10
# print(inverted)

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10) # развернули число
#     original //= 10
#     print(original)
# else:
#     print('Пожалуй')
#     print('хатит )')
# print(inverted)

# Управляющие конструкции: for
# Когда мы знаем, что хотим

# list = [1,2,3,4,5]
# for i in list:
#     print(i**2)

# r = range(10) #Вывод чисел от 0 до 9
# for i in r:
#     print(i)

# for i in range(5):
#     print(i)

# for i in range(1, 5): # Вывод от 1 до 4
#     print(i)

# for i in range(1, 10, 2): # Вывод от 1 до 9 с шагом 2 (нечетные числа)
#     print(i)

# for i in 'qwe - rty': # По буквенная разбивка
#     print(i)

# Немного о строках

# text = 'съешь ещё этих мягких французских булок'
# print(len(text)) # Кол-во знаков(символов) # 39
# print('ещё' in text) # находется ли данное выражение "ещё" в тексте # True
# print(text.isdigit()) # Являются ли все символы в строке числами # False
# print(text.islower()) # Являются ли все сивмолы нижниго регистра # True
# print(text.replace('ещё','ЕЩЁ')) # Заменили "ещё" на "ЕЩЁ"

# text = 'съешь ещё этих мягких французских булок'
# print(text[0]) # c
# print(text[1]) # ъ
# print(text[len(text)-1]) # к
# print(text[-5]) # б
# print(text[:]) # print(text)
# print(text[:2]) # съ
# print(text[len(text)-2:]) # ок
# print(text[2:9]) # ешь ещё
# print(text[6:-18]) # ещё этих мягких
# print(text[0:len(text):6]) # сеикакл
# print(text[::6]) # сеикакл
# text = text[2:9] + text[-5] + text[:2] # ..

# Списки: введение
# Список – пронумерованная, изменяемая коллекция
# объектов произвольных типов

# numbers = [1, 2, 3, 4, 5]
# print(numbers)  # [1, 2, 3, 4, 5]
# numbers = list(range(1, 6))
# print(numbers)  # [1, 2, 3, 4, 5]
# numbers[0] = 10
# print(numbers)  # [10, 2, 3, 4, 5]
# for i in numbers:
#     i *= 2
#     print(i)  # [20, 4, 6, 8, 10]
# print(numbers)  # [10, 2, 3, 4, 5

# colors = ['red', 'green', 'blue']
# for e in colors:
#  print(e) # red green blue
# for e in colors:
#  print(e*2) # redred greengreen blueblue
# colors.append('gray') # добавить в конец
# print(colors == ['red', 'green', 'blue', 'gray']) # True
# colors.remove('red') #del colors[0] # удалить элемент

                        #Функции
                        #Это фрагмент программы, используемый многократно
# def function_name(x):
    # body line 1
    # . . .
    # body line n
    # optional return

import re


def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

arg = 1
print(f(arg))
