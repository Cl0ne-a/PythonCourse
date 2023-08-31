# Задача з рядками: Напишіть функцію, яка приймає рядок і
# повертає рядок, де всі слова великими літерами зберігають першу та останню літеру, а інші літери в нижньому регістрі.
import re
import string


def restyle_word_if_upper(line):

    for arg in line.split():

        if arg.isupper() and len(arg) > 1:
            rep = arg[0] + arg[1:-1].lower() + arg[-1]
            line = line.replace(arg, rep)
    print(line)


restyle_word_if_upper("I be THRONE like")
