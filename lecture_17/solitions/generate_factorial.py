# Факторіали: Створіть генератор, який буде обчислювати факторіал для заданого числа.
def gen_factorial(num):
    if num == 1 or num == 0:
        yield 1
    else:
        yield num * (next(gen_factorial(num - 1)))


res = gen_factorial(5)


print(next(res))
