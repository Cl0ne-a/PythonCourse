# Відсортуйте список слів за їх довжиною за допомогою лямбда-функції.
words_sorter = lambda words: sorted(words, key=len)

l = ["apple", "orange", "lime"]
print(words_sorter(l))


