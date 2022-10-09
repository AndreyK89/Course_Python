# В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.
# 0 1 2 3 4 6 7 8

with open('file.txt', 'r') as rd:
    lst = list(map(int, rd.read().split(' ')))

    for i in range(1, len(lst)):
        if lst[i] != lst [i-1] +1:
            lst.insert(i, lst[i]-1)

print (lst)
with open('file.txt', 'w') as rd:
    rd.write(' '.join(map(str, lst)))
