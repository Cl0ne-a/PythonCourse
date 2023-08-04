# Читання з файлу: Створіть функцію, яка зчитує числа з
# текстового файлу "numbers.txt", сортує їх у порядку спадання
# та записує в інший файл "sorted_numbers.txt".
def make_bubblesort(list):
    for i in range(len(list) - 1):
        for j in range(len(list) - i - 1):
            if list[j] < list[j + 1]:
                tmp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = tmp
    return list


with open("files\\numbers.txt", "r") as file:
    list = file.read().split(", ")
    nums = []
    for el in list:
        nums.append(int(el))
    make_bubblesort(nums)

with open("files\\sorted_numbers.txt", "w+") as f:
    for num in nums:
        f.write(f"{str(num)}\n")
    print(nums)