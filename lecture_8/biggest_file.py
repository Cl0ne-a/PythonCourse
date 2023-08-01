# Завдання: Знайти найбільший файл у директорії
# Опис: Напишіть програму, яка знаходить найбільший файл у поточній директорії та виводить його назву та розмір.
import os

base_path = os.path.abspath("..")
dir_size_dict = {}
directories = os.listdir(base_path)


def is_directory(path):
    return os.path.isdir(path)


def get_subdirs(initial_path, d):
    base_path = initial_path + "\\" + d

    if is_directory(base_path):
        dir_size_dict[d] = os.path.getsize(base_path)

        for elem in os.listdir(base_path):
            if is_directory(base_path + "\\"+ elem):
                get_subdirs(base_path, elem)


for d in directories:
    get_subdirs(base_path, d)

max_size = max(dir_size_dict.values())
for k, v in dir_size_dict.items():
    if v == max_size:
        print("Max directory: {directory}: {size}".format(directory=k, size=v))