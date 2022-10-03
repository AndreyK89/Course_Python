# Задайте строку из набора чисел. Напишите программу,
# которая покажет большее и меньшее число. В качестве символа-разделителя используйте пробел.

str = '66 7 34 0 9'
lst = str.split(sep=' ')
max = int(lst[0])
min = int(lst[0])
print(lst)
for i in range(len(lst)):
    lst[i] = int(lst[i])
for i in range(1,len(lst)):
    if lst[i] > max:
        max = lst[i]
    if lst[i] < min:
        min = lst[i]
print(f'Максимальное число: {max}, Минимальное число: {min}')
