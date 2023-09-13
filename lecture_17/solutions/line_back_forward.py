# Обернений рядок: Створіть генератор, який буде повертати рядки зі списку
# у зворотньому порядку.

words = ["word", "another word", "some next word"]


def reverse_order(lines):
    lines = reversed(lines)
    for line in lines:
        yield line


res = reverse_order(words)
print(next(res))
print(next(res))
print(next(res))
