# Требуется вывести все целые степени двойки (т.е. числа
# вида 2**k), не превосходящие числа N.

n = int(input("Введите число: "))
count = 0 
k = 0
while count < n:
    count += 2**k
    print(2**k)
    k += 1