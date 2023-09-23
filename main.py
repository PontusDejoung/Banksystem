from time import time
from dataclasses import dataclass
from decorators import timing_decorator
import random
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
def generate_account_numbers_in_random_order(num_customers):
    timestamp = datetime.now()
    customer_list = [
    Customer(f'Customer{i}', f'01/01/1990', f'1111-{account_number:010d}', 0,timestamp,timestamp)
    for i, account_number in enumerate(random.sample(range(1, 10_000_000 + 1), num_customers))
    ]
    return customer_list
        
def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index)
        quicksort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[(low + high) // 2].account_number
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while arr[i].account_number < pivot:
            i += 1
        j -= 1
        while arr[j].account_number > pivot:
            j -= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]


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
    customers_list = generate_account_numbers_in_random_order(10_000_000)
    start = time()
    sort_customers = quicksort(customers_list,0,len(customers_list) - 1)
    end = time()
    sorting_time = (end - start) * 1000
    print(f"It took {sorting_time:.2f}ms to sort ")
    account_numbers_to_find = ["1111-0000001000", "1111-0009999999", "1111-9999999999"]
    results = [binary_search(customers_list, account_number) for account_number in account_numbers_to_find]
    for result, account_number in zip(results, account_numbers_to_find):
        if result:
            print(f"Kontonummer {account_number} hittat: {result}")
        else:
            print(f"Kunde inte hitta kontonummer {account_number}")

    print(f"Första kundens kontonummer: {customers_list[0].account_number}")
    print(f"Sista kundens kontonummer: {customers_list[-1].account_number}")
    