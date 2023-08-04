import string

from lecture_9.cypher_algorighm.const import letters_list, punctuation


def shift_back_by_key(letter, key, alphabet_letters):
    if letter == ' ' or letter in punctuation:
        return str(letter)
    elif letter.isdigit():
        return str(int(letter) // key)
    elif alphabet_letters.index(letter) - key < 0:
        ind = len(alphabet_letters) - (key - (alphabet_letters.index(letter)))
    else:
        ind = alphabet_letters.index(letter) - key
    return alphabet_letters[ind]


def decipher(string, shift):
    new_line = []
    for s in string:
        new_line.append(shift_back_by_key(s, shift, letters_list))

    return new_line
