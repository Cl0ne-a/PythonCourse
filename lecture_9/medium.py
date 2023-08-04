# Пошук у списку: Напишіть функцію для сортування списку чисел методом бульбашки (bubble sort).
list_to_sort = [4, 1, 6, 3, 2, 8, 10, 0]

def sort(unsorted_list):
    for index in range(len(unsorted_list) - 1):
        for inner_index in range(0, len(unsorted_list) - index - 1):
            if unsorted_list[inner_index] > unsorted_list[inner_index + 1]:
                temp = list_to_sort[inner_index]
                unsorted_list[inner_index] = unsorted_list[inner_index + 1]
                unsorted_list[inner_index + 1] = temp

sort(list_to_sort)
print(list_to_sort)

# Читання та обробка файлу: Створіть програму, яка зчитує текстовий файл "data.csv" з даними
# у форматі CSV (Comma-Separated Values) та обчислює середнє значення чисел у кожному рядку,
# записуючи результати у новий файл "averages.txt".
data_list = []
with open("files\\data.csv", "r+") as data:
    lines = data.readlines()
    for line in lines:
        broken_line = line.split(",")
        for elem in broken_line:
            n_of_elems = 0
            sum_of_elems = 0
            if elem.isdigit():
                sum_of_elems = sum_of_elems + int(elem)
                n_of_elems = n_of_elems + 1
            if n_of_elems != 0:
                res = sum_of_elems // n_of_elems
                data_list.append(res)

with open("files\\averages.txt", "w") as averages:
    averages.write(str(data_list))
