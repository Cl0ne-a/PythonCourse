# Об'єднати два списки за допомогою map.

l1 = ["a", "b", "c"]
l2 = ["d", "e", "f"]

for i in range(3):
    list(lambda a_list, b_list: a_list + b_list, l1)