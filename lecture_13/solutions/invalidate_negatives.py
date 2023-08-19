class NegativeNumberExceptin(Exception):
    pass


def convert(user_input):
    return user_input * 3, 28084


meter = int(input("number: "))

try:
    if meter < 0:
        raise NegativeNumberExceptin

    else:
        ft = convert(meter)
        print(ft)

except NegativeNumberExceptin:
    print("negative value cannot be input")


