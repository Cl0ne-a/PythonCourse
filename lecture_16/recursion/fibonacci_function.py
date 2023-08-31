# Реалізуйте рекурсивну функцію для обчислення чисел Фібоначчі.
# 0 + 1 + 1 + 2 + 3 + 5 + 8 + 13
def calc_fibonacci__(num):
    fib_nums = [0, 1, 1]
    while fib_nums[len(fib_nums) - 1] <= num:
        fib_nums.append(fib_nums[len(fib_nums) - 1] + fib_nums[len(fib_nums) - 2])
    fib_nums.pop(len(fib_nums) - 1)
    print(fib_nums)


calc_fibonacci__(120000)


def fibonacci_of(n):
    if n in {0, 1}:  # Base case
        return n
    return fibonacci_of(n - 1) + fibonacci_of(n - 2)  # Recursive case


print([fibonacci_of(x) for x in range(26)])