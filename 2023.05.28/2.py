a = int (input())
b = int (input())
num = a // b
rem = a % b
if rem == 0:
    print (f'{a} Делится на {b} нацело\n' f'Частное: {num}')
else:
    print (f'{a} Не делится на {b} нацело\n' f'Неполное частное: {num}\n' f'Остаток: {rem}')



#6
#2
#6 Делится на 2 нацело
#Частное: 3
