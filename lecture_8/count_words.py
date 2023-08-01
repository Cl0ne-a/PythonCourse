import re
import os

path = os.path.relpath("text", "..\\lecture_8")
text_path = path + "\\text.txt"


with open(text_path, "r+") as source_file:
    text = source_file.readlines()


r = re.compile("\\w+")
count = 0


for line in text:
    count = count + len(r.findall(line))


print("Number of words in line {n}".format(n=count))