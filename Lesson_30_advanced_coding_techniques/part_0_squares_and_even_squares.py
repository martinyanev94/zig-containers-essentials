squares = [x**2 for x in range(10)]
print(squares)  # Outputs: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)  # Outputs: [0, 4, 16, 36, 64]
