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
def generate_account_numbers_in_random_order(num_customers: int):
    timestamp = datetime.now()
    customer_list = [
    Customer(f'Customer{i}', f'01/01/1990', f'1111-{account_number:010d}', 0,timestamp,timestamp)
    for i, account_number in enumerate(random.sample(range(1, 10_000_000 + 1), num_customers))
    ]
    return customer_list
 
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

def partition(array, start, end, compare_func):
    pivot = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and compare_func(array[high], pivot):
            high = high - 1

        while low <= high and not compare_func(array[low], pivot):
            low = low + 1

        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

def quick_sort(array, start, end, compare_func):
    if start >= end:
        return
    p = partition(array, start, end, compare_func)
    quick_sort(array, start, p-1, compare_func)
    quick_sort(array, p+1, end, compare_func)

def find_customer(customers:list,*account_numbers_to_find:str):
    results = [binary_search(customers, account_number) for account_number in account_numbers_to_find]
    for result, account_number in zip(results, account_numbers_to_find):
        if result:
            print(f"Account Number:{account_number} hittat: {result}")
        else:
            print(f"Could not find Account Number:{account_number}")


if __name__ == "__main__":
    customer_list = generate_account_numbers_in_random_order(10_000_000)
    start = time()
    quick_sort(customer_list, 0, len(customer_list) - 1, lambda x, y: x.account_number > y.account_number)
    end = time()
    sorting_time = (end - start) * 1000
    print(f"It took {sorting_time:.2f}ms to sort ")
    print(f"Första kundens kontonummer: {customer_list[0].account_number}")
    print(f"Sista kundens kontonummer: {customer_list[-1].account_number}")
    find_customer(customer_list,"1111-0000001000")
    find_customer(customer_list,"1111-0009999999",)
    find_customer(customer_list,"1111-9999999999")
    
    