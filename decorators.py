from time import time

def timing_decorator(func):
    def inner(*args,**kwargs):
        start_time = time()
        result = func(*args,**kwargs)
        end_time = time()
        elapsed_time = (end_time - start_time) * 1000
        print(f"{func.__name__} executed in {elapsed_time:.2f} ms")
        return result
    return inner
