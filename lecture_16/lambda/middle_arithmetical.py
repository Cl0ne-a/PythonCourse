# Знайдіть середнє арифметичне чисел у списку за допомогою лямбда-функції.
from functools import reduce

l = [1, 3, 5, 9]


mid_ar = reduce(lambda a,  b: a + b, l)/len(l)


print(mid_ar)