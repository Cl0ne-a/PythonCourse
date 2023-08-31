# Повторне виконання функції:
# Напишіть декоратор, який дозволить автоматично повторювати
# виконання функції при певних умовах


def re_runner(function):
    def wrapper(num):
        num_start = 1
        while not num_start == num + 1:
            print(function(num_start))
            num_start += 1

    return wrapper


@re_runner
def my_fun(num):
    return num


my_fun(9)