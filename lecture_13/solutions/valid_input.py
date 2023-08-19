# Перетворення рядка: Реалізуйте програму, яка приймає рядок від користувача
# та намагається перетворити його в ціле число.
# Якщо це не вдається, виведіть повідомлення "Неможливо перетворити в число".
try:
    user_input = input("what is your age?")
    age = int(user_input)
    print("nice age")
except ValueError:
    print("not a number")