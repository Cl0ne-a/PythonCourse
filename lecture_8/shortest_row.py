# Знайти найкоротший рядок у файлі
# Опис: Напишіть програму, яка зчитує файл і знаходить
# найкоротший рядок у ньому.
# Програма виводить на екран цей найкоротший рядок.
import os

path = os.path.relpath("text", "..\\lecture_8")
text_path = path + "\\text.txt"


with open(text_path, "r+") as source_file:
    text_as_list = list(source_file.readlines())
    min_row_size = len(text_as_list[0].split())
    kv = {}

    for line in text_as_list:
        stripped_len = len(line.split())
        kv[stripped_len] = line

    print("shortest row is \"{row}\" of length {length}"
          .format(row=kv[min(kv.keys())], length=min(kv.keys())))

