# Перетворити список рядків на список їх заголовків
# (перша буква велика, інші малі) використовуючи map.
import re

text = "Hello my friend.This is amazing day."

splitted_text = [x for x in re.split("[//.|//!|//?]", text) if x != ""]

res = list(map(lambda word: word.split(" ")[0], splitted_text))

print(res)
