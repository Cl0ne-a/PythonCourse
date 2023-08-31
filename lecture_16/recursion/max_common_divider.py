# Напишіть рекурсивну функцію для обчислення найбільшого спільного дільника двох чисел.
def max_common_divider(a, b):
    a_divs = []
    b_divs = []
    for i in range(1, a//2):
        if a%i == 0:
            a_divs.append(i)
    for j in range(1, b//2):
        if b%j == 0:
            b_divs.append(j)
    a_divs.reverse()
    b_divs.reverse()
    for a in a_divs:
        for b in b_divs:
            if a == b:
                return a


max_common_divider(9, 18)