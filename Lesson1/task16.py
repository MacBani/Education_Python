# Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих 
# строках записаны N целых чисел Ai. Последняя строка содержит число X
import random

list_1 = list()
n = int(input("Введите количество элементов в массиве: "))
count = 0
for i in range(n):
    list_1.append(random.randint(0, 9))
print(*list_1)
x = int(input("Введите число, чтобы узнать сколько вхождений у него в данном массиве: "))
for i in range(n):
    if list_1[i] == x:
        count += 1
print(count)