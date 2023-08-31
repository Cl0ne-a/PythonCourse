# Парні числа: Напишіть генератор, який буде генерувати послідовність парних чисел.
def generate_even(max_num):
    evens = []
    for i in range(1, max_num + 1):
        if i%2 == 0:
            evens.append(i)

    yield iter(evens)


vals = generate_even(10)

for val in vals:
    print(next(val))
    print(next(val))
    print(next(val))
    print(next(val))
    print(next(val))
