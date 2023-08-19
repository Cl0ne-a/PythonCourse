# Зворотний рядок: Напишіть функцію, яка повертає зворотний рядок для даного рядка.
sent = "Even a small step forward makes you small step closer to the goal!"


def revert_row(line) -> str:
    return line[::-1]


print(revert_row(sent))