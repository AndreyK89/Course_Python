# Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное)
# и НОД (наименьший общий делитель), этих двух чисел.

a = int(input('Input A :'))
b = int(input('Input B :'))

nod = 2
while True:
    if b%nod == 0 and a%nod == 0:
        print(nod)
        break
    else:
        nod +=1

if a > b:
    nok = a
else:
    nok = b

while True:
    if nok%b == 0 and nok%a == 0:
        print(nok)
        break
    else:
        nok += 1
