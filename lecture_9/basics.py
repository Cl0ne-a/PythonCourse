# Змінні: Створіть змінну "x" і присвойте їй значення 10.
# Потім виведіть її значення на екран.
import os

x = 10
print("Variable: {x}".format(x=x))

# Числа: Обчисліть площу прямокутника з довжиною 5 і шириною 3.
# Результат виведіть на екран.

l = 5
w = 3
print("Square: {s}".format(s=l * w))

# Словники: Створіть словник "ages" з ключами "John" і "Alice"
# та значеннями 25 і 30 відповідно.
# Виведіть вік Alice на екран.
ages = {"John": 25, "Alice": 30}
print("Alice's age is {a}".format(a=ages.get("Alice")))

# Кортежі: Створіть кортеж з трьох елементів: 1, 2 та 3. Перевірте, чи є число 2 в цьому кортежі.
cort = {1, 2, 3}
print("If 2 is in tuple: {d}".format(d=(2 in cort)))

# Множини: Створіть множину "set1" з елементами 1, 2 та 3,
# і множину "set2" з елементами 3, 4 та 5.
# Об'єднайте ці дві множини і виведіть результат.
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print("United set1 and set2: {s}".format(s=set1.union(set2)))

# Читання з файлу: Створіть текстовий файл "example.txt"
# і запишіть у нього декілька рядків тексту.
# Потім відкрийте цей файл і виведіть його вміст на екран.
with open("..\\lecture_9\\files\\example.txt", "w+") as file:
    file.write("Abu Dhabi")
    file.seek(0)
    print(file.read())

# Запис у файл: Створіть список "names" з іменами "John", "Alice" та "Bob".
# Запишіть цей список в текстовий файл "names.txt", кожне ім'я на окремому рядку.
basic_bath = "..\\lecture_9\\files"
if not os.path.exists(basic_bath):
    os.mkdir(basic_bath)
names_list = ["John", "Alice", "Bob"]
"\n".join(names_list)
with open(basic_bath + "\\" + "names.txt", "w") as names_file_writer:
    for name in "\n".join(names_list).split():
        names_file_writer.write(name + "\n")

# Обчислення: Обчисліть суму чисел від 1 до 10 (включно) і виведіть результат.
s = 0
for i in range(10):
    s = s + i
print("Summed 1...10: {sum}".format(sum=s))
# Зріз рядка: Задано рядок "Hello, world!". Виведіть перші 5 символів цього рядка.
line = "Hello, world!"
print("Slice: {slice}".format(slice=line[:5]))
