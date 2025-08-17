input_valid = False

while not input_valid:
    num = input("Enter a number between 1 and 100: ")
    try:
        num = int(num)
        if 1 <= num <= 100:
            input_valid = True
            print(f"You entered a valid number: {num}")
        else:
            print("Number out of range, try again.")
    except ValueError:
        print("That's not a valid number! Please enter a numeric value.")
