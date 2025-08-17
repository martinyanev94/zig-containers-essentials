def divide_numbers(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None
    else:
        return result

print(divide_numbers(10, 2))  # Outputs: 5.0
print(divide_numbers(10, 0))  # Outputs: Error: Cannot divide by zero.
