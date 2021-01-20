class Account:
    def __init__(self, number, balance):
        self.number = number
        self.balance = balance

    def getNumber(self):
        return self.number

    def getBalance(self):
        return self.balance 

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance-=amount
            return amount
        else:
            raise Exception("Abort! The amount exceed your balance")

    def deposit(self, amount):
        self.balance+=amount