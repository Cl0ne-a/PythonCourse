# Пошук найбільшого спільного дільника: Напишіть функцію
# для пошуку найбільшого спільного дільника двох чисел.

def max_common_dev(a, b):
    min_num = min(a, b)
    highest_div = 1
    for n in range(min_num+1)[::-1]:
        if a % n == 0 and b % n == 0:
            highest_div = n
            break

    return highest_div


print(max_common_dev(8, 878))
