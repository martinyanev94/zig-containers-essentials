def compute(n):
    return [x**2 for x in range(n) if x % 2 == 0][:5]
def compute_even_squares(n):
    return [x**2 for x in range(n) if x % 2 == 0]

def first_five(lst):
    return lst[:5]

result = first_five(compute_even_squares(10))
print(result)  # Outputs: [0, 4, 16, 36, 64]
