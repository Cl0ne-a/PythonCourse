# Шифрування Цезаря: Реалізуйте алгоритм шифрування Цезаря,
# який шифрує текст з використанням ключа (зсуву)
# та розшифровує зашифрований текст.

import string

letters_list = string.ascii_letters


def shift_by_key(letter, key, alphabet_letters):
    if letter == ' ' or letter in string.punctuation:
        return str(letter)
    elif letter.isdigit():
        return str(int(letter) * key)
    elif alphabet_letters.index(letter) + key >= len(alphabet_letters):
        ind = len(alphabet_letters) - alphabet_letters.index(letter) - 2
    else:
        ind = alphabet_letters.index(letter) + key
    return alphabet_letters[ind]

def shift_back_by_key(letter, key, alphabet_letters):
    if letter == ' ' or letter in string.punctuation:
        return str(letter)
    elif letter.isdigit():
        return str(int(letter) // key)
    elif alphabet_letters.index(letter) - key < 0:
        ind = len(alphabet_letters) - (key - (alphabet_letters.index(letter)))
    else:
        ind = alphabet_letters.index(letter) - key
    return alphabet_letters[ind]


word = "Here, all the elements in the list are individual string, so we can use the join function directly. Note that each element in the new string is delimited with a single space."
shift = 2


def cipher(string):
    new_line = []
    for s in string:
        new_line.append(shift_by_key(s, shift, letters_list))

    return new_line


ciphered = "".join(cipher(word))

print(ciphered)


def decipher(string):
    new_line = []
    for s in string:
        new_line.append(shift_back_by_key(s, shift, letters_list))

    return new_line


print("".join(decipher(ciphered)))