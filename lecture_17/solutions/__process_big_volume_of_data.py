# Обробка великих об'ємів даних:
# Створіть декоратор, який буде автоматично обробляти
# великі об'єми даних, розбиваючи їх на частини.


# def text_breaker(function):
#     def wrapper(path):
#         for line in function(path):
#             yield line
#     return wrapper

def text_breaker(function):
    def wrapper(path):
        yield next(iter(function(path)))
        # for line in iter(function(path)):
        #     yield line
    return wrapper


@text_breaker
def print_text(path):
    yield from open(path, "r").read().split(". ")


print(next(print_text("text.txt")))
print(next(print_text("text.txt")))


# OUTPUT:
# This code defines a fun ction called plus_one that takes a single argument number and returns that number plus
# This code defines a fun ction called plus_one that takes a single argument number and returns that number plus
# This code defines a fun ction called plus_one that takes a single argument number and returns that number plus
# text = iter(list(open("text.txt", "r").read().split(". ")))
#
#
# def reader(some_text):
#     for line in iter(some_text):
#         yield line
#
#
# print(next(reader(text)))
# print(next(reader(text)))
# print(next(reader(text)))
