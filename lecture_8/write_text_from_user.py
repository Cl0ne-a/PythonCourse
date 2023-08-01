# Записати текст у файл
# Опис: Напишіть програму, яка зчитує текст від користувача і записує
# його у файл з заданою назвою. Користувач вводить текст, і програма створює
# або перезаписує файл з цим текстом.
import os

# name = input("file without extension")
base_path = "..\\lecture_8\\msm"
if not os.path.exists(base_path):
    os.mkdir(base_path)

with open(base_path + "\\" + input("filename") + ".txt", "w") as file:
    file.write(input("write your message"))