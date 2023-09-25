from dataclasses import dataclass
from decorators import timing_decorator
from datetime import datetime

@dataclass
class Customer:
    name: str
    birthdate: str
    account_number: str
    balance: float
    created: datetime 
    last_updated: datetime

@timing_decorator
def create_customers_with_dict(num_customers):
    timestamp = datetime.now()
    customer_dict = {f'1111-{i:010}': Customer(f'Customer{i}', f'01/01/1990', f'1111-{i:010}', 0,timestamp,timestamp) for i in range(1, num_customers)}
    return customer_dict

@timing_decorator
def find_customer_by_account(customers, *account_numbers_to_find):
    found_customers = {account: customers.get(account, None) for account in account_numbers_to_find}
    for account, customer in found_customers.items():
        if customer:
            print(f"Found Account:{account}")
        else:
            print(f"Account:{account} not found")

if __name__ == "__main__":
    customers_dict = create_customers_with_dict(10_000_000)
    find_customer_by_account(customers_dict,'1111-0000001000')
    find_customer_by_account(customers_dict,'1111-9999999999')
    find_customer_by_account(customers_dict,'1111-0009999999')
    