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

@timing_decorator
def create_customers_with_dict(num_customers):
    customer_dict = {f'1111-{i:010}': Customer(f'Customer{i}', f'01/01/1990', f'1111-{i:010}', 0) for i in range(1, num_customers)}
    return customer_dict

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