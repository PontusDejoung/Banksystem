from time import time

class Customer:
    def __init__(self,name,birthdate,account_number,balance):
        self.created = time()
        self.last_updated = self.created
        self.name = name
        self.birthdate = birthdate
        self.account_number = account_number
        self.balance = balance

def create_customers(num_customer)-> str: 
    customers = []
    start_time = time()
    for i in range(1,num_customer):
        account_number = f'1111-{i:010d}'
        customer = Customer(f'Customer {i}', '2000-01-01', account_number,0)
        customers.append(customer)
    end_time = time()
    elapsed_time = (end_time - start_time) * 1000
    print(f"Created {num_customer} customers in {elapsed_time:.2f} ms")
    return customers

def find_customer_by_account(customers, account_number_to_find)->str:
    start_time = time()
    for customer in customers:
        if customer.account_number == account_number_to_find:
            end_time = time()
            elapsed_time = (end_time - start_time) * 1000
            print(f"Found customer {account_number_to_find} in {elapsed_time:.2f} ms")
            return
    end_time = time()
    elapsed_time = (end_time - start_time) * 1000
    print(f"Customer {account_number_to_find} not found in {elapsed_time:.2f} ms")

if __name__ == "__main__":
    num_customers = 10000000
    customers = create_customers(num_customers)

    find_account = "1111-0000010000"
    find_customer_by_account(customers, find_account)

    non_existent_account = "1111-9999999999"
    find_customer_by_account(customers, non_existent_account)