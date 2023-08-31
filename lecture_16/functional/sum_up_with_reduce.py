# Обчислити суму елементів списку використовуючи reduce.
from functools import reduce

l = [2, 7, 101]

summed = reduce(lambda a, b: a + b, l)

print(summed)