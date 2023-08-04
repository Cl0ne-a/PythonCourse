# Запис у файл: Напишіть програму, яка зчитує
# великий текстовий файл "big_file.txt"
# та створює новий файл "shortened_file.txt",
# в якому кожен рядок містить не більше 50 символів.

with open("files\\big_file.txt", "r") as big_file:
    content = big_file.readlines()
    with open("files\\shortened_file.txt", "w+") as sh_file:
        for line in content:
            sh_file.write(f"\n{line[:50]}")

        sh_file.seek(0)
        print(sh_file.read())
