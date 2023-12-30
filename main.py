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
def generate_account_numbers_in_random_order(num_customers:int):
    timestamp = datetime.now()
    customer_list = [
    Customer(f'Customer{i}', f'01/01/1990', f'1111-{account_number:010d}', 0,timestamp,timestamp)
    for i, account_number in enumerate(random.sample(range(1, 10_000_000 + 1), num_customers))
    ]
    return customer_list

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

if __name__ == "__main__":
    customers_list = generate_account_numbers_in_random_order(10_000_000)
    start = time()
    quick_sort(customers_list, 0, len(customers_list) - 1, lambda x, y: x.account_number > y.account_number)
    end = time()
    sorting_time = (end - start) * 1000
    print(f"It took {sorting_time:.2f}ms to sort ")
