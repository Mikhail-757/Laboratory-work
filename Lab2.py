import math

def greet(name):
    print(f"Привет, {name}!")

greet('Иван')

def square(number):
    return number * number
result = square(5)
print(result)

def max_of_two(x, y):
    if x >= y:
        return x
    else:
        return y
maximum = max_of_two(3, 6)
print(maximum)

def describe_person(name, age=30):
    print(f"{name}, возраст: {age}")
describe_person("Иван", 20)

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

print(is_prime(29))