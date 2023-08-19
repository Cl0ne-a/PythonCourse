from lecture_13.solutions.custom_ex import NegativeNumberException


def convert(user_input):
    return user_input * 3.28084


meter = int(input("number: "))

try:
    ft = convert(meter)
    print(ft)
except NegativeNumberException:
    print("negative is not allowed")


