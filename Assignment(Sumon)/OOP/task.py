# Banking System using Constructor, Methods and Inheritance

class BankAccount:

    def __init__(self, account_name, account_number, balance):
        self.account_name = account_name
        self.account_number = account_number
        self.balance = balance

    def display_info(self):
        print("\n--- Account Information ---")
        print("Name:", self.account_name)
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)
        print("New Balance:", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
            print("New Balance:", self.balance)
        else:
            print("Insufficient balance.")

class SavingsAccount(BankAccount):

    def __init__(self, account_name, account_number, balance, interest_rate):
        self.account_name = account_name
        self.account_number = account_number
        self.balance = balance
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * self.interest_rate / 100
        print("Interest:", interest)

class CurrentAccount(BankAccount):

    def __init__(self, account_name, account_number, balance, overdraft_limit):
        self.account_name = account_name
        self.account_number = account_number
        self.balance = balance
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print("Withdrawn:", amount)
            print("New Balance:", self.balance)
        else:
            print("Withdrawal exceeds overdraft limit.")

savings = SavingsAccount("Sumon", "S001", 10000, 5)

savings.display_info()
savings.deposit(2000)
savings.withdraw(3000)
savings.calculate_interest()

current = CurrentAccount("Rahim", "C001", 5000, 3000)

current.display_info()
current.deposit(2000)
current.withdraw(8000)