from time import time
from dataclasses import dataclass
from decorators import timing_decorator

@dataclass
class Customer:
    name: str
    birthdate: str
    account_number: str
    balance: float
    created: float = None
    last_updated: float = None

def generate_account_numbers(num_customers):
    for i in range(1, num_customers):
        yield f'1111-{i:010d}'

@timing_decorator
def create_customers_with_dict(num_customers):
    account_numbers = generate_account_numbers(num_customers)
    current_time = time()
    customers = {
        account_number: Customer(
            name=f'Customer {account_number}',
            birthdate='2000-01-01',
            account_number=account_number,
            balance=0,
            created=current_time,
            last_updated=current_time
        ) for account_number in account_numbers
    }
    return customers

@timing_decorator
def find_customer_by_account(customers, account_number_to_find):
    customer = customers.get(account_number_to_find, None)
    if customer:
        print(f"Found customer {account_number_to_find}")
    else:
        print(f"Customer not found {account_number_to_find}")

if __name__ == "__main__":
    customers_dict = create_customers_with_dict(10000000)

    find_customer_by_account(customers_dict, '1111-0000001000')
    find_customer_by_account(customers_dict, '1111-0009999999')
    find_customer_by_account(customers_dict, '1111-9999999999')