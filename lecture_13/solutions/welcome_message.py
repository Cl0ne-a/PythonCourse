# Контроль введення: Напишіть програму, яка виводить на екран повідомлення
# "Привіт!" лише тоді, коли користувач вводить слово "hello".
# Якщо введення не відповідає цьому слову, виведіть повідомлення "Невідомий ввід".

class WrongVelcomeException(Exception):
    "Raised when the input massage is no a welcome message"
    pass


welcomes = ["hi", "hello"]

try:
    word = input("have a say")
    if word not in welcomes:
        raise WrongVelcomeException
    else:
        print("Hello")

except WrongVelcomeException:
    print("Exception occurred: Say hi first")
