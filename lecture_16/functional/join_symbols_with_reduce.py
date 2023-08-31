# Об'єднати символи рядка в одну строку за допомогою reduce.
from functools import reduce

line = "a b c d".split(" ")

res = reduce(lambda a, b: a + b, line)
print(res)
