squares_dict = {x: x ** 2 for x in range(1, 6)}

print(squares_dict)

t = "text"
for i in enumerate(t):
    print(i)

# Завдання: Генерація словника квадратів чисел
my_dict = {x: x ** 2 for x in range(10)}
print(my_dict)
my_dict2 = {x: x * 2 for x in range(1, 20, 2)}
print(my_dict2)
# Злиття двох словників
my_dict.update(my_dict2)
print(my_dict)
# Перетворення рядка в словник літер та їх кількостей
line = "my new line"
dicted = {char: line.count(char) for char in line}
print(dicted)
# Відфільтрувати словник
filtered = {char for char in line if char != ' '}
print(filtered)

# Завдання: Генерація множини квадратів чисел
s = {i*i for i in range(4)}
print(s)
# Завдання: Видалення дублікатів зі списку
l = [1, 1, 3, 2, 4, 3]
s2 = {i for i in l}
print(s2)
# Завдання: Виявлення спільних літер у словах
w1 = "text"
w2 = "tax"
s3 = {i for i in w1 if i in w2}
print(s3)
# Завдання: Генерація множини символів у рядку
# Завдання: Перетин множин
i1 = {1, 2, 3}
i2 = {2, 4, 1}
s4 = {i for i in i1 if i in i2}
print(s4)

