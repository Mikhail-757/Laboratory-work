import math
from typing import get_origin

def menu():
    choice = int(input("Введите номер задания: "))
    if choice == 1:
        n_1()
    elif choice == 2:
        n_2()
    else:
        print("Неверный выбор.")

def n_1():
    class Book:
        def __init__(self, title, author, year):
            self.title = title
            self.author = author
            self.year = year

        def get_info(self):
            return f"Название книги: {self.title}, Автор: {self.author}, Год издания: {self.year}"

    book1 = Book("Путешествие Гулливера", "Джонатан Свифт", 1726)
    book2 = Book("Собачье сердце", "Булгаков", 1924)

    print(book1.get_info())
    print(book2.get_info())
    return

def n_2():
    class Circle:
        def __init__(self, radius):
            self.radius = radius

        def get_radius(self):
            return self.radius

        def set_radius(self, new_radius):
            self.radius = new_radius
            return
        def get_square(self):
            self.get_square = math.pi*self.radius**2
            return self.get_square
        def get_perimetr(self):
            self.get_perimetr = 2 * math.pi*self.radius
            return self.get_perimetr

    old_radius = float(input("Введите исходный радиус: "))
    new_radius = float(input("Введите новый радиус: "))

    circle1 = Circle(old_radius)
    print(f"Изначальный радиус: {circle1.get_radius()}")
    circle1.set_radius(new_radius)
    print(f"Новый радиус: {circle1.get_radius()}")
    print(f'Площадь: {circle1.get_square()}')
    print(f"Периметр: {circle1.get_perimetr()}")

menu()

