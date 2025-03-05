class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initialAmount, accName):
        self.balance = initialAmount
        self.name = accName

        print(f"\nAccount '{self.name}' created with initial balance of ${self.balance:.2f}")

    
    def getBalance(self):
        print(f"\nCurrent balance for {self.name}: ${self.balance:.2f}")

    
    def deposit(self, amount):
        self.balance += amount
        print(f"\nDeposited ${amount:.2f} into account '{self.name}'")
        self.getBalance()


    def viableTransaction(self, amount):
        if self.balance - amount < 0:
            raise BalanceException(f"\nInsufficient funds for transaction. Current balance for {self.name} : ${self.balance:.2f}")
        else:
            return
        
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance -= amount
            print(f"\nWithdrew ${amount:.2f} from account '{self.name}'")
            self.getBalance()
        except BalanceException as error:
            print(error)
            self.getBalance()


    def Transfer(self, amount, account):
        print("\n\n***** TRANSFER BEGINS *****")
        try:
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print(f"\nTransferred ${amount:.2f} from account '{self.name}' to account '{account.name}'")
            self.getBalance()
            account.getBalance()
            print("\n***** TRANSFER complete *****\n\n")
        except BalanceException as error:
            print(error)
            self.getBalance()
            account.getBalance()



class InterestRewardsAcct(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount*1.05)
        print(f"\nDeposited ${amount:.2f} into account '{self.name}'")
        self.getBalance()


class SavingsAcct(InterestRewardsAcct):
    def __init__(self, initial_amount, acct_name): 
        super().__init__(initial_amount, acct_name)
        self.fee = 5

    def withdraw(self, amount): 
        try: 
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee) 
            print("\nWithdraw completed.")
            self.getBalance() 
        except BalanceException as error: 
            print(f'\nWithdraw interrupted: {error}')