class Account:
    def __init__(self, accNum, accHolder, bal=0):
        self.accountNumber = accNum
        self.accountHolder = accHolder
        self.balance = bal

    def deposit(self, amount):
        self.balance += amount
        print("You have deposited " + amount + " Rupees")

    def withdraw(self, amount):
        if (self.balance >= amount):
            self.balance -= amount
            print("You have withdrawn " + amount + " Rupees")
        else:
            print("Sorry, Insufficient Balance!")


class Savings_Account(Account):
    def __init__(self, accNum, accHolder, bal, intRate):
        super.__init__(accNum, accHolder, bal)
        self.interestRate = intRate

    def calculate_interest(self):
        return self.balance * (self.interestRate / 100)