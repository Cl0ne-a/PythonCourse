# Напишіть рекурсивну функцію для обчислення числа цифр у заданому числі.
def sum_up_digits(num):
    if num < 10:
        return num
    else:
        return num%10 + sum_up_digits(num//10)


print(sum_up_digits(101206))