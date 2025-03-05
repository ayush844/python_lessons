from bank_accounts import *

Dave = BankAccount(1000, "Dave")

Sara = BankAccount(3000, "Sara")



Dave.getBalance()


Dave.deposit(3000)


Dave.withdraw(500)

Dave.Transfer(1000, Sara)

Jim = InterestRewardsAcct(5000, "Jim")
Jim.getBalance()
Jim.deposit(100)
Jim.Transfer(100, Dave)


Blaze = SavingsAcct(1000, "Blaze")
Blaze.getBalance()
Blaze.deposit(500)
Blaze.Transfer(500, Dave)