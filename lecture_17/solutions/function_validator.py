# Перевірка правильності реалізації функції: Напишіть декоратор, який буде перевіряти, чи функція повертає правильний результат.
import re


def name_validator(function):
    def wrapper():
        name = function()
        if re.match("^[A-Za-z_-]*$", name):
            print(f'input {name} is valid')
            return name
        else:
            print("input invalid")
            pass

    return wrapper


@name_validator
def get_user_name():
    return input("Name: ")


t = get_user_name()
print(t.upper() if t is not None else "")
