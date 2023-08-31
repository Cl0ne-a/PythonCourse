# Задача зі списками: Напишіть функцію, яка приймає список чисел і
# повертає новий список, де елементи впорядковані за зростанням.

def reorder_nums_ascending(some_list):
    some_list.sort()
    return some_list


print(reorder_nums_ascending([2, 1, 4]))