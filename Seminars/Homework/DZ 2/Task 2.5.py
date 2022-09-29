# Выполнил Юрий Савоськин (преподователь) Аналитика | 6 | 3040 | 21.09.2022
# Реализуйте алгоритм перемешивания списка.(Без использования библиотеки random)

import datetime

def myShuffle2(some_list):
    for i in range(0, len(some_list)-1):
            print(datetime.datetime.now().microsecond)
            j = datetime.datetime.now().microsecond % len(some_list)-1  # текущее время в микросекундах
            some_list[j], some_list[i] = some_list[i], some_list[j]
    return some_list

print(myShuffle2([4,2,3,1,5,6]))

