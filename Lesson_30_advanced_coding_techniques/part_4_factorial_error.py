class NegativeNumberError(Exception):
    pass

def factorial(n):
    if n < 0:
        raise NegativeNumberError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

try:
    print(factorial(-5))
except NegativeNumberError as e:
    print(f"Error: {e}")  # Outputs: Error: Factorial is not defined for negative numbers.
