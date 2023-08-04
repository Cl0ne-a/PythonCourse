# Списки: Напишіть функцію, яка приймає список чисел і повертає новий список,
# де кожен елемент - квадрат відповідного числа вхідного списку.

list = [1, 4, 6]


def square_elems(list):
    sqaared_elems_list = []
    for el in list:
        sqaared_elems_list.append(el * el)

    return sqaared_elems_list


print(square_elems(list))