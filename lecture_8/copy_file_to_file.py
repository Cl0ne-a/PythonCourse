# Скопіювати вміст одного файлу в інший
# Опис: Напишіть програму, яка копіює вміст одного файлу в інший.
# Користувач вводить назви двох файлів, і програма копіює вміст з першого файлу в другий.
import os

basic_path = os.path.relpath("text", "..\\lecture_8")
source = basic_path + "\\text.txt"
dest = basic_path + "\\{name}.txt".format(name=input("name"))

cmd = f'copy "{source}" "{dest}"'

os.system(cmd)

with open(dest, "r") as file:
    cnt = file.readlines()
    print(cnt)
