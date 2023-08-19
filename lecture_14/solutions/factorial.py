# Обчислення факторіалу: Напишіть функцію для обчислення факторіалу числа.
def fuctorial(n):
    print(n)
    if n == 0 or n == 1:

        return 1
    else:

        return n * fuctorial(n - 1)


print(fuctorial(5))