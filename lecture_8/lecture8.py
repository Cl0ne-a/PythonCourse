import os
# Створіть список, додайте до нього декілька елементів, і потім зробіть його копію за допомогою зрізу та методу list.copy().
# Змініть значення в одному списку і переконайтеся, що другий список залишився незмінним.
my_list = [1, 4, 5, 2]
my_list.insert(3, 4)
my_list.append(0)
my2_list = my_list[0:]
print(my2_list)

# Створіть словник, додайте до нього декілька ключів та значень, і потім зробіть його копію за
# допомогою методу dict.copy(). Змініть значення для одного ключа в одному словнику і переконайтеся,
# що значення в другому словнику залишилися незмінними.

my_dict = {"r": "run"}

my_dict["s"] = "squat"
my2_dict = my_dict.copy()
my_dict["s"] = "sweem"
print(my_dict)
print(my2_dict)

# Завдання: Зчитати вміст файлу
# Опис: Напишіть програму, яка зчитує вміст з файлу "input.txt" та виводить його на екран.
with open("input.txt") as file:
    lines = file.readlines()
    print(lines)

with open("input_and_write.txt", "r+") as file:
    file.write("Hello, World!")
    lines = file.readlines()
    file.close()
    print(lines)

# Завдання: Записати текст у файл
# Опис: Напишіть програму, яка запитує користувача ввести текст і записує його у файл "output.txt".
message = "input()"
with open("output.txt", "r+") as new_file:
    new_file.write(message)
    new_file.readlines()

# Завдання: Перевірити наявність файлу
# Опис: Напишіть програму, яка перевіряє, чи існує файл "dat.txt" у поточній директорії. Якщо файл існує, вивести повідомлення "Файл існує", в іншому випадку - "Файл не знайдено".
res = os.path.exists("dat.txt")
if res:
    print(res)
else:
    print("no such file")

# Завдання: Копіювати файли
# Опис: Напишіть програму, яка копіює вміст файлу "source.txt" в новий файл "destination.txt".
import shutil

with open("source.txt", "w+") as entry:
    new_message = "input()"
    entry.write(new_message)
    print(entry.readlines())

shutil.copy("source.txt", "destination.txt")