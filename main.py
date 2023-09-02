import time

class Customer:
    def __init__(self, name, birthdate, account_no, balance=0):
        self.created = time.time()
        self.last_updated = self.created
        self.name = name
        self.birthdate = birthdate
        self.account_no = account_no
        self.balance = balance

class CustomerRegistry:
    def __init__(self):
        self.customer_list = []

    def add_customer(self, customer):
        self.customer_list.append(customer)

    def get_customer_by_account(self, account_no):
        for customer in self.customer_list:
            if customer.account_no == account_no:
                return customer
        return None

def create_customer_list(num_customers):
    start_time = time.time()
    registry = CustomerRegistry()
    for i in range(1, num_customers + 1):
        account_no = f'1111-{i:010}'
        customer = Customer(f'Customer {i}', f'01/01/2000', account_no)
        registry.add_customer(customer)
    
    end_time = time.time()
    elapsed_time = (end_time - start_time) * 1000 
    return registry, elapsed_time

def search_customer(account_no, registry):
    start_time = time.time()
    customer = registry.get_customer_by_account(account_no)
    end_time = time.time()
    elapsed_time = (end_time - start_time) * 1000  
    return customer, elapsed_time


if __name__ == "__main__":

    # Skapa 10 miljoner kunder och mäta tiden
    num_customers = 10000000
    customer_registry, creation_time = create_customer_list(num_customers)
    print(f"Time to create {num_customers} customers: {creation_time:.2f} ms")

    # Sök efter ett specifikt konto (1111-0000001000)
    search_account = '1111-0000001000'
    found_customer, search_time = search_customer(search_account, customer_registry)
    if found_customer:
        print(f"Found account {search_account} for {found_customer.name} in {search_time:.2f} ms")
    else:
        print(f"Account {search_account} not found in {search_time:.2f} ms")

    # Sök efter ett konto som inte finns (1111-9999999999)
    search_account = '1111-9999999999'
    found_customer, search_time = search_customer(search_account, customer_registry)
    if found_customer:
        print(f"Found account {search_account} for {found_customer.name} in {search_time:.2f} ms")
    else:
        print(f"Account {search_account} not found in {search_time:.2f} ms")