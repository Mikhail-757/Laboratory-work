def main_menu():
    print("\nМеню:")
    print("1 - Защита данных пользователя.")
    print("2 - Полиморфизм и наследование.")
    print("0 - Выход.")

    while True:
        choice = input("Введите номер задания или 0 для выхода: ")

        if choice in ["1", "2", "0"]:
            break
        else:
            print("Неверный ввод. Попробуйте еще раз.")

    if choice == "1":
        n_1()
    elif choice == "2":
        n_2()
    elif choice == "0":
        return

def n_1():
    print("\nЗадание 1:")

    class UserAccount:
        def __init__(self, username, email, password):
            self.username = username
            self.email = email
            self.password = password

        def set_password(self, new_password):
            if len(new_password) >= 8:
                self.password = new_password
                print("Пароль успешно изменен.")
            else:
                print("Новый пароль слишком короткий. Он должен содержать минимум 8 символов.")

        def check_password(self, password):
            return self.password == password

    user = UserAccount('Mikhail', 'Mikhail@gmail.com', '12345678')
    print(f"Текущий пароль:{user.password}")

    new_username = input("Введите новое имя пользователя: ")
    while True:
        new_pass = input("Введите новый пароль (пароль должен содержать минимум 8 символов):")
        if len(new_pass) >= 8:
            user.set_password(new_pass)
            break
        else:
            print("Пароль слишком короткий! Должен содержать минимум 8 символов.")

    if user.check_password(new_pass):
        print(f"Пользователь {new_username} создан! Новый пароль: {new_pass}")
    else:
        print("Ошибка при проверке нового пароля. Введите пароль корректно.")

    main_menu()


def n_2():
    print("\nЗадание 2:")

    class Vehicle:
        def __init__(self, make, model):
            self.make = make
            self.model = model

        def get_info(self):
            return f"{self.make} {self.model}"

    class Car(Vehicle):
        def __init__(self, make, model, fuel_type):
            super().__init__(make, model)
            self.fuel_type = fuel_type

        def get_info(self):
            info = super().get_info()
            return f"{info}, Fuel type: {self.fuel_type}"

    car = Car('Volkswagen', 'Golf', 95)
    print(car.get_info())

    main_menu()

if __name__ == "__main__":
    main_menu()