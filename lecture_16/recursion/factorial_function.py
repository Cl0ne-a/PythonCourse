def calc_factorial(num) :
    if num == 0 or num == 1:
        return 1
    else:
        return num * calc_factorial(num - 1)


print(calc_factorial(6))