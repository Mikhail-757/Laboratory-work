def task_1():
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(my_list[0])
    print(my_list[2])
    print(my_list[-1])

def task_2():
    for i in range(1, 11):
        print(i)
    i = 10
    while i >= 1:
        print(i)
        i -= 1

def task_3():
    num = int(input("Введите число: "))
    if num % 2 == 0:
        print("Число четное")
    else:
        print("Число нечетное")
    num = int(input("Введите число: "))
    if num > 0:
        print("Число положительное")
    elif num < 0:
        print("Число отрицательное")
    else:
        print("Число равно нулю")

def task_4():
    number = int(input("Введите число: "))

    for i in range(1, number + 1):
        print(i)

def task_5():
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))

    if num1 > num2:
        print(f"Больше число: {num1}")
    elif num2 > num1:
        print(f"Больше число: {num2}")
    else:
        print("Числа равны")

def main_menu():
    while True:
        print("\nМеню:")
        print("1 - Задание № 1")
        print("2 - Задание № 2")
        print("3 - Задание № 3")
        print("4 - Домашнее задание 1")
        print("5 - Домашнее задание 2")
        print("0 - Выход из программы")

        choice = input("Выберите № задания: ")

        if choice == '1':
            task_1()
        elif choice == '2':
            task_2()
        elif choice == '3':
            task_3()
        elif choice == '4':
            task_4()
        elif choice == '5':
            task_5()
        elif choice == '0':
            break
        else:
            print("Нужно выбрать номер из вариантов представленных выше!")
main_menu()

