# Відфільтруйте парні числа зі списку використовуючи лямбда-функцію та filter.
res = list(filter(lambda x: (x % 2 == 0), [y for y in range(10)]))
print(res)
