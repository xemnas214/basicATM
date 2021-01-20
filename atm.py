from bank import CURRENT_ACCOUNTS, PINS

class ATMController:
    "A Simple ATM Controller"
    def showMessage(self,msg):
        print(msg)

    def readCard(self):
        cardNumber = input()
        if cardNumber in CURRENT_ACCOUNTS:
            return cardNumber
        else:
            raise Exception("Card invalid")

    def readKeyboard(self):
        return input()

    def readNumber(self):
        while True:
            try:
                return int(self.readKeyboard())
            except Exception:
                self.showMessage("Please enter a number")

    def readMoney(self):
        while True:
            try:
                value = int(input())
                if value >= 0:
                    return value
                else:
                    self.showMessage("Invalid amount of money")
            except Exception:
                self.showMessage("Please enter a valid number for money")

    def checkPIN(self, cardNumber, PIN):
        if PINS[cardNumber] != PIN:
            raise Exception("Pin invalid")

    def getAccounts(self, cardNumber, PIN):
        self.checkPIN(cardNumber, PIN)
        accounts = CURRENT_ACCOUNTS[cardNumber]
        return accounts

    def withdraw(self, account):
        self.showMessage("Input your amount for withdraw")
        amount = self.readMoney()
        account.withdraw(amount)
        balance = account.getBalance()
        self.showMessage("Withdrew! Your current balance $" + str(balance))

    def deposit(self, account):
        self.showMessage("Deposit your money. Input the amount")
        amount = self.readMoney()
        account.deposit(amount)
        balance = account.getBalance()
        self.showMessage("Deposited! Your current balance $" + str(balance))

    def start(self):
        self.showMessage("Input your card number")
        try:
            cardNumber = self.readCard()
            self.showMessage("Enter your PIN number")
            PIN = self.readKeyboard()
            accounts = self.getAccounts(cardNumber, PIN)
            self.showMessage("Your accounts")
            for idx, acc in enumerate(accounts):
                self.showMessage(str(idx + 1) + ") " + acc.getNumber())
            self.showMessage("Select your account")
            while True:
                try:
                    selected = self.readNumber() - 1
                    selectedAccount = accounts[selected]
                    break
                except Exception:
                    self.showMessage("Invalid selection. Please enter [1-" + str(len(accounts)) + "]")
            self.showMessage("Account Number: " + selectedAccount.getNumber())
            self.showMessage("Your Balance: $" + str(selectedAccount.getBalance()))
            self.showMessage("What do you want to do?")
            self.showMessage("1. Deposit")
            self.showMessage("2. Withdraw")
            self.showMessage("3. Exit")
            options = {
                1: self.deposit,
                2: self.withdraw,
            }
            while (True):
                option = self.readNumber()
                if option == 3:
                    self.showMessage("Exited")
                    return
                if option in options:
                    options[option](selectedAccount)
                    return
                self.showMessage("Invalid option. Please enter [1-3]")

        except Exception as e:
            self.showMessage(str(e))

        
if __name__ == "__main__":
    ATM = ATMController()
    while True:
        ATM.start()
