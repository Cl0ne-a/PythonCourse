# Перетворіть список рядків на список їх довжин за допомогою лямбда-функції.
conv = lambda line: len(line)

l = ["apple", "orange"]

for elem in l:
    print(conv(elem))

