#  Файлы :
#  Хранение данных
#  Передача данных в клиент серверных проектах
#  Хранение конфигов
#  Логирование дийствий - Логировани - это процес записи информации о событиях, происходящих в рамках кого-либо процесса с некоторым объектом.

# Как работать с файлами:
# Связать файловую переменную с файлом,
# определив модификотор работы.
# "а" - открытие для добавления данных # дописать в несу=ществующий файл если файла нет то он его создаст и запишет
# "r" - открытие для чтение данных # если данные будут считываться с несуществующего файла то ожидается ошибка
# "w" - открытие для записи данных # записывает данные и создавать файл если его не существует. ПЕРЕЗАПИСЬ
# "w+", "r+"

# colors = ['red', 'green', 'blue']  # записаны данные в качестве источника данных выступает список
# data = open('file.txt', 'a') # создаем текстовую переременную "data" и связывае ее с текстовым файлом
# data.writelines(colors) # разделителей не будет.  функционал позволяющий записать некоторый набор данных. Пример: redgreenblue
# data.write('LINE 121\n') #записывается LINE 121 на след строке
# data.write('LINE321\n') #записывается LINE321 на след строке
# data.close() # выход/разрыв подключение с файлом
#
# with open('file.txt', 'a') as data: # конструкция для записи данных with  аналог предыдущего варианта
#     data.write('line 111\n')
#     data.write('line 222\n') # после завершения цикла авто-ки вых из файла "close"не нужно

###
# Чтение данных

# from configparser import LegacyInterpolation
# import re


# path = 'file.txt'  # создали путь к файлу
# data = open(path, 'r')  # открыли в режиме чтения
# for line in data:  # при помощи цикла пробежимся по файлу
#     print(line)  # считаем все строки
# data.close()


########   Функции и модули  ###########

# Функции
# Это фрагмент программы, используемый многократно

# def function_name(x):
#     # body line 1
#     # .  .  .
#     # body line n
#     # optional return

# import lec # импортировали файл lec (файл с предыдущей лекции)

# print(lec.f(1)) # вызвали функцию (f) из импортируемого файла lec

# import lec as l # импортировали файл и переименоволи его для упращенного ввода

# print(l.f(1))

######

# def new_string(symbol, count): # функция принимает некий символ и число
#     return symbol * count      # умножаем символ на число

# print(new_string('!', 5)) # результат !!!!! - пять воскл знака
# print(new_string('!')) # выдаст ошибку, не указано значение count


# def new_string(symbol, count=3): # функция принимает некий символ и число равное трем (всегда по умолчанию)
#     return symbol * count

# print(new_string('!', 5)) # !!!!!
# print(new_string('!'))    # !!!  выведит три воскл знака т.к. по умолчанию count = 3
# print(new_string(4))      # 12

#######

# Передача неограниченного кол-во аргументов

# def concatenatio(*params): # перед аргументом ставим звездочку(знак умножения)(*)
#     res: str = "" # указываем тип данных строка
#     for item in params:
#         res += item
#     return res

# print(concatenatio('a', 's', 'd', 'w')) # asdw
# print(concatenatio('a', '1', 'd', '2')) # a1d2
# #print(concatenatio(1, 2, 3, 4))  # Ошибка т.к. тип данных int


###########

### Рекурсия - это функция вызываемая сама себя

# def fib(n):
#     if n in [1, 2]: # если попали в первый и второй элемент числа то возвращаем 1
#         return 1    # возвращаем 1 когда условие if выполнино
#     else:           # Иначе выполняе условие else
#         return fib(n-1) + fib(n-2) # выполняется условие else по формуле фибоначи

# lst = []
# for e in range(1,20):  # смотрим первые 10 чисел
#     lst.append(fib(e))
# print(lst)


###########

#####    Кортежи - это неизменяемый "список"
# Кортеж используют для создании "пары"

# присоднании кортежа обязательно ставить запятую Пример: a = (3,)

# a = (3, 4) # для создания кортежа элименты заключаем в скобки
# print(a) # (3,4)
# print(a[0]) # 3 #обращаемся к нулевому элименту
# print(a[-1]) # 4

# a = (3, 1, 41, 4)
# print(a)
# print(a[-2]) #41

#a[0] = 12 # EROR # нулевому элементу присвоеить 12 в кортежи не получиться. КОРТЕЖ неизменяемый список

# Кортежи можно переберать при помощи циклов
# a = (3, 1, 41, 4)

# for item in a:
#     print(item) # 3 1 41 4

#    Кортежи - это неизменяемый "список"

# t = ()
# print(type(t)) # tuple

# t = (1,)
# print(t) # (1,)
# print(type(t)) # tuple

# t = (1)
# print(t) # 1
# print(type(t)) # int

# t = (28, 9 , 1990)
# print(t) # (28,9,1990)
# print(type(t)) #tuple

# colors = ['red', 'green', 'blue']
# print(colors) # ['red', 'green', 'blue']
# t = (colors)
# print(t) # ['red', 'green', 'blue']
# t = tuple(colors)
# print(t) # ('red', 'green', 'blue')

# t = tuple(['red', 'green', 'blue'])
# # print(t[0]) # red
# # print(t[2]) # blue
# # print(t[-2]) # green

# for item in t:
#     print(item) # red blue green

# t = tuple(['red', 'green', 'blue'])
# red, green, blue = t
# print('r:{} g:{} b:{}'.format(red, green, blue)) # r:red g:green b:blue


#############  Словари
# ## Словари - Неупорядоченные колекции произвольных объектов с доступом по ключу

# dictionary = {}
# dictionary = \
#  {
#  'up': '↑',
#  'left': '←',
#  'down': '↓',
#  'right': '→'
#  }
 # \ обратный слэш нужен для переноса значений
# print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['left']) # ←
# типы ключей могут отличаться

# for k in dictionary.keys():
#     print(k) # распечатали все ключи # up left down right
# for k in dictionary.values():
#     print(k)  # распечатали все значения (стрелочки)

# for v in dictionary:
#     print(v) # распечатали все ключи # up left down right

# for v in dictionary:
#     print(dictionary[v])  # распечатали все значения (стрелочки)

# print(dictionary['up']) # ↑
# # типы ключей могут отличаться
# dictionary['left'] = '⇐'
# print(dictionary['left']) # ⇐
# #print(dictionary['type']) # KeyError: 'type'

# del dictionary['left'] # удаление элемента

# for item in dictionary: # for (k,v) in dictionary.items():
#     print('{}: {}'.format(item, dictionary[item])) # up: ↑ # down: ↓ # right: →

############## Множества
#### Множества - Неупорядоченна совокупность элементов

# colors ={'red', 'green', 'blue'}
# print(type(colors)) # <class 'set'> тип данных множеств это 'set'
# print(colors) # {'red', 'green', 'blue'}
# colors.add('red') # .add дабавляет элемент 'red'
# print(colors) # {'red', 'green', 'blue'} такой элимент 'red' есть он не добавляется
# colors.add('gray') # дабавили элемент 'gray'
# print(colors) # {'red', 'green', 'blue', 'gray'}
# colors.remove('red') # .remove удаляет элемент 'red'
# print(colors) # {'blue', 'green', 'gray'} элемент 'red' удален из множества
# colors.discard('red') # удаляет значения
# print(colors) # {'gray', 'blue', 'green'}
# colors.clear() # .clear удаляет множества очищает {}
# print(colors) # set()

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # .copy копируем множество {a} в {c}
# print(c) # {1, 2, 3, 5, 8}
# u = a.union(b) # .union() объеденяем множества a и b
# print(u) # {1, 2, 3, 5, 8, 13, 21}
# i = a.intersection(b) # пересечение множест a И b
# print(i) # {8, 2, 5}
# dl = a.difference(b) # не пересекаются с b
# print(dl) # {1, 3}
# dr = b.difference(a) # не пересекаются с a
# print(dr) #{13, 21}

# #q = a.union(b).difference(a.intersection(b)) # или можно записать не в одну строку а с переносом
# q = a\
#     .union(b)\
#     .difference(a.intersection(b)) # объединили множства "a.union(b)" вывели не пересекаемый мноства ".difference" предворительно убрав (a.intersection(b)) пересекаемые
# print(q) # {1, 21, 3, 13}

# a = {1, 2, 3, 5, 8}
# b = frozenset(a) # неименяемое множество
# print(b) # frozenset({1, 2, 3, 5, 8})


########### СПИСКИ

# list1 = [1, 2, 3, 4, 5] # создаем список
# list2 = list1 # присваеваем list2 список из list1
# # печатаем список list1
# for e in list1:
#     print(e)
# # пробел
# print()
# # печатаем список list2
# for e in list2:
#     print(e)

# list1 = [1, 2, 3, 4, 5]
# # .pop() удаление последнего элемента списка
# # print(list1.pop()) # 5 показывает удаляемыйэлемент
# # print(list1) # [1, 2, 3, 4]

# list1 = [1, 2, 3, 4, 5]
# # # удаление нужного элемента из списка .pop(2) в скобках указываем какой элемент удалить
# # print(list1.pop(2)) # удален 2 элемент цифра 3
# # print(list1) # [1, 2, 4, 5]

# list1 = [1, 2, 3, 4, 5]
# # .insert() вставка элемента
# print(list1.insert(2, 11)) # .insert(2, 11) где 2 это позиция 11 цифра элемента
# print(list1) # [1, 2, 11, 3, 4, 5]

# list1 = [1, 2, 3, 4, 5]
# # .append() добавление в конец списка
# print(list1.append(11)) # добавление элемента в конец списка
# print(list1) # [1, 2, 3, 4, 5, 11]