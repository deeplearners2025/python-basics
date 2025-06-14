class Account :
    def __init__(self, account, balance):
        self.account = account
        self.balance = balance

    def deposit(self, amount):
        print("Depositing amount", amount)
        self.balance += amount

    def show(self):
        print(f"Account number : {self.account}  Balance : {self.balance}")

    def withdraw(self, amount):
        print("Withdrawing amount", amount)
        self.balance -= amount

account = Account("SB-101", 100000)
account.deposit(10000)
account.show()
account.withdraw(5000)
account.show()