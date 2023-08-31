# Створіть рекурсивну функцію для знаходження найбільшого елемента в списку.

def max_elem(elems_list):
    if len(elems_list) == 1:
        return elems_list[0]
    else:
        return max(elems_list[0], max_elem(elems_list[1:]))


print(max_elem([1000, 3, 2, 7, 100]))