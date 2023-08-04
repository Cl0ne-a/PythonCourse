# Кортежі: Напишіть функцію, яка приймає два кортежі однакового розміру
# та повертає новий кортеж, який складається з сум елементів на відповідних
# позиціях у вхідних кортежах.
a = 2
b = 3
c = 4
d = 5
tup1 = (a, b)
tup2 = (c, d)


def sum_by_position(tupl1, tuple2):
    l = []
    for ind in range(len(tupl1)):
        l.append(tupl1[ind] + tuple2[ind])
    return tuple(l)


print(sum_by_position(tup1, tup2))
