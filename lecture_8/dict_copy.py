# Завдання: Копіювати словник
# Опис: Напишіть програму, яка створює словник dict1 та копіює його у словник dict2 за
# допомогою функції copy.copy().
# Змініть значення ключа в dict2 і
# виведіть обидва словники, щоб побачити, що вони впливають один на одного.
import copy

dict1 = {1:"a"}
dict2 = copy.copy(dict1)
del dict2[1]
dict2[9] = "w"
print(dict1)
print(dict2)