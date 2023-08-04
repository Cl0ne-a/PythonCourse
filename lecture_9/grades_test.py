# Перевірка ключа: Створіть програму, яка приймає текстовий файл "grades.txt" зі списком студентів і їх оцінками.
# Зчитайте файл та перевірте, чи є у ньому запис про певного студента за іменем.
my_dict = {}
with (open("files\\grades.txt", "r+") as data):
    contents = data.readlines()
    for c in contents:
        line = c.split()
        my_dict[line[0][:-1]] = int(line[1][:-1])

a = input("name").upper()
if a in my_dict.keys():
    print(my_dict[a])
