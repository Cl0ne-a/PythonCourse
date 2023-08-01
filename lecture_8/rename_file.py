# Перейменувати файл
# Опис: Напишіть програму, яка перейменовує файл.
# Користувач вводить початкову назву файлу та нову назву, і програма перейменовує файл.
import os
base = "rename"
if base not in os.listdir():
    os.mkdir(base)

source = base + "\\"+input("old name") + ".txt"
dest = base + "\\"+input("new name") + ".txt"


with open(source, "a+") as src:
    src.write(input("say something to put into the file"))
    src.close()


os.renames(source, dest)

# Видалити файл
# Опис: Напишіть програму, яка видаляє файл. Користувач вводить назву файлу, і програма видаляє цей файл.

# file_to_delete = dest
# os.remove(file_to_delete)