# Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.

number = float(input('Input Number :'))

number = number * 10 % 10
print(int(number))
