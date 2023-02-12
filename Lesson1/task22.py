# Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

list_1 = list()
list_2 = list()
a = set()

n = int(input())
m = int(input())
i = 0
while i < n:
    list_1.append(int(input()))
    i += 1

i = 0

while i < m:
    list_2.append(int(input()))
    i += 1

if n >= m:
    for j in range(n):
        for g in range(m):
            if list_1[j] == list_2[g]:
                a.add(list_1[j])
if m > n:
    for j in range(m):
        for g in range(n):
            if list_2[j] == list_1[g]:
                a.add(list_2[j])
a = sorted(a)
print(a)
