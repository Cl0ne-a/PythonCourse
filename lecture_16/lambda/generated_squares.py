# Згенеруйте список квадратів чисел від 1 до 10 за допомогою лямбда-функції та map.
res = list(map(lambda x: x*x, [y for y in range(10)]))

print(res)