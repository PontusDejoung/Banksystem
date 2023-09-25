import time
from dataclasses import dataclass
from datetime import datetime
from decorators import timing_decorator

@dataclass
class Customer:
   name: str
   birthdate: str
   account_number: str
   balance: float
   created: datetime
   last_updated: datetime

@timing_decorator
def create_customer_list(num_customers:int):
    timestamp = datetime.now()
    customers = []
    for i in range(1, num_customers + 1):
        account_no = f'1111-{i:010}'
        customers.append(Customer(f'Customer {i}', '2000-01-01', account_no, 0, timestamp, timestamp))
    return customers

@timing_decorator
def find_customer_by_account(customers:list, account_number_to_find:str):
    for customer in customers:
        if customer.account_number == account_number_to_find:
            print(f"Account Number:{account_number_to_find} Found:{customer}")
            return
    else:
        print(f'Customer {account_number_to_find} not found')


if __name__ == "__main__":
    customers = create_customer_list(10_000_000)
    find_customer_by_account(customers,'1111-0000001000')
    find_customer_by_account(customers,'1111-0009999999')
    find_customer_by_account(customers,'1111-9999999999')
