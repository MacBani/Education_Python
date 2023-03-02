# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной
# записи (Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной
# 5. Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.

def create_file(new_files):
    data = open(new_files, "a")
    data.close()

def write_data(s, n, p):
    data = open("phonebook.txt", "a")
    data.writelines(f"{s} {n} {p}\n")
    data.close()

def read_file():
    with open("phonebook.txt") as file:
        lines = list(enumerate(file.read().splitlines()))
    for i in range(len(lines)):
        print(*lines[i])

def find_number(finder_word):
    dic = {}
    with open("phonebook.txt") as file:
        lines = list(file.read().splitlines())
        l = list()
        for i in range(len(lines)):
            l.append(lines[i].split())
        l = list(enumerate(l))
    for key, values in l:
        dic.update({key: values})
    for j in range(len(dic)):
        for word in dic[j]:
            if word == finder_word:
                print(*dic[j])


def delete_data(keys):
    dic = {}
    with open("phonebook.txt") as file:
        lines = list(file.read().splitlines())
        l = list()
        for i in range(len(lines)):
            l.append(lines[i].split())
        l = list(enumerate(l))
        for key, values in l:
            dic.update({key: values})
        del dic[keys]
    data = open("phonebook.txt", "w")
    for word in dic.values():
        for j in range(len(word)):
            data.writelines(f"{word[j]} ")
        data.writelines(f"\n")
    data.close()
    

def change_data(id, name, what_change):
    dic = {}
    with open("phonebook.txt") as file:
        lines = list(file.read().splitlines())
        l = list()
        for i in range(len(lines)):
            l.append(lines[i].split())
        l = list(enumerate(l))
        for key, values in l:
            dic.update({key: values})
    if what_change == 1:
        dic1 = dic[id]
        dic1[0] = name
        dic[id] = dic1
    elif what_change == 2:
        dic2 = dic[id]
        dic2[0] = name
        dic[id] = dic2
    data = open("phonebook.txt", "w")
    for word in dic.values():
        for j in range(len(word)):
           data.writelines(f"{word[j]} ")
        data.writelines(f"\n")
    data.close()
    
#new_files = input("Введите имя нового файла: ")
# create_file()
#surname = input("Введите фамилию: ")
#name = input("Введите имя: ")
#phone_number = input("Введите номер телефона: ")

#write_data(surname, name, phone_number)
#read_file()

#lines = list(enumerate(file.read().splitlines()))
#find_number("Petrov")
#delete_data(2)

change_data(2, "Panin", 1)