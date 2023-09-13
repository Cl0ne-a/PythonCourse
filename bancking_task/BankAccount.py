# Банківський рахунок: Створіть клас BankAccount,
# який має приватні змінні балансу і номеру рахунку.
# Реалізуйте методи для додавання та зняття коштів,
# а також метод для перевірки балансу.
# Забезпечте захист від несанкціонованого доступу до змінних.
import sys


class BankAccount:
    __balance = 0
    __account_number = "123-asd"

    def top_up_balance(self, top_up_sum):
        try:
            if top_up_sum > 0:
                self.__balance += top_up_sum
            else:
                raise ValueError("Invalid value error")

        except ValueError:
            print("You can't update balance with negative value")
            sys.exit()

    def withdraw_from_balance(self, withdraw_sum):
        current_balance = self.__balance
        try:
            if withdraw_sum < current_balance:
                self.__balance -= withdraw_sum
            else:
                raise ValueError("Invalid value error")

        except ValueError:
            print("You can't update balance with negative value")
            sys.exit()

    def get_balance(self):
        return self.__balance
