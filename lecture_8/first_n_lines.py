import os

path = os.path.relpath("text", "..\\lecture_8")
text_path = path + "\\text.txt"
n = 3

with open(text_path, "r") as text:
    for i in range(n):
        line = next(text).strip()
        print(line)