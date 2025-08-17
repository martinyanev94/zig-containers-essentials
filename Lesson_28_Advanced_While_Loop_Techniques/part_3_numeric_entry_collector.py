num_entries = 3
entry_count = 0

while entry_count < num_entries:
    entry = ""
    while not entry.isdigit():  # Inner loop for validating numeric input
        entry = input(f"Enter entry #{entry_count + 1}: ")
        if entry.isdigit():
            print(f"Valid entry: {entry}")
            entry_count += 1
        else:
            print("Invalid input, please enter a number.")

print("All entries collected successfully!")
