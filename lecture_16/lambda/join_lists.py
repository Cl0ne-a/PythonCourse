# Об'єднайте два списки в один за допомогою лямбда-функції та reduce.

a_list = ["a", "b"]
b_list = ["c", "d"]

joined = [a_list.append(x) for x in b_list]

# why reduce ?
print(a_list)