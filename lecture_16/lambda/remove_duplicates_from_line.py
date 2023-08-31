# Видаліть дублікати зі списку за допомогою лямбда-функції та set.

l = ["ana", "ana", "bamboo", "toy", "taboo", "toy"]
# a / 10 if a < 20 else a


filtered = lambda w: set(w)


res = filtered(l)

print(res)