# Поділ на парні та непарні: Напишіть функцію,
# яка розділить список чисел на парні та непарні.

def odd_even(mixed_list):
    odd = [o for o in mixed_list if o % 2 != 0]
    even = [e for e in mixed_list if e & 2 == 0]
    return odd, even


print(odd_even([7, 4, 8, 9, 6, 80, 88, 2]))
