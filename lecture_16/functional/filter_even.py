# Відфільтрувати парні числа зі списку використовуючи filter.
l = [2, 3, 4]
ll = filter(lambda elem: elem%2 == 0, l)

print(list(ll))