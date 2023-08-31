# Напишіть рекурсивну функцію для підрахунку суми елементів списку.
def sum_elems(list):
    if len(list) == 0:
        return 0

    else:
        return list[0] + sum_elems(list[1:])


elems = [1, 3, 6, 5, 5]

a = sum_elems(elems)
print(a)