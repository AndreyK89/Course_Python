# Посчитайте, сколько раз символ встречается в строке.

stroka = 'Посчитайте, сколько раз символ встречается в строке'
simvol = 'о'
final = 0
for i in stroka:
    if simvol == i:
        final +=1
print(final)
