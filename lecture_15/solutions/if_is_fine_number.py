# Задача з числами: Реалізуйте функцію, яка перевіряє,
# чи є задане число досконалим (рівним сумі своїх дільників, крім самого себе).
num = 28


def get_dividers_sum(nums) -> []:
    digit_sum = 0
    for num in nums:
        digit_sum = digit_sum + num
    return digit_sum


def get_dividers(number):
    dividers_list = []
    for n in range(number):
        if n == 0:
            pass
        elif number % n == 0:
            dividers_list.append(n)

    return dividers_list


print(get_dividers(num))


def define_if_num_is_perfect(number_in_test):
    return get_dividers_sum(get_dividers(number_in_test)) == number_in_test


print(define_if_num_is_perfect(num))  # example: 28 with dividers [1, 2, 4, 7, 14]
