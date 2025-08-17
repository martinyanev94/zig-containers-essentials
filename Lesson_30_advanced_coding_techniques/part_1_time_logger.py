import time

def time_logger(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'Function {func.__name__} executed in: {end_time - start_time:.4f} seconds')
        return result
    return wrapper

@time_logger
def some_heavy_computation(n):
    total = 0
    for i in range(n):
        total += i
    return total

some_heavy_computation(1000000)  # Logs execution time
