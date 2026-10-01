
class BankinCustomer:

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