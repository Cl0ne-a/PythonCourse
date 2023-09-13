# Кастомні логи: Створіть декоратор,
# який дозволить користувачу задавати кастомні повідомлення для логування.


def logger(function):
    def wrapper(message, message_for_logger, another_message):
        print(f'{function(another_message)} {message}!  \n{message_for_logger}')

    return wrapper


@logger
def set_log(*args):
    if len(args) >=3:
        return args[2]
    else:
        return args[0]


set_log("there","it's me",  "hi")