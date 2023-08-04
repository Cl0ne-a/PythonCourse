# Шифрування Цезаря: Реалізуйте алгоритм шифрування Цезаря,
# який шифрує текст з використанням ключа (зсуву)
# та розшифровує зашифрований текст.

from lecture_9.cypher_algorighm.cypher import cipher
from lecture_9.cypher_algorighm.decipher import decipher

word = "Here, all the elements in the list are individual string, so we can use the join function directly. Note that each element in the new string is delimited with a single space."
shift = 2


ciphered = "".join(cipher(word, shift))


print(ciphered)
print("".join(decipher(ciphered, shift)))