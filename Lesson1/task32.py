# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
max_number = int(input())
min_number = int(input())
list2 = list()

for i in range(len(list_1)):
    if list_1[i] >= min_number and list_1[i] <= max_number:
        list2.append(i)
print(list2)       