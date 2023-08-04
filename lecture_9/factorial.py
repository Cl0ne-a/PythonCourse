# Обчислення: Напишіть функцію, яка знаходить факторіал заданого числа N рекурсивно.
def factorial(n):
    num = 1
    for i in (x+1 for x in range(n)):
        num = num*i

    print(f"factorial: {num}")


factorial(1)
factorial(2)
factorial(3)
factorial(4)
factorial(5)
