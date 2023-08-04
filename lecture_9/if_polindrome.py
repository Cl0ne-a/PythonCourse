# Рядки: Створіть програму, яка приймає рядок від користувача
# та перевіряє, чи є він паліндромом (читається однаково зліва направо та справа наліво).
s = "rur"


def check_if_polindrome(s):

    if len(s) % 2 == 0:
        return s[:len(s) // 2:] == s[:len(s) // 2 - 1: -1]
    else:
        return s[:len(s) // 2:] == s[:len(s) // 2: -1]


print(check_if_polindrome(s))
