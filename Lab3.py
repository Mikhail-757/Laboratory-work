from fileinput import filename
def menu():
    kontr1 = True
    kontr2 = True
    kontr3 = True
    while (kontr1) or (kontr2) or (kontr3):
        choice = int(input("Задания: \n 1 - Открытие и чтение файла \n 2 - Запись в файл "
                           "\n 3 - Проверка файла на существование\n Выберете номер:"))
        if choice == 1:
            n_1()
            kontr1 = False
        elif choice == 2:
            n_2()
            kontr2 = False
        elif choice == 3:
            n_3()
            kontr3 = False
        else:
            print("Выберете из одно из трёх задний!")
    return

def read_is_file(filename):
    my_file = open(filename, 'r')
    content = my_file.read()
    print(content)
    my_file.close()
    return

def rif(filename,s):
    if s == "all":
        read_is_file(filename)
    elif s == "lin":
        my_file = open(filename,'r')
        lines = my_file.readlines()
        for line in lines:
            print ("Построчно   ", line)
        my_file.close()

def n_1():
    filename = "example.txt"
    my_file = open(filename, "w")
    my_file.write("строка 1 12233.\nстрока 2 65734.\n")
    my_file.write("строка 3 6576765.\n")
    my_file.close()
    print("Читаем просто из файла :")
    read_is_file(filename)

    x = True
    while x:
        s = str(input("Уточнение: \n1 - вывод полностью\n2 - вывод по строкам\n3 - выход\nВыберете вывод:"))
        if s == '1':
            rif(filename,"all")
        elif s == "2":
            rif(filename,"lin")
        elif s == "3":
            x = False
        else:
            x = True
    return

def n_2():
    filename = 'user_input.txt'
    file = open(filename,'w+')
    file.close()
    print(f' Файл {filename} создан и закрыт ')

    file = open('user_input.txt', 'a')
    print(f' Файл {filename}  открыт   для дозаписи')
    i = 0
    while i <= 5:
        i += 1
    print("файл закрыт")
    file = open('user_input.txt', 'a')
    h = "Файл filename} открыт для дозаписи"
    print(f' Файл {filename}  открыт   для дозаписи')
    i = 0
    while i <= 5:
        i += 1

    file.close()
    test = True
    while test:
        if (str(input(' Если хотите добавить текст введите 1 или любую цифру для выхода:'))) == "1":
            file = open(filename, 'a')
            file.write(str(input("Введите текст :")) + "\n")
            file.close()
        else:
            test = False
    read_is_file(filename)
    return

def n_3():
    filename = "example.txt"
    print("Файл существует")
    try:
        with open(filename) as file:
            cont = file.read()
    except FileNotFoundError:
        print (f"Запрашиваемый файл {filename} не найден!")

menu()

