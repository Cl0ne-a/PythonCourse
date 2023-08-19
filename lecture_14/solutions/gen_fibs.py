# Генерація послідовності Фібоначчі: Напишіть функцію, яка генерує послідовність Фібоначчі до заданого числа.
# 1 1 2 3 5 8
def gen_fibonacci(num):
    l = []
    for ind in range(num):
        if ind == 0:
            l.append(1)
            print(1)
        elif ind == 1:
            print(1)
            l.append(1)
        elif ind == 2:
            print(2)
            l.append(2)
        else:
            print(l[ind-1] + l[ind - 2])
            l.append(l[ind-1] + l[ind - 2])

    return l



gen_fibonacci(9)