# Відсортуйте слова у реченні за їх довжиною використовуючи лямбда-функцію та sorted


line = "this is hello world"


res = sorted(line.split(), key=len)


print(res)
