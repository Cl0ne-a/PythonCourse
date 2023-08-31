# Знайдіть суму всіх елементів списку за допомогою лямбда-функції та reduce.
from functools import reduce

l = [2, 5, 3]

res = reduce(lambda a, b: a + b, l)

print(res)