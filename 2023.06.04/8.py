n = int(input("Введите число: "))
f1 = 1
f2 = 2

print(f1, f2, end=" ")

for i in range(3 , n+1):
    print(f1 + f2, end=" ")
    b = f1
    f1 = f2
    f2 = b + f1

print()

#Введите число: 31
#1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946 17711 28657 46368 
#75025 121393 196418 317811 514229 832040 1346269 2178309