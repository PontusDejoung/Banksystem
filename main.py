from time import time
from dataclasses import dataclass
from decorators import timing_decorator
import random

@dataclass
class Customer:
    name: str
    birthdate: str
    account_number: str
    balance: float
    created: float = None
    last_updated: float = None

def generate_account_numbers(num_customers):
    account_numbers = []
    for i in range(1, num_customers):
        account_number = random.randint(1, 10_000_0000)
        if account_number not in account_numbers:
            account_number_str = f'1111-{account_number:010d}'
            account_numbers.append(account_number_str)
            yield account_number_str
        
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2].account_number
    left = [x for x in arr if x.account_number < pivot]
    middle = [x for x in arr if x.account_number == pivot]
    right = [x for x in arr if x.account_number > pivot]
    return quicksort(left) + middle + quicksort(right)

@timing_decorator
def create_customers_with_list(num_customers):
    account_numbers = generate_account_numbers(num_customers)
    current_time = time()
    customers = [
        Customer(
            name=f'Customer {account_number}',
            birthdate='2000-01-01',
            account_number=account_number,
            balance=0,
            created=current_time,
            last_updated=current_time
        ) for account_number in account_numbers
    ]
    return customers

@timing_decorator
def binary_search(customers, account_number_to_find):
    left = 0
    right = len(customers) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_customer = customers[mid]

        if mid_customer.account_number == account_number_to_find:
            return mid_customer
        elif mid_customer.account_number < account_number_to_find:
            left = mid + 1
        else:
            right = mid - 1

    return None

if __name__ == "__main__":
    customers_list = create_customers_with_list(10_000_00)
    start = time()
    sort_customers = quicksort(customers_list)
    end = time()
    sorting_time = (end - start) * 1000
    print(f"It took {sorting_time:.2f}ms to sort ")
    binary_search(sort_customers,"1111-0000001000")

    print(f"Första kundens kontonummer: {sort_customers[0].account_number}")
    print(f"Sista kundens kontonummer: {sort_customers[-1].account_number}")
    