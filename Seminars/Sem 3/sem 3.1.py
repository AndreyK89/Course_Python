# Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.

stroka1 = 'Привет как у вас дела Привет'
stroka2 = 'Привет'
lst = stroka1.split (sep=' ')
print(lst)
count = 0
for i in range (len(lst)):
    if lst[i] == stroka2:
        count+=1
print(count)
