import math
import datetime
from mypackage import add, subtract, multiply
from mypackage import reverse_str

def f():
    a = 16
    d = math.sqrt(a)
    print('результат', d)
    dt_now = datetime.datetime.now()
    print(dt_now)
    return

def n():
    d = my_module.sum(2, 3)
    print('Сумма', d)
    return

def b():
    sum_result = add(5, 7)
    difference = subtract(15, 8)
    product = multiply(3, 9)
    reversed_s = reverse_str("Привет")

    print(f"Сумма 5 и 7 = {sum_result}")
    print(f"Разница между 15 и 8 = {difference}")
    print(f"Произведение 3 и 9 = {product}")
    print(f"Реверс 'Привет': {reversed_s}")

c = int(input('Введите номер задания: '))

if c == 1:
    f()
elif c == 2:
    n()
elif c == 3:
    b()
