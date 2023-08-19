import sys


def calculator(a, b, op):
    a, b = check_input_is_valid(a, b)

    match op:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            try:
                res = a / b
                return res
            except ZeroDivisionError:
                print("Divider can't be zero")
                sys.exit(1) #
        case _:
            print("Invalid operation. Valid operations are: +, -, *, / ")


def check_input_is_valid(a, b):
    try:
        a = int(a)
        # raise ValueError
    except ValueError:
        print("a cant be parsed to digit")
        sys.exit(1)  #
    try:
        b = int(b)
    except ValueError:
        print("b cant be parsed to digit")
        sys.exit(1)  #
    return a, b


res = calculator(input("a: "), input("b: "), input("operation: "))
print(res)
