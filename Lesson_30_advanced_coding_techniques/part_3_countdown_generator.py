def countdown(n):
    while n > 0:
        yield n
        n -= 1

for count in countdown(5):
    print(count)  # Outputs: 5, then 4, then 3, then 2, then 1
