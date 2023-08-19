# Пошук середнього арифметичного: Напишіть функцію,
# яка знаходить середнє арифметичне для списку чисел.

def mid_arithm(nums):
    s = 0
    for n in nums:
        s += n
    return s / len(nums)


print(mid_arithm([1, 3, 5]))
