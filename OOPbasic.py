class BankingCustomer:

    def __init__(self, full_name, account_id, age, acc_type="Savings"):
        self.full_name = full_name
        self.account_id = account_id
        self.age = age
        self.acc_type = acc_type

    def display_customer_profile(self):
        print("\n" + "=" * 25)
        print("CUSTOMER PROFILE")
        print("=" * 25)
        print(f"Name         : {self.full_name}")
        print(f"Customer ID  : {self.account_id}")
        print(f"Age          : {self.age}")
        print(f"Account Type : {self.acc_type}")

    def is_eligible(self):
        eligible = self.age >= 18
        status = "Eligible" if eligible else "Not eligible"
        print(f"\nAccount Status: {status} for banking services.")
        return eligible


class LoanService(BankingCustomer):

    def __init__(self, full_name, account_id, age, acc_type, principal_amount, annual_rate, tenure_months):
        super().__init__(full_name, account_id, age, acc_type)
        
        self.principal_amount = principal_amount
        self.annual_rate = annual_rate
        self.tenure_months = tenure_months
        
        # Track the total balance including interest
        self.total_interest = self._compute_interest()
        self.current_balance = self.principal_amount + self.total_interest

    def _compute_interest(self):
        return (self.principal_amount * self.annual_rate) / 100

    def show_loan_summary(self):
        print("\n" + "-" * 25)
        print("LOAN BREAKDOWN")
        print("-" * 25)
        print(f"Principal     : {self.principal_amount:,.2f}")
        print(f"Interest Rate : {self.annual_rate}%")
        print(f"Total Interest: {self.total_interest:,.2f}")
        print(f"Total Payable : {self.current_balance:,.2f}")

    def get_monthly_installment(self):
        monthly = (self.principal_amount + self.total_interest) / self.tenure_months
        print(f"\nEstimated Monthly Installment: {monthly:,.2f}")
        return monthly

    def process_payment(self, payment_amount):
        if payment_amount <= 0:
            print("\nTransaction failed: Payment amount must be positive.")
            return False

        if payment_amount <= self.current_balance:
            self.current_balance -= payment_amount
            print(f"\nPayment processed: {payment_amount:,.2f}")
            print(f"Updated Remaining Balance: {self.current_balance:,.2f}")
            return True
        else:
            print(f"\nPayment of {payment_amount:,.2f} exceeds remaining debt ({self.current_balance:,.2f}).")
            return False

    def view_loan_status(self):
        print("\n" + "-" * 25)
        if self.current_balance == 0:
            print("Status: Loan is completely settled.")
        else:
            print(f"Status: Active | Outstanding Debt: {self.current_balance:,.2f}")
        print("-" * 25)

    def calculate_service_fee(self, amount, fee_percentage=1.5):
        fee = (amount * fee_percentage) / 100
        total_with_fee = amount + fee
        print(f"\nService Fee ({fee_percentage}%): {fee:,.2f}")
        print(f"Total Net Charge: {total_with_fee:,.2f}")
        return total_with_fee


# Execution Demo
client = LoanService("Rahim", "101", 26, "Loan Account", 80000, 9, 12)

client.display_customer_profile()
client.is_eligible()

client.show_loan_summary()
client.get_monthly_installment()

client.view_loan_status()
client.process_payment(10000)

client.view_loan_status()
client.calculate_service_fee(4000)
