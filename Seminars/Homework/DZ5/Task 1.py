# Выполнил Андрей Кошелев Аналитика | 6 | 3040 | 21.09.2022
# Задача 1. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

a) Добавьте игру против бота

b) Подумайте как наделить бота ""интеллектом""

print("*" * 10, " Игра Крестики-нолики для двух игроков ", "*" * 10)

board = list(range(1,10))

def draw_board(board):
   print("-" * 13)
   for i in range(3):
      print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
      print("-" * 13)

def take_input(player_token):
   valid = False
   while not valid:
      player_answer = input("Куда поставим " + player_token+"? ")
      try:
         player_answer = int(player_answer)
      except:
         print("Некорректный ввод. Вы уверены, что ввели число?")
         continue
      if player_answer >= 1 and player_answer <= 9:
         if(str(board[player_answer-1]) not in "XO"):
            board[player_answer-1] = player_token
            valid = True
         else:
            print("Эта клетка уже занята!")
      else:
        print("Некорректный ввод. Введите число от 1 до 9.")

def check_win(board):
   win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for each in win_coord:
       if board[each[0]] == board[each[1]] == board[each[2]]:
          return board[each[0]]
   return False

def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
           take_input("X")
        else:
           take_input("O")
        counter += 1
        if counter > 4:
           tmp = check_win(board)
           if tmp:
              print(tmp, "выиграл!")
              win = True
              break
        if counter == 9:
            print("Ничья!")
            break
    draw_board(board)
main(board)

input("Нажмите Enter для выхода!")

import os
import random


# def ask_name(n):
#     return input(f'Введите имя игрока {n}: ')
#
# def define_player_list(p1, p2):
#     rand = random.randint(0,1)
#     return [p1, p2] if rand == 0 else [p2, p1]
#
# def ask_number(player, total_number):
#     number = input(f'Игрок {player}, сколько конфет вы хотите взять? ')
#     if(not number.isdigit()):
#         print('Ошибка: вы ввели не число! Повторите ввод')
#         return ask_number(player, total_number)
#     number = int(number)
#     if(number > 28):
#         print(f'Ошибка: за один ход можно забрать не более чем 28 конфет')
#         return ask_number(player, total_number)
#     if (number > total_number):
#         print(f'Ошибка: вы не можете взять больше чем {total_number} конфет')
#         return ask_number(player, total_number)
#     return number
#
# def turn(player, total):
#     print(f'Ходит игрок {player}')
#     number = ask_number(player,total)
#     return total - number
#
# def game():
#     candies = 2021
#     print(f'На столе лежит {candies} конфета')
#     player_1 = ask_name(1)
#     player_2 = ask_name(2)
#     print('Бросаем жребий...')
#     player_list = define_player_list(player_1,player_2)
#     cursor = 0
#     current_player = player_list[cursor]
#     winner = None
#     print(f'Первым будет ходить игрок {current_player}!')
#     while(winner == None):
#         current_player = player_list[cursor]
#         candies = turn(current_player, candies)
#         print(f'На столе осталось {candies} конфет')
#         cursor += 1
#         if(cursor > 1):
#             cursor = 0
#         if (candies == 0):
#             winner = player_list[cursor]
#     print(f'Игрок {current_player} проиграл')
#     print('=======================================')
#     print(f'======= Игрок {winner} победил !!! =========')
#     print('=======================================')
#
# game()
