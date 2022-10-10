# Выполнил Андрей Кошелев Аналитика | 6 | 3040 | 21.09.2022
# Задача 1. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""



from random import randint

def input_dat(name):
    x = int(input(f"Игрок {name}, возмите конфет от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"Игрок {name}, можно взять не более 28 конфет: "))
    return x

def p_print(name, k, counter, value):
    print("=" * 58)
    print(f"Игрок {name}, взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")

player1 = input("Введите имя первого игрока: ")
player2 = input("Введите имя второго игрока: ")
candies = int(input("Введите количество конфет на столе: "))  #  2021 конфет, очень долго играть, сделал рандом.
turn = randint(0,2)    # очередность
if turn:
    print("=" * 44)
    print(f"Бросаем жребий...Первый ходит игрок {player1}.")
else:
    print("=" * 44)
    print(f"Бросаем жребий...Первый ходит игрок {player2}.")

counter1 = 0
counter2 = 0

while candies > 28:
    if turn:
        k = input_dat(player1)
        counter1 += k
        candies -= k
        turn = False
        p_print(player1, k, counter1, candies)
    else:
        k = input_dat(player2)
        counter2 += k
        candies -= k
        turn = True
        p_print(player2, k, counter2, candies)

if turn:
    print("=" * 58)
    print(f"        ======= Ура!!! Выиграл => Игрок {player1} =======")
else:
    print("=" * 58)
    print(f"        ======= Ура!!! Выиграл => Игрок {player2} =======")