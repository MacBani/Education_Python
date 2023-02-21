vse_gls = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
puh = input().split()
flag = 0
n = len(puh)
for i in range(n):
    for z in puh[i]:
        for j in vse_gls:
            if z == j:
                flag += 1
        if flag == 0:
            puh[i] = puh[i].replace(z, "")
        flag = 0   
for le in range(n):
    if len(puh[le]) == len(puh[(le + 1)%n]):
        flag += 1
if flag == n:
    print("Парам пам-пам")
else:
    print("Пам парам")
