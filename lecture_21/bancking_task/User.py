from lecture_21.bancking_task.BankAccount import BankAccount

account = BankAccount()

account.top_up_balance(20)
account.top_up_balance(30)
account.top_up_balance(-10)
account.withdraw_from_balance(10)

print(account.get_balance())

