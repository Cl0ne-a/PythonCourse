# Логування параметрів і результатів:
# Напишіть декоратор, який буде логувати параметри виклику та результати функції.
#
# def decorator_fun(func):
#     def inner():
#         current_time = "12:00"
#         return func() + current_time
#
#     return inner
#
#
# @decorator_fun
# def func_to():
#     return "current time is "
#
#
# print(func_to())
from datetime import time, datetime


def logger(function):
    def wrapper(name):
        print(f'Function arguments: {name}')
        person_name = function(name)
        print(f'Hi there. {person_name}, for your attention - you are being wrapped')

        now = datetime.now()

        print(now.strftime("%H:%M:%S"))

        
    return wrapper


@logger
def get_name(name):
    return name


get_name("Anna")