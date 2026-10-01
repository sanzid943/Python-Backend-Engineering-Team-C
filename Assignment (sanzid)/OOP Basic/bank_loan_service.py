
class BankingCustomer:

    def __init__(self, name, customer_id, age, account_type):
        self.name = name
        self.customer_id = customer_id
        self.age = age
        self.account_type = account_type


    def display_customer(self):

        print("\nCUSTOMER INFORMATION-")
        print("Name: ", self.name)
        print("Customer ID: ", self.customer_id)
        print("Age: ", self.age)
        print("Account type: ", self.account_type)

    def check_eligibility(self):

        if self.age >= 18:
            print("customer is eligible for banking service")

        else:
            print("customer is not eligible")


class LoanService(BankingCustomer):

    def __init__(self, name, customer_id, age, account_type, loan_amount, interest_rate, loan_months):
        super().__init__(name, customer_id, age, account_type)
        
        self.loan_amount = loan_amount
        self.interest_rate = interest_rate
        self.loan_months = loan_months

    def calculate_interest(self):

        interest = self.loan_amount * self.interest_rate /100
        return interest

    def calculate_total_loan(self):

        interest = self.calculate_interest()
        total = self.loan_amount + interest

        print("\nLOAN DETAILS-")
        print("Loan amount: ", self.loan_amount)
        print("Interest: ", interest)
        print("Total loan: ", total)


    def calculate_monthly_payment(self):
        
        total = self.loan_amount + self.calculate_interest()
        monthly_payment = total / self.loan_months
        print("Monthly payment: ", monthly_payment)

    
    def make_loan_payment(self, amount):

        if(amount <= self.loan_amount):
            self.loan_amount -= amount
            print("\nPayment made: ", amount)
            print("Remaining loan: ", self.loan_amount)

        else:
            print("\nPayment is greater than remaining loan")


    def check_loan_status(self):

        if self.loan_amount == 0:
            print("Loan status: Fully paid")

        else:
            print("Loan status: Active")
            print("Remaining loan: ", self.loan_amount)


    def calculate_transaction_fee(self, amount)

        fee = amount * 1 /100
        print("Transaction amount: ", amount)
        print("Transaction fee: ", fee)
        print("Total amount: ", amount + fee)

customer = LoanService("Rahim", "101", 26, "Loan account", 80000, 10, 12)

