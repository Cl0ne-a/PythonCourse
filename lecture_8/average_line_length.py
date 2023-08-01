# Знайти середню довжину рядків у файлі
# Опис: Напишіть програму, яка зчитує файл і знаходить середню довжину рядків у ньому.
# Програма виводить на екран середню довжину рядків.
with open("text\\text.txt", "r") as file:
    all_lines = []
    content = file.readlines()
    for line in content:
        all_lines.append(len(line))
    print(sum(all_lines) // len(all_lines))
