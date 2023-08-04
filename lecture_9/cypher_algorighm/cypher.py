import string

from lecture_9.cypher_algorighm.const import punctuation, letters_list


def shift_by_key(letter, key, alphabet_letters):
    if letter == ' ' or letter in punctuation:
        return str(letter)
    elif letter.isdigit():
        return str(int(letter) * key)
    elif alphabet_letters.index(letter) + key >= len(alphabet_letters):
        ind = len(alphabet_letters) - alphabet_letters.index(letter) - 2
    else:
        ind = alphabet_letters.index(letter) + key
    return alphabet_letters[ind]


def cipher(string, shift):
    new_line = []
    for s in string:
        new_line.append(shift_by_key(s, shift, letters_list))

    return new_line
