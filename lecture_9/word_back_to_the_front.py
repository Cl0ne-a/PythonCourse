# Операції зі списками: Напишіть функцію, яка приймає список слів
# та повертає список, в якому кожне слово написано задом наперед.
my_list = ["apple", "carrot", "salmon"]


def revert_letters_order(some_list):
    for word in some_list:
        some_list[some_list.index(word)] = word[::-1]


revert_letters_order(my_list)
print(my_list)
