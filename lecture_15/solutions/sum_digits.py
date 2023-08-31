# Задача з функціями: Створіть функцію, яка обчислює суму цифр заданого числа.

def sum_digits(num):
    digits_sum = 0
    while num > 0:
        digits_sum += num % 10
        num //= 10
    return digits_sum

print(sum_digits(1220))