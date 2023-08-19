# Підрахунок геометричної прогресії: Напишіть функцію,
# яка обчислює суму перших n членів геометричної прогресії.


# Sn = a + ar + a*a*r+ a*a*a*r +…+ ..
#      1 + 1*3 * 1*3*3 + 1*3*3*3 ...

def geometric_progression(r, max_num):
    s = 1
    p = 2
    print(1)
    while s <= max_num:
        num = pow(r, p - 1)
        s += num
        p += 1
        print(num)

    return s


print(geometric_progression(4, 1000))
