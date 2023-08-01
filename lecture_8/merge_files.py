# Завдання: Об'єднати вміст декількох файлів
# Опис: Напишіть програму, яка об'єднує вміст трьох файлів
# "file1.txt", "file2.txt" і "file3.txt" і записує його в новий файл "merged.txt".
import os

if not "files" in os.listdir("..\\lecture_8"):
    os.mkdir("..\\lecture_8\\files")

text = []

with open("files\\file1.txt", "w+") as file1:
    file1.write("file1")

with open("files\\file2.txt", "w+") as file2:
    file2.write("file2")

with open("files\\file3.txt", "w+") as file3:
    file3.write("file3")

merging_list = []

for f in os.listdir("..\\lecture_8\\files"):
    if os.path.basename(f).title() != "merged.txt":
        with open("..\\lecture_8\\files\\" + f, "r+") as file:
            text = file.read()
            merging_list.append(text + "\n")

with open("files\\merged.txt", "w") as merged:
    for message in merging_list:
        merged.write(message)




