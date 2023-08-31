# Обробка великих об'ємів даних:
# Створіть декоратор, який буде автоматично обробляти
# великі об'єми даних, розбиваючи їх на частини.


def text_breaker(function):
    def wrapper(path):
        text = iter(function(path))
        for line in text:
            yield line
    return wrapper


@text_breaker
def print_text(path):
    my_file = open(path, "r")
    text = my_file.read().split(".")
    my_file.close()

    return text


print(next(print_text("text.txt")))
print(next(print_text("text.txt")))
print(next(print_text("text.txt")))
