 ==========  1  ========== 

name1 = input("Введите имя: ")
name2 = input("Введите фамилию: ")
age = int(input("Введите год рождения: "))
age2 = int(input('Какой сейчас год: '))
print(name2, name1, ',', age2 - age)

 ==========  2  ========== 

num = int(input())
print(f'Следующее за числом {num} число:', num + 1)
print(f'Для числа {num} предыдущее число:', num - 1)

==========  3  ========== 

n=int(input())
h=n // 60
m=n % 60
print(f'{n} мин - это {h} час {m} минут.')

==========  4  ========== 

num = int(input())
a = num % 10
b = (num % 100) // 10
c = num // 100
print("Сумма цифр =", c + b + a)
print("Произведение цифр =", c * b * a)

==========  5  ==========

a = float(input())
k = 1.61
sum = a*k
print(a, 'миль = ', round(sum, 1), 'км')


