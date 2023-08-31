# Реалізуйте рекурсивну функцію для обчислення числа ступеня.

def power_of(num, pow):
    if pow == 1:
        return num
    else:
        return num * power_of(num, pow - 1)


print(power_of(2, 5))