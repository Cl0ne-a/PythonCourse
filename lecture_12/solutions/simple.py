# Завдання: Генерація списку квадратів чисел
# Створіть список, що містить квадрати чисел від 1 до 10, за допомогою List Comprehension.

gen_list = [x * x for x in range(10)]
print(gen_list)

# авдання: Створення словника зі списку
# Дано список слів. Створіть словник, де ключами будуть слова, а значеннями - їх довжина, за допомогою Dictionary Comprehension.
words = ["apple", "banana", "grapes"]
gen_dict = {x: len(x) for x in words}
print(gen_dict)

# Завдання: Фільтрація списку чисел за парність
# Дано список чисел. Створіть список, що містить тільки парні числа з вихідного списку, за допомогою List Comprehension.
nums_list = [1, 3, 1, 2, 4, 5, 4, 3]

duplicated_list = [x for x in nums_list if x in nums_list[nums_list.index(x) + 1:]]
print(set(duplicated_list))

# Завдання: Генерація множини кубів чисел
# Створіть множину, що містить куби чисел від 1 до 7, за допомогою Set Comprehension.
gen_set = {pow(x, 3) for x in range(10)}
print(gen_set)

# Завдання: Фільтрація словника за умовою
# Дано словник зі студентами та їх віками. Створіть новий словник, що містить тільки тих студентів, вік яких менше 25 років, за допомогою Dictionary Comprehension.
ful_dict = {"a": 40, "b": 20, "c": 30}
filtered_dict = {x: y for x, y in ful_dict.items() if y < 25}
print(filtered_dict)

# Завдання: Створення списку з великими літерами
# Дано список слів. Створіть список, де кожне слово записано великими літерами, за допомогою List Comprehension.
words2 = ["apple", "banana", "grapes"]
words2_upper = [w.upper() for w in words2]
print(words2_upper)

# Завдання: Видалення дублікатів зі списку
# Дано список чисел. Створіть список, де видалено всі дублікати чисел, за допомогою List Comprehension.
list1 = [1, 2, 3, 1]
print(set(list1))

# Завдання: Створення словника з пар чисел
# Дано два списки: один містить ключі, інший - відповідні значення. Створіть словник, використовуючи ці два списки, за допомогою Dictionary Comprehension.
l1 = ["a", "b"]
l2 = [1, 3]
print({x: l2[l1.index(x)] for x in l1})

# Завдання: Фільтрація списку слів за довжиною
# Дано список слів. Створіть список, що містить слова з довжиною більше 5 літер, за допомогою List Comprehension.
words3 = ["apple", "banana", "grapes"]
print([w for w in words3 if len(w) > 5])
