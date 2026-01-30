from models.Bankaccount import Bankaccount
my_account = Bankaccount(1000)
your_account = Bankaccount(500)
our_account = my_account + your_account
our_account -= your_account
print("My account:", our_account)