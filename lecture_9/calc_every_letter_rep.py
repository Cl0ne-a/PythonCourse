# Словники: Створіть програму, яка приймає рядок від користувача
# та підраховує кількість кожної літери в рядку,
# записуючи результат у словник, де ключі - літери, а значення - кількість їх зустрічань.

s = "Have a nice day today and always".lower()
incr = 1

dict = {}


def count_letter_repetitions(line):
    for character in line:
        if dict.__contains__(character):
            val = dict[character]
            dict[character] = val + incr
        elif character == " ":
            print("Skipping space")
        else:
            dict[character] = incr


count_letter_repetitions(s)

print(dict)
