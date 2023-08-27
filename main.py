from time import time

class Customer:
    def __init__(self,name,birthdate,account_number,balance):
        self.created = time()
        self.last_updated = self.created
        self.name = name
        self.birthdate = birthdate
        self.account_number = account_number
        self.balance = balance

def create_customers_with_dict(num_customer)-> str: 
    customers = {}
    start_time = time()
    for i in range(1,num_customer):
        account_number = f'1111-{i:010d}'
        customer = Customer(f'Customer {i}', '2000-01-01', account_number,0)
        customers[account_number] = customer
    end_time = time()
    elapsed_time = (end_time - start_time) * 1000
    print(f"Created {num_customer} customers in {elapsed_time:.2f} ms")
    return customers

def find_customer_by_account(customers, account_number_to_find)->str:
    start_time = time()
    customer = customers.get(account_number_to_find)
    if customer:
        end_time = time()
        elapsed_time = (end_time - start_time) * 1000
        print(f"Found customer {account_number_to_find} in {elapsed_time:.2f} ms")
    else:
        end_time = time()
        elapsed_time = (end_time - start_time) * 1000
        print(f"Customer not found {account_number_to_find} in {elapsed_time:.2f} ms")
    return customer

if __name__ == "__main__":
    customers_dict = create_customers_with_dict(10000000)

    find_customer_by_account(customers_dict, '1111-0000001000')
    find_customer_by_account(customers_dict, '1111-0009999999')
    find_customer_by_account(customers_dict, '1111-9999999999')