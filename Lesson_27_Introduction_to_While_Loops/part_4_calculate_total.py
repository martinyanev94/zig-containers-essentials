numbers = [1, 3, 5, 7, 9, 11]
total = 0
index = 0

while index < len(numbers) and total <= 20:
    total += numbers[index]
    index += 1

print("Total:", total)
