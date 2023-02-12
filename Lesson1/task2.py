# Найдите сумму цифр трехзначного числа.

number = int(input('Введите трёхзначное число: '))
number_3 = number%10
number_2 = number//100
number_1 = (number%100)//10
print(f'Сумма чисел трёхзначного числа {number} равна {number_1+number_2+number_3}')